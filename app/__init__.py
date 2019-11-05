from flask import Flask, render_template, request
from app.models import DBSession



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sdf'


from app.api.todo import api_bp as todo_api_bp



app.register_blueprint(todo_api_bp)



@app.route('/')
@app.route('/index')
def index():

	return render_template('index.html')


