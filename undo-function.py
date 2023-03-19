HEIGHT = 900
WIDTH = 1500
MAX_X = 1500
MAX_Y = 900
TITLE = "Drawing App"
FRAME_RATE = 60
import pyray

pyray.init_window(MAX_X, MAX_Y, TITLE)
pyray.set_target_fps(FRAME_RATE)

squares = []

while not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.clear_background(pyray.BLACK)

    if pyray.is_mouse_button_pressed(1):
        squares.append([pyray.get_mouse_x(), pyray.get_mouse_y()])
 
    if pyray.is_key_down(pyray.KEY_Z) and len(squares) != 0:
        squares.pop()

    for square in squares:
        pyray.draw_text("X", square[0], square[1], 40, pyray.RED)
 
    pyray.end_drawing()

pyray.close_window()