import json


def load_data(file_name):
    with open(file_name, encoding='utf8') as file:
        data = json.load(file)
    return data


def load_posts(search_word=None, user_name=None):
    posts = load_data("data/posts.json")

    if search_word:
        posts = filter(lambda x: search_word in x['content'].lower(), posts)
    if user_name:
        posts = filter(lambda x: user_name == x['poster_name'].lower(), posts)

    # filter_posts = []
    # for post in posts:
    #    if search_word in post['content'].lower():
    #        filter_posts.append(post)

    return posts


def load_comments(posts_pk):
    all_comments = load_data("data/comments.json")
    comments = []
    for comment in all_comments:
        if comment["post_id"] == posts_pk:
            comments.append(comment)
    return comments


def load_post(pk):
    posts = load_posts()
    for post in posts:
        if post['pk'] == pk:
            return post

