# adding new line and column to the json file
# author: atacan

import json

file_path = 'data/employee.json'

with open(file_path, 'r+') as file:
    data = json.load(file)
    for employee in data['employees']:
        employee.setdefault('age', None)
        employee.setdefault('address', "")
    new_employee = {'firstName': 'Atacan', 'lastName': 'Buyuktalas', 'age': 25, 'address': 'Istanbul'}
    data["employees"].append(new_employee)

    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate()

print(json.dumps(data, indent=4))