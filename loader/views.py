from json import JSONDecodeError

import templates as templates
from flask import Blueprint, render_template, request
from functions import save_picture

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route('/post')

def add_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])

def add_post():
    picture = request.files.get('picture')
    content = request.files.get('content')

    if not picture or not content:
        return 'Picture and/or content not found'
    if picture.filename.split('.')[-1] not in ['.jpeg', '.png']:
        return 'Extention of file is false'

    try:
        picture_path: str = '/' + save_picture(picture)
    except FileNotFoundError:
        return 'File not found'
    except JSONDecodeError:
        return 'Invalid file'
    post: dict = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)

