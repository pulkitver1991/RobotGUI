from __future__ import division

GUI_MIN_COORD = (0, 0)
GUI_MAX_COORD = (1000, 425)
ARENA_MIN_COORD = (0, 0)
ARENA_MAX_COORD = (10, 8)

# pix = 		{'y': [121.96665954589844, 136.96665954589844, 152.96665954589844, 169.96665954589844, \
# 				  184.96665954589844, 197.96665954589844, 204.96665954589844, 209.96665954589844, \
# 				  212.96665954589844, 214.96665954589844, 214.96665954589844, 215.96665954589844, \
# 				  215.96665954589844, 215.96665954589844, 214.96665954589844, 212.96665954589844, \
# 				  207.96665954589844, 202.96665954589844, 194.96665954589844, 185.96665954589844, \
# 				  178.96665954589844, 171.96665954589844, 164.96665954589844, 158.96665954589844, \
# 				  152.96665954589844, 150.96665954589844, 148.96665954589844, 147.96665954589844, \
# 				  147.96665954589844, 147.96665954589844, 149.96665954589844, 152.96665954589844, \
# 				  154.96665954589844, 155.96665954589844], \
# 			'x': [179.8333282470703, 183.8333282470703, 188.8333282470703, 195.8333282470703, \
# 				  204.8333282470703, 219.8333282470703, 234.8333282470703, 249.8333282470703, \
# 				  264.8333282470703, 283.8333282470703, 299.8333282470703, 320.8333282470703, \
# 				  335.8333282470703, 355.8333282470703, 373.8333282470703, 394.8333282470703, \
# 				  411.8333282470703, 428.8333282470703, 446.8333282470703, 463.8333282470703, \
# 				  477.8333282470703, 495.8333282470703, 512.8333282470703, 528.8333282470703, \
# 				  544.8333282470703, 560.8333282470703, 578.8333282470703, 595.8333282470703, \
# 				  612.8333282470703, 627.8333282470703, 646.8333282470703, 665.8333282470703, \
# 				  681.8333282470703, 690.8333282470703]}
# met = 		{'y': [2.296, 2.578, 2.879, 3.199, 3.482, 3.726, 3.858, 3.952, 4.009, 4.046, 4.046, \
# 				   4.065, 4.065, 4.065, 4.046, 4.009, 3.915, 3.821, 3.67, 3.501, 3.369, 3.237, \
# 				   3.105, 2.992, 2.879, 2.842, 2.804, 2.785, 2.785, 2.785, 2.823, 2.879, 2.917, 2.936], 
# 			 'x': [1.944, 1.987, 2.041, 2.117, 2.214, 2.377, 2.539, 2.701, 2.863, 3.068, 3.241, \
# 			 	   3.468, 3.631, 3.847, 4.041, 4.268, 4.452, 4.636, 4.831, 5.014, 5.166, 5.36, 5.544, \
# 			 	   5.717, 5.89, 6.063, 6.258, 6.441, 6.625, 6.787, 6.993, 7.198, 7.371, 7.468]}

def pixels2meter(pix, invert=True):
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

def meter2pixel(met, invert=True):
	x_vals = met['x']
	y_vals = met['y']

	M2m = 1000 #meter to mm
	XPixPerMm = GUI_MAX_COORD[0] / (ARENA_MAX_COORD[0] * M2m)
	YPixPerMm = GUI_MAX_COORD[1] / (ARENA_MAX_COORD[1] * M2m)
	# print "YPixPerMm", XPixPerMm, YPixPerMm
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

# def meter2pixel(met):
# 	x_vals = met['x']
# 	y_vals = met['y']

# 	M2m = 1000 #meter to mm
# 	XPixPerMm = GUI_MAX_COORD[0] / (ARENA_MAX_COORD[0] * M2m)
# 	YPixPerMm = GUI_MAX_COORD[1] / (ARENA_MAX_COORD[1] * M2m)
# 	cx = []
# 	cy = []

# 	for i in range(len(x_vals)):
# 		if  x_vals[i] > ARENA_MAX_COORD[0] or \
# 			x_vals[i] < ARENA_MIN_COORD[0] or \
# 			y_vals[i] > ARENA_MAX_COORD[1] or \
# 			y_vals[i] < ARENA_MIN_COORD[1]: 
# 			continue
# 		else:
# 			x_in_pix = x_vals[i] * M2m * XPixPerMm
# 			y_in_pix = y_vals[i] * M2m * YPixPerMm
# 			cx.append(x_in_pix)
# 			cy.append(y_in_pix)
# 	return {'x': cx, 'y': cy}
