from json import JSONDecodeError

import templates
from flask import Blueprint, render_template, request

from functions import get_posts_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    try:
        posts = get_posts_by_word(search_query)
    except ModuleNotFoundError:
        return 'File not found'
    except JSONDecodeError:
        return 'Invalid file'
    return render_template('post_list.html', posts=posts)
