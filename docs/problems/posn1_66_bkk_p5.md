# [ข้อสอบท้ายค่าย 1 ศูนย์ สอวน.กรุงเทพมหานคร ปี 2566 ข้อที่ 5](https://grader.gchan.moe/problemset/c1_bkk66_5)

---

## Problem

### สรุปโจทย์

รับ String ที่มีแค่ตัวอักษรภาษาอังกฤษตัวพิมพ์ใหญ่มา จงหาตัวอักษรที่มี [ASCII VALUE](https://www.ascii-code.com/) น้อยที่สุดและไม่มีตัวซ้ำใน String

### สิ่งที่ต้องทำ

หาตัวอักษรที่น้อยที่สุดและไม่มีตัวซ้ำใน String

!!! note "ตัวอย่าง"
    | Input      | Output                          |
    | ----------- | ------------------------------------ |
    | COMPUTER    |C|
    |THANAKIT     |K|

!!! note "Prerequisites"
    - If-Else Conditions
    - Arrays
---

## Solution

### วิธีทำ

เราจะใช้ Array เก็บว่าตัวอักษรแต่ละตัวมีการปรากฏมาทั้งหมดกี่ครั้ง และไล่จาก 'A' - 'Z' เพื่อตรวจสอบว่าตัวอักษรใดที่ปรากฏมาเพียง 1 ครั้ง และมีค่าน้อยที่สุด

---

### Code

```cpp title="posn1_66_bkk_p5.cpp"
#include <stdio.h>

int main(){
    char str[25];
    scanf("%s", str);
    int cnt[26] = {0};
    for (int i = 0; str[i] != '\0'; i++) cnt[str[i] - 'A']++;
    for (int i = 0; i < 26; i++) {
        if (cnt[i] == 1) {
            printf("%c", 'A' + i);
            break;
        }
    }
}
```

หากมีข้อสงสัย comment ไว้ใต้ [post]() ได้เลยนะครับ หรือพิมพ์ inbox มาได้เลยนะครับ 🙇‍♂️🙇‍♂️
