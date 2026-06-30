import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    

    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3
        
    dist = [float('inf')] * n
    dist[0] = 0
    
    pq = [(0, 0)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
                
    for i in range(n):
        if dist[i] == float('inf'):
            print(f"Odleglosc od 0 do {i} wynosi INF")
        else:
            print(f"Odleglosc od 0 do {i} wynosi {dist[i]}")

if __name__ == '__main__':
    main()
