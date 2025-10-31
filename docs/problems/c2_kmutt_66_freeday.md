---
title: c2_kmutt_66_heroes
---
# ข้อสอบท้ายค่าย 2 ปีการศึกษา 2566 ศูนย์ สอวน. มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี ข้อ [FreeDay](https://grader.gchan.moe/problemset/c2_st66_freeday/)
---
### Author: Nagorn Phongphasura
---

## Problem 

### สรุปโจทย์
มีคนอยู่ $N$ คน โดยแต่ละคน จะไม่ว่างกันเป็นช่วงของวันที่ $S_{(i, j)}$ ถึง $E_{(i, j)}$ (ก็คือ ช่วงที่ $j$ ของคนที่ $i$ เริ่มที่ $S_{(i, j)}$ และจบที่ $E_{(i, j)}$)

### สิ่งที่ต้องทำ
หาช่วงของวันที่คนทุกคนว่างพร้อมกัน (โดยไม่นับช่วงที่ไม่มีขอบเขต)

!!! note "Constraints"
    $2 \leq N \leq 10^4$<br>
    $1 \leq S_{(i,1)} < E_{(i, 1)} < S_{(i, 2)} < E_{(i, 2)} < ... \leq 1,000$

!!! note "Prerequisites"
    - `Sweep Line`

---

## Solution

### วิธีทำ


---

## Code: 

```cpp title="c2_kmutt_66_freeday.cpp"


```
!!! note "Total Time Complexity"
	$O(n \log n)$
