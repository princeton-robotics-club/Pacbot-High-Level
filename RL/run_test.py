from stable_baselines3 import PPO
from gym_simulator.gym_wrapper import PacBotEnv

import sys

import time

def print_state(state):
    grid = PacBotEnv.get_grid_from_state(state)
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

if __name__ == "__main__":
    assert len(sys.argv) == 2, "must supply algorithm argument (either DQN or PPO)"
    
    ALGORITHM = sys.argv[1]
    assert ALGORITHM in ["DQN", "PPO"], "ALGORITHM must be either DQN or PPO"
    FINAL_MODEL_NAME = ALGORITHM + "_final_model"

    model = PPO.load(FINAL_MODEL_NAME)

    # testing
    env = PacBotEnv(speed=1)
    obs = env.reset()
    print_state(obs)
    while True:
        action, _states = model.predict(obs, deterministic=True) # return deterministic actions
        obs, rewards, dones, info = env.step(action)
        print_state(obs)
        time.sleep(1)
