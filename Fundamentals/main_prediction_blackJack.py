import gymnasium as gym
import numpy as np
from prediction_blackJack import Agent
import matplotlib.pyplot as plt

if __name__ == '__main__':
    env = gym.make('Blackjack-v1')
    agent = Agent()
    n_episodes = 500000
    for i in range(n_episodes):
        if i % 50000 == 0:
            print('starting episode', i)
        observation, _ = env.reset()
        done = False
        while not done:
            action = agent.policy(observation)
            observation_, reward, terminated, truncated, info = env.step(action)
            agent.memory.append((observation, reward))
            observation = observation_
            done = terminated or truncated
        agent.update_V()
    print(agent.V[(21, 3, True)])
    print(agent.V[(4, 1, False)])

