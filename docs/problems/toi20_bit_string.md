---
title: TOI20_Bit_String
---
# Tutorial สำหรับ Bitmask DP & คำอธิบายวิธีทำพร้อม Code สำหรับข้อ [toi20_bit_string](https://programming.in.th/tasks/toi20_bit_string/)

---

## Problem

### สรุปโจทย์

เรามี Binary String (สตริงที่ประกอบด้วย '1' และ '0' เท่านั้น) ความยาว $N$ ซึ่งหากเราพิจารณา String ความยาว $N$ ทุกรูปแบบ จะพบว่ามี $2^N$ รูปแบบ โดยแต่ละรูปแบบ จะมีค่าน้ำหนัก $C_i$

การลดทอนคุณภาพ จะเป็นการเปลี่ยน '1' เป็น '0' ซึ่งสามารถทำได้ 2 วิธี

1. เปลี่ยน '1' เป็น '0'
2. เปลี่ยน '11' (อักขระ '1' สองตัวติดกัน) เป็น '00' (อักขระ '0' สองตัวติดกัน)

โดยเมื่อได้ Binary String ใหม่ที่เกิดจากการเปลี่ยน '1' เป็น '0' เราจะ**บวกค่าน้ำหนักของ Binary String ในขณะนั้น** ไปกับ **"ค่าลดทอนคุณภาพ"**
แล้ว Operation นี้ จะจบลงเมื่อ String กลายเป็น "00000........0" ซึ่งเราจะต้องการให้ **ค่าลดทอนคุณภาพ** ค่ามากที่สุด

### **ตัวอย่างการลดทอนคุณภาพ**

$N = 3$<br>
$001 = 9$<br>
$000 = 0$<br>
$100 = 9$<br>
$010 = 1$<br>
$101 = 1$<br>
$110 = 2$<br>
$111 = 3$<br>
$011 = 1$<br>

Binary String ที่กำหนดให้: $111$

**ขั้นตอน:**
ค่าลดทอนคุณภาพ เริ่มต้นที่ $C_{111}$ = 3<br>

1. 111 -> 011 : $ans$ เพิ่มไป $C_{011}$ = 1 -> 4<br>
2. 011 -> 001 : $ans$ เพิ่มไป $C_{001}$ = 9 -> 13<br>

ดังนั้น คำตอบของ Binary String $111$ คือ 13

โดยโจทย์จะกำหนด Binary String มาให้ $Q$ อัน และให้ตอบให้ครบ

### สิ่งที่ต้องทำ

เขียนโค้ดเพื่อหา **ค่าลดทอนคุณภาพ** ที่มีค่ามากที่สุด สำหรับ Binary String ทั้ง $Q$ อัน
!!! note "Constraints"
    - $2 \leq N \leq 20$
    - $-500,000 \leq C_i \leq 1,000,000$
!!! note "Prerequisites"
    - Bitmasks
    - Dynamic Programming
---

## Bitmask DP

สำหรับข้อนี้ เราจะใช้สิ่งที่เรียกว่า Bitmask DP ซึ่งเป็นรูปแบบการทำ Dynamic Programming ที่จะค่อนข้างพิสดารเล็กน้อย

โดย Bitmask DP นั้น ลักษณะจะเป็นการเล่นกับ **เลขฐานสอง** ซึ่งแทนที่จะเก็บ DP ในแต่ละ Index เราจะเก็บ DP ในแต่ละ Mask (เลขฐานสอง) แทน นั่นคือ เราจะมีทั้งหมด $2^N$ Mask (เราต้องการเล่นกับทุกรูปแบบของเลขฐานสองที่มี $N$ หลัก)

โดยโจทย์ส่วนใหญ่นั้น เราจะเก็บ State DP ในลักษณะของ

- $dp[mask] =$ สามารถทำ operation บางอย่างให้มาลงที่ state ที่ $mask$ ได้หรือไม่
- $dp[mask] =$ min/max value ที่จะนำพาเรามายัง state ที่ $mask$

ลักษณะการทำ Bitmask DP ทั่วไปคือ<br>

1. loop ตามทุกๆ $mask$ ที่เป็นไปได้ $O(2^N)$<br>
2. ลูปตามแต่ละตัวใน $mask$ นั้น แล้วเช็กว่า หากสับ bit นั้นออก $(1 > 0)$ แล้ว $dp$ ของ state นั้น เคยทำมาแล้วหรือไม่ แล้วทำได้มั้ย ดังรูปด้านล่าง (เปลี่ยนทุก bit ที่เป็น 1 ให้เป็น 0 แล้วเช็ก)<br>

