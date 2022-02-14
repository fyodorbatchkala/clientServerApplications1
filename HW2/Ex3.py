import yaml


data_in = {'items': ['phone', 'scanner', 'printer', 'computer'],
           'items_quantity': 4,
           'items_price': {'phone': '100 рублей',
                           'scanner': '150 рублей',
                           'printer': '20 рублей',
                           'computer': '1500 рублей'
                           }
           }

with open('file_1.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(data_in, f_in, default_flow_style=False, allow_unicode=True, sort_keys=True)

with open('file_1.yaml', 'r', encoding='utf-8') as f_out:
    data_out = yaml.load(f_out, Loader=yaml.SafeLoader)

print(data_in == data_out)
    