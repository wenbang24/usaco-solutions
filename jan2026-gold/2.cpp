#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
using ll = long long;
#define FOR(i, a, b) for (int i = a; i < b; i++)

struct BIT {
    int        n;
    vector<ll> bit;
    BIT(int n) : n(n), bit(n + 1, 0) {}
    void add(int i, ll val) {
        for (; i <= n; i += i & -i) {
            bit[i] += val;
        }
    }
    ll sum(ll i) {
        ll s = 0;
        for (; i > 0; i -= i & -i) {
            s += bit[i];
        }
        return s;
    }
};

signed main() {
    cin.tie(0)->sync_with_stdio(0);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<pair<ll, int>> b;
        b.reserve(n);
        FOR(i, 0, n) {
            int a;
            cin >> a;
            b.push_back({a, i});
        }
        sort(b.begin(), b.end());
        BIT bit(n);
        ll  ans = 0;
        int s = 0, l = 0;
        while (l < n) {
            int r = l;
            while (r < n && b[r].first == b[l].first) {
                r++;
            }
            FOR(i, l, r) {
                ll x = bit.sum(b[i].second + 1);
                ans += min(x, s - x);
            }
            FOR(i, l, r) {
                bit.add(b[i].second + 1, 1);
            }
            s += (r - l);
            l = r;
        }
        cout << ans << "\n";
    }
}
