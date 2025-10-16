# [ข้อสอบท้ายค่าย 1 ศูนย์ สอวน.กรุงเทพมหานคร ปี 2567 ข้อที่ 1](https://grader.gchan.moe/problemset/c1_bkk67_1)

---

## Problem

### สรุปโจทย์

เรามี String ที่ประกอบด้วยตัวอักษรภาษาอังกฤษ 1 String แล้วเราต้องการหาตัวอักษรแต่ละตัวใน String นั้น เรียงจากตัวพิมพ์ใหญ่ก่อนตัวพิมพ์เล็ก แล้วเรียงตามลำดับพจนานุกรม

### สิ่งที่ต้องทำ

เขียนโค้ดเพื่อเรียงลำดับ String ตามเงื่อนไขของโจทย์

!!! note "ตัวอย่าง"
    | Input      | Output                          |
    | ----------- | ------------------------------------ |
    | ILOVECOMPUTERJa       |C E I J L M O P R T U V a|
    |myNameis|N a e i m s y|

!!! note "Prerequisites"
    - Strings
    - Sortings
---

## Solution

### วิธีทำ

รับ Input มาเป็น String แล้วก็แค่ทำการ Sort ตรงๆเลย โดยสำหรับข้อนี้ สามารถใช้อัลกอริทึมการเรียงลำดับแบบใดก็ได้ ไม่ว่าจะเป็น Bubble Sort, Insertion Sort, Selection Sort, ฯลฯ

---

### Code

```cpp title="string_sorting.c"
#include <stdio.h>
#include <string.h>

int main() {
    char str[35];
    scanf("%s", str);
    int n = strlen(str); // strlen(): หาความยาวของ String

    // ทำการเรียงตัวอักษรใน String (Bubble Sort)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1; j++) {
            if (str[j] > str[j + 1]) {
                char temp = str[j];
                str[j] = str[j + 1];
                str[j + 1] = temp;
            }
        }
    }

    // พิมพ์คำตอบออกมา
    printf("%c ", str[0]);
    for (int i = 1; i < n; i++) {
        if (str[i] == str[i - 1]) continue;
        printf("%c ", str[i]);
    }
    return 0;
}
```
