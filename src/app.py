from flask import Flask
from flask import Flask, jsonify
from flask import request


app = Flask(__name__)

todos =  [ { "label": "My first task", "done": False },
]


@app.route('/todos', methods=['GET'])
def hello_world():
        json_text = jsonify(todos)

        return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # Decode request body
    request_body = request.json
    print("Incoming request with the following body", request_body)

    # Add the new task to the todos list
    todos.append(request_body)

    # Return the updated todos list
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]

    return jsonify(todos)





# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)