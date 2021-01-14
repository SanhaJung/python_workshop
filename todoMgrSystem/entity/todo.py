class Todo:
    # 생성자: todoNum, title
    def __init__(self, todoNum, title):
        self.todoNum = todoNum
        self.title = title

    # 객체 todoNum이 같은 경우 True
    def __eq__(self, todoNum):
        if self.todoNum == todoNum:
            return True
        else:
            return False

    # 객체를 대표하는 문자열
    def __str__(self):
        return f"{self.todoNum}번 {self.title}"
