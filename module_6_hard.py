class Figure:
    def __init__(self, color):                                          # Инициализация фигуры с цветом и списком сторон
        self.__sides = []                                               # Скрытый атрибут для хранения длин сторон
        self.__color = list(color)                                      # Скрытый атрибут для хранения цвета в RGB
        self.filled = False                                             # Публичный атрибут, заполнение фигуры

    def sides_count(self):
        return len(self.__sides)                                        # Возвращает количество сторон фигуры

    def get_color(self):
        return self.__color                                             # Возвращает цвет фигуры

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))# Проверяет, корректность значения цвета

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):                              # Устанавливает цвет, если значения корректны
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0                   # Проверяет корректность новых сторон
                   for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides                                             # Возвращает длины сторон фигуры

    def __len__(self):
        return sum(self.__sides)                                        # Возвращает суммарную длину (периметр) фигуры

    def set_sides(self, *new_sides):

        if self.__is_valid_sides(*new_sides):                      # Устанавливает стороны, если кол-во сторон совпадает
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1                                                     # Количество сторон у круга

    def __init__(self, color, circumference):                           # Инициализация круга
        super().__init__(color)                                         # Вызывает конструктор родительского класса
        self.set_sides(circumference)                                   # Устанавливает длину окружности как сторону

    def get_radius(self):                                          # Вычисляет радиус круга, деля длину окружности на 2π
        circumference = self.get_sides()[0]                             # Достает длину окружности
        radius = circumference / (2 * 3.1415926536)                # Вычисляет радиус
        return radius                                                   # Возвращает радиус

    def get_square(self):                                               # Вычисляет площадь круга (πr²)
        radius = self.get_radius()                                      # Получает радиус
        square = 3.1415926536 * (radius ** 2)                      # Вычисляет площадь
        return square                                                   # Возвращает площадь


class Triangle(Figure):
    sides_count = 3                                                     # Количество сторон треугольника

    def __init__(self, color, *sides):                                  # Инициализация треугольника
        super().__init__(color)                                         # Вызывает конструктор родительского класса
        self.set_sides(*sides)                                          # Устанавливает стороны треугольника

    def get_square(self):                                               # Вычисляет площадь треугольника по Герону
        a, b, c = self.get_sides()                                      # Берет длины сторон
        s = (a + b + c) / 2                                             # Вычисляет полупериметр
        square = (s * (s - a) * (s - b) * (s - c)) ** 0.5               # Вычисляет площадь по формуле Герона
        return square                                                   # Возвращает площадь

class Cube(Figure):
    sides_count = 12                                                    # Количество сторон у куба

    def __init__(self, color, side):                                    # Инициализация куба
        super().__init__(color)                                         # Вызывает конструктор родительского класса
        self.set_sides(*([side] * 12))                                  # Устанавливает 12 одинаковых сторон

    def get_volume(self):                                               # Вычисляет объем куба (сторона^3)
        side = self.get_sides()[0]                                      # Берет длину стороны
        volume = side ** 3                                              # Вычисляет объем
        return volume                                                   # Возвращает объем


# Проверка
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина
print(len(circle1))

# Проверка объёма (куба)
print(cube1.get_volume())
