#include <bits/stdc++.h>
#define int long long

using namespace std;

int32_t main() {
    cin.tie(NULL)->sync_with_stdio(false);

    // input
    int n;
    cin >> n;
    vector <int> p(n + 1);
    for (int i = 1; i <= n; i++) cin >> p[i];

    int ans = 0; // เก็บผลรวมคำตอบ

    // Loop เพื่อคำนวณ
    for (int i = 1; i < n; i++) {
        ans += max(0ll, p[i + 1] - p[i]);
    }

    // Output
    cout << ans << "\n";
    return 0;
}
