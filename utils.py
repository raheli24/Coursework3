import json


def load_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def load_posts():
    data = load_json("data/posts.json")

    return data


def load_post_by_pk(pk):
    data = load_posts()

    for post in data:
        if post['pk'] == pk:
            return post


def load_post_by_word(word):
    """

    """
    data = load_posts()
    post_filtered = []
    print(word)
    for post in data:

        if word.lower() in post['content'].lower():
            post_filtered.append(post)

    return post_filtered


def load_post_by_name(user_name):
    """

    """
    data = load_posts()
    post_filtered = []

    for post in data :

        if user_name == post['poster_name']:
            post_filtered.append(post)

    return post_filtered
