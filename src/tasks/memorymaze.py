import gymnasium as gym
import os

os.environ['MUJOCO_GL']='osmesa'

# class GymToGymnasium(gym.Wrapper):
#     def __init__(self, env: gym.Env):
#         gym.Wrapper.__init__(self, env)

#     def reset(self, seed=None, options=None):
#         # TODO: pass seed on reset
#         state = self.env.reset()
#         info = {}
#         return state, info
    
#     def step(self, action):
#         state, reward, done, info = self.env.step(action)
#         truncated = info.get('TimeLimit.truncated', False)
#         return state, reward, done, truncated, info

def create_memorymaze(env_name):
    env = gym.make(env_name)
    # env = GymToGymnasium(env)
    return env 