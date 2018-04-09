import os as computer

def rename_files():
# 1 - get file names
    file_list = computer.listdir(r"C:\Users\mike6\Google Drive\FullStack\UdacityFSWD\prank")
    print(file_list)
    saved_path = computer.getcwd()
    print(saved_path)
    computer.chdir(r"C:\Users\mike6\Google Drive\FullStack\UdacityFSWD\prank")
# 2 - for each file, rename
    for file_name in file_list:
        new_name = file_name.translate(None, "0123456789")
        computer.rename(file_name, new_name)
    print(file_list)
    
rename_files()
