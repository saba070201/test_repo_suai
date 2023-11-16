# # Задача 2 
def dd(a):
    b=[]
    while a > 0:
        b.append(a % 10)
        a = a // 10
    b.reverse()
    return b
def create_full_sorted_list(l):
    l.sort(reverse=True)
    return list(map(dd,l))

nums=[86,85,90,7,91]
nums=create_full_sorted_list(nums)
## Задача 3
def find_max(l):
    if len(l)>1:
        max_ = find_max(l[1:])
        if l[0]<max_:
            return max_
        else:
            return l[0]
    if len(l)==1: 
        return l[0] 
l=[-1,-125125,2151261,0,125215166,-1521267888]
print(find_max(l))
# задача 4 
import random 
def find_colour(colours):
    list_of_colours = []
    for colour in colours:
        if colour['r'] > colour['g'] and colour['r'] > colour['b']:
            list_of_colours.append('red')
        elif colour['g'] > colour['r'] and colour['g'] > colour['b']:
            list_of_colours.append('green')
        elif colour['b'] > colour['r'] and colour['b'] > colour['g']:
            list_of_colours.append('blue')
    return list_of_colours
bitmap =[{'r':random.randint(0,255),'g':random.randint(0,255),'b':random.randint(0,255)} for i in range(20000)]
print(find_colour(bitmap))

