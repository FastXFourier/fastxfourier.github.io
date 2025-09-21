# C/C++ In A Nutshell

## C/C++ Syntax
```c
#include <stdio.h>
int main(){
    printf("Hello World");
    return 0;
}
```

- `#include <stdio.h>` : เป็นการนำ Library ที่จะมี Function ต่างๆ เพื่อให้โปรแกรมสามารถประมวลผลได้<br>
**(โค้ดทุกข้อ จะต้องมีบรรทัดนี้)**
- `int main()` : การเริ่มต้นโปรแกรม โดยทุกอย่างจะถูกประมวลผลในนี้<br>
**(โค้ดทุกข้อ จะต้องมีบรรทัดนี้)**
- `printf("Hello World");` : ใช้ฟังก์ชั่น `printf` ในการแสดงผลคำว่า "Hello World"
- `return 0;` : จบการทำงาน

## Input/Output and Variables
จะถูกใช้ในการเขียน `printf` หรือ `scanf` 
```cpp
int n;
scanf("%d", &n);      // ใช้ในการรับ Input
printf("%d", n + n);  // ใช้ในการพิมพ์ Output
```

|Variable Type|Format Specifier|What It Collects|
|-----|-----|-----|
|`int`|`%d`|จำนวนเต็ม|
|`float`|`%f`|จำนวนทศนิยม|
|`double`|`%lf`|จำนวนทศนิยม (เก็บได้มากกว่า `float`)|
|`char`|`%c`|ตัวอักษร 1 ตัว|
|`unsigned int`|`%u`|จำนวนเต็มไม่เป็นลบ|

## If-Else

## Loop

## Arrays & Strings

## Sorting

## Sequential Search & Substring Search

## Functions

## Pointers

## Structs
