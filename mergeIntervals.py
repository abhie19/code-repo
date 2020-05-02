class Solution:
    def overlap(self, int1, int2):
            return int1[0] <= int2[1] and int2[0] <= int1[1]
        
    def build_graph(self, intervals):
        graph = collections.defaultdict(list)
        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)
        return graph
    
    def merge_nodes(self, nodes):
            min_start = min(node[0] for node in nodes)
            max_end = max(node[1] for node in nodes)
            return [min_start, max_end]
    
    # Basically graph traversal of undirected graph
    def get_components(self, graph, intervals):
        visited = set()
        comp_n = 0
        nodes_in_comp = collections.defaultdict(list)
        
        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_n].append(node)
                    stack.extend(graph[node])
                    
        for interval in intervals:
            if tuple(interval) not in visited:
                mark_component_dfs(interval)
                comp_n += 1
        
        return nodes_in_comp, comp_n
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.build_graph(intervals)
        nodes, comp_n = self.get_components(graph, intervals)
        
        return [self.merge_nodes(nodes[comp]) for comp in range(comp_n)]
