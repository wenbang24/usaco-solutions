#include <array>
#include <iostream>
#include <vector>

using namespace std;
using ll = long long;
#define FOR(i, a, b) for (int i = a; i < b; i++)

struct DSU {
    vector<int> parent, sink;
    DSU(int n) : sink(n, -1), parent(n, -1) {}
    int find(int x) {
        if (parent[x] < 0) {
            return x;
        }
        return parent[x] = find(parent[x]);
    }
    bool unite(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) {
            return false;
        }
        if (parent[x] > parent[y]) {
            swap(x, y);
        }
        parent[x] += parent[y];
        parent[y] = x;
        if (sink[x] == -1) {
            sink[x] = sink[y];
        }
        return true;
    }
    int size(int x) {
        return -parent[find(x)];
    }
    bool same_set(int x, int y) {
        return find(x) == find(y);
    }
};

signed main() {
    cin.tie(0)->sync_with_stdio(0);

    int n, m;
    cin >> n;
    vector<int> a(n);
    FOR(i, 0, n) {
        cin >> a[i];
        a[i]--;
    }
    auto typ = [](char ch) {
        if (ch == 'C') {
            return 0;
        }
        if (ch == 'O') {
            return 1;
        }
        return 2;
    };
    cin >> m;
    vector<int>  cow(m), newType(m), type(n, -1), prevType(m, -1);
    vector<bool> activator(m, false);
    FOR(i, 0, m) {
        char ch;
        cin >> cow[i] >> ch;
        cow[i]--;
        newType[i]   = typ(ch);
        prevType[i]  = type[cow[i]];
        activator[i] = (type[cow[i]] == -1);
        type[cow[i]] = newType[i];
    }
    vector<bool> isHost(n + 1, false);
    FOR(i, 0, n) {
        isHost[i] = (type[i] != -1);
    }
    DSU dsu(n);
    FOR(i, 0, n) {
        if (!isHost[i]) {
            dsu.unite(i, a[i]);
        }
    }
    FOR(i, 0, n) {
        if (isHost[i]) {
            dsu.sink[dsu.find(i)] = i;
        }
    }
    array<ll, 3> cnt = {0, 0, 0};
    FOR(i, 0, n) {
        if (dsu.find(i) == i && dsu.sink[i] != -1) {
            cnt[type[dsu.sink[i]]] += dsu.size(i);
        }
    }
    vector<array<ll, 3>> ans(m);
    for (int t = m - 1; t >= 0; t--) {
        ans[t] = cnt;
        int v  = cow[t];
        if (!activator[t]) {
            ll  sz   = dsu.size(dsu.find(v));
            int prev = prevType[t];
            cnt[type[v]] -= sz;
            cnt[prev] += sz;
            type[v] = prev;
        }
        else {
            int rv = dsu.find(v);
            int s  = dsu.sink[rv];
            if (s != -1) {
                cnt[type[s]] -= dsu.size(rv);
            }
            dsu.sink[rv] = -1;
            isHost[v]    = false;
            type[v]      = -1;
            int ru       = dsu.find(a[v]);
            rv           = dsu.find(v);
            if (ru != rv) {
                if (dsu.sink[ru] != -1) {
                    int sink = dsu.sink[ru];
                    cnt[type[sink]] += dsu.size(rv);
                }
                dsu.unite(rv, ru);
            }
        }
    }
    FOR(i, 0, m) {
        cout << ans[i][0] << " " << ans[i][1] << " " << ans[i][2] << "\n";
    }
}
