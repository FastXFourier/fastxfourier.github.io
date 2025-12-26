---
title: TOI20_Tour
---
# คำอธิบายวิธีทำพร้อม code สำหรับข้อ [toi20_tour](https://api.otog.in.th/problem/1017)

---

## Problem

### สรุปโจทย์

มีจำนวนโซนร้านค้า ทั้งหมด $L$ โซน แต่ละโซนจะมีร้านค้า $N_i$ ร้าน แต่ละร้านจะมีสินค้าแค่ $1$ ประเภท เป็น “ตุ๊กตาน้องส้มโอหวาน” หรือ “ตุ๊กตาน้องข้าวสารขาว”
กติกาในการแข่งขันของคู่รักคนแรกจะเริ่ม shopping จากร้านค้าที่ $1$ ซึ่งอยู่ในโซนที่ $1$ จากนั้น จะไป shopping ต่อไปยังร้านค้าที่อยู่ในโซนถัดไป (โซนที่ $2$) เพียง $1$ ร้านเท่านั้น (สามารถเข้า shopping ได้เพียง $1$ ร้านต่อ $1$ โซนเท่านั้น) จากนั้นจะต้องเดินทางจากร้านดังกล่าวไป shopping ยังร้านถัดไปในโซนถัดไปเรื่อยๆ จนกว่าจะถึงร้านค้าสุดท้ายในโซนที่ $L$ โดยการ shopping จะต้อง shopping ภายใต้เส้นทางที่จัดสรรให้เท่านั้น
คู่รักที่จะได้รับรางวัลในการแข่งขัน shopping ในครั้งนี้คือคู่รักที่สามารถทําให้ค่าความต่างใจ $D = (F − F′)^2 + (G − G′)^2$

($F =$ จำนวนตุ๊กตาน้องส้มโอหวานที่คู่รักคนแรกได้รับมา, $F′ =$ จำนวนตุ๊กตาน้องส้มโอหวานที่คู่รักคนที่สองได้รับมา, $S =$ จำนวนตุ๊กตาน้องข้าวสารขาวที่คู่รักคนแรกได้รับมา, $S′ =$ จำนวนตุ๊กตาน้องข้าวสารขาวที่คู่รักคนที่สองได้รับมา)

มีค่าที่น้อยที่สุด เพราะถือว่าคู่รักทั้งคู่มีใจตรงกันมาก แต่อย่างไรก็ตามหากค่าความต่างใจดังกล่าวมีค่าเป็น 0 กรรมการจะทําการตรวจสอบเส้นทาง shopping ของคู่รักทั้งคู่ หากพบว่า คู่รักทั้งคู่ใช้เส้นทางรูปแบบเดียวกัน $100$% ในการ shopping การแข่งขันดังกล่าวถือว่าไม่สุจริต และจะไม่อนุญาตให้รับรางวัลในกรณีนี้


### สิ่งที่ต้องทำ

เขียนโค้ดที่จะคำนวณว่า ค่าความต่างใจที่น้อยที่สุดจะมีค่าเท่าใด

!!! note "Constraints"
    $N$ หมายถึง จํานวนร้านค้าทั้งหมด และ $4\leq N\leq 200,000$<br>
    $M$ หมายถึง จํานวนเส้นทาง และ $3\leq M\leq 300,000$<br>
    $L$ หมายถึง จํานวนโซน และ $3\leq L\leq 10$<br>
    $n_i$ หมายถึง จำนวนร้านในแต่ละโซน และ
    - $\sum_{i=1}^{L} n_i=N$
    - $\prod_{i=1}^{L} n_i \leq 10^6$
    - $n_1=n_L=1$
      

!!! note "Prerequisites"
	- `Brute Force`
    - `Divide and Conquer`

---

## Solution

### ข้อสังเกต

- $\prod_{i=1}^{L} n_i \leq 10^6$
- สูตรคำนวณ “ค่าความต่างใจ”: $D = (F − F′)^2 + (G − G′)^2$ ค่อนข้างคล้ายกับสูตรคำนวณ Euclidean Distance: $D=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$

### วิธีทำ

