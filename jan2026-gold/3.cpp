#include <iostream>
#include <vector>

using namespace std;
using ll = long long;
#define FOR(i, a, b) for (int i = a; i < b; i++)

constexpr ll MOD = 1e9 + 7;

struct F {
    ll   mul;
    void operator+=(F oth) {
        mul *= oth.mul;
        mul %= MOD;
    }
};
F fid = {1};
struct S {
    ll   sm;
    void apply(F f, int width) {
        sm *= f.mul;
        sm %= MOD;
    }
    S operator+(S oth) {
        return {(sm + oth.sm) % MOD};
    }
};
S sid = {0};
template <int sz> struct SegTree {
    vector<S> seg;
    vector<F> lazy;
    SegTree() : seg(4 * sz, sid), lazy(4 * sz, fid) {}
    void push(int i, int l, int r) {
        seg[i].apply(lazy[i], r - l);
        if (r - l > 1) {
            lazy[2 * i] += lazy[i];
            lazy[2 * i + 1] += lazy[i];
        }
        lazy[i] = fid;
    }
    void upd(int lo, int hi, F val, int i = 1, int l = 0, int r = sz) {
        push(i, l, r);
        if (r <= lo || l >= hi) {
            return;
        }
        if (lo <= l && r <= hi) {
            lazy[i] += val;
            push(i, l, r);
            return;
        }
        int m = (l + r) / 2;
        upd(lo, hi, val, 2 * i, l, m);
        upd(lo, hi, val, 2 * i + 1, m, r);
        seg[i] = seg[2 * i] + seg[2 * i + 1];
    }
    void add(int pos, S val, int i = 1, int l = 0, int r = sz) {
        if (r - l == 1) {
            seg[i] = seg[i] + val;
            return;
        }
        push(i, l, r);
        int m = (l + r) / 2;
        if (pos < m) {
            add(pos, val, 2 * i, l, m);
        }
        else {
            add(pos, val, 2 * i + 1, m, r);
        }
        seg[i] = seg[2 * i] + seg[2 * i + 1];
    }
    S query(int lo, int hi, int i = 1, int l = 0, int r = sz) {
        push(i, l, r);
        if (r <= lo || l >= hi) {
            return sid;
        }
        if (lo <= l && r <= hi) {
            return seg[i];
        }
        int m = (l + r) / 2;
        return query(lo, hi, 2 * i, l, m) + query(lo, hi, 2 * i + 1, m, r);
    }
};

signed main() {
    cin.tie(0)->sync_with_stdio(0);

    int n, d;
    cin >> n >> d;
    SegTree<1'000'005> st;
    vector<int>        coaches;
    coaches.reserve(n);
    int m = 0, no = 0;
    FOR(i, 0, n) {
        int p, o;
        cin >> p >> o;
        if (o == 1) {
            ll sm = (m > 0) ? st.query(1, m + 1).sm : 0;
            m++;
            coaches.push_back(p);
            st.add(m, {(sm + 1) % MOD});
        }
        else {
            while (no < m && coaches[no] < p - d) {
                no++;
            }
            if (no + 1 <= m) {
                st.upd(no + 1, m + 1, {2});
            }
        }
    }
    cout << ((m > 0) ? st.query(1, m + 1).sm : 0) << "\n";
}
