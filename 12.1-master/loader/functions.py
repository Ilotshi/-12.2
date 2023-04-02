import json

def json_add(picture_path,content):
    """
    Функция записи данных поста в json файл
    """
    data = json.load(open("posts.json",encoding='utf-8'))
    new_data = {'pic': picture_path, 'content': content, }
    data.append(new_data)
    with open('posts.json',mode='w',encoding='utf-8')as f:
        json.dump(data,f,ensure_ascii=False,indent=2)

