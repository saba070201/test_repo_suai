# # Задача 1 
# PATH100 = 'module2/pr1/data100.txt'
# PATH1000 = 'module2/pr1/data1000.txt'
# PATH10000 = 'module2/pr1/data10000.txt'
# PATH100000 = 'module2/pr1/data100000.txt'
# PATH1000000 = 'module2/pr1/data1000000.txt'
# import random
# import time 

# def write_list_to_file(count_of_nums, path):
#     l = [random.randint(-10000000, 10000000) for i in range(count_of_nums)]
#     with open(path, 'w+') as f:
#         for i in l:
#             f.write(str(i) + '\n')


# # write_list_to_file(1000, PATH1000)
# # write_list_to_file(10000, PATH10000)
# # write_list_to_file(100000, PATH100000)
# # write_list_to_file(1000000,PATH1000000)
# def read_data_from_file(path):
#     l = []
#     with open(path,'r') as f:
#         for i in f:
#             l.append(int(i))
#     return l
start_time=time.time()
# выполнение какой либо сортировки 
finish_time=time.time()
print(finish_time-start_time)
# Задача 1
# import json
# class Developer:
#     def __init__(self,stack,notebook) -> None:
#         self.stack=stack
#         self.notebook=notebook

# class NoteBook:
#     def __init__(self,model) -> None:
#         self.model=model

# # образец json : {
# # 'stack': '...',
# # 'notebook' : {'model':'...'}
# # }
# class ReadJson:
#     @staticmethod
#     def get_json_data():
#         with open('path/to/json/file') as f:
#             file_content=f.read()
#             json_data=json.loads(file_content)
#         return json_data

# # задача 2 
# ## обычный поиск 
# def simple_search(arr,value):
#     j=1
#     for i in range(len(arr)):
#         print(j)
#         j+=1
#         if arr[i]==value:
#             return i
# ## оптимизированный  поиск 
# def binary_search(arr,value):
#     low_index=0
#     high_index=(len(arr))-1
#     i=1
#     while low_index<=high_index:
#         print(i)
#         i+=1
#         mid_index=(low_index+high_index)//2
#         if arr[mid_index]==value:
#             return mid_index
#         if arr[mid_index]>value:
#             high_index=mid_index-1
#         else:
#             low_index=mid_index+1
#     return None
import random


def find_el(element, data):
    for i in range(len(data)):
        if data[i] == element:
            return i


nums = [random.randint(-1000000, 1000000) for _ in range(100000)]
print(find_el(1000,nums))

