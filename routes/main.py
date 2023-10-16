from flask import Blueprint

bp = Blueprint("main", __name__, url_prefix='/main')

@bp.route('create', methods =['POST'])
def hello():
    '''Hello function call from the main route'''
    return 'Hello there from main'