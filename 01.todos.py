todos = []
index = 0

while True:
    print("=========일정관리 시스템=========")
    print("1. 일정 등록")
    print("2. 일정 수정")
    print("3. 일정 삭제")
    print("4. 일정 목록 조회")
    print("5. 일정 전체 삭제")
    print("0. 시스템 종료")

    print()
    menu = input("메뉴 입력: ")
    if menu == "1":
        todo = {}
        print()
        print("일정의 제목을 입력하세요.")
        title = input("제목: ")
        todo["title"] = title

        todo["todoNum"] = index + 1
        index += 1
        todos.append(todo)
        print()
        print("'{0}'일정이 추가되었습니다.".format( todo["title"]))
        print()
    elif menu == "2":
        print()
        print("수정할 일정의 제목을 입력하세요.")
        title_change = input("일정 제목: ")
        for todo in todos:
            if todo['title'] == title_change:
                temp_title = todo['title']
                new_title = input("수정할 제목: ")
                todo['title'] = new_title
                print()
                print("{0}번 {1} -> {2} 수정되었습니다.".format(todo["todoNum"], temp_title, todo['title']))
                print()
    elif menu == "3":
        print()
        print("삭제할 일정의 제목을 입력하세요.")
        delete = input("일정 제목: ")
        for todo in todos:
            if todo['title'] == delete:
                print()
                print("{0}번 '{1}'일정이 삭제되었습니다.".format(todo["todoNum"], todo['title']))
                print()
                todos.remove(todo)


    elif menu == "4":
        print()
        print("<일정 목록>")
        for todo in todos:
            print("{0}번 {1}".format(todo["todoNum"], todo["title"]))
        print()
    elif menu == "5":
        agree = input("전체 일정을 삭제합니다.[Y]  ")
        if agree == 'Y' or agree == 'y':
            todos.clear()
            print()
            print("전체일정을 삭제하였습니다.")
            print()
        else:
            print()
            print("처음으로 돌아갑니다.")
            print()
    elif menu == "0":
        agree = input("프로그램을 종료합니다.[Y]  ")
        if agree == 'Y' or agree == 'y':
            break
        else:
            print()
            print("처음으로 돌아갑니다.")
            print()
    else:
        print()
        print("메뉴를 다시 입력하세요.")
        print()
