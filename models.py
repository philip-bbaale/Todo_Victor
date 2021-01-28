class Airflow:
    todolist_list = []

    def __init__(self, todolist_name):
        self.todoList_name = todolist_name

    def save_todolist_item(self):
        Airflow.todolist_list.append(self)

