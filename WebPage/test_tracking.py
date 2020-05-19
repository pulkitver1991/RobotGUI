import mapping as Map
import pure_pursuit as G2G
from pure_pursuit import State

import matplotlib.pyplot as plt
show_animation = True

def tracking(path):
	target_speed = 0.3
	cx = path['x']
	cy = path['y']
	cyaw = [0]*len(cx)
	lastIndex = len(cx) - 1
	# initial state of the robot
	state = State(x=cx[0], y=cy[0], yaw=1.57, v=0.0)
	x = [state.x]
	y = [state.y]
	yaw = [state.yaw]
	v = [state.v]
	# w = [state.w]
	target_ind = G2G.calc_target_index(state, cx, cy)

	while (lastIndex > target_ind):
		ai = G2G.PIDControl(target_speed, state.v)
		di, target_ind = G2G.pure_pursuit_control(state, cx, cy, target_ind)
		state = G2G.update(state, ai, di)
		# print state.x, state.y
		x.append(state.x)
		y.append(state.y)
		yaw.append(state.yaw)
		v.append(state.v)
		# w.append(state.w)
		pose = Map.meter2pixel({'x':[state.x], 'y': [state.y]})
		# print pose	

		if show_animation:
			plt.cla()
			plt.plot(cx, cy, ".r", label="course")
			plt.plot(x, y, "-b", label="trajectory")
			plt.plot(cx[target_ind], cy[target_ind], "xg", label="target")
			plt.axis("equal")
			plt.grid(True)
			plt.title("Speed[km/h]:" + str(state.v * 3.6)[:4])
			plt.pause(0.001)

path =  {'y': [2.296, 2.578, 2.879, 3.199, 3.482, 3.726, 3.858, 3.952, 4.009, 4.046, 4.046, \
			   4.065, 4.065, 4.065, 4.046, 4.009, 3.915, 3.821, 3.67, 3.501, 3.369, 3.237, \
			   3.105, 2.992, 2.879, 2.842, 2.804, 2.785, 2.785, 2.785, 2.823, 2.879, 2.917, 2.936], 
		 'x': [1.944, 1.987, 2.041, 2.117, 2.214, 2.377, 2.539, 2.701, 2.863, 3.068, 3.241, \
			   3.468, 3.631, 3.847, 4.041, 4.268, 4.452, 4.636, 4.831, 5.014, 5.166, 5.36, 5.544, \
			   5.717, 5.89, 6.063, 6.258, 6.441, 6.625, 6.787, 6.993, 7.198, 7.371, 7.468]}

tracking(path)