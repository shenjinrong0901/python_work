from HashTableClass import HashTable

def put(self,key,data):
    hashvalue = self.hashfunction(key,len(self.slots)) #计算初始散列值

    if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data  #键值都不存在
    else:
        if self.slots[hashvalue] == key:
            self.data[hashvalue] = data  #如果键已存在，则替换新的值
        else:
            nextslot = self.rehash(hashvalue,len(self.slots))
            while self.slots[nextslot] != None and \
                            self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

def hashfunction(self,key,size):
    return key % size

def rehash(self,oldhash,size):
    return (oldhash + 1) % size


def get(self,key):
    startslot = self.hashfunction(key,len(self.slots))

    data = None
    stop = False
    found = False
    position = startslot
    while self.slots[position] != None and \
                not found and not stop:
        if self.slots[position] == key:
            found = True
            data = self.data[position]
        else:
            position = self.rehash(position,len(self.slots))
            if position == startslot:
                stop = True
    return data

def __getitem__(self,key):
    return self.get(key)

def __setitem__(self,key,data):
    self.put(key,data)

H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "row"
H[55] = "pig"
H[20] = "chicken"
print(H.slots)



