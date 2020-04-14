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
curr_state = START_CELL
rewards = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
# for i in range(5):
# 	for j in range(6):	
# 		rewards[i][j] = 0.0
exploration_prob = 0.4
learning_rate = 0.25
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
		end = True
	end = False

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

def reset():
	rewards = np.zeros([5,6])
	curr_state = START_CELL


while i<rounds:
	print("Current position : ",curr_state)
	print("Game has Ended : ",end)
	if end == True:
		rewards[curr_state] = giveReward()
		for i in reversed(paths):
			reward = rewards[i]+learning_rate*(rewards[curr_state] - rewards[i])
		reset()
		i = i+1
	else:
		p = np.random.rand()
		print("Current prob : ",p)
		if(p>=exploration_prob):
			max_next_reward = 0.0
			for action in actions:
				print('Action taken : ',action)
				print('Max reward : ',max_next_reward)
				new_pos = position(action)
				r=new_pos[0]
				c=new_pos[1]
				print(new_pos)
				# rewards[r][c]
				next_reward = rewards[r][c]
				print('Next reward : ',next_reward) 
				if next_reward >= max_next_reward:
					next_pos = new_pos
					next_action = action
					max_next_reward = next_reward
		else:
			next_action = np.random.choice(actions)
			next_pos = position(next_action)
		print('Next final action : ', next_action)
		print('Next final position : ', next_pos)
		paths.append(next_pos)
		curr_state = next_pos
		if curr_state == WIN_CELL or curr_state == LOSE_CELL:
			end = True

