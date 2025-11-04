#include <bits/stdc++.h>
#define int long long

using namespace std;

int32_t main() {
    cin.tie(NULL)->sync_with_stdio(false);
    
    // input
    int n, m;
    cin >> n >> m;
    vector <vector <char>> a(n, vector <char>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }

    int ans = 0; // ตัวแปรที่ทำหน้าที่เก็บขนาดเกาะที่ใหญ่ที่สุดที่เคยตรวจสอบมา
    
    // visited: เก็บว่าช่องที่ i, j เคยวนมาแล้วหรือยัง
    vector <vector <bool>> visited(n, vector <bool>(m, false));
    // d_ : เก็บทิศทาง แกน x และ แกน y
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};

    // loop i = 0 -> n, j = 0 -> m
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // ตรวจสอบว่าเป็นพื้นเกาะ และยังไม่ได้ตรวจสอบ
            if (!visited[i][j] && a[i][j] == '1') {
                visited[i][j] = true; // ตั้งเป็นตรวจสอบแล้ว
                queue<pair<int, int>> q; // queue ใช้ BFS
                q.push({i, j});
                int cnt = 1; // cnt ใช้นับพื้นที่เกาะปัจจุบัน

                while (!q.empty()) {
                    auto [x, y] = q.front(); // ดึงตำแหน่งปัจจุบันออกมาจาก queue
                    q.pop();

                    // Loop 4 ทิศทาง
                    for (int k = 0; k < 4; k++) {
                        // ตำแหน่งใหม่หากเดินไปตามทิศทางนั้นๆ
                        int nx = x + dx[k];
                        int ny = y + dy[k];

                        // ตรวจสอบว่า:
                        // 1. อยู่ในอาณาเขตหรือไม่
                        // 2. เป็นพื้นเกาะหรือไม่
                        // 3. เคยตรวจสอบแล้วหรือไม่
                        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                        if (visited[nx][ny] || a[nx][ny] == '0') continue;

                        visited[nx][ny] = true; // ตั้งว่าเคยตรวจสอบแล้ว
                        q.push({nx, ny}); // ใส่เข้า queue
                        cnt++;
                    }
                }

                ans = max(ans, cnt); // ปรับค่า ans ว่า เกาะปัจจุบัน มีขนาดใหญ่กว่าเกาะที่ใหญ่ที่สุดที่เคยตรวจสอบมาหรือไม่
            }
        }
    }

    // Output
    cout << ans;
    return 0;
}
