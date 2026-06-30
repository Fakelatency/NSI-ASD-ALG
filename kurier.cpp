#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const long long INF = 1e18;

struct State {
    long long time;
    int nodes;
    int u;

    bool operator>(const State& other) const {
        if (time != other.time) return time > other.time;
        return nodes > other.nodes;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;
  
    vector<vector<pair<int, long long>>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w}); 
    }

    vector<long long> dist(n + 1, INF);
    vector<int> min_nodes(n + 1, 1e9);

    dist[s] = 0;
    min_nodes[s] = 1; 

    priority_queue<State, vector<State>, greater<State>> pq;
    pq.push({0, 1, s}); 

    while (!pq.empty()) {
        auto [d, nodes, u] = pq.top();
        pq.pop();

        if (d > dist[u] || (d == dist[u] && nodes > min_nodes[u])) continue;

        for (auto edge : adj[u]) {
            int v = edge.first;
            long long weight = edge.second;

            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                min_nodes[v] = nodes + 1;
                pq.push({dist[v], min_nodes[v], v});
            } 
            else if (dist[u] + weight == dist[v]) {
                if (nodes + 1 < min_nodes[v]) {
                    min_nodes[v] = nodes + 1;
                    pq.push({dist[v], min_nodes[v], v});
                }
            }
        }
    }

    if (dist[t] == INF) {
        cout << "NIE\n";
    } else {
        cout << dist[t] << " " << min_nodes[t] << "\n";
    }

    return 0;
}
