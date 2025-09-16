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

### วิธีทำที่ 1 (Brute Force)

รับ Input เข้ามา แล้วเราจะ Loop ตามตัวอักษรแต่ละตัวใน String แรก ซึ่งแต่ละครั้งที่ Loop เราจะ Loop ตั้งแต่ตัวอักษรแรกจนจบของ String ที่สอง แล้วเมื่อเจอตัวอักษรซ้ำ เราก้สามารถเพิ่มคำตอบไป 1 แล้วออกจาก Loop ได้เลย

### วิธีทำที่ 2 (Arrays)

รับ Input มาเป็น String แล้วเราก็แค่ Loop ตามตัวอักษรแต่ละตัว และเมื่อพบแต่ละตัว ก็นับเพิ่มลงใน Array ที่จะเก็บเป็นตัวเลข ว่าพบตัวอักษรที่ $i$ มาแล้วกี่ตัว ซึ่งเราจะมีอยู่ 2 Array (ตั้งชื่อว่า $aa$ และ $bb$) แล้วเมื่อเรา Loop ตามตัวอักษร เราจะเขียนว่า $aa[a[i]]$++; (เหตุผลที่เราทำแบบนี้ได้ เป็นเพราะว่า ในภาษา C จะ convert ตัวอักษร ให้เป็นค่า [ASCII VALUE](https://www.ascii-code.com/) ของมันให้เลย)

---

### Code (วิธีทำที่ 2)

```cpp title="repeating_string.c"
#include <stdio.h>
#include <string.h>

int main(){
    char a[25], b[25];
    scanf("%s %s", a, b);
    int n = strlen(a), m = strlen(b);
    int aa[200] = {0};
    for (int i = 0; i < n; i++) {
        aa[a[i]]++;
    }
    int bb[200] = {0};
    for (int i = 0; i < m; i++) {
        if (aa[b[i]] > 0 && bb[b[i]] == 0) {
            printf("%c ", b[i]);
            bb[b[i]]++;
        }
    }
}
```

หากมีข้อสงสัย comment ไว้ใต้ [post](https://web.facebook.com/share/p/1BF9b2z7V9/) ได้เลยนะครับ 🙇‍♂️🙇‍♂️  
