import json


def write_order_to_json(item: str, quantity: str, price: str, buyer: str, date: str):
    with open("orders.json", 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders.json', 'w', encoding='utf-8') as f_in:
        orders_list = data['orders']
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        orders_list.append(order_info)
        json.dump(data, f_in, indent=4)


write_order_to_json('computer', '2', '1000', 'zxcvb', '14/02/2022')
write_order_to_json('printer', '1', '1020', '1fhcvb', '12/02/2002')
