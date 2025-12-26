---
title: TOI20_Orbs
---
# คำอธิบายวิธีทำพร้อม Code สำหรับข้อ [toi20_orbs](https://programming.in.th/tasks/toi20_orbs/)

---

## Problem

### สรุปโจทย์

มีลูกแก้ว $N$ ลูก ลูกที่ $i$ หนัก $w_i$ โดยเราจะทำการเลือกลูกแก้วสองลูก $L$ ครั้ง โดยในทุกๆครั้งจะเลือกลูกแก้วที่มีน้ำหนักเป็นอันดับที่ $a$ เป็นลูกแรกและเลือกลูกแก้วน้ำหนักเป็นอันดับที่ $b$ เป็นลูกที่สองไปใส่ในเครื่องจักร

สิ่งที่เกิดขึ้นเมื่อใส่ลูกแก้วที่มีน้ำหนักเท่ากับ $p,q$ เป็นลูกแรกกับลูกที่สองตามลำดับในเครื่องจักร:เมื่อใส่ในเครื่องจักรแล้ว เครื่องจักรจะทำลายลูกแก้วทั้งสองลูกและให้ลูกแก้วที่มีน้ำหนัก $q-p$ กับลูกแก้วที่มีน้ำหนัก $⌊\frac{p+q}{2}⌋$ ออกมาแทน

หมายเหตุ: $⌊x⌋$ หมายถึง floor function ของ $x$ ซึ่งเป็นจำนวนเต็มที่มีค่ามากที่สุดที่น้อยกว่าหรือเท่ากับ $x$

### สิ่งที่ต้องทำ

ให้ print น้ำหนักลูกแก้วที่เรียงจากน้อยไปมาก

!!! note "Prerequisites"
    - Multiset

!!! note "Constraints"
    - $2 \leq N \leq 2\cdot 10^6$
    - $1 \leq L \leq 2\cdot 10^6$
    - $1\leq a < b \leq N$
    - $1 \leq w_i \leq 10^9$
---

## Solution

### วิธีทำ

สังเกตได้ว่าจะเลือกลูกแก้วที่ทีน้ำหนักเป็นอันดับที่ $a$ กับ $b$ เสมอแปลว่าเราแค่ต้องใช้ Data Structure ที่สามารถหาค่าในอันดับที่ $a$ และอันดับที่ $b$ ได้อย่างรวดเร็ว ดังนั้นเราจึงควรใช้ multiset เป็น Data Structure นั้นและทำให้มีรูปแบบเหมือนกับรูปต่อไปนี้
![](https://i.ibb.co/HDXZDQHR/image.png)

โดย<br>
1.ลูกแก้วใน multiset1 ทุกลูกจะต้องน้อยกว่าลูกแก้วใน multiset2 ทุกลูก<br>
2.ลูกแก้วใน multiset2 ทุกลูกจะต้องน้อยกว่าลูกแก้วใน multiset3 ทุกลูก

ถ้าให้ $p$ เป็นค่าน้ำหนักในอันดับที่ $a$ และ $q$ เป็นค่าน้ำหนักในอันดับที่ $b$
จะสังเกตได้ว่า $q-p,⌊\frac{p+q}{2}⌋ \leq q$ ดังนั้นเวลาใส่ลูกแก้วกลับเราจำเป็นต้องใส่ใน multiset1 หรือ multiset2 เท่านั้น โดยใส่ใน multiset2 ก่อนแล้วค่อยย้ายลูกแก้วมาใน multiset1 โดยให้เงื่อนไข 1 ยังเป็นจริง
---

### Code

```cpp title="toi20_orbs.cpp"
#include <bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(NULL)->sync_with_stdio(false);
    int n, t, l, r;
    cin >> n >> t >> l >> r;
    vector <int> v(n);
    for(int i = 0; i < n; i++) cin >> v[i];
    sort(v.begin(), v.end());
    multiset<int> a, b, o;
    for(int i = 0; i < l; i++){
        a.insert(v[i]);
    }
    for(int i = l; i < r; i++){
        b.insert(v[i]);
    }
    for(int i = r; i < n; i++){
        o.insert(v[i]);
    }

    while(t--){
        int x = *--a.end();
        int y = *--b.end();
        a.erase(--a.end());
        b.erase(--b.end());
        int new1 = y - x, new2 = (x + y) / 2;
        b.insert(new1);
        b.insert(new2);
        int firstB = *b.begin();
        b.erase(b.begin());
        a.insert(firstB);
        if (*--a.end() > *b.begin()) {
            int temp1 = *--a.end(), temp2 = *b.begin();
            a.erase(--a.end());
            b.erase(b.begin());
            a.insert(temp2);
            b.insert(temp1);
        }
    }

    for(int i : a) cout << i << ' ';
    for(int i : b) cout << i << ' ';
    for(int i : o) cout << i << ' ';
}
```

!!! note "Total Time Complexity"  
    $O(N\log N)$
