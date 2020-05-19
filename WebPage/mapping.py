from __future__ import division

GUI_MIN_COORD = (0, 0)
GUI_MAX_COORD = (1000, 425)
ARENA_MIN_COORD = (0, 0)
ARENA_MAX_COORD = (10, 8)

def pixels2meter(pix, invert=True, GUI_MAX_COORD=GUI_MAX_COORD):
	x_vals = pix['x']
	y_vals = pix['y']

	M2m = 1000 #meter to mm
	XdistPerPix = ARENA_MAX_COORD[0] * M2m / GUI_MAX_COORD[0]
	YdistPerPix = ARENA_MAX_COORD[1] * M2m / GUI_MAX_COORD[1]
	cx = []
	cy = []

	for i in range(len(x_vals)):
		if  x_vals[i] > GUI_MAX_COORD[0] or \
			x_vals[i] < GUI_MIN_COORD[0] or \
			y_vals[i] > GUI_MAX_COORD[1] or \
			y_vals[i] < GUI_MIN_COORD[1]: 
			continue
		else:
			x_in_meters = x_vals[i] * XdistPerPix / M2m
			if invert:
				y_vals[i] = GUI_MAX_COORD[1] - y_vals[i]
			y_in_meters = y_vals[i] * YdistPerPix / M2m
			cx.append(round(x_in_meters, 3))
			cy.append(round(y_in_meters, 3))
	return {'x': cx, 'y': cy}	

def meter2pixel(met, invert=True, GUI_MAX_COORD=GUI_MAX_COORD):
	x_vals = met['x']
	y_vals = met['y']

	M2m = 1000 #meter to mm
	XPixPerMm = GUI_MAX_COORD[0] / (ARENA_MAX_COORD[0] * M2m)
	YPixPerMm = GUI_MAX_COORD[1] / (ARENA_MAX_COORD[1] * M2m)
	cx = []
	cy = []

	for i in range(len(x_vals)):
		if  x_vals[i] > ARENA_MAX_COORD[0] or \
			x_vals[i] < ARENA_MIN_COORD[0] or \
			y_vals[i] > ARENA_MAX_COORD[1] or \
			y_vals[i] < ARENA_MIN_COORD[1]: 
			continue
		else:
			x_in_pix = x_vals[i] * M2m * XPixPerMm
			if invert:
				y_vals[i] = ARENA_MAX_COORD[1] - y_vals[i]
			y_in_pix = y_vals[i] * M2m * YPixPerMm
			cx.append(x_in_pix)
			cy.append(y_in_pix)
	return {'x': cx, 'y': cy}