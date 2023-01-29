'''
Organize csv file data into data sets used to train machine learning models.
Returns a json file with a list of training data sets of input variables and a target number.
'''


import csv
import json


#   Training dataset template
dataset = {
    "input": [],
    "target": 0
}
months = ["January", "February", "March", "April", "May",
          "June", "July", "August", "September", "October", "November", "December"]
filtered_data = []


def organize_data(
        line, curr_line: int,
        dataset_copy: dict,
        header, curr_months,
        input_months,
        target_months) -> None:
    '''Record new month into the snapshot. Organize input and target month data for every data set.'''

    #   Climate Index values used as input data for each training set
    input_types = {header[i]: var for i, var in enumerate(line[1:], 1)}

    #   Translate dates into the name of the month as an input variable
    input_types['date'] = months[int(line[0].split("-")[1])-1]

    #   Cycle in the newest month and remove the oldest one in each snapshot
    curr_months.pop(0)
    curr_months.insert(len(curr_months), input_types)

    #   Start adding training data sets once line 13 is reached (for a complete data set)
    if curr_line > (input_months + target_months - 1):
        dataset_copy["input"] = curr_months[:input_months]
        dataset_copy["target"] = sum(
            [float(month["precipitation"]) for month in curr_months[-target_months:]])
        filtered_data.append(dataset_copy)


def main(
        filename: str,
        curr_months: list,
        input_months: int,
        target_months: int) -> None:
    with open(f'MainData/{filename}.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        curr_line = 0

        for line in reader:
            curr_line += 1
            organize_data(line, curr_line, dataset.copy(), header,
                          curr_months, input_months, target_months)

    json_file_path = f'TrainingData/JSONData/{input_months}Inputs/test_{input_months}input_{target_months}target.json'
    with open(json_file_path, 'w') as file:
        json_string = json.dumps(
            filtered_data, indent=None, separators=(',', ':'))
        file.write(json_string)


for i in range(5, 11):
    for j in range(1, 6):
        filtered_data.clear()

        #   Record snapshots of months (input months + target months) while scanning the csv file
        curr_months = [{} for _ in range(i + j)]
        main("00_all_ClimateIndices_and_precip",
             curr_months, i, j)

# input_months = int(input("Enter # of months to use as the input: "))
# target_months = int(input("Enter # of months to use as the target: "))