เราจะทำการ Brute Force เพื่อหาทุกๆคู่อันดับ $(F,G)$ ที่เป็นไปได้ (เราสามารถทำการ Brute Force ได้เพราะว่า ผลคูณของจำนวนร้านทั้งหมดในแต่ละโซน จะมีค่าไม่เกิน $10^6$) และเมื่อเราหาออกมาแล้ว เราจะใช้อัลกอริทึมที่ชื่อว่า “Closest Pair of Points” ซึ่งจริงๆแล้วใช้หาระยะที่สั้นที่สุดระหว่างจุดสองจุด แต่เนื่องจากสูตรคำนวณค่าความต่างใจเหมือนกับสูตรคำนวณ Euclidean Distance (ต่างกันแค่สูตรคำนวณ Euclidean Distance จะมีการใส่เครื่องหมาย Square Root ($\sqrt{}$) เราจึงสามารถใช้อัลกอริทึมดังกล่าวเพื่อหาคู่อันดับ $(F,G)$ 2 คู่ที่เมื่อคำนวณ “ค่าความต่างใจ” ออกมาแล้ว จะมีค่าน้อยที่สุด

### Summary

- ใช้การ Brute Force ในการหาคู่อันดับ $(F,G)$ ทั้งหมด
- ใช้อัลกอริทึม Closest Pair of Points ในการหา “ค่าความต่างใจ” ที่น้อยที่สุด

---

## Code

```cpp title="toi20_tour.cpp"
#include <bits/stdc++.h> 

#define int long long 

using namespace std; 

const int N = 1e1 + 5; 

int n, m, l, z[N]; 
vector <pair <int, int>> p; 
vector <tuple <int, int, int>> adj[200005]; 

void dfs(int u, int x, int y) { 
	for (auto [s, w, v] : adj[u]) { 
		if (v == n) { 
			p.emplace_back((s == 1 ? make_pair(x + w, y) : make_pair(x, y + w))); continue; 
		} 
		if (s == 1) dfs(v, x + w, y); 
		else dfs(v, x, y + w); 
	} 
} 
int dis(pair <int, int> a, pair <int, int> b) { // ใช้คำนวณ ค่าความต่างใจ / euclidean distance 
	return (a.first - b.first) * (a.first - b.first) + (a.second - b.second) * (a.second - b.second); 
} 

int cpop(int l, int r){ 
	if (r - l + 1 <= 3) { 
		int ans = 1e18; 
		for (int i = l; i < r; i++) { 
			for (int j = i + 1; j <= r; j++) { 
				ans = min(ans, dis(p[i], p[j])); 
			} 
		} 
		return ans; 
	} 
	int mid = (l + r) / 2; 
	int left = cpop(l, mid), right = cpop(mid, r); 
	int mn = min(left, right); 
	int xm = p[mid].first; 
	vector <pair <int, int>> pts; 
	for (int i = l; i <= r; i++) { 
		if ((p[i].first - xm) * (p[i].first - xm) < mn) pts.emplace_back(p[i]); 
	} 
	sort(pts.begin(), pts.end(), [](const pair <int, int> &a, const pair <int, int> &b){ 
		return a.second < b.second;
	}); 
	for (int i = 0; i < pts.size(); i++) { 
		for (int j = i + 1; j < pts.size() && dis(pts[i], pts[j]) < mn; j++) { 
			mn = min(mn, dis(pts[i], pts[j])); 
		} 
	} 
	return mn; 
} 

int32_t main(){ 
	cin.tie(NULL)->sync_with_stdio(false); // input 
	cin >> n >> m >> l; 
	for (int i = 1; i <= l; i++) cin >> z[i]; 
	for (int i = 1; i <= m; i++) { 
		int u, v, s, w; cin >> u >> v >> s >> w; 
		adj[u].emplace_back(s, w, v); 
	} 
	// brute force calculations 
	dfs(1, 0, 0); 
	// closest pair of points algorithm 
	sort(p.begin(), p.end()); 
	cout << cpop(0, p.size() - 1); 
}
```

!!! note "Total Time Complexity"
    กำหนดให้ $x=$ จำนวนคู่อันดับ $(F,G)$ ที่หาออกมาได้

    - Brute Force: $O(x)$
    - Closest Pair of Points: $O(x\log x)$
    - **Total: $O(x+x\log x)=O(x\log x)$**
