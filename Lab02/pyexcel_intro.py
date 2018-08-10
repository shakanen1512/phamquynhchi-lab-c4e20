import pyexcel
a_list = [
    {"name": "Alpha", "age": 28},
    {"name": "Beta", "age": 29},
    {"name": "Delta", "age": 30}
]
pyexcel.save_as(records=a_list, dest_file_name="List_example.xlsx")