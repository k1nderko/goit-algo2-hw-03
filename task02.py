import csv
import timeit
from BTrees.OOBTree import OOBTree


def load_data(filename):
    data = {}
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item_id = int(row['ID'])
            data[item_id] = {
                'Name': row['Name'],
                'Category': row['Category'],
                'Price': float(row['Price'])
            }
    return data

def add_item_to_tree(tree, item_id, item_data):
    tree[item_id] = item_data

def add_item_to_dict(dictionary, item_id, item_data):
    dictionary[item_id] = item_data

def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items() if min_price <= item['Price'] <= max_price]

def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item['Price'] <= max_price]

if __name__ == "__main__":
    filename = "generated_items_data.csv"
    data = load_data(filename)

    tree = OOBTree()
    dictionary = {}

    for item_id, item_data in data.items():
        add_item_to_tree(tree, item_id, item_data)
        add_item_to_dict(dictionary, item_id, item_data)

    min_price, max_price = 10, 50  
    iterations = 100

    time_tree = timeit.timeit(lambda: range_query_tree(tree, min_price, max_price), number=iterations)
    time_dict = timeit.timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=iterations)

    print(f"Total range_query time for OOBTree: {time_tree:.6f} seconds")
    print(f"Total range_query time for Dict: {time_dict:.6f} seconds")