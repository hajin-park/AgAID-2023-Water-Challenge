import json
import random


def main():
    for i in range(5, 11):
        for j in range(1, 6):
            data_file_path = f'TrainingData/JSONData/{i}Inputs/{i}input_{j}target.json'
            test_file_path = f'TrainingData/JSONData/{i}Inputs/test_{i}input_{j}target.json'
            extracted_test_cases = []

            with open(data_file_path, "rb") as f:
                json_data = json.load(f)
                for _ in range(50):
                    test_options = list(range(len(json_data)))
                    extracted_test_cases.append(json_data.pop(
                        test_options.pop(random.randint(0, len(test_options)-1))))

                with open(data_file_path, 'w') as file:
                    json_string = json.dumps(
                        json_data, indent=None, separators=(',', ':'))
                    file.write(json_string)

            with open(test_file_path, 'w') as file:
                json_string = json.dumps(
                    extracted_test_cases, indent=None, separators=(',', ':'))
                file.write(json_string)


main()
