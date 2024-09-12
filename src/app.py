# libs
from flask import Flask, jsonify, request

# Criação de uma aplicação Flask
app = Flask(__name__)

# Fonte de dados
tasks = [
    {
        "id": 1,
        "title": "Estudar APIs REST",
        "description": "Ler documentação e assistir vídeos sobre APIs RESTful.",
        "status": "pendente",
        "priority": "alta",
        "created_at": "2024-09-12T10:00:00Z",
        "due_date": "2024-09-15T10:00:00Z",
        "tags": ["estudo", "desenvolvimento"],
        "subtasks": [
            {
                "id": 1,
                "title": "Ler documentação",
                "status": "concluída"
            },
            {
                "id": 2,
                "title": "Assistir vídeos",
                "status": "pendente"
            }
        ]
    },
    {
        "id": 2,
        "title": "Estudar Python",
        "description": "Ler documentação e assistir vídeos sobre Python.",
        "status": "pendente",
        "priority": "alta",
        "created_at": "2024-09-12T10:00:00Z",
        "due_date": "",
        "tags": ["estudo", "desenvolvimento"],
        "subtasks": [
            {
                "id": 1,
                "title": "Ler documentação",
                "status": "concluída"
            },
            {
                "id": 2,
                "title": "Assistir vídeos",
                "status": "pendente"
            }
        ]
    }
]

# Consultar todas as tarefas
@app.route('/tasks', methods=['GET'])
def consultar_tasks():
    return jsonify(tasks)

# Consultar tarefa por id
@app.route('/tasks/<int:id>', methods=['GET'])
def consultar_task_id(id):
    for task in tasks:
        if task.get('id') == id:
            return jsonify(task)
        
# Editar uma task por id
@app.route('/tasks/<int:id>', methods=['PUT'])
def editar_task_id(id):
    task_modificada = request.get_json()
    for indice, task in enumerate(tasks):
        if task.get('id') == id:
            tasks[indice].update(task_modificada)
            return jsonify(tasks[indice])

# Criar uma task
@app.route('/tasks', methods=['POST'])
def criar_task():
    nova_task = request.get_json()
    tasks.append(nova_task)
    return jsonify(nova_task)

# Deletar uma task por id
@app.route('/tasks/<int:id>', methods=['DELETE'])
def deletar_task(id):
    for indice, task in enumerate(tasks):
        if task.get('id') == id:
            del tasks[indice]
    return jsonify(tasks)

app.run(port=5000, host='localhost', debug=True)