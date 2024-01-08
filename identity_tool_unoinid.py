'''
思路：
2022年9月之前，微信UnionID的前7位固定为oHl0it-，有的小程序使用检测UnionID前7位来判断UnionID是否合规。
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
    wrong_way = ['oHl0it-']
    scan_directory(folder_path, wrong_way)

if __name__ == "__main__":
    main()
