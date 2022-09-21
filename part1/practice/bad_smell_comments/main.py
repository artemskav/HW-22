class Unit:

    def movement_object_field(self, field, x_koord: int, y_koord: int, directions,
                              fly: bool, crawl: bool, speed: int = 1):
        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')
        if fly:
            speed *= 1.2
            if directions == 'UP':
                new_y = y_koord + speed
                new_x = x_koord
            elif directions == 'DOWN':
                new_y = y_koord - speed
                new_x = x_koord
            elif directions == 'LEFT':
                new_y = y_koord
                new_x = x_koord - speed
            elif directions == 'RIGHT':
                new_y = y_koord
                new_x = x_koord + speed
        if crawl:
            speed *= 0.5
            if directions == 'UP':
                new_y = y_koord + speed
                new_x = x_koord
            elif directions == 'DOWN':
                new_y = y_koord - speed
                new_x = x_koord
            elif directions == 'LEFT':
                new_y = y_koord
                new_x = x_koord - speed
            elif directions == 'RIGHT':
                new_y = y_koord
                new_x = x_koord + speed

            field.set_unit(x=new_x, y=new_y, unit=self)
