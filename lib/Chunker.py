from abc import ABC, abstractmethod
from .CodeParser import CodeParser
from .utils import count_tokens


class Chunker(ABC):
    def __init__(self, encoding_name="gpt-4"):
        self.encoding_name = encoding_name

    @abstractmethod
    def chunk(self, content, token_limit):
        pass

    @abstractmethod
    def get_chunk(self, chunked_content, chunk_number):
        pass

    @staticmethod
    def print_chunks(chunks):
        for chunk_number, chunk_code in chunks.items():
            print(f"Chunk {chunk_number}:")
            print("=" * 40)
            print(chunk_code)
            print("=" * 40)

    @staticmethod
    def consolidate_chunks_into_file(chunks):
        return "\n".join(chunks.values())

    @staticmethod
    def count_lines(consolidated_chunks):
        lines = consolidated_chunks.split("\n")
        return len(lines)


class CodeChunker(Chunker):
    def __init__(self, file_extension, encoding_name="gpt-4"):
        super().__init__(encoding_name)
        self.file_extension = file_extension

    def chunk(self, code, token_limit) -> dict:
        code_parser = CodeParser(self.file_extension)
        chunks = {}
        token_count = 0
        lines = code.split("\n")
        i = 0
        chunk_number = 1
        start_line = 0
        breakpoints = sorted(code_parser.get_lines_for_points_of_interest(code, self.file_extension))
        comments = sorted(code_parser.get_lines_for_comments(code, self.file_extension))
        adjusted_breakpoints = []

        # Adjust breakpoints based on comments as before
        for bp in breakpoints:
            current_line = bp - 1
            highest_comment_line = None
            while current_line in comments:
                highest_comment_line = current_line
                current_line -= 1

            if highest_comment_line:
                adjusted_breakpoints.append(highest_comment_line)
            else:
                adjusted_breakpoints.append(bp)

        breakpoints = sorted(set(adjusted_breakpoints))

        # Function to determine if the logical structure ends at the current line
        def is_logical_end(i):
            line = lines[i]
            # Check if we are at a class or function definition line, which might logically conclude the structure
            return any(keyword in line for keyword in ["class ", "def "])

        # Parse through the lines of code
        while i < len(lines):
            line = lines[i]
            new_token_count = count_tokens(line, self.encoding_name)
            
            # Check if adding this line exceeds the token limit
            if token_count + new_token_count > token_limit:
                # If the current chunk contains a logical structure that exceeds the limit,
                # move the entire structure to the next chunk
                if not is_logical_end(i):
                    # Skip lines and ensure the next chunk starts after the logical structure
                    while i < len(lines) and not is_logical_end(i):
                        token_count += count_tokens(lines[i], self.encoding_name)
                        i += 1

                # Now, we should be at the end of a logical structure, so chunk it
                current_chunk = "\n".join(lines[start_line:i])
                if current_chunk.strip():
                    chunks[chunk_number] = current_chunk
                    chunk_number += 1

                # Reset token count and update start line
                token_count = 0
                start_line = i

            else:
                # If the token count is still within the limit, add the line to the current chunk
                token_count += new_token_count
                i += 1

        # Append remaining code, ensuring it's not empty or whitespace
        current_chunk_code = "\n".join(lines[start_line:])
        if current_chunk_code.strip():
            chunks[chunk_number] = current_chunk_code

        return chunks

    def get_chunk(self, chunked_codebase, chunk_number):
        return chunked_codebase[chunk_number]
