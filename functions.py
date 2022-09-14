import json

POSTS_PATH = 'posts.json'


def load_posts():
    with open(POSTS_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(word):
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def save_picture(picture) -> str:
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path


def func_add_post(post: dict) -> dict:
    posts = load_posts()
    posts.append(post)
    with open(POSTS_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post
