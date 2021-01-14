# 입력데잍 valid 체크, service에 비즈니스 로직 호출, data 저장, view(template) 선택

from service.todo_service import TodoService
from view_template.template_view import message_display, list_display


class TodoController:

    def register(self, todo):
        service = TodoService()
        bm = service.register(todo)
        message_display(bm)

    def getAlltodos(self):
        service = TodoService()
        todos = service.getAlltodos()
        list_display(todos)

    def update(self, todoNum, title_new):
        if todoNum == "" or title_new == "":
            message_display("일정 번호와 제목 입력이 필요합니다.")
        service = TodoService()
        message = service.update(todoNum, title_new)
        message_display(message)

    def remove(self, todoNum):
        if todoNum == "":
            message_display("일정 번호 입력이 필요합니다.")
        service = TodoService()
        message = service.remove(todoNum)
        message_display(message)

    def clear(self):
        service = TodoService()
        service.clear()

    def file_read(self):
        service = TodoService()
        service.file_read()

    def file_write(self):
        service = TodoService()
        service.file_write()
