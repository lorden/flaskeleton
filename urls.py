from flask import Blueprint

flaskeleton_urls = Blueprint('flaskeleton',
                             __name__,
                             template_folder='templates')

flaskeleton_urls.add_url_rule('/get/',
                              view_func=GetView.as_view('get'),
                              methods=['GET'])
flaskeleton_urls.add_url_rule('/post/',
                              view_func=PostView.as_view('get'),
                              methods=['POST'])
flaskeleton_urls.add_url_rule('/both/',
                              view_func=BothView.as_view('both'),
                              methods=['GET', 'POST'])
