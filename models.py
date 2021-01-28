class Airflow:
    todolist_list = []

    def __init__(self, todolist_id, todolist_name=None):
        if todolist_name is None:
            todolist_name = []
        self.todolist_name = todolist_name
        self.todolist_id = todolist_id

        def add_todolist_item(todolist_item):
            todolist_item = todolist_item
            todolist_name.append(todolist_item)
            return add_todolist_item(todolist_item)

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
