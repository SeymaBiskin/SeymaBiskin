import json

def write_to_json(data, file_name):
    with open(file_name, "a") as file:
        json.dump(data, file)
        print("Data stored succesfully.")