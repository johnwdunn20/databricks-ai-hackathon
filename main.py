from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.query_engine import PandasQueryEngine

load_dotenv()

# Load the csv data
population_path = os.path.join(os.path.dirname(__file__), 'data', 'population.csv')
population_df = pd.read_csv(population_path)

# create a query engine so that we can query the data
# verbose=True will print out details from the query engine
population_query_engine = PandasQueryEngine(df=population_df, verbose=True)

# pass a template query to the query engine

