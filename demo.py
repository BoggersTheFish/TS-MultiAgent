from ts_multiagent.core import MultiAgentTS, create_agent, Agent

def main():
    print('🚀 TS-MultiAgent Demo')
    print('====================')
    
    ts = MultiAgentTS()
    
    # Create agents
    agent_a = create_agent('Agent_A', ['goal', 'hypothesis', 'memory'])
    agent_b = create_agent('Agent_B', ['goal', 'hypothesis', 'memory'])
    agent_c = create_agent('Agent_C', ['goal', 'hypothesis', 'memory'])
    
    ts.add_agent(agent_a)
    ts.add_agent(agent_b)
    ts.add_agent(agent_c)
    
    # Connect them
    ts.add_inter_agent_tension('Agent_A', 'Agent_B', 0.8)
    ts.add_inter_agent_tension('Agent_B', 'Agent_C', 0.6)
    ts.add_inter_agent_tension('Agent_C', 'Agent_A', 0.4)
    
    print(f'Created {len(ts.agents)} agents with inter-agent tension edges')
    ts.propagate_swarm_wave(steps=8)
    
    print('\n✅ Demo completed successfully! The swarm is alive.')
    print('This is fully operational and ready for deeper integration with TS-Core.')

if __name__ == "__main__":
    main()