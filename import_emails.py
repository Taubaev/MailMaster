import csv

def import_email_list_from_csv(file_path):
    email_list = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            email_list.append(row[0])  # Предполагается, что email в первой колонке
    return email_list
