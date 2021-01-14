from controller_view.todo_controller import TodoController
from view_template.template_view import menu_display, menu_select_display
from view_template.template_view import input_display, delete_display
from view_template.template_view import message_display, update_display

controller = TodoController()  # 클래스 선언할때 괄호쓰기
controller.file_read()

while True:
    menu_display()
    menu = menu_select_display()  # 함수 선언할대 괄호 쓰기

    if menu == "1":
        todo = input_display()
        controller.register(todo)

    elif menu == "2":
        todoNum, title = update_display()
        controller.update(todoNum, title)

    elif menu == "3":
        todoNum = delete_display()
        controller.remove(todoNum)

    elif menu == "4":
        controller.getAlltodos()

    elif menu == "5":
        agree = input("전체 일정을 삭제합니다.[Y]  ")
        if agree == 'Y' or agree == 'y':
            controller.clear()
            message_display("전체일정을 삭제하였습니다.")
        else:
            message_display("처음으로 돌아갑니다.")

    elif menu == "0":
        agree = input("프로그램을 종료합니다.[Y]  ")
        if agree == 'Y' or agree == 'y':
            controller.file_write()
            break
        else:
            message_display("처음으로 돌아갑니다.")
    else:
        message_display("메뉴를 다시 입력하세요.")
