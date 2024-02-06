from peewee import *

db = SqliteDatabase('shop.db')


class Product(Model):
    name = CharField()
    price = IntegerField()

    class Meta:
        database = db
# создание таблицы
Product.create_table()
# вставка данных
new_product = Product(name='chicken eggs', price=10000)
new_product.save()
# чтение данных
product = Product.select().where(Product.id==1).get()
print(product)
# обновление данных
product.name = 'Gold'
product.save()
# удаление данных
product.delete_instance()