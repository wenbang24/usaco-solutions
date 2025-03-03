#include <algorithm>
#include <iostream>
#include <stack>
#include <unordered_map>
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

inline bool lexGreater(const vector<int>& a, const vector<int>& b) {
    FOR(i, min(a.size(), b.size())) {
        if (a [i] > b [i]) {
            return true;
        }
        else if (a [i] < b [i]) {
            return false;
        }
    }
    return a.size() > b.size();
}

vector<int> lexGreatest(const vector<int>& nums) {
    stack<int> st;
    FOR(i, nums.size()) {
        while (!st.empty() && st.top() < nums [i]) {
            st.pop();
        }
        st.push(nums [i]);
    }
    vector<int> ans;
    while (!st.empty()) {
        ans.push_back(st.top());
        st.pop();
    }
    reverse(ans.begin(), ans.end());
    return ans;
}

void solve() {
    int n;
    cin >> n;
    vector<int> cows(n);
    FOR(i, n) {
        cin >> cows [i];
    }
    vector<pair<int, int>> candidates;
    vector<int>            ind;
    FOR(i, n) {
        while (!ind.empty() && cows [ind.back()] < cows [i]) {
            candidates.push_back({ind.back(), i});
            ind.pop_back();
        }
        ind.push_back(i);
    }
    
    vector<int> best = lexGreatest(cows);
    for (auto [pos, move_index]: candidates) {
        vector<int> candidateCows = cows;
        int         moveVal       = candidateCows [move_index];
        candidateCows.erase(candidateCows.begin() + move_index);
        candidateCows.insert(candidateCows.begin() + pos, moveVal);

        vector<int> res = lexGreatest(candidateCows);
        if (lexGreater(res, best)) {
            best = res;
        }
    }
    FOR(i, best.size()) {
        cout << best [i] << (i < best.size() - 1 ? ' ' : endl);
    }
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
