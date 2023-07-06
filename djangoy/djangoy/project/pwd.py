import os

def traverse_directory(path, indentation=""):
    # 获取当前目录下的所有文件和文件夹
    contents = os.listdir(path)

    for item in contents:
        # 获取当前项目的完整路径
        item_path = os.path.join(path, item)

        # 判断当前项目是文件还是文件夹
        if os.path.isfile(item_path):
            # 输出文件
            print(f"{indentation}- {item}")
        elif os.path.isdir(item_path):
            # 输出文件夹，并对子目录进行递归遍历
            print(f"{indentation}+ {item}")
            traverse_directory(item_path, indentation + "  ")

# 指定要遍历的文件夹路径
folder_path = "D:\project\Python\chatpdfupload\linuxChatPdf\djangoy"

# 开始遍历文件夹
traverse_directory(folder_path)
