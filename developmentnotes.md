# General
- Community Edition doesn't allow me to link to VSCode so need to manually export/import notebooks between the two. This will allow me to have version control in git

## Set Up for my own libraries
1. Set up virtual environment with `virtualenv venv` and activate it `source venv/bin/activate`
  a. Note: Windows commands are slightly different
2. In the virtual environment shell, run `pip install -r requirements.txt`
3. To add newly installed libraries to requirements.txt, can fun `pip freeze > requirements.txt` after installation

## Data sources
- World Population by Country: [https://www.kaggle.com/datasets/joebeachcapital/world-population-by-country-2023](https://www.kaggle.com/datasets/joebeachcapital/world-population-by-country-2023)

## General Notes
- Uses LLama Index