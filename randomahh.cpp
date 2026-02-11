#include <bits/stdc++.h>

using namespace std;

int main(){
    long long n, m;
    cin >> n >> m;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    long long l = 1, r = 1e18;
    long long ans = 1e18;
    while (l <= r) {
        long long mid = (l + r) / 2;
        long long sum = 0;
        for (int i = 0; i < n; i++) {
            sum += mid / a[i];
        }
        if (sum >= m) {
            ans = min(mid, ans);
            r = mid - 1;
        }
        else {
            l = mid + 1;
        }
    }
    cout << ans;
}
