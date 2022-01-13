import json
import yaml


def shipping_address(yaml_content):
    address = yaml_content['bill-to']['address']
    for key, values in address.items():
        print(key, values, end='')
    print()


def bill_number(yaml_content):
    print('Bill number is: ')
    print(yaml_content['invoice'])


def address_cost_number(yaml_content):
    var = yaml_content['product']
    for i in var:
        print('Description: ', i['description'])
        print('Price: ', i['price'])
        print('quantity: ', i['quantity'])


with open('order.yaml') as file:
    content = yaml.safe_load(file)
    print('^' * 50)
    shipping_address(content)
    print('^' * 50)
    bill_number(content)
    print('^' * 50)
    address_cost_number(content)
    print('^' * 50)

with open('task.json', 'w') as task_json:
    string_format = yaml.dump(content)
    json.dump(string_format, task_json)

with open('new_file.yaml', 'w') as new_file:
    yaml.dump(content, new_file)
