from flask.views import MethodView
from flask import render_template


class GetView(MethodView):
    def get(self):
        return render_template('blank.html')


class PostView(MethodView):
    def post(self):
        return render_template('blank.html')


class BothView(MethodView):
    def get(self):
        return render_template('blank.html')

    def post(self):
        return render_template('blank.html')
