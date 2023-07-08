# 705. Design HashSet
# Design a HashSet without using any built-in hash table libraries.
# Implement MyHashSet class:
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def hash_funtion(self, key: int):
        return key % self.size

    def add(self, key: int) -> None:
        hash_key = self.hash_funtion(key)
        bucket = self.buckets[hash_key]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        hash_key = self.hash_funtion(key)
        bucket = self.buckets[hash_key]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        hash_key = self.hash_funtion(key)
        bucket = self.buckets[hash_key]
        return key in bucket

obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
obj.remove(2)
print(obj.contains(2))

# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)