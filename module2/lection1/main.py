# f = open('module2/lection1/file.txt', 'w')
# f.write('Hello world')
# f.close()
# f = open('module2/lection1/file.txt', 'r')
# file_content = f.read()
# print(file_content)
# f.close()
# with open('module2/lection1/file.txt', 'w') as f:
#     f.write('Hello world')
# with open('module2/lection1/file.txt', 'r') as f:
#     file_content = f.read()
#     print(file_content)
# import json
# data={'name':'Misha','age':22}
# with open('module2/lection1/file.json', 'w') as f:
#     f.write(json.dumps(data))
# with open('module2/lection1/file.json') as f:
#     file_content = f.read()
#     json_data = json.loads(file_content)
#     print(json_data)
# import yaml
# yaml_data={'name':'Misha','age':22}
# with open('module2/lection1/file.yaml', 'w') as f:
#     yaml.dump(yaml_data, f)

# with open('module2/lection1/file.yaml') as f:
#     print(f.read())
# from PIL import Image

# image = Image.open('module2/lection1/karelia.jpeg')
# cropped_image = image.crop((100, 700, 200, 800))  # обрезка фотографии
# pixels = list(image.getdata()) # получить каждый пиксель в изображении 
# print(pixels) 
# cropped_image.show()
# from docxtpl import DocxTemplate
# doc = DocxTemplate("module2/lection1/template.docx")
# context = { 'first_name':'Misha','last_name':'Sabadash'}
# doc.render(context)
# doc.save("module2/lection1/result.docx")
