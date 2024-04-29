from llama_index.core import PromptTemplate

instruction_str= """
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The does should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION
    5. Do not quote the expression."""
    
# Prompt template allows us to embed whatever we specify here into the model prompt    
new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}
    
    Folllow these instructions:
    {instruction_str}
    Query: {query_str}
    
    Expression: """
)
# query_str is a placeholder that will be replaced with the actual query