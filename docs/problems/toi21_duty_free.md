---
title: TOI21_Duty_Free
tags: [TOI, Bruteforce, Disjoint Set Union, Hard]
---
# คำอธิบายวิธีทำพร้อม Code สำหรับข้อ [toi21_duty_free](https://api.otog.in.th/problem/doc/1090)

---

## Problem

### สรุปโจทย์

เรามีลูกค้าจะซื้อกระเป๋า `N` คน ไล่คิวจากคนที่ `1` ถึงคนที่ `N` โดยคนที่ `i` สามารถเดินได้ไกลสุด `max_allowed_positions[i - 1]` ตำแหน่ง โดย:

- ลูกค้าแต่ละคนจะเดินตรงไปหยิบกระเป๋าของตน โดยไม่หยิบกระเป๋าของคนอื่น
- พนักงานสามารถนำกระเป๋าที่เหลือทั้งหมดมาจัดวางใหม่บนชั้นวางแต่ละหมายเลขได้อย่างอิสระ (ภายใต้เงื่อนไข **1 กระเป๋า ต่อ 1 ชั้นวาง**)

### สิ่งที่ต้องทำ

เขียนโค้ดที่จะคำนวณจำนวนครั้งที่พนักงานต้องจัดวางกระเป๋าใหม่ให้น้อยที่สุด

!!! note "Constraints"
    $1 \leq N \leq 2,000,000$ <br>
    $1 \leq max\_allowed\_positions[i-1] \leq N$

!!! note "Prerequisites"
    - `Disjoint Set Union`
---

## Solution

### ไอเดียหลัก

เราจะพยายามวางกระเป๋าของลูกค้าคนที่ `i` ให้อยู่ไกลที่สุดที่เป็นไปได้  
เพื่อจะได้มีพื้นที่ด้านหน้าให้กับลูกค้าคนอื่นที่ `max_allowed_positions[i - 1]` มีค่าน้อย ๆ

### วิธีทำ

วิธีการเขียนแบบ Brute Force คือ เราจะมี array ที่จะเก็บว่า $arr[i] =$ ชั้นวางที่ $i$ ได้วางกระเป๋าไว้หรือยัง (ตอนเริ่มต้น `arr[i] = false` สำหรับทุกๆ $i$)  
โดยเราจะเริ่ม loop จาก slot ที่ $max\_allowed\_positions[i - 1]$ ไปจนถึง $1$  
แล้วถ้าหากว่าช่องที่เรากำลังตรวจสอบอยู่ยังไม่ได้วางกระเป๋าไว้ (`arr[i] == false`)  
เราจะ mark ช่องนั้นว่าถูกใช้แล้ว (`arr[i] = true`)  

และถ้าหากว่าเรา loop จาก $max\_allowed\_positions[i - 1]$ ถึง $1$ แล้วไม่มีช่องใดที่ว่างเลย  
แสดงว่า ทุกๆช่องที่ลูกค้าคนนี้สามารถเดินไปได้ ไม่มีช่องไหนว่างเลย  
เราจะ reset array โดยตั้งให้ทุกช่องเป็น $false$ และก็คำนวณเหมือนเดิมจนครบ $N$ คน

ปัญหาของการเขียนวิธีนี้คือ time complexity ในกรณีที่แย่ที่สุด จะเป็น $O(n^2)$ ซึ่งยังไงก็จะโดน TLE แน่ๆ

ดังนั้น ความยากของโจทย์ข้อนี้คือ วิธีการที่เราจะ optimize โค้ดให้เหลือ $O(n)$  
โดยเราจะใช้ DSU (Disjoint Set Union) ในการ optimize โค้ดข้อนี้

### วิธีการ optimize

เราจะเก็บ auxiliary array ซึ่งจะเก็บว่า ชั้นวางที่ $i$ เราจะวางกระเป๋าของลูกค้าคนที่เท่าไหร่  
และเราจะเก็บตัวแปรเพิ่ม 1 ตัวเป็น integer ชื่อว่า $f$ (ย่อจาก first)  
โดย $f$ จะเก็บว่า สำหรับการจัดกระเป๋ารอบนี้ ลูกค้าคนแรกที่เราจัดกระเป๋าให้คือลูกค้าคนที่เท่าไหร่  

โดยตอนที่เราหา root ของ $X$ เราจะเช็กใน auxiliary array นั้นก่อนว่า  
กระเป๋าที่เราจะวางในชั้นวางที่ $X$ นั้น เป็นกระเป๋าของใคร  
ถ้าหากว่าเป็นกระเป๋าของลูกค้าที่หมายเลขน้อยกว่า $f$ (```aux[X] < f```)  
ก็แสดงว่าเราไม่ต้องสนใจลูกค้าคนนั้นแล้ว เพราะว่าลูกค้าคนนั้นได้รับกระเป๋าไปแล้ว  
และเรากำลังจะจัดกระเป๋าบนชั้นวางใหม่อีกรอบ  

ซึ่งจะทำให้ time complexity ทั้งหมดลดเหลือ $O(n)$ นั่นเอง  

### Summary

- ใช้ Greedy Algorithm ในการเลือกช่องที่จะวางกระเป๋า  
- ใช้ Disjoint Set Union ในการ optimize โค้ด  

---

### Code

```cpp title="toi21_duty_free.cpp"
#include <bits/stdc++.h>

using namespace std;

const int N = 2e6 + 5;

int i, f, aux[N], par[N];

int dsu(int x){
    if (aux[x] < f) {
        aux[x] = i;
        par[x] = x;
    }
    return par[x] = (par[x] == x ? x : dsu(par[x]));
}

int minimum_bag_rearrangement_time(vector<int> max_allowed_positions){
    int n  = max_allowed_positions.size(); 
    f = 1;
    iota(par, par + N, 0);
    memset(aux, -1, sizeof aux);
    int ans = 0;
    for (i = 1; i <= n; i++) {
        int x = dsu(max_allowed_positions[i - 1]);
        if (x <= 0) {
            ans++, f = i;
            x = dsu(max_allowed_positions[i - 1]);
        }
        par[x] = dsu(x - 1);
    }
    return ans;
}
```

!!! note "Total Time Complexity"  
    $O(N)$
