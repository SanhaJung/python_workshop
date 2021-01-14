import os.path
from entity.todo import Todo


# 프로그램 종료시 list todos "todos.dat"피일 저장
def save_list(todos):
    with open("todos.dat", "w", encoding="utf-8") as save_file:
        for index, todo in enumerate(todos):
            save_file.write(f"{todo.todoNum} | {todo.title}\n")


# 프로그램 시작시 "todos.dat" 파일이 존재하고 있는 경우 list todos에 저장
def init_data_load():
    fileExist = os.path.isfile("todos.dat")
    todos = []
    if fileExist:
        with open("todos.dat", "r", encoding="utf-8") as read_file:
            while True:
                line_data = read_file.readline()
                if len(line_data.split('|')) == 2:
                    new_todoNum = line_data.split('|')[0].strip()
                    new_title = line_data.split('|')[1].strip()
                    todos.append(Todo(new_todoNum, new_title))
                if not line_data:
                    break
    return todos