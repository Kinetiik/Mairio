from gym.envs.registration import register

register(
    id='mairio-v0',
    entry_point='gym_mairio.envs:MairioEnv',
)
