import os.path

# 일정 관리 시스템
todos = []


# 일정등록: 딕셔너리로 todo 받아서 일정 등록
#           일정 제목 중복체크
def register(todoNum, title):
    todo = {}
    if exist_todo(title) < 0:
        todo['todoNum'] = todoNum
        todo['title'] = title
        todos.append(todo)
    else:
        message_display("이미 존재하는 일정입니다.")


# 일정 수정: 일정제목 받아서 있는지 확인 후 일정 수정
def update(title, new_title):
    if exist_todo(title) > -1:
        for index, todo in enumerate(todos):
            if todo['title'] == title:
                todos[index]['title'] = new_title
                message_display(f"'{title}' -> '{todos[index]['title']}'일정이 변경되었습니다.")
    else:
        message_display("존재하지 않는 일정입니다.")


# 일정 목록 조회: list todos 리턴
def getAlltodos():
    for todo in todos:
        print(f"{todo['todoNum']}번 {todo['title']}")


# 일정 삭제: title이 존재하는지 확인 후 일정 삭제
def remove_todo(title):
    if exist_todo(title) > -1:
        for index, todo in enumerate(todos):
            if todo['title'] == title:
                todos.remove(todo)
                message_display(f"{todo['todoNum']}번 '{todo['title']}'일정이 삭제되었습니다.")
    else:
        message_display("존재하지 않는 일정입니다.")


# 전체삭제
def clear_todos():
    todos.clear()


# 메뉴 display
def menu_display():
    print()
    print("=========일정관리 시스템=========")
    print("1. 일정 등록")
    print("2. 일정 수정")
    print("3. 일정 삭제")
    print("4. 일정 목록 조회")
    print("5. 일정 전체 삭제")
    print("0. 시스템 종료")


# message display
def message_display(message):
    print()
    print(message)


# 일정 존재 여부
def exist_todo(title):
    for index, todo in enumerate(todos):
        if todo['title'] == title:
            return index
    return -1


# 프로그램 종료시 list todos "todos.dat"피일 저장
def save_list():
    with open("todos.dat", "w", encoding="utf-8") as save_file:
        for index, todo in enumerate(todos):
            save_file.write(f"{todo['todoNum']} | {todo['title']}\n")


# 프로그램 시작시 "todos.dat" 파일이 존재하고 있는 경우 list todos에 저장
def init_data_load():
    fileExist = os.path.isfile("todos.dat")
    if fileExist:
        with open("todos.dat", "r", encoding="utf-8") as read_file:
            while True:
                line_data = read_file.readline()
                if len(line_data.split('|')) == 2:
                    new_todoNum = line_data.split('|')[0].strip()
                    new_title = line_data.split('|')[1].strip()
                    todos.append({"todoNum": new_todoNum, "title": new_title})
                if not line_data:
                    break


init_data_load()
while True:
    menu_display()

    menu = input("메뉴 입력: ")
    if menu == "1":
        todo = {}
        message_display("일정의 제목을 입력하세요.")
        title = input("제목: ")
        todoNum = len(todos) + 1
        register(todoNum, title)
        message_display(f"'{todos[len(todos)-1]['title']}'일정이 추가되었습니다.")


    elif menu == "2":
        print()
        print("수정할 일정의 제목을 입력하세요.")
        title_change = input("일정 제목: ")
        new_title = input("수정할 제목: ")
        new_todo = update(title_change, new_title)


    elif menu == "3":
        message_display("삭제할 일정의 제목을 입력하세요.")
        delete = input("일정 제목: ")
        remove_todo(delete)


    elif menu == "4":
        message_display("<일정 목록>")
        getAlltodos()

    elif menu == "5":
        agree = input("전체 일정을 삭제합니다.[Y]  ")
        if agree == 'Y' or agree == 'y':
            clear_todos()
            message_display("전체일정을 삭제하였습니다.")
        else:
            message_display("처음으로 돌아갑니다.")

    elif menu == "0":
        agree = input("프로그램을 종료합니다.[Y]  ")
        if agree == 'Y' or agree == 'y':
            save_list()
            break
        else:
            message_display("처음으로 돌아갑니다.")
    else:
        message_display("메뉴를 다시 입력하세요.")

