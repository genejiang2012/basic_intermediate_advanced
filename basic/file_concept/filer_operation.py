with open(r"C:\Users\Administrator\Desktop\test\test.txt", 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        print(line)

        if line == "":
            break