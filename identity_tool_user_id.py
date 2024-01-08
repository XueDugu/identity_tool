'''
思路：
主要是查看支付宝小程序，因为现在要逐渐淘汰user_id，所以扫描是否包含调用user_id进行身份识别的方法。
'''
import os
import re

def find_methods(file_path, methods):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        found_methods = set()
        for method in methods:
            pattern = re.compile(f'{method}\(\)')
            matches = pattern.findall(content)
            if matches:
                found_methods.add(method)

        for found_method in found_methods:
            print(f'File: {file_path}, Method: {found_method}')

def scan_directory(directory, methods):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".js"):
                file_path = os.path.join(root, file)
                find_methods(file_path, methods)

def main():
    folder_path = input("Enter the absolute path of the folder: ")
    methods_to_find = ['wechat.logger', 'wechat.put']
    scan_directory(folder_path, methods_to_find)

if __name__ == "__main__":
    main()
