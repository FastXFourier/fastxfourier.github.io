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
    - Sortings
---
## Solution
### วิธีทำ

รับ Input มาเป็น String แล้วก็แค่ทำการ Sort ตรงๆเลย โดยสำหรับข้อนี้ สามารถใช้อัลกอริทึมการเรียงลำดับแบบใดก็ได้ ไม่ว่าจะเป็น Bubble Sort, Insertion Sort, Selection Sort, ฯลฯ

---
### Code

```cpp title="string_sorting.c"

```
!!! note "Total Time Complexity"  
    $O(N^2)$

หากมีข้อสงสัย comment ไว้ใต้ [post](https://web.facebook.com/share/p/1BF9b2z7V9/) ได้เลยนะครับ 🙇‍♂️🙇‍♂️  