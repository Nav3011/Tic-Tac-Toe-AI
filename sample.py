		#(0,0)		(0,1)		(0,2)		(0,3)		(0,4)		(0,5)					-	-	+	-	-	*
		#(1,0)		(1,1)		(1,2)		(1,3)		(1,4)		(1,5)					o	-	o	-	-	-
		#(2,0)		(2,1)		(2,2)		(2,3)		(2,4)		(2,5)					-	-	-	o	o	-
		#(3,0)		(3,1)		(3,2)		(3,3)		(3,4)		(3,5)					-	-	o	-	-	o
		#(4,0)		(4,1)		(4,2)		(4,3)		(4,4)		(4,5)					$	-	-	-	o	-

import numpy as np
actions = ['up', 'down', 'left', 'right']
WIN_CELL = (0,5)
LOSE_CELL = (0,2)
START_CELL = (4,0)

i=0
rounds = 1
curr_state = WIN_CELL
rewards = np.zeros([5,6])
exploration_prob = 0.4
paths = list()
end = False
def giveReward():
	if curr_state == WIN_CELL:
		return 1
	elif curr_state == LOSE_CELL:
		return -1
	else:
		return 0
def gamehasEnded():
	if curr_state == WIN_CELL or curr_state == LOSE_CELL:
		return True
	return False

def position(action):
	if action == 'up':
		pos = (curr_state[0]-1, curr_state[1])
	elif action == 'down':
		pos = (curr_state[0]+1, curr_state[1])
	elif action == 'left':
		pos = (curr_state[0], curr_state[1]-1)
	else:
		pos = (curr_state[0], curr_state[1]+1)
	if(pos[0]>=0 or pos[0]<=4):
		if(pos[1]>=0 or pos[1]<=5):
			return pos
	return curr_state


while i<rounds:
	if gamehasEnded:
		rewards[curr_state] = giveReward()
		# print()
		# reverse order to update the rewards
		# reset the game
		i = i+1
	else:
		p = np.random.rand()
		if(p>=exploration_prob):
			max_next_reward = 0.0
			for action in actions:
				new_pos = position[action]
				next_reward = rewards[new_pos]
				if next_reward >= max_next_reward:
					next_pos = new_pos
					next_action = action
					max_next_reward = next_reward
			paths.append(next_pos)
			curr_state = next_pos
			