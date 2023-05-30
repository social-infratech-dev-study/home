### 2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

```rust

    // Definition for singly-linked list.
    // #[derive(PartialEq, Eq, Clone, Debug)]
    // pub struct ListNode {
    //   pub val: i32,
    //   pub next: Option<Box<ListNode>>
    // }
    // 
    // impl ListNode {
    //   #[inline]
    //   fn new(val: i32) -> Self {
    //     ListNode {
    //       next: None,
    //       val
    //     }
    //   }
    // }

    impl Solution {
        pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
            let mut head = Box::new(ListNode::new(0));
            let mut l3 = &mut head;
            let mut carry = 0;
            let mut m1 = &l1;
            let mut m2 = &l2;

            loop {
                let mut sum = 0;
                
                match(m1, m2) {
                    (Some(n1), Some(n2)) => {
                        sum = n1.val + n2.val;
                        m1 = &n1.next;
                        m2 = &n2.next;
                    }
                    (Some(n1), None) => {
                        sum = n1.val;
                        m1 =  &n1.next;
                    }
                    (None, Some(n2)) => {
                        sum = n2.val;
                        m2 = &n2.next;
                    }
                    (None, None) => {
                        break
                    }

                }
                if carry + sum > 9 {
                    sum = carry + sum - 10;
                    carry = 1;
                } else {
                    sum = carry + sum;
                    carry = 0;
                }

                l3.next = Some(Box::new(ListNode::new(sum)));
                l3 = l3.next.as_mut().unwrap();
            }

            if carry > 0 {
                l3.next = Some(Box::new(ListNode::new(carry)));
            }
            head.next
        }
    }

```
