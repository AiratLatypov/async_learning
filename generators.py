from time import time
# генератор это функция
# генератор при вызове функции next идет до ключего слова yeild, но продолжает после него. Так мы можем
# писать какой-то код после генераторов
#

def gen(s):
    for i in s:
        yield i


g = gen("test text")


def get_filename():
    while True:
        pattern = "file-{}.jpeg"
        t = int(time() * 1000)
        yield pattern.format(str(t))
