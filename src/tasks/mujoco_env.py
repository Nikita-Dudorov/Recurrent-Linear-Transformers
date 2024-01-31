import gymnasium as gym

def create_mujoco_env(env_name):
    env = gym.make(env_name)
    return env 