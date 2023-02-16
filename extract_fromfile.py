import pandas as pd
from time import sleep
import openpyxl
from datetime import datetime

workbook = openpyxl.load_workbook("Weather_data_sample.xlsx")

sheet = workbook.active
df = pd.read_csv('sample_data.csv')
location_names = df['location'].tolist()
temp_date_str = df['date'].tolist()
temp_date = [datetime.strptime(date_str, "%B %d, %Y").strftime("%Y-%-m-%-d") for date_str in temp_date_str]
ROW = 4

for location, tdate in zip(location_names, temp_date):
    with open(f"files/{location}_{tdate}.txt", "r") as file:
        contents = file.read()

    lines = contents.split("\n")
    dict_list = []
    for line in lines:
        # Split the line into components
        try:
            components = line.split()
            if not ':30' in components[0]:
                extract_data = components[2], components[4], components[6], components[8], components[9], components[
                    11], \
                    components[13], components[15], components[17]
                dict_list.append(extract_data)
        except:
            None
    START = 7
    for i, data in enumerate(dict_list):
        for j, value in enumerate(data):
            sheet.cell(row=ROW, column=START + j, value=value)
        START += j + 1
    print(location, tdate)
    workbook.save("Weather_data_sample.xlsx")
    ROW += 1
    print('Next ROW',ROW)
