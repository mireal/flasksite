import plotly.express as px
import csv
import pandas as pd


# def show_data(arg):
#     with open('data.txt', 'r+') as file:
#         data = []
#         for line in file:
#             line = line.split()
#             data.append(line[arg])
#     return data

def show_data(i):
    with open('data.csv', 'r+') as file:
        data = []
        csvreader = csv.reader(file)
        for ind, row in enumerate(csvreader):
            if ind > 0:
                if row[i].isdigit():
                    data.append(float(row[i]))
                else:
                    data.append(row[i])
        return data

file = pd.read_csv('data.csv')
df = pd.DataFrame(file)
print(df)






