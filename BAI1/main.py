from datetime import datetime
file_path = 'data.txt'

def sort_by_name(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    # Sắp xếp dữ liệu theo tên
    sorted_data = sorted(data, key=lambda x: x.split()[0])

    return sorted_data

def sort_by_name_and_time(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    # Tạo danh sách các tuple (tên, thời gian)
    name_time_pairs = [(line.split()[0], datetime.strptime(line.split()[1], '%H:%M:%S')) for line in data]

    # Sắp xếp danh sách theo tên và thời gian tăng dần
    sorted_pairs = sorted(name_time_pairs, key=lambda x: (x[0], x[1]))

    # Tạo danh sách kết quả từ các tuple đã sắp xếp
    sorted_data = [f"{name} {time.strftime('%H:%M:%S')}" for name, time in sorted_pairs]

    return sorted_data

sorted_by_name = sort_by_name(file_path)
print("Sắp xếp theo tên:")
for line in sorted_by_name:
    print(line.strip())

print("\nSắp xếp theo tên và thời gian tăng dần:")
sorted_by_name_and_time = sort_by_name_and_time(file_path)
for line in sorted_by_name_and_time:
    print(line)