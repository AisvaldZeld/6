import gym
import random
import matplotlib.pyplot as plt
import numpy as np
env = gym.make("CartPole-v1")
env._max_episode_steps = 1000
observation = env.reset()

def Random_solution(solution):
  result = []
  for i in range(solution):
    result.append(random.random() - 0.5)
  return result

def calc_mean(data):
  sum = 0
  for i in data:
    sum += i
  return sum / len(data)

def Mutate(x):
  neighbour = x[:]
  c = random.randint(0, len(neighbour) - 1)
  m = (random.random() - 0.5)
  neighbour[c] = m

  return neighbour

if __name__ == "__main__":

  best = Random_solution(4)
  best_cost = 0
  counter = 0

  plot_x = []
  plot_y = []
  plot_z = []

  plt.ion()

  T = 1.0
  Tmin = 0.001
  alpha = 0.99

  count = 1

  for _ in range(100000):
    # action = random.randint(0,1)

    if observation[2] > 0:
      action = 1
    else:
      action = 0

    env.render()

    observation, reward, done, info = env.step(action)

    if done:
      observation = env.reset()

      plot_x.append(_)
      plot_y.append(counter)
      plot_z.append(calc_mean(plot_y))

      print("mean score: ", calc_mean(plot_y))

      plt.clf()
      plt.plot(plot_x, plot_y)
      plt.plot(plot_x, plot_z)
      plt.draw()
      plt.pause(0.0001)

      print(best)
      counter = 0
    else:
      counter += 1

  plt.ioff()
  plt.show()
  env.close()
