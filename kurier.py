import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    s = int(input_data[2])
    t = int(input_data[3])
    
    adj = [[] for _ in range(n + 1)]
    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w)) 
        idx += 3
        
    dist = [float('inf')] * (n + 1)
    min_nodes = [float('inf')] * (n + 1)
    
    dist[s] = 0
    min_nodes[s] = 1 
    
    pq = [(0, 1, s)]
    
    while pq:
        d, nodes, u = heapq.heappop(pq)
        
        if d > dist[u] or (d == dist[u] and nodes > min_nodes[u]):
            continue
            
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                min_nodes[v] = nodes + 1
                heapq.heappush(pq, (dist[v], min_nodes[v], v))
            elif dist[u] + weight == dist[v]:
                if nodes + 1 < min_nodes[v]:
                    min_nodes[v] = nodes + 1
                    heapq.heappush(pq, (dist[v], min_nodes[v], v))
                    
    if dist[t] == float('inf'):
        print("NIE")
    else:
        print(dist[t], min_nodes[t])

if __name__ == '__main__':
    main()
