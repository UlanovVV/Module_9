from random import choice
# Lambda - Функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(list(result))
print("Lambda-функция решена. Ниже ответ на следуюшее задание" + "\n")


def get_advanced_writer(file_name):

    def write_everything(*data_set):

        with open(file_name, 'a') as f:
            for i in data_set:
                f.write(str(i) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
print("Замыкание решено. Ниже ответ на следующее задание" + "\n")



class MysticBall:

    def __init__(self, *words):
        self.words = words


    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())