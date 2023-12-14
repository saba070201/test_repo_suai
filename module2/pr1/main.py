PATH100 = 'module2/pr1/data100.txt'
PATH1000 = 'module2/pr1/data1000.txt'
PATH10000 = 'module2/pr1/data10000.txt'
PATH100000 = 'module2/pr1/data100000.txt'
PATH1000000 = 'module2/pr1/data1000000.txt'
import random


def write_list_to_file(count_of_nums, path):
    l = [random.randint(-10000000, 10000000) for i in range(count_of_nums)]
    with open(path, 'w+') as f:
        for i in l:
            f.write(str(i) + '\n')


# write_list_to_file(1000, PATH1000)
# write_list_to_file(10000, PATH10000)
# write_list_to_file(100000, PATH100000)
# write_list_to_file(1000000,PATH1000000)
def read_data_from_file(path):
    l = []
    with open(path,'r') as f:
        for i in f:
            l.append(int(i))
    return l


list1000 = read_data_from_file(PATH1000)
print(list1000)
f = open(PATH1000)
print(type(f))
f.close()
