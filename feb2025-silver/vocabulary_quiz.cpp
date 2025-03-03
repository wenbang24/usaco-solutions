#include <iostream>
#include <unordered_set>
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

struct Node {
    Node*         parent;
    int           num_children;
    int           depth;
    unordered_set<Node*> children;
    Node() : num_children(0), depth(0) {}
};

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;
    vector<Node> words(n + 1);
    for (int i = 1; i <= n; i++) {
        int parent;
        cin >> parent;
        words [i].parent = &words [parent];
        words [parent].children.insert(&words [i]);
        words [parent].num_children++;
        words [i].depth = words [parent].depth + 1;
    }
    int m = 0;
    FOR(i, n) {
        if (words [i].num_children == 0) {
            m++;
        }
    }
    vector<int> queries(m);
    FOR(i, m) {
        cin >> queries [i];
    }
    vector<bool> touched(n + 1, false);
    vector<int>  ans;
    for (int x: queries) {
        Node* node = &words [x];
        while (node != nullptr && !touched [node - &words [0]] &&
               node->parent->num_children <= 1) {
            touched [node - &words [0]] = true;
            node                        = node->parent;
        }
        cout << node->depth << endl;
        node->parent->num_children--;
        node->parent->children.erase(node);
        node->parent = nullptr;
    }
    cout << 0 << endl;
}
