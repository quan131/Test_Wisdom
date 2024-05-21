def find_max_index(data):
    result = {}
    for line in data:
        char, value = line.split()
        value = int(value)
        if value in result:
            if char in result[value]:
                if result[value][char] < data.index(line):
                    result[value][char] = data.index(line)
            else:
                result[value][char] = data.index(line)
        else:
            result[value] = {char: data.index(line)}

    sorted_result = sorted(result.items())
    for value, char_indices in sorted_result:
        chars = []
        for char, index in char_indices.items():
            chars.append(f"{char}-{index}")
        print(f"giá trị {value} -> {', '.join(chars)}")

# Đọc dữ liệu từ file
with open("data.txt", "r") as file:
    data = file.readlines()

find_max_index(data)
