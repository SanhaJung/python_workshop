# 비즈니스 로직처리
from exception.duplicate_exception import DuplicateException
from exception.idnotfound_exception import IDNotFoundException
from dao.todo_file import init_data_load, save_list


# 일정 관리 시스템
class TodoService:

    todos = []

    def is_exist(self, todoNum):
        for index, todo in enumerate(TodoService.todos):
            if todo.todoNum == todoNum:
                return index
        return -1

    def register(self, todo):
        index = self.is_exist(todo.todoNum)
        if index < 0:
            TodoService.todos.append(todo)
            return f"{todo.todoNum}번 {todo.title}이 등록되었습니다.\n"
        else:
            try:
                raise DuplicateException(todo.todoNum)
            except DuplicateException as inputError:
                return str(inputError)

    def getAlltodos(self):
        return TodoService.todos

    def update(self, todoNum, title_new):
        index = self.is_exist(todoNum)
        if index > -1:
            for i, todo in enumerate(TodoService.todos):
                if todo.todoNum == todoNum:
                    temp = todo.title
                    TodoService.todos[i].title = title_new
                    return f"'{temp}' -> '{TodoService.todos[i].title}'일정이 변경되었습니다."
        else:
            try:
                raise IDNotFoundException(todoNum)
            except IDNotFoundException as updateError:
                return str(updateError)

    def remove(self, todoNum):
        index = self.is_exist(todoNum)
        if index > -1:
            for i, todo in enumerate(TodoService.todos):
                if todo.todoNum == todoNum:
                    TodoService.todos.remove(todo)
                    return f"{todo.todoNum}번 '{todo.title}'일정이 삭제되었습니다."
        else:
            try:
                raise IDNotFoundException(todoNum)
            except IDNotFoundException as removeError:
                return str(removeError)

    def clear(self):
        TodoService.todos.clear()

    def file_read(self):
        TodoService.todos = init_data_load()

    def file_write(self):
        save_list(TodoService.todos)
