from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental import PandasQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from pdf import US_engine

load_dotenv()

# Load the csv data
population_path = os.path.join(os.path.dirname(__file__), 'data', 'population.csv')
population_df = pd.read_csv(population_path)

# create a query engine so that we can query the data
# verbose=True will print out details from the query engine
population_query_engine = PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})


# Specify the tools we'll have access to
tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_query_engine",
            description="Query the population data",
        )
    ),
    QueryEngineTool(
        query_engine=US_engine,
        metadata=ToolMetadata(
            name="US_query_engine",
            description="Query the United States pdf",
        )
    ),
]

# Test the query engine
llm = OpenAI(model='gpt-3.5-turbo-1106')
# create an agent that has access to the tools - ReActAgent will determine the best tool to use based on the query
agent = ReActAgent.from_tools(llm=llm, tools=tools, verbose=True, context=context)
# start the agent (:= is the walrus operator and is used to assign a value to a variable as part of an expression. The while loop will run until the user enters the string 'q' as the prompt)
while (prompt := input("Enter a prompt (q to quit): ")) != 'q':
    result = agent.query(prompt)
    print(result)