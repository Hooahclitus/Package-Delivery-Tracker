class HashTable:
    # Initialize hash table with size and optional entries
    def __init__(self, size=40, *entries):
        self.table = [[] for _ in range(size)]

        if entries:
            for i in range(0, len(entries), 2):
                key = entries[i]
                val = entries[i + 1]
                self.assoc(key, val)

    # Get bucket for a key
    def __bucket(self, key):
        return self.table[hash(key) % len(self.table)]

    # Associate key-value pairs in hash table
    def assoc(self, *entries):
        for i in range(0, len(entries), 2):
            key = entries[i]
            val = entries[i + 1]
            for entry in enumerate((bucket := self.__bucket(key))):
                if entry[1][0] == key:
                    bucket[entry[0]] = [key, val]
                    break
            else:
                bucket.append([key, val])

    # Remove key-value pairs from hash table
    def dissoc(self, *keys):
        for key in keys:
            for entry in (bucket := self.__bucket(key)):
                if entry[0] == key:
                    bucket.remove(entry)

    # Get values for keys from hash table
    def get(self, *keys):
        match keys:
            case [key]:
                return next((v for k, v in self.__bucket(key) if k == key), None)
            case [*keys]:
                return [next((v for k, v in self.__bucket(key) if k == key), None) for key in keys]

    # Clear hash table
    def clear(self):
        self.table.clear()

    # Get the size of hash table
    def size(self):
        return len([package for package in self.table])

    # Initialize iterator
    def __iter__(self):
        self.__index = 0
        self.__current_bucket = None
        return self

    # Get next item in iteration
    def __next__(self):
        if self.__index < len(self.table):
            if self.__current_bucket is None or len(self.__current_bucket) == 0:
                while self.__index < len(self.table):
                    self.__current_bucket = self.table[self.__index]
                    self.__index += 1
                    if len(self.__current_bucket) > 0:
                        break
            if len(self.__current_bucket) > 0:
                return self.__current_bucket.pop(0)
            else:
                raise StopIteration
        else:
            raise StopIteration

    # Get all key-value pairs
    def items(self):
        all_items = []
        for bucket in self.table:
            for key, value in bucket:
                all_items.append((key, value))
        return all_items

    # Get all keys
    def keys(self):
        all_keys = []
        for bucket in self.table:
            for key, _ in bucket:
                all_keys.append(key)
        return all_keys

    # Get all values
    def values(self):
        all_values = []
        for bucket in self.table:
            for _, value in bucket:
                all_values.append(value)
        return all_values
