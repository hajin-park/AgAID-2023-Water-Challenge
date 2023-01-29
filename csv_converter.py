import json
import csv


def main():
    for i in range(8, 9):
        for j in range(5, 6):
            json_data_file_path = f'TrainingData/JSONData/{i}Inputs/{i}input_{j}target.json'
            json_test_file_path = f'TrainingData/JSONData/{i}Inputs/test_{i}input_{j}target.json'
            csv_data_file_path = f'TrainingData/CSVData/{i}Inputs/{i}input_{j}target.csv'
            csv_test_file_path = f'TrainingData/CSVData/{i}Inputs/test_{i}input_{j}target.csv'
            climate_indices = ["date", "CAR_ersst", "NTA_ersst", "aao", "ammsst", "amon_sm", "amon_sm_long", "amon_us", "amon_us_long", "ao", "atltri", "brazilrain", "censo", "censo_long", "ea", "eofpac", "epo", "espi", "gmsst", "hurr", "indiamon",
                               "ipotpi_hadisst2", "jonesnao", "meiv2", "nao", "nina1_anom", "nina34_anom", "nina3_anom", "nina4_anom", "noi", "np", "oni", "pdo", "pna", "qbo", "sahelrain", "soi", "solar", "swmonsoon", "tna", "tni", "trend", "tsa", "whwp", "wp", "precipitation"]

            #   Read json training data used in conversion to csv
            with open(json_data_file_path, 'r') as json_file:
                json_training_data = json.load(json_file)
                header = [f"{i}_{ci}" for i in range(
                    len(json_training_data[0]["input"])) for ci in climate_indices]
                header.append("target")

                with open(csv_data_file_path, 'w') as csv_file:
                    writer = csv.DictWriter(
                        csv_file, fieldnames=header, lineterminator='\n')
                    writer.writeheader()
                    for dataset in json_training_data:
                        counter = 0
                        row = {}
                        for month in dataset["input"]:
                            for k, v in month.items():
                                row[f"{counter}_{k}"] = v
                            counter += 1
                        row["target"] = dataset["target"]
                        writer.writerow(row)

            #   Read json test data used in conversion to csv
            with open(json_test_file_path, 'r') as json_file:
                json_test_data = json.load(json_file)

                with open(csv_test_file_path, 'w') as csv_file:
                    writer = csv.DictWriter(
                        csv_file, fieldnames=header, lineterminator='\n')
                    writer.writeheader()
                    for dataset in json_test_data:
                        counter = 0
                        row = {}
                        for month in dataset["input"]:
                            for k, v in month.items():
                                row[f"{counter}_{k}"] = v
                            counter += 1
                        row["target"] = dataset["target"]
                        writer.writerow(row)


main()
