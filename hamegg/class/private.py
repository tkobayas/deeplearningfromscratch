class Spam:
    __attr = 100
    def __init__(self):
        self.__attr = 999
    def method(self):
        self.__method()
    def __method(self):
        print(self.__attr)

spam =Spam()
spam.method()   #OK
spam.__method() #NG
spam.__attr     #NG
