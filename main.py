import random as r
import arcade

width_screen = 750
height_screen = 750


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width_screen, height_screen, "Snake")
        self.snake_position = []
        self.start_postion = [8, 8]
        self.apple = []
        self.direction = [0, -1]
        self.direction_chosen = False
        self.show_lines = False

    def setup(self):
        for i in range(3):
            self.snake_position.append([self.start_postion[0], self.start_postion[1]+3-i])
        self.snake_position.append(self.start_postion)
        arcade.schedule(self.move, 0.5)

    def on_draw(self):
        arcade.start_render()

        if self.apple != []:
            arcade.draw_rectangle_filled((self.apple[0]-1) * 50 + 25, (self.apple[1]-1) * 50 + 25, 50, 50, arcade.color.RED)

        for i in self.snake_position:
            if self.snake_position.index(i) != len(self.snake_position)-1:
                arcade.draw_rectangle_filled((i[0]-1)*50+25, (i[1]-1)*50+25, 50, 50, arcade.color.BLUE)

        arcade.draw_rectangle_filled((self.snake_position[-1][0] - 1) * 50 + 25, (self.snake_position[-1][1] - 1) * 50 + 25, 50, 50,arcade.color.DARK_BLUE)

        if self.show_lines:
            for x in range(15):
                arcade.draw_line(0, x*50, 850, x*50, arcade.color.RED)
                for y in range(15):
                    arcade.draw_line(x*50, 0, x*50, 850, arcade.color.RED)

    def move(self, delta_time):
        if self.apple == []:
            self.apple = [r.randint(1, 15), r.randint(1, 15)]
            while self.apple in self.snake_position:
                self.apple = [r.randint(1, 15), r.randint(1, 15)]

        if self.snake_position[-1] == self.apple:
            self.apple = []
            self.snake_position.append([self.snake_position[-1][0]+self.direction[0], self.snake_position[-1][1]+self.direction[-1]])
        else:
            self.snake_position.append([self.snake_position[-1][0] + self.direction[0], self.snake_position[-1][1] + self.direction[-1]])
            self.snake_position.pop(0)

        self.direction_chosen = False

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W and self.direction != [0, -1] and self.direction_chosen == False:
            self.direction = [0, 1]
            self.direction_chosen = True

        elif key == arcade.key.S and self.direction != [0, 1] and self.direction_chosen == False:
            self.direction = [0, -1]
            self.direction_chosen = True

        elif key == arcade.key.A and self.direction != [1, 0] and self.direction_chosen == False:
            self.direction = [-1, 0]
            self.direction_chosen = True

        elif key == arcade.key.D and self.direction != [-1, 0] and self.direction_chosen == False:
            self.direction = [1, 0]
            self.direction_chosen = True


def main():
    game = Game()
    game.setup()
    arcade.run()


main()
