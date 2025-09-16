# [ข้อสอบท้ายค่าย 1 ศูนย์ สอวน.กรุงเทพมหานคร ปี 2567 ข้อที่ 2](https://grader.gchan.moe/problemset/c1_bkk67_2)
---
## Problem
### สรุปโจทย์
เรามี String จำนวน 2 อัน และเราต้องการหาตัวอักษรที่ซ้ำกัน (ต้องเป็นตัวพิมพ์เล็ก-พิมพ์ใหญ่เหมือนกันด้วย)

### สิ่งที่ต้องทำ
เขียนโค้ดเพื่อหาตัวอักษรที่ซ้ำกัน

!!! note "ตัวอย่าง"
    | Input      | Output                          |
    | ----------- | ------------------------------------ |
    |PHYSICSMATH<br>COMPUTER|C M P T|
    |agodinCAR<br>bookontable|a o n|

!!! note "Prerequisites"
    - Arrays
---
## Solution
### วิธีทำ

รับ Input มาเป็น String แล้วเราก็แค่ Loop ตามตัวอักษรแต่ละตัว และเมื่อพบแต่ละตัว ก็นับเพิ่มลงใน Array ที่จะเก็บเป็นตัวเลข ว่าพบตัวอักษรที่ $i$ มาแล้วกี่ตัว ซึ่งเราจะมีอยู่ 2 Array (ตั้งชื่อว่า $aa$ และ $bb$) แล้วเมื่อเรา Loop ตามตัวอักษร เราจะเขียนว่า $aa[a[i]]$++; (เหตุผลที่เราทำแบบนี้ได้ เป็นเพราะว่า ในภาษา C จะ convert ตัวอักษร ให้เป็นค่า [ASCII VALUE](https://www.ascii-code.com/) ของมันให้เลย)

---
### Code

```cpp title="repeating_string.c"

```
!!! note "Total Time Complexity"  
    $O(N)$

หากมีข้อสงสัย comment ไว้ใต้ [post](https://web.facebook.com/share/p/1BF9b2z7V9/) ได้เลยนะครับ 🙇‍♂️🙇‍♂️  