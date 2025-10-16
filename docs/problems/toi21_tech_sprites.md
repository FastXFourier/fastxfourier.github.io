---
title: toi21_tech_sprites
tags: [TOI, DSU, Bruteforce, Medium]
---
# คำอธิบายวิธีทำพร้อม Code สำหรับข้อ  [toi21\_tech\_sprites](https://otog.in.th/problem/1086)

---

## Problem

### สรุปโจทย์

มี Graph หนึ่งที่มีจำนวน node และ edge ดังนี้:

* $n$ nodes (บ้านของ Tech-Sprites ที่ $i$)
* $m$ edges

แต่ละ node $i$ มีค่า 2 ค่า: $a[i], b[i]$.

ในแต่ละ connected-component (เซตของ node ที่เชื่อมถึงกัน) ตัว Tech-Sprites จะออกมาตามลำดับ: ก่อนโดยเรียงตามค่า $a[i]$ (ค่าต่ำกว่าก่อน) — ถ้า $a$ เท่ากันให้เรียงตาม $b$ (b น้อยก่อน)

เราต้องเพิ่ม edge น้อยที่สุด เพื่อให้เมื่อ Tech-Sprites ออกมาทีละ connected-component แล้ว component ต่างๆ เรียงตาม $(a,b)$ ที่ถูกต้องได้ (component ทั้งก้อนจะออกทีละก้อน โดยลำดับการออกของก้อนถูกกำหนดจากค่า $a$ แล้ว $b$)

**โจทย์:** หาจำนวน edge ขั้นต่ำที่ต้องเพิ่ม

### ตัวอย่าง

กรณีนี้ไม่ต้องเพิ่ม edge:

![example1](https://i.ibb.co/pBWmjjxd/Screenshot-2025-05-27-170133.png)

กรณีนี้ต้องเพิ่ม edge อย่างน้อย 1 เส้น:

![example2](https://i.ibb.co/0jwbYVYB/Screenshot-2025-05-27-170725.png)

สามารถเพิ่มเส้นเชื่อม node `2-3` แบบนี้ได้:

![example3](https://i.ibb.co/rKb6Gbh7/Screenshot-2025-05-27-171026.png)

!!! note "Constraints"
    $1 \le n \le 10^6$
    $1 \le m \le 3\cdot 10^6$
  
!!! note "Prerequisites"
    - `Disjoint Set Union`

---

## Solution

### วิธีทำ (สรุปขั้นตอน)

1. เก็บข้อมูล `(a[i], b[i], i)` ลงใน array แล้ว sort ตามลำดับการออกจริง — คือเรียงตาม `(a[i], b[i])` (a ก่อน ถ้า a เท่ากันใช้ b)
2. ใช้ DSU เพื่อหา connected-components ของกราฟเดิม
3. สร้าง mapping `mp[idx]` ให้แปลง index ต้นฉบับของ node ไปเป็นตำแหน่งหลัง sort (ตำแหน่งใน array ที่เรียงแล้ว)
4. เราจะ loop จาก `1` ถึง `N-1` (ตำแหน่งใน array ที่เรียงแล้ว) และเก็บข้อมูลช่วยเหลือสอง array:
   * `sz[root]` = ขนาดของ connected-component (จำนวน node) ของ root นั้น
   * `cnt[root]` = จำนวน node ที่ในลูปปัจจุบันมี root เป็น root นั้น (นับรวม node ที่เชื่อมเพิ่มแล้วด้วย)
5. ถ้า `cnt[dsu(i)] != sz[dsu(i)]` แปลว่า connected-component ของตำแหน่ง `i` ยังไม่ครบ (ยังมี node ที่อยู่กระจัดกระจายไม่ต่อเนื่องในตำแหน่งเรียง) — เราต้องตรวจดูตำแหน่งถัดไป `i+1` ว่า belong to root เดียวกันหรือไม่

   * ถ้าไม่ใช่ ให้เพิ่ม edge เพื่อเชื่อมตำแหน่ง `i` กับ `i+1` (คือ `unite(i, i+1)`) และเพิ่ม `ans` ขึ้น 1
6. ทำจนจบแล้ว `ans` คือคำตอบ (จำนวน edge ขั้นต่ำที่ต้องเพิ่ม)

หลักการสั้น ๆ: เราต้องการให้ทุก connected-component หลังจาก sort ตาม $(a,b)$ เป็นช่วงติดต่อกัน (contiguous) ในลำดับที่เรียงแล้ว ถ้าช่วงไหนคั่นด้วย node ที่ไม่ได้อยู่ใน component เดียวกัน เราจะแทรก edge เพื่อรวมช่วงให้ต่อเนื่อง — ขั้นต่ำจะเป็นจำนวนครั้งที่เรต้องเชื่อมช่องว่างระหว่างตำแหน่งเรียงที่มี root ต่างกันจนกว่าจะครบขนาดของ component นั้น

ภาพประกอบ:

* ภาพ array ที่ถูก sort แล้ว:
  ![sorted\_array](https://i.ibb.co/nsX3kZ1B/Screenshot-2025-05-27-172956.png)
* ตำแหน่งที่ตรวจแล้วไม่ตรงเงื่อนไข ต้องเพิ่มเส้นเชื่อม:
  ![extra\_edges](https://i.ibb.co/1fn0K1wq/Screenshot-2025-05-27-174405.png)

---

## Code

```cpp title="toi21_tech_sprites"
#include <bits/stdc++.h>
using namespace std;

#define int long long
const int N = 1000000 + 5;
const int M = 3000000 + 5;

int n, m;
int par[N], sz[N], cnt[N], mp[N];
tuple<int,int,int> a[N]; // (a, b, idx)

// DSU
int dsu(int x){
    return par[x] == x ? x : par[x] = dsu(par[x]);
}

void unite(int u, int v){
    u = dsu(u); v = dsu(v);
    if(u == v) return;
    if(sz[u] < sz[v]) swap(u, v);
    par[v] = u;
    sz[u] += sz[v];
    cnt[u] += cnt[v];
}

int32_t main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    for(int i = 0; i <= n; ++i){
        par[i] = i;
        sz[i] = 1;
        cnt[i] = 0;
    }

    for(int i = 1; i <= n; ++i){
        int x, y;
        cin >> x >> y;
        a[i] = make_tuple(x, y, i);
    }

    sort(a + 1, a + 1 + n);

    for(int i = 1; i <= n; ++i){
        int x, y, idx;
        tie(x, y, idx) = a[i];
        mp[idx] = i;
    }

    for(int i = 0; i < m; ++i){
        int u, v;
        cin >> u >> v;
        int pu = mp[u];
        int pv = mp[v];
        int ru = dsu(pu), rv = dsu(pv);
        if(ru != rv){
            if(sz[ru] < sz[rv]) swap(ru, rv);
            par[rv] = ru;
            sz[ru] += sz[rv];
        }
    }

    int ans = 0;
    for(int i = 1; i <= n; ++i){
        int r = dsu(i);
        cnt[r]++;
        if(cnt[r] == sz[r]) continue;
        if(i + 1 <= n && dsu(i + 1) != r){
            int ru = dsu(i), rv = dsu(i + 1);
            if(ru != rv){
                if(sz[ru] < sz[rv]) swap(ru, rv);
                par[rv] = ru;
                cnt[ru] += cnt[rv];
                sz[ru] += sz[rv];
            }
            ans++;
        }
    }
    
    cout << ans << "\n";
    return 0;
}
```

!!! note "Total Time Complexity"
    $O(n\log n)$
