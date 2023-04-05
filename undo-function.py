'''Note: Left-click to draw'''

import pyray

HEIGHT = 900
WIDTH = 1500
MAX_X = 1500
MAX_Y = 900
TITLE = "Drawing App"
FRAME_RATE = 60

pyray.init_window(MAX_X, MAX_Y, TITLE)
pyray.set_target_fps(FRAME_RATE)

squares = []
z_pressed = False
game_over = False

while not game_over and  not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.clear_background(pyray.BLACK)

    if pyray.is_mouse_button_pressed(0):
        squares.append([pyray.get_mouse_x(), pyray.get_mouse_y()])
 
    # to detect key up, use is_key_up
    if pyray.is_key_down(pyray.KEY_Q):
        game_over = True

    if pyray.is_key_down(pyray.KEY_Z):
        z_pressed = True

    if z_pressed and pyray.is_key_up(pyray.KEY_Z) and len(squares) != 0:
        squares.pop()
        z_pressed = False

    for square in squares:
        pyray.draw_text("o", square[0], square[1], 40, pyray.RED)
 
    pyray.end_drawing()

pyray.close_window()