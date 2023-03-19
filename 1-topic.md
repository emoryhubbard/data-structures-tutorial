# II. Stack
## Why Stacks?
	Talk about applications for performance and history.
	Relevant personal notes: Stack topic.

<p>You'll find stacks in many places: the call stack, your browser history, the word processor undo button, etc.</p>
<p>The reason stacks find so many uses, is because they are the simplest data structure that (1) keeps track of the last thing put in and (2) returns the last thing put in.</p>
<p>This is called LIFO (Last in First Out). The last thing you put on, comes off first</p>

## Stack And Heap
	Talk about applications of stack in memory
	management for C++, and well-known stack-related
	errors like stack overflow.
	Relevant personal notes: C++ stack topic, Stack overflow topic.

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
	Relevant personal notes: Rocketship project topic.

	Note: Right-click to draw

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

		for square in squares:
			pyray.draw_text("X", square[0], square[1], 40, pyray.RED)
	
		pyray.end_drawing()

	pyray.close_window()

# Solution

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



