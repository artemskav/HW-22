# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    new_x = 0
    new_y = 0

    def __init__(self,  x_coord, y_coord, direction, speed):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.direction = direction
        self.speed = speed

    def move(self, field, is_fly, crawl):
        if is_fly:
            self.direction_and_speed(1.2)
        elif crawl:
            self.direction_and_speed(0.5)
        else:
            raise ValueError('Рожденный ползать летать не должен!')

        field.set_unit(x=self.new_x, y=self.new_y, unit=self)

    def direction_and_speed(self, k):
        self.speed *= k
        if self.direction == 'UP':
            self.new_y = self.y_coord + self.speed
            self.new_x = self.x_coord
        elif self.direction == 'DOWN':
            self.new_y = self.y_coord - self.speed
            self.new_x = self.x_coord
        elif self.direction == 'LEFT':
            self.new_y = self.y_coord
            self.new_x = self.x_coord - self.speed
        elif self.direction == 'RIGTH':
            self.new_y = self.y_coord
            self.new_x = self.x_coord + self.speed
