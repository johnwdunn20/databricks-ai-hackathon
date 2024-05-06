from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Might need to load dotenv if I don't export it in my shell

# load data from the data directory
documents = SimpleDirectoryReader('data').load_data()
# create an index on that data
index = VectorStoreIndex.from_documents(documents)
# query engine
query_engine = index.as_query_engine()

# test the query engine
response = query_engine.query('What did the author do growing up?')
print(response)