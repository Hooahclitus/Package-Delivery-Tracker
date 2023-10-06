class HashTable:
    def __init__(self, size=40, *entries):
        self.table = [[] for i in range(size)]

        if entries:
            for i in range(0, len(entries), 2):
                key = entries[i]
                val = entries[i + 1]
                self.assoc(key, val)

    def __bucket(self, key):
        return self.table[hash(key) % len(self.table)]

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

    def dissoc(self, *keys):
        for key in keys:
            for entry in (bucket := self.__bucket(key)):
                if entry[0] == key:
                    bucket.remove(entry) 

    def get(self, *keys, entry=False):
        get_value = ((lambda key: next(([k, v] for k, v in self.__bucket(key) if k == key), None)) 
                     if entry == True 
                     else (lambda key: next((v for k, v in self.__bucket(key) if k == key), None)))

        match keys:
            case [key]:
                return get_value(key)
            case [*keys]:
                return [get_value(key) for key in keys] 

    def size(self):
        return len([package for package in self.table])

    def __iter__(self):
        self.__index = 0
        self.__current_bucket = None
        return self

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

    def items(self):
        all_items = []
        for bucket in self.table:
            for key, value in bucket:
                all_items.append((key, value))
        return all_items
    
    def keys(self):
        all_keys = []
        for bucket in self.table:
            for key, _ in bucket:
                all_keys.append(key)
        return all_keys

    def values(self):
        all_values = []
        for bucket in self.table:
            for _, value in bucket:
                all_values.append(value)
        return all_values
