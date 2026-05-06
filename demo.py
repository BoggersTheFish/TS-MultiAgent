from ts_multiagent.core import MultiAgentTS

if __name__ == '__main__':
    print('TS-MultiAgent Demo')
    swarm = MultiAgentTS(num_agents=6)
    state = swarm.propagate_swarm_wave(steps=20)
    print('Final swarm state:', state)
    print('\nEmergent coordination achieved!')