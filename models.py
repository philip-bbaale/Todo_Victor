class Airflow:
    todolist_list = []

    def __init__(self, todolist_name):
        self.todoList_name = todolist_name

    def save_todolist_item(self):
        Airflow.todolist_list.append(self)

    @classmethod
    def todolist_exists(cls, todolist_name):
        for list_name in cls.todolist_list:
            if list_name.todolist_name == todolist_name:
                return True
            return False

    @classmethod
    def display_todolist_list(cls):
        return cls.todolist_list

    def delete_todolist_list(self):
        Airflow.todolist_list.remove(self)


class TodoList:
    def __init__(self, todolist_name):
        self.todolist_name = todolist_name
