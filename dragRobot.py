import time
import mouse
import keyboard as kb

pixels_cordinates = []

def map_pixels_to_arena():
	pass


try:
	test_counter = 0
	while True:
		# if mouse.is_pressed():
		if kb.is_pressed("ctrl"):
			test_counter = 1
			print mouse.get_position()
			# pixels_cordinates.append(mouse.get_position())
			time.sleep(0.1)
		else:
			if test_counter == 1:
				break
		
except KeyboardInterrupt:
	print pixels_cordinates
	print("Press Ctrl-C to terminate while statement")
	pass