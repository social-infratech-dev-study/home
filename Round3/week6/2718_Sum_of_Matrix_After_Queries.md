### 2718. Sum of Matrix After Queries

https://leetcode.com/problems/sum-of-matrix-after-queries/

You are given an integer n and a 0-indexed 2D array queries where queries[i] = [typei, indexi, vali].

Initially, there is a 0-indexed n x n matrix filled with 0's. For each query, you must apply one of the following changes:

if typei == 0, set the values in the row with indexi to vali, overwriting any previous values.
if typei == 1, set the values in the column with indexi to vali, overwriting any previous values.
Return the sum of integers in the matrix after all queries are applied.

Example 1:

```
Input: n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
Output: 23
Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 23.
```

Example 2:

```
Input: n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
Output: 17
Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 17.
```

Constraints:

1 <= n <= 104
1 <= queries.length <= 5 * 104
queries[i].length == 3
0 <= typei <= 1
0 <= indexi < n
0 <= vali <= 105


```rust
use std::collections::HashMap;

impl Solution {
    pub fn matrix_sum_queries(n: i32, queries: Vec<Vec<i32>>) -> i64 {
        let mut answer :i64 = 0;
        let mut row_count : i16 = 0;
        let mut col_count : i16 = 0;
        let mut row_hash : HashMap<i16, bool> = HashMap::new();
        let mut col_hash : HashMap<i16, bool> = HashMap::new();
        for i in (0..queries.len()).rev() {
            if queries[i][0] == 0 {
                if let Some(_) = row_hash.get(&(queries[i][1] as i16)) {
                    continue;
                }
                answer += (queries[i][2] as i64)*((n as i64)-(col_count as i64));
                row_count += 1;
                row_hash.insert(queries[i][1] as i16, true);
            }

            if queries[i][0] == 1 {
                if let Some(_) = col_hash.get(&(queries[i][1] as i16)) {
                    continue;
                }
                answer += (queries[i][2] as i64)*((n as i64)-(row_count as i64));
                col_count += 1;
                col_hash.insert(queries[i][1] as i16, true);
            }
        }

        return answer;
    }
```
