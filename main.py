from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str

load_dotenv()

# Load the csv data
population_path = os.path.join(os.path.dirname(__file__), 'data', 'population.csv')
population_df = pd.read_csv(population_path)

# create a query engine so that we can query the data
# verbose=True will print out details from the query engine
population_query_engine = PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)
population_query_engine.update_prompt({"pandas_prompt" :new_prompt})

# Test the query engine
population_query_engine.query("What is the population of Canada?")

