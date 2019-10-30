from flask import Flask
from app import app
from flask_restful import Resource, Api, reqparse, abort


app = Flask(__name__)
api = Api(app)

TODOS = {
'todo1': {'task': 'build an API'},
'todo2': {'task': '?????'},
'todo3': {'task': 'profit!'},
}



class Todo(Resource):
	def get(self, todo_id):
		abort_if_todo_doesnt_exist(todo_id)
		return TODOS[todo_id]

def delete(self, todo_id):
	abort_if_todo_doesnt_exist(todo_id)
	del TODOS[todo_id]
	return '', 204

def put(self, todo_id):
	args = parser.parse_args()
	task = {'task': args['task']}
	TODOS[todo_id] = task
	return task, 201



if __name__ == '__main__':
app.run(debug=True)








#GET /todos
@app.route('/todos')
def get(self):
	return [TODOS]


#POST /todos
#{
#  'id': 4,
#  'name': 'Ajanda',
#  'content': 'Ajanda alınacak',
#  'due_date': datetime(2020,8,20)            
#}



def abort_if_todo_doesnt_exist(todo_id):
if todo_id not in TODOS:
	abort(404, message="Todo {} doesn't exist".format(todo_id))
parser = reqparse.RequestParser()
parser.add_argument('task')


#/todos/id

@app.route('/todos', methods=['POST'])
def add_todo():
	request_data = request.get_json()
	if(validTodoObject(request_data)):
		new_todo = {
			"id": request_data['id'],
			"name": request_data['name'],
			"content": request_data['content'],
			"due_date": request_data['due_date']
		}
		todos.insert(0, new_todo)
		response = Response("",201, mimetype='application/json')
		response.headers['Location'] = "/todos/" + str(new_todo['id'])
		return response
	else:
		invalidTodoObjectErrorMsg = {
			"error": "Invalid todo object passed in request",
			"helpString": "Data passed in similar to this { 'id': 5, 'name':'Toplantı', 'content': 'Salı toplantı yapılacak', 'due_date':'2020,3,18' }"
		}

		response = Response(json.dumps(invalidTodoObjectErrorMsg), status=400, mimetype='application/json');
		return response



#GET /todos/id
@app.route('/todos/<int:id>')
def get_todo_by_id(id):
	return_value = {}
	for todo in todos:
		if todo["id"] == id:
			return_value = {
				'name':todo["name"],
				'content':todo["content"]
			}
	return jsonify(return_value)


#PUT /todos/id
#{
# 'name': 'Toplantı',
# 'content': 'Bilet alınacak',
# 'due_date': '2030,3,5'
#}

def valid_put_request_data(request_data):
	if("id" in request_data and "name" in request_data 
			and "content" in request_data and "due_date" in request_data):
		return True
	else:
		return False


@app.route('/todos/<int:id>', methods=['PUT'])
def replace_todo(id):
	request_data = request.get_json()
	if(not valid_put_request_data(request_data)):
		invalidTodoObjectErrorMsg = {
			"error": "Invalid todo object passed in request",
			"helpString": "Data passed in similar to this { 'id': 5, 'name':'Toplantı', 'content': 'Salı toplantı yapılacak', 'due_date':'2020,3,18' }"
		}

	response = Response(json.dumps(invalidTodoObjectErrorMsg), status=400, mimetype='application/json');
	return response

	new_todo = {
		'id':id,
		'name': request_data['name'],
		'content': request_data['content'],
		'due_date': request_data['due_date']
	}

	i = 0
	for todo in todos:
		currentId =todo["id"]
		if currentId == id:
			todos[i] = new_todo
		i += 1
	response = Response("", status=204)
	return response



#PATCH /todos/id
#{
# 'name': 'Toplantı'
#}

#PATCH /todos/id
#{
# 'due_date': '2020,4,8'
#}


@app.route('/todos/<int:id>', methods=['PATCH'])
def update_todo(id):
	request_data = request.get_json()
	updated_todo = {}
	if("name" in request_data):
		updated_todo["name"] = request_data["name"]
	if("due_date" in request_data):
		updated_todo["due_date"] = request_data["due_date"]
	for todo in todos:
		if todo["id"] == id:
			todo.update(updated_todo)
	response = Response("", status=204)
	response.headers['Location'] = "/todos/" + str(id)
	return response





#DELETE /todos/id
#Body :{'name':'test'}

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
	i = 0
	for todo in todos:
		if todo["id"] == id:
			todos.pop(i)
		i += 1
	return "";
app.run(port=5000)

'''






