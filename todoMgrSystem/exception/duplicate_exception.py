class DuplicateException(Exception):
    def __init__(self, duplicate_todoNum):
        super().__init__(duplicate_todoNum+"는 이미 등록된 번호입니다.")
