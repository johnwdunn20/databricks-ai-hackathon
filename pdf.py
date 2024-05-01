# will use a reader from llama index to read the pdf
# we will use a vector store index to store the pdf


import os
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.readers import PDFReader

def get_index(data, index_name):
    index = None
    # if index name doesn't exist, create it
    if not os.path.exists(index_name):
        print(f"Creating index {index_name}")
        # create the index
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        # store the index
        index.storage_context.persist(persist_dir=index_name)
    # if it does exist, load it
    else:
        index = load_index_from_storage(StorageContext.from_defaults(persist_dir=index_name))

# we can just create the index once and store it in the storage

pdf_path = os.path.join(os.path.dirname(__file__), 'data', 'United_States.pdf')
US_pdf = PDFReader().load_data(file=pdf_path)