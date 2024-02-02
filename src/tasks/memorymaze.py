import gym

class GymToGymnasium(gym.Wrapper):
    def __init__(self, env: gym.Env):
        gym.Wrapper.__init__(self, env)

    def reset(self, **kwargs):
        state = super().reset(**kwargs)
        info = {}
        return state, info
    
    def step(self, action):
        state, reward, done, info = self.env.step(action)
        truncated = False
        return state, reward, done, truncated, info

def create_memorymaze(env_name):
    env = gym.make(env_name)
    env = GymToGymnasium(env)
    return env 