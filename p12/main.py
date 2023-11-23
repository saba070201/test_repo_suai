

# Задача 1 
# class SodaDrink:
#     def __init__(self,add=None) -> None:
#         self.add=add
#     def show_my_drink(self):
#         if self.add:
#             print(f'Газировка с {self.add}')
#         else: 
#             print('Обычная газировка')
# sd1=SodaDrink('карамель')
# sd1.show_my_drink()
# sd2=SodaDrink()
# sd2.show_my_drink()
# Задача 2 
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return f'Точка x:{self.x} y:{self.y}'
#     def __add__(self,other_point):
#         return Section(self,other_point)
# class Section:
#     def __init__(self,point1,point2):
#         self.point1=point1
#         self.point2=point2
#     def __str__(self) -> str:
#         return f'{self.point1} {self.point2}'

# point1=Point(1,1)
# point2=Point(2,2)
# section=point1+point2
# print(type(section),section)

# Задача 3 
# import random
# class Warior: 
#     def __init__(self,health,damage,name) -> None:
#         self.name=name
#         self.health=health
#         self.damage=damage
#     def attack(self,other_warior):
#         other_warior.get_damage(self)
#     def get_damage(self,other_warior):
#         self.health-=other_warior.damage

# class Batle:
#     @staticmethod
#     def batle(war1:Warior,war2:Warior):
#         while True: 
#             if war1.health<=0:
#                 print(war2.name,'победил')
#                 break 
#             if war2.health<=0:
#                 print(war1.name,'победил')
#                 break 
#             who_beat=random.randint(0,1)
#             if who_beat==0:
#                 war1.attack(war2)
#                 print(war1.name,'attack',war2.name,'hp',war2.health)
               
#             else: 
#                 war2.attack(war1)
#                 print(war2.name,'attack',war1.name,'hp',war1.health)
                

# artes=Warior(100,10,'Artes')
# illidan=Warior(50,20,'Illidan')
# Batle.batle(artes,illidan)
class Telephone:
    def __init__(self,m) -> None:
        self.m=m

class Computer:
    def __init__(self,p) -> None:
        self.p=p

class Smartphone(Telephone,Computer):
    def __init__(self,m,p,s) -> None:
      
        Computer.__init__(self,p=p)
        Telephone.__init__(self,m=m)
        self.s=s

       

sp=Smartphone(m='m',p='p',s='s')
       
            
            
