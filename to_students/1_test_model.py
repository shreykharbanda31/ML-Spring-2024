"""Test a random policy.

Author: Elie KADOCHE.
"""

import torch

from src.envs.cartpole_v0 import CartpoleEnvV0
from src.envs.cartpole_v1 import CartpoleEnvV1
from src.models.actor_v0 import ActorModelV0
from src.models.actor_v1 import ActorModelV1
import numpy as np

if __name__ == "__main__":
    # Create environment and policy
    env = CartpoleEnvV0()
    policy = ActorModelV0()

    # ------------------------------------------
    # ---> TODO: UNCOMMENT FOR SECTION 4 ONLY
    env = CartpoleEnvV1()
    policy = ActorModelV1()
    # ------------------------------------------

    # Testing mode
    policy.eval()
    print(policy)

    # Reset it
    total_reward = 0.0
    state, _ = env.reset(seed=None)

    # While the episode is not finished
    terminated = False
    while not terminated:

        # Use the policy to generate the probabilities of each action
        probabilities = policy(state)

        # ---> TODO: how to select an action
        epsilon = 0.1  # Exploration parameter

        # Randomly choose between exploration or exploitation
        if np.random.rand() < epsilon:
            action = env.action_space.sample()  # Random action from the space
        else:
            # Get the action with the highest probability from the policy
            action = torch.argmax(policy(state)).item()


        # One step forward
        state, reward, terminated, _, _ = env.step(action)

        # Render (or not) the environment
        total_reward += reward
        env.render()

    # Print reward
    print("total_reward = {}".format(total_reward))
