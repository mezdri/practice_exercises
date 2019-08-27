data = [
    {
        'id': "1",
        'title': "hole",
        'desc': "#here",
        'hashtag': "hola"
    },
    {
        'id': "2",
        'title': "hole",
        'desc': "#hola",
        'hashtag': "hola"
    }
]


def get_id_by_text(text):
    response = []
    for dic in data:
        if text:
            if not dic['title'].find(str(text)) == -1 or not dic['desc'].find(str(text)) == -1:
                response.append(dic['id'])
    return response if response else False


def get_hashtag():
    response = []
    for dic in data:
        for x in dic['hashtag']:
            if not x in response:
                response.append(x)
        for key in dic:
            if key == 'desc':
                text_list = dic[key].split(" ")
                for text in text_list:
                    if not text.find('#') == -1:
                        text.join(e for e in text if e.isalnum() && e != '\'')
                        response.append(text)
    return response


