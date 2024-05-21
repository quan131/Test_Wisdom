def get_lines_by_value(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    result = {}
    for line in lines:
        values = line.strip().split()
        value = int(values[0])
        if value in result:
            result[value].insert(0, line.strip())
        else:
            result[value] = [line.strip()]

    for value, lines in sorted(result.items()):
        print(f"giá trị {value}: {' -> '.join(lines)}")

# Đường dẫn tới file dữ liệu
file_path = 'data.txt'

get_lines_by_value(file_path)
