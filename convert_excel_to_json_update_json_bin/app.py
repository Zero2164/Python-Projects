import json
import csv
import pandas as pd
from decouple import config
from pathlib import Path

totalAUM = 'Total AUM Combined'
totalROI = 'Total ROI'
totalTrades = 'Total Trades by Month'
BIN_KEY = config('BIN_KEY')
BIN_ID = config('BIN_ID')


def convertToCSV(xlsx_sheet):
    read_file = pd.read_excel(r'backend/data/xlsx/'+xlsx_sheet+'.xlsx')
    read_file.to_csv(r'backend/data/csv/'+xlsx_sheet +
                     '.csv', index=None, header=True)


def convertToJSON(csv_sheet):
    with open(r'backend/data/csv/'+csv_sheet+'.csv') as f:
        reader = csv.reader(f)
        next(reader)

        if csv_sheet == 'Total AUM Combined':
            data = {'TOTAL AUM': []}
            for row in reader:
                data['TOTAL AUM'].append({
                    'x': row[0],
                    'y': row[1]
                })

            with open('backend/data/json/Total AUM.json', 'w') as f:
                json.dump(data, f, indent=4)
        elif csv_sheet == 'Total ROI':
            print('pending')
        elif csv_sheet == 'Total Trades by Month':
            print('pending')
        elif csv_sheet == 'Total Clients':
            print('pending')
        elif csv_sheet == 'Total Volume':
            print('pending')


def updateBin(json_file):
    url = 'https://api.jsonbin.io/v3/b/'+BIN_ID
    headers = {
        'Content-Type': 'application/json',
        'X-Access-Key': BIN_KEY
    }
    # data = {"sample": "Hello World"}
    if json_file == 'Total AUM':
        data_folder = Path("json/")
        file_to_open = data_folder / "Total AUM.json"
        f = open(file_to_open)
        print(f.read())
    # req = requests.put(url, json=data, headers=headers)
    # print(req.text)


updateBin('Total AUM')


def get_total_aum():
    convertToCSV(totalAUM)
    convertToJSON(totalAUM)
    updateBin()
