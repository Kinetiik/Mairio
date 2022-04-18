from tensorforce import Agent, Environment

environment = Environment.create(environment="costum")

agent = Agent.create(
    agent='tensorforce',
    # alternatively: states, actions, (max_episode_timesteps)
    environment=environment,
    memory=10000,
    update=dict(unit='timesteps', batch_size=64),
    optimizer=dict(type='adam', learning_rate=3e-4),
    policy=dict(network='auto'),
    objective='policy_gradient',
    reward_estimation=dict(horizon=20)
)

for _ in range(3000):

    # Initialize episode
    states = environment.reset()
    terminal = False

    while not terminal:
        # Episode timestep
        actions = agent.act(states=states)
        states, terminal, reward = environment.execute(actions=actions)
        agent.observe(terminal=terminal, reward=reward)

agent.close()
environment.close()
