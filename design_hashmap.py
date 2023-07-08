# 706. Design HashMap
# Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        if self.buckets[hash_key] is None:
            self.buckets[hash_key] = ListNode(key, value)
        else:
            curr = self.buckets[hash_key]
            while True:
                if curr.key == key:
                    curr.val = value
                    return
                if curr.next is None:
                    break
                curr = curr.next
            curr.next = ListNode(key, value)
        
    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        curr = self.buckets[hash_key]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        prev = curr = self.buckets[hash_key]
        while curr:
            if curr.key == key:
                if curr == prev:
                    self.buckets[hash_key] = curr.next
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next

obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
print(obj.get(3))
obj.put(2,1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))

# Time Complexity:
# Add - O(1) and O(n) (Worst case)
# Remove - O(1) and O(n) (Worst case)
# Conatins - O(1) and O(n) (Worst case)
# Space Complexity:
# O(n) -> n - number of linked lists stored in buckets

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]