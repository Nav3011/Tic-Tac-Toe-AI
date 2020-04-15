import numpy as np
actions = ['up', 'down', 'left', 'right']
WIN_CELL = (0,5)
LOSE_CELL = (0,2)
START_CELL = (4,0)


epochs = 50
count = 0
curr_state = START_CELL
rewards = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

exploration_prob = 0.4
learning_rate = 0.25
path = []
end = 0

def position(action):
	# print('CURRENT : ',curr_state)
	# print('ACTION  :',action)
	new=curr_state
	if action == 'up':
		pos = (curr_state[0]-1, curr_state[1])
	elif action == 'down':
		pos = (curr_state[0]+1, curr_state[1])
	elif action == 'left':
		pos = (curr_state[0], curr_state[1]-1)
	else:
		pos = (curr_state[0], curr_state[1]+1)
	if (pos[0] >= 0) and (pos[0] <= 4):
		if (pos[1] >= 0) and (pos[1] <= 5):
			if pos not in [(1,0),(1,2),(3,2),(2,3),(2,4),(4,4)]:
	# if((pos[0] in [0,1,2,3,4]) and (pos[1] in [0,1,2,3,4,5])):
				new = pos
	else:
		new = curr_state
	# print('NEXT : ',new)
	return new
def reset():
	rewards = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]	
	curr_state = START_CELL
	path = []	

def show_reward_matrix():
	for i in range(len(rewards)):
		for j in range(len(rewards[0])):
			# print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format())
			print(rewards[i][j],end='\t')
		print()	
# check for the game end
# if the game has ended then end variable would 
while count < epochs:
	print('GAME STATUS : ', end)
	if end == 1:
		if curr_state == WIN_CELL:
			reward = 1
		elif curr_state == LOSE_CELL:
			reward = -1
		else:
			reward = 0
		rewards[curr_state[0]][curr_state[1]] = reward
		reward_path = path[::-1]
		# print('REWARD PATH : ')
		# print(reward_path)
		# print(reward)
		for i in reward_path:
			reward = rewards[i[0]][i[1]] + learning_rate*(reward - rewards[i[0]][i[1]])
			rewards[i[0]][i[1]]=round(reward,3)
		# print('REWARD : ')
		show_reward_matrix()
		reset()
		count = count + 1
	else:
		prob = round(np.random.rand(),2)
		# print('PROBABILITY : ', prob)
		if prob >= exploration_prob:
			max_reward = 0.0
			for action in actions:
				temp_pos = position(action)
				reward_at_pos = rewards[temp_pos[0]][temp_pos[1]]
				if reward_at_pos >= max_reward:
					new_action = action
					new_position = temp_pos
					max_reward = reward_at_pos
		else:
			new_action = np.random.choice(actions)
			new_position = position(new_action)
		path.append(new_position)
		# print("CURRENT : {0}\t ACTION : {1}\t NEW : {2}".format(curr_state,new_action,new_position))
		curr_state = new_position
		if curr_state == WIN_CELL or curr_state == LOSE_CELL:
			end = 1
	# print('PATH : ')
	# print(path)
	