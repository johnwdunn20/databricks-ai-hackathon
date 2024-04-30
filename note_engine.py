# FunctionTool is a wrapper around any function that converts it to a tool (supports both sync and async)
from llama_index.core.tools import FunctionTool
import os

# create a file to save notes
note_file = os.path.join(os.path.dirname(__file__), 'data', 'notes.txt')

# function takes in a note and saves it to a file
def save_note(note: str):
    # create the file if it does not exist
    if not os.path.exists(note_file):
        open(note_file, 'w').close()
    # append the note to the file
    with open(note_file, 'a') as f:
        f.writelines([note + '\n'])
        
    return "Note saved"

note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="Save a text based note to a file for the user",
)