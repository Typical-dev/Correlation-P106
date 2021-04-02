import csv
import plotly.express as px
import numpy as np
def getDataSource(data_path):
    Marks_In_Percentage = []
    Days_Present= []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_In_Percentage.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row["Days Present"]))
        return{"x": Marks_In_Percentage, "y":Days_Present}
def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print(f"correlation coefficient is {correlation}")
def setup():
    data_path = "report-card.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
setup()