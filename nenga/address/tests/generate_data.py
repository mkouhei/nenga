# -*- coding: utf-8 -*-
import os
import json
import shortuuid


def generate_data(key):
    return {
        "model": "nenga.%s" % key,
        "pk": shortuuid.uuid(),
        "fields": {
            "%s" % key: shortuuid.uuid()
        }
    }


def generate_contact(owner_id):
    return {
        "model": "address.contact",
        "pk": shortuuid.uuid(),
        "fields": {
            "last_name": shortuuid.uuid(),
            "first_name": shortuuid.uuid(),
            "zip_code": shortuuid.uuid(),
            "prefecture": shortuuid.uuid(),
            "city": shortuuid.uuid(),
            "address": shortuuid.uuid(),
            "address2": shortuuid.uuid(),
            "partner_name": shortuuid.uuid(),
            "owner": owner_id
        }
    }


def generate_json():
    data_list = []
    for i in range(20):
        data_list.append(generate_contact(i % 4 + 1))
    return json.dumps(data_list)


def main():
    dirpath = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(dirpath, 'dummy_data.json')

    with open(json_path, 'w') as f:
        f.write(generate_json())


if __name__ == "__main__":
    main()
