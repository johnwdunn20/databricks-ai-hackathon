# will use a reader from llama index to read the pdf
# we will use a vector store index to store the pdf


import os
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage