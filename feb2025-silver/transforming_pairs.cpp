#include <iostream>
#include <numeric>
#include <vector>

#ifdef LOCAL
#include "print.h"
#else
template <typename... Args> inline void print(const Args&... args) {}
inline void                             newline() {}
#endif

using ll = long long;
#define endl      '\n'
#define FOR(i, n) for (int i = 0; i < n; i++)

using namespace std;

void solve() {
    ll a, b, c, d;
    cin >> a >> b >> c >> d;

    if (gcd(a, b) != gcd(c, d) || a > c || b > d) {
        cout << -1 << endl;
        return;
    }
    ll ans = 0;
    while (c != a || d != b) {
        if (c < a || d < b) {
            cout << -1 << endl;
            return;
        }
        if (c > d) {
            ll k = (c - a) / d;
            if (k == 0) {
                k = 1;
            }
            c -= k * d;
            ans += k;
        }
        else {
            ll k = (d - b) / c;
            if (k == 0) {
                k = 1;
            }
            d -= k * c;
            ans += k;
        }
    }
    cout << ans << endl;
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}
