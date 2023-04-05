# II. Stack

## Why Stacks?

<p>You'll find stacks in many places: the call stack, your browser history, the word processor undo button, etc.</p>
<p>The reason stacks find so many uses, is because they are the simplest data structure that (1) keeps track of the last thing put in and (2) returns the last thing put in.</p>
<p>This is called LIFO (Last in First Out). The last thing you put on, comes off first</p>

## Stack And Heap

<p> A form of memory
management is also referred to as the "stack"--more precisely,
it is the memory reserved for local variables that belong to functions
that are in the call stack. Each time a function is called, it gets added to the call stack. When an error occurs, the current state
of the call stack is printed for debugging purposes, called a stack trace.</p>
<p>This form of memory is in contrast to the heap, which is used for everything else that isn't simply a local, temporary variable. The key difference is that memory is allocated specifically somewhere with an accessible address. This is what happens when you create an object in C++ using the new keyword, which is often simply passed into a smart pointer to manage that memory automatically.</p>
<p>Since the heap is used for everything else, it has much more capacity than the stack. If you try make a local variable that takes up too much memory, you can get a stack overflow error.</p>
<p>For example, int hugeArray[1000000] does it for me, but half that
(int hugeArray[500000]) doesn't, so I'd be careful going anywhere
over 100,000 ints, or 400 kilobytes.
CAREFUL -- this error can be silent!!! There was no indication for
me other than the console not printing any output when it finished.</p>
<p>Other possible triggers of the error are infinite recursion, and even regular recursion if it goes too deep. Every time
you enter another layer of function more memory is reserved for it
on the stack. Non-recursive functions nested too deeply will do it too.</p>

## Guess-a-Stack Example

Make word game where you have to put letters in right order.

	answer = ["r", "o", "c", "k"]
	letters = []
	gameover = False

	while gameover != True:
		letter = input("Guess the next letter: ")
		letters.append(letter)
		print(f"Current letters: {letters}")

		if letter != answer[len(letters) - 1]:
			letters.pop()
			print("Last letter not a match, try again.")
			print(f"Current letters: {letters}")

		if letters == answer:
			gameover = True

## Undo Function Problem
Finish implementing the missing undo function for a simple
drawing app.

	'''Note: Left-click to draw'''

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
	game_over = False

	while not game_over and  not pyray.window_should_close():
		pyray.begin_drawing()
		pyray.clear_background(pyray.BLACK)

		if pyray.is_mouse_button_pressed(0):
			squares.append([pyray.get_mouse_x(), pyray.get_mouse_y()])
	
		# to detect key up, use is_key_up
		if pyray.is_key_down(pyray.KEY_Q):
			game_over = True

		for square in squares:
			pyray.draw_text("o", square[0], square[1], 40, pyray.RED)
	
		pyray.end_drawing()

	pyray.close_window()

# Solution

	'''Note: Left-click to draw'''

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