<div class="bitmask-container">
<img src="https://i.ibb.co/6RKWGJ6n/Screenshot-2025-08-23-123831.png" class="bitmask_dp"><br>
</div>
3.
หากทำได้ ก็เอาเข้า cost function เพื่อนำมาใส่ใน $dp[mask]$ ปัจจุบัน

โดยในโจทย์ข้อนี้ เราจะกำหนดลักษณะ DP เป็นรูปแบบที่ 2 นั่นคือ $dp[mask] =$ ค่าที่ต่ำที่สุดที่จะนำเรามายัง state ที่ $mask$

---

## Solution

### วิธีทำ

ก่อนอื่น เราก็จะต้องรับ input ว่า สำหรับแต่ละ $mask$ ค่าลดทอนคุณภาพของมันจะเป็นเท่าไหร่ เราก็จะรับ input มาเป็น Binary String แล้วก็เข้า function $binary$ ที่เขียนไว้ เพื่อแปลง Binary String เป็น เลขฐานสิบ

หลักจากนั้น เราก็แค่นำไอเดียของ Bitmask DP ด้านบน ลงมาใช้ โดยเราจะเก็บว่า คำตอบที่มากที่สุดสำหรับ $dp[mask]$ เป็นเท่าไหร่ โดยเราจะ Loop ไปทุกๆ $mask$ (นั่นคือ วน $2^N$ รอบ) โดยสำหรับแต่ละ $mask$ จะคำนวณดังนี้:<br>
**Loop ครั้งที่ 1 (สับออก 1 bit)**

- เช็กแต่ละ index ว่า $mask$ ปัจจุบันในตำแหน่งที่ $i$ เป็น 1 หรือ 0
  - หากเป็น 0 ก็ข้าม  
  - หากเป็น 1 ให้เอา bit นั้นเป็น 0 (ตั้งชื่อว่า $nm$ ย่อจาก $new mask$) แล้วก็  
      เก็บ $dp[mask] = \max(dp[mask], dp[nm] + a[mask])$ ซึ่งคือ cost function ของเรา

**Loop ครั้งที่ 2 (สับออก 2 bit)**

- เช็กแต่ละ index ว่า $mask$ ปัจจุบันในตำแหน่งที่ $i$ และ $i+1$ เป็น 1 หรือ 0
  - หากสักอันเป็น 0 ก็ข้าม  
  - หากเป็น 1 ทั้งคู่ ให้เอาทั้งสอง bit นั้นเป็น 0 (ตั้งชื่อว่า $nm$ ย่อจาก $new mask$) แล้วก็  
      เก็บ $dp[mask] = \max(dp[mask], dp[nm] + a[mask])$

แล้วเมื่อรับคำถามมา เราก็แค่ส่ง Output ไปเป็น $dp[input]$ สำหรับแต่ละอินพุตได้เลย

---

### Code

```cpp title="toi20_bit_string.cpp"
#include <bits/stdc++.h>

using namespace std;

const long long mod = 1e9 + 7;
const long long inf = 1e18;

long long binary(string s){
    long long ans = 0;
    reverse(all(s));
    for (long long i = 0; i < s.length(); i++) {
        ans += (s[i] - '0') * (1 << i);
    }
    return ans;
}

int32_t main(){
    cin.tie(NULL)->sync_with_stdio(false);
    long long n, q; cin >> n >> q;
    vector <long long> a(1 << n);
    for (long long i = 0; i < (1 << n); i++) {
        string s; cin >> s;
        long long num; cin >> num;
        a[binary(s)] = num;
    }
    vector <long long> dp(1 << n, -inf); dp[0] = 0;
    for (long long mask = 1; mask < (1 << n); mask++) {
        // swap 1 bit
        for (long long i = 0; i < n; i++) {
            if ((mask & (1 << i)) == 0) continue;
            long long nm = mask ^ (1 << i);
            dp[mask] = max(dp[mask], dp[nm] + a[mask]);
        }
        // swap 2 bits
        for (long long i = 0; i < n - 1; i++) {
            if ((mask & (1 << i)) == 0 || (mask & (1 << (i + 1))) == 0) continue;
            long long nm = mask ^ (1 << i) ^ (1 << (i + 1));
            dp[mask] = max(dp[mask], dp[nm] + a[mask]);
        }
    }
    while (q--) {
        string s; cin >> s;
        cout << dp[binary(s)] << "\n";
    }
}
```

!!! note "Total Time Complexity"  
    $O(2^N \cdot N)$
