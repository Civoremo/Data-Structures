Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
O(1) -> constant
We are only dealing with one item at a time

2. What is the runtime complexity of `dequeue`?
O(1) -> constant
We only deal with removing one item at a time

3. What is the runtime complexity of `len`?
O(1) -> constant
We only reference the value

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
O(1) -> constant

2. What is the runtime complexity of `ListNode.insert_before`?
O(1) -> constant

3. What is the runtime complexity of `ListNode.delete`?
O(1) -> constant

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1) -> constant

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1) -> constant

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(1) -> constant

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(1) -> constant

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(1) -> constant

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(n) -> depending on which element needs to be moved; if head or tail, time complexity if O(n) otherwise it turns to O(n) as it goes throught the list to find the item that needs to be moved

10. What is the runtime complexity of `DoublyLinkedList.delete`?
O(1) -> constant

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?