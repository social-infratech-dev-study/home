### 898. Bitwise ORs of Subarrays

https://leetcode.com/problems/bitwise-ors-of-subarrays/

Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.
The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

```
Input: arr = [0]
Output: 1
Explanation: There is only one possible result: 0.
```

Example 2:

```
Input: arr = [1,1,2]
Output: 3
Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
```

Example 3:

```
Input: arr = [1,2,4]
Output: 6
Explanation: The possible results are 1, 2, 3, 4, 6, and 7.
```

```rust
use std::collections::HashSet;

impl Solution {
    pub fn combination(level:i32, start:i32, reach:i32, arr:&Vec<i32>, result: &mut Vec<i32>, answer: &mut Vec<Vec<i32>>) {
        if level == reach {
            answer.push(result.to_vec());
            return;
        }
        for i in start..arr.len() as i32 {
            result[level as usize] = arr[i as usize];
            Solution::combination(level+1, start+1, reach, arr, result, answer);
        }
    }

    pub fn get_all_bitwise_result(arr: Vec<i32>, results : &mut Vec<i32>) {
        results.extend(&arr);
        let mut result : Vec<i32> = vec![0; 2];
        let mut answer : Vec<Vec<i32>> = Vec::new();
        Solution::combination(0, 0, 2, &arr, &mut result, &mut answer);
        for i in answer.iter() {
            results.push(i[0] | i [1])
        }
    }

    pub fn subarray_bitwise_o_rs(arr: Vec<i32>) -> i32 {
        let set : HashSet<i32> = arr.into_iter().collect();
        let mut results : Vec<i32> = Vec::new();
        Solution::get_all_bitwise_result(set.into_iter().collect::<Vec<_>>(), &mut results);
        let distinct_results : HashSet<i32> = results.into_iter().collect();
        println!("{:?}", distinct_results);
        return distinct_results.len() as i32;
    }
}
```
