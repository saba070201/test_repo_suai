# class Ape(object):
#     def __init__(self,height,weight) -> None:
#         self.height=height
#         self.weight=weight
#     def use_tools(self):
#         print('use tools')

# class Person(Ape):
#     def __init__(self,height,weight,language):
#         super().__init__(height,weight)
#         self.language=language
        
#     def abstract_thinking(self):
#         print('abstract_thinking')
# # p=Person(180,63,'ru')
# # ape=Ape(140,63)
# # p.use_tools()
# # p.abstract_thinking()
# # ape.use_tools()
# # ape.abstract_thinking()
# o=object()
# print(type(o))

# # person1=Person()
# # person1.age=22
# # person1.name='Misha'
# # person1.about()
# # person2=Person()
# # person2.age=16
# # person2.name='Daniil'
# # person2.about()
# # persons=[person1,person2]
class Engine(object):
    def __init__(self,power) -> None:
        self.power=power
    def __str__(self) -> str:
        return f'{self.power}'
class Car(object):
    def __init__(self,wheels,engine) -> None:
        self.wheels=wheels
        self.engine=engine
    def __str__(self) -> str:
        return f'{self.wheels},{self.engine}'

engine=Engine(100)
car=Car(['wheel1','wheel2','wheel3','wheel4'],engine)
print(car)