import gym
import numpy as np

env = gym.make('CartPole-v0')

def run_episode(env, params):
	observation = env.reset()
	totalreward = 0
	for _ in range(200):
		env.render()
		action = 0 if np.matmul(params, observation) < 0 else 1
		observation, reward, done, info = env.step(action)
		totalreward += reward
		if done:
			break
	return totalreward

bestparams = None
bestreward = 0
for _ in range(10000):
	params = np.random.rand(4)*2-1 #random weight vector
	reward = run_episode(env, params)
	if reward > bestreward:
		bestreward = reward
		bestparams = params

		if reward ==200:
			env.render()
			break

print(bestparams)


	


	

