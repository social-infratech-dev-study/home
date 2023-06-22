### 31 Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

```
Input: nums = [1,2,3]
Output: [1,3,2]
```

```
Input: nums = [3,2,1]
Output: [1,2,3]
```

```
Input: nums = [1,1,5]
Output: [1,5,1]
```


```rust
use std::collections::HashMap;

impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        let compare : Vec<i32> = nums.to_vec();
        nums.sort();
        nums.reverse();
        if compare == nums.to_vec() {
            nums.reverse();
            return;
        }
        nums.reverse();
        let mut duplicated = HashMap::new();
        let mut temp : Vec<i32> = Vec::new();
        let mut used : Vec<i32> = vec![0;nums.len()];
        let mut answer : Vec<i32> = Vec::new();
        let mut found : bool = false;
        let mut finished : bool = false;
        Solution::dfs(nums, nums.len(), &mut used, &mut duplicated, &temp, &compare, &mut answer, &mut found, &mut finished);
        *nums = answer.clone();
        return;
    }

    pub fn dfs(nums : &mut Vec<i32>, l : usize, used : &mut Vec<i32>, duplicated : &mut HashMap<Vec<i32>, bool>, temp : &Vec<i32>, compare : &Vec<i32>, answer : &mut Vec<i32>, found : &mut bool, finished : &mut bool){
        if *finished {
            return;
        }
        if temp.len() == l {
            match duplicated.get(&temp.clone()) {
                Some(&_value) => {
                    return;
                }
                _ => {
                    duplicated.insert(temp.clone(), true);
                }
            }
            if *found && temp.to_vec() != *compare {
                *answer = temp.to_vec();
                *found = false;
                *finished = true;
            } else {
                if temp.to_vec() == *compare {
                    *found = true;
                }
            }
        } else {
            for i in 0..nums.len() {
                let mut temp2 : Vec<i32> = Vec::new();
                temp2.extend(temp);
                if used[i] == 0 {
                    temp2.push(nums[i]);
                    used[i] = 1;
                    Solution::dfs(nums, l, used, duplicated, &temp2, compare, answer, found, finished);
                    used[i] = 0;
                }
            }
        }
        return;
    }
}
```
