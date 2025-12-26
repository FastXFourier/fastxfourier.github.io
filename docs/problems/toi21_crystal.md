---
title: TOI21_Crystal
---
# คำอธิบายวิธีทำพร้อม Code สำหรับข้อ [toi21_crystal](https://otog.in.th/problem/1089)

---

## Problem

### สรุปโจทย์

มีจักรวาลอยู่ $U$ จักรวาล และมี Crystal $N$ อัน
แต่ละอันมี

* $p[i]$: ตำแหน่ง
* $w[i]$: จักรวาล
* $t[i]$: เวลา

ต้องเก็บ Crystal เรียงตาม

1. $p[i]$ จากน้อยไปมาก
2. $t[i]$ จากน้อยไปมาก

ขณะที่อยู่ในจักรวาล $j$ สามารถทำได้ 1 อย่าง จาก 2 operations

1. เก็บ Crystal ในจักรวาลปัจจุบัน (ข้ามบางอันได้)
2. ย้ายไปจักรวาลอื่น แต่ต้องเสีย Crystal $K$ อัน (ถ้ามีเก็บมาแล้ว $\ge K$)

**โจทย์:** หาว่าเก็บ Crystal ได้มากสุดเท่าไร

!!! note "Constraints"
    $1 \le U \le 1000$<br>
    $0 \le k \le 1000$<br>
    $10 \le N \le 100,000$<br>
    $1 \le p[i] \le 10^9$<br>
    $0 \le w < U$<br>
    $1 \le t[i] \le 10^9$ และไม่มีค่า $t[i]$ ที่ซ้ำกัน

!!! note "Prerequisites"
    - `Longest Increasing Subsequence`
    - `Data Structures`
    - `Dynamic Programming`

---

## Solution

### วิธีทำ

เราสามารถสังเกตได้ว่า ถ้า $U = 1$ และ sort Crystal ด้วย $p[i]$ จากน้อยไปมาก จะเห็นได้ว่าเป็นโจทย์หาความยาว LIS ธรรมดา (ตามค่า $t$)

ดังนั้นเราจะมี array `v` ที่เป็นการ sort Crystal ด้วย $p_i$ จากน้อยไปมาก แล้วทำ sweep line ตามแต่ละตัวของ `v` (หลังจากนี้การพูดถึง Crystal ที่ `i` หมายถึง Crystal ที่ `i` ของ array `v`)

สมมติว่าเราอยากเก็บ Crystal ที่ `i` มี 2 case คือ

* Crystal ล่าสุดก่อนที่เราเก็บ Crystal `i` อยู่จักรวาลเดียวกับ Crystal `i`
* Crystal ล่าสุดก่อนที่เราเก็บ Crystal `i` ไม่ได้อยู่จักรวาลเดียวกับ Crystal `i`

พิจารณา case ที่ 1 จะได้ว่าต้องหาจำนวน Crystal มากที่สุด (ให้ $c_1$ แทนค่านี้) โดยที่ Crystal ล่าสุดก่อนที่เราเก็บ Crystal `i` อยู่จักรวาลเดียวกับ Crystal `i` และ Crystal นั้นมีค่า $t < t[i]$.

พิจารณา case ที่ 2 จะได้ว่าต้องหาจำนวน Crystal มากที่สุด (ให้ $c_2$ แทนค่านี้) โดยที่ Crystal ล่าสุดก่อนที่เราเก็บ Crystal `i` อยู่คนละจักรวาลกับ Crystal `i` และ Crystal นั้นมีค่า $t < t[i]$.

จะได้ว่า ถ้าเราอยากเก็บ Crystal ที่ `i` จะเก็บได้มากสุดคือ $max(c_1, c_2 - k) + 1$.

เห็นได้ว่านี่ก็คือโจทย์ LIS โดยเราจะใช้ Fenwick Tree เป็น data structure ในการทำ LIS (ถ้าไม่รู้วิธีทำให้ลองศึกษาจากบทความนี้: [Longest Increasing Subsequence using BIT — GeeksforGeeks](https://www.geeksforgeeks.org/longest-increasing-subsequence-using-bit))
**note:** ในวิธีนี้จะใช้ coordinate compression ซึ่งเป็นสิ่งที่จำเป็นต้องใช้

---

## Code

```cpp
#include <bits/stdc++.h>
#define int long long
using namespace std;

const int mod = 1e9 + 7;
const int inf = 1e18;
const int N = 100000 + 5;
const int U = 1000 + 5;

int u, k, n, ans;
map<int,int> com;
set<int> ins;
tuple<int,int,int> a[N];

struct Fenwick {
    int fw[N];
    Fenwick() { fill(fw, fw+N, 0); }

    void update(int idx, int val) {
        while (idx < N) {
            fw[idx] = max(fw[idx], val);
            idx += idx & -idx;
        }
    }

    int query(int idx) {
        int res = 0;
        while (idx > 0) {
            res = max(res, fw[idx]);
            idx -= idx & -idx;
        }
        return res;
    }
} fenwick[U];

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> u >> k >> n;
    for (int i = 1; i <= n; i++) {
        auto &tp = a[i];
        int p, w, t;
        cin >> p >> w >> t;
        a[i] = make_tuple(t, w, p);
        ins.emplace(p);
    }

    vector<int> temp(ins.begin(), ins.end());
    for (size_t i = 0; i < temp.size(); ++i) {
        com[temp[i]] = (int)i + 1;
    }

    sort(a + 1, a + 1 + n); 

    for (int i = 1; i <= n; i++) {
        int t, w, pp;
        tie(t, w, pp) = a[i];
        int p = com[pp];

        int x1 = fenwick[w].query(p - 1) + 1;
        int x2 = fenwick[U - 1].query(p - 1) + 1 - k;
        int x  = max(x1, x2);

        fenwick[U - 1].update(p, x);
        fenwick[w].update(p, x);

        ans = max(ans, x);
    }

    cout << ans << "\n";
    return 0;
}
```

!!! note "Total Time Complexity"
    $O(n \log n)$

