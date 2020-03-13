import os


def get_file_size(file_path):
    file_path_size = []
    for root, dirs, files in os.walk(file_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > 1000000:
                file_size = file_size / 1024 / 1024
            internal_file_path_size = "{},{}".format(file_path, file_size)
            file_path_size.append(internal_file_path_size)
    return file_path_size


file_path = r"C:\Users\Administrator\Downloads\split_normal"
store_txt = file_path + '\path.csv'
with open(store_txt, 'w+') as f:
    f.write("FileName, FileSize\n")
    for item in get_file_size(file_path):
        f.write(item + '\n')
