from json import load, dumps

from PyQt5.QtCore import QMessageAuthenticationCode
from PyQt5.QtWidgets import QMessageBox


def output_database(table_value: str) -> dict:
    """Parse JSON file and return dict"""
    with open(f"database/{table_value}.json", "r", encoding="utf-8") as file:
        json_text = load(file)
        return json_text


def database_add_department(values: list) -> None | int:
    """Add info into database"""
    json_text = output_database("department")
    # Check values.
    for _, value in json_text.items():
        if values[0] == value[0]:
               return 1

    if json_text != {}:
        maximum_index = max(list(map(int, json_text.keys())))
    else:
        maximum_index = 0
    json_text[maximum_index+1] = values

    with open("database/department.json", "w", encoding="utf-8") as file_write:
        in_json = dumps(json_text, indent=4, ensure_ascii=False)
        file_write.write(in_json)


def database_add_product(values: list) -> None | int:
    #TODO Сделать проверку на аналогичный товар
    """Add info about product in database"""
    json_text = output_database("products")
    # Check values.
    for _, value in json_text.items():
        if values[0] == value[0] and values[1] == values[1] and \
           values[2] == value[2] and values[3] == values[3]:
               return 1

    if json_text != {}:
        maximum_index = max(list(map(int, json_text.keys())))
        print(maximum_index)
    else:
        maximum_index = 0
    json_text[maximum_index+1] = values

    with open("database/products.json", "w", encoding="utf-8") as file_write:
        in_json = dumps(json_text, indent=4, ensure_ascii=False)
        file_write.write(in_json)


def database_delete_product(values: list[str]) -> None:
    json_text = output_database("products")
    for key, value in json_text.items():
        if value[0] == values[0] and \
           value[1] == values[1] and \
           value[2] == values[2] and \
           value[3] == values[3]:
            value_for_delete = key
    del json_text[value_for_delete]

    with open("database/products.json", "w", encoding="utf-8") as file_write:
        in_json = dumps(json_text, indent=4, ensure_ascii=False)
        file_write.write(in_json)


def database_add_product_in_department(values: list) -> None:
    """Add product in department"""
    department = output_database("department")
    products = output_database("products")
    json_text = output_database("product_in_department")
    department_index = None
    product_index = None

    for index, department_name in department.items():
        if department_name[0] == values[0]:
            department_index = index 
            break

    for index, product_name in products.items():
        if product_name[0] == values[1]:
            product_index = index
            break

    if json_text != {}:
        maximum_index = max(list(map(int, json_text.keys())))
    else:
        maximum_index = 0

    for key, value in json_text.items():
        if department[value[0]][0] == values[0] and \
                products[value[1]][0] == values[1] and \
                value[3] == values[3]:
            json_text[key] = [
                    department_index,
                    product_index,
                    str(int(value[2]) + int(values[2])),
                    values[3],
                    ]
            break

    else:
        json_text[maximum_index+1] = [department_index,
                                      product_index,
                                      values[2],
                                      values[3],
                                      ]

    with open("database/product_in_department.json", "w", encoding="utf-8") as file_write:
        in_json = dumps(json_text, indent=4, ensure_ascii=False)
        file_write.write(in_json)
    


def database_get_products() -> list[str]:
    """Get products from database"""
    products = output_database("products")
    product_list = []
    
    for product in products.values():
        product_list.append([product[0], 
                             product[1],
                             product[2],
                             product[3],])
    return product_list


def database_get_departments_and_products() -> tuple[list[str], list[str]]:
    """Get list with departments"""
    departments = output_database("department")
    department_list = []

    for department in departments.values():
        department_list.append(department[0])
    
    product_list = database_get_products()

    return (department_list, product_list)

    
    
