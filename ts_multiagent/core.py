import networkx as nx
import numpy as np
from typing import Dict

class MultiAgentTS:
    def __init__(self, num_agents: int = 4):
        self.graph = nx.Graph()
        for i in range(num_agents):
            self.graph.add_node(f'agent_{i}',
                              activation=1.0,
                              stability=0.8,
                              tension=0.1,
                              local_graph=nx.Graph())  # each agent has its own sub-graph
        # Inter-agent constraints
        for i in range(num_agents):
            for j in range(i+1, num_agents):
                self.graph.add_edge(f'agent_{i}', f'agent_{j}', weight=np.random.uniform(0.3, 0.7))

    def propagate_swarm_wave(self, steps: int = 10) -> Dict:
        '''Propagate waves across agents with tension resolution'''
        for _ in range(steps):
            new_acts = {}
            for node in self.graph.nodes:
                neighbors = list(self.graph.neighbors(node))
                if neighbors:
                    neighbor_acts = [self.graph.nodes[n]['activation'] for n in neighbors]
                    avg = np.mean(neighbor_acts)
                    tension = self.graph.nodes[node]['tension']
                    new_act = self.graph.nodes[node]['activation'] * 0.65 + avg * 0.35 - tension * 0.15
                    new_acts[node] = max(0.0, min(1.0, new_act))
                else:
                    new_acts[node] = self.graph.nodes[node]['activation']
            for node, act in new_acts.items():
                self.graph.nodes[node]['activation'] = act
                # Simple tension decay
                self.graph.nodes[node]['tension'] *= 0.9
        return {n: data for n, data in self.graph.nodes(data=True)}

if __name__ == '__main__':
    swarm = MultiAgentTS(5)
    print('Swarm initialized with', len(swarm.graph.nodes), 'agents')
    print(swarm.propagate_swarm_wave(15))