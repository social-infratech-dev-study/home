### 335. Self Crossing

https://leetcode.com/problems/self-crossing/description/

You are given an array of integers distance.

You start at the point (0, 0) on an X-Y plane, and you move distance[0] meters to the north, then distance[1] meters to the west, distance[2] meters to the south, distance[3] meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.

Return true if your path crosses itself or false if it does not.

Example 1:

```
Input: distance = [2,1,1,2]
Output: true
Explanation: The path crosses itself at the point (0, 1).
```

Example 2:

```
Input: distance = [1,2,3,4]
Output: false
Explanation: The path does not cross itself at any point.
```

Example 3:

```
Input: distance = [1,1,1,2,1]
Output: true
Explanation: The path crosses itself at the point (0, 0).
```

```rust
impl Solution {
    pub fn is_self_crossing(distance: Vec<i32>) -> bool {
        let mut b : i32 = 0;
        let mut c : i32 = 0;
        let mut d : i32 = 0;
        let mut e : i32 = 0;
        let mut f : i32 = 0;
        for a in &distance {
            if ((d >= b) && (b > 0)) && ((*a >= c && c > 0) || (((f + b) >= d && d > 0 ) && ((*a + e) >= c) && c > 0 && c >= e)) {
                return true;
            }
            f = e;
            e = d;
            d = c;
            c = b;
            b = *a as i32;
        }
        return false;
    }
}
```
