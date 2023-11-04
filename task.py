import pandas as pd

# Provide the raw file URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

# Read the CSV file
pingwiny = pd.read_csv(url, encoding='ISO-8859-1')
pingwiny

pingwiny.info()
