def save_csv(file_name, column_names, data):
    f = open(file_name, 'w')  # 'w' means write mode. NOTE: It will create a file if doesn't already exist

    for column_name in column_names:
        f.write(str(column_name) + ",")

    f.write("\n")

    for record in data:
        csv_record = ','.join(str(r) for r in record) + '\n'
        f.write(csv_record)

    f.close()
