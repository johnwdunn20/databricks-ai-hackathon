from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import os
import logging
import sys

# to see the logs
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

# This way we persist the data and only need to store it once
PERSIST_DIR = os.path.join(os.path.dirname(__file__), 'persist')
if not os.path.exists(PERSIST_DIR):
    print('Creating index from data')
    # load documents and create the index
    # load data from the data directory
    documents = SimpleDirectoryReader(os.path.join(os.path.dirname(__file__), 'data')).load_data()
    # create an index on that data (vector embeddings in memory by default)
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index from storage
    print('Loading index from storage')
    storage_contect = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_contect)

# create the query engine
query_engine = index.as_query_engine()

# test the query engine
response = query_engine.query('What did the author do growing up?')
print(response)