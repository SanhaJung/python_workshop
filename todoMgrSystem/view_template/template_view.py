from entity.todo import Todo


def menu_display():
    print()
    print("=========일정관리 시스템=========")
    print("1. 일정 등록")
    print("2. 일정 수정")
    print("3. 일정 삭제")
    print("4. 일정 목록 조회")
    print("5. 일정 전체 삭제")
    print("0. 시스템 종료")


def menu_select_display():
    print()
    menu = input("메뉴 입력: ")
    return menu


def message_display(message):
    print()
    print(message)


def list_display(todos):
    print("<일정 목록>")
    for todo in todos:
        print(todo)         # Todo의 재정의한 __str__


def input_display():
    print("일정의 제목을 입력하세요.")
    todoNum = input("일정 번호: ")
    title = input("일정 제목: ")
    return Todo(todoNum, title)


def update_display():
    todoNum = input("수정할 일정 번호: ")
    title = input("수정할 제목: ")
    return (todoNum, title)


def delete_display():
    todoNum = input("삭제할 일정 번호: ")
    return todoNum
