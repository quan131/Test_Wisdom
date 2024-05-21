def find(file_name):
    dic = {}
    with open(file_name, "r") as file:
        # Tách văn bản thành các câu bằng dấu xuống dòng
        sentences  = file.read().split('\n')
        
        # Đánh số thứ tự câu
        for i, sentence in enumerate(sentences, start=1):
            words = sentence.split()
            for word in words:
                if word in dic:
                    dic[word].append(i)
                else:
                    dic[word] = [i]
    return dic

if __name__ == "__main__":
    dic = find("vanban.txt")
    for key, value in dic.items():
        print(f"{key}: {', '.join(map(str, value))}")