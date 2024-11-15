from utils.chunk_description import Description
from utils.chunk_translation import Translation
from utils.chunking import Chunker

#Defining the variables 
chunk = Chunker()
translator = Translation()
descriptor = Description()

chunk_chain = chunk | translator | descriptor