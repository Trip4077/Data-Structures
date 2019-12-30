from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=3):
        self.limit = limit
        self.size = 0
        self.list = DoublyLinkedList()
        self.storage = {}

    def print_storage(self):
        for key,value in self.storage.items():
            print("<%=  " + key + ":" + value.value[key] + "  =%>")

    def print_list(self):
        self.list.print()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if not key in self.storage: return None
        print(self.storage[key].value[key])
        return self.storage[key].value[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        self.size += 1
        # if limit is exceeded, make space before insert
        if self.limit < self.size and not key in list( self.storage.keys() ):       
            # get key in node and remove from storage
            for tail_key in self.list.tail.value:
                self.storage.pop( tail_key, None )
           
            self.list.remove_from_tail()
            self.size -= 1
       
        # Check if key needs to be inserted or updated
        if key in list( self.storage.keys() ):
            self.list.delete( self.storage[key] )
            self.storage.pop( key, None )

            self.list.add_to_head({ key: value })
            self.storage[key] = self.list.head

        else:
            self.list.add_to_head({ key: value })
            self.storage[key] = self.list.head
            
        
        #print(self.print_storage())
        
        
# cache = LRUCache()

# cache.set('item1', 'a')
# cache.set('item2', 'b')
# cache.set('item3', 'c')

# cache.set('item2', 'z')

# cache.get('item1')
# cache.get('item2')

# cache.set('item1', 'a')
# cache.set('item2', 'b')
# cache.set('item3', 'c')

# cache.get('item1')

# cache.set('item4', 'd')

# cache.get('item1')
# cache.get('item3')
# cache.get('item4')
# cache.get('item2')

# cache.print_list()
# cache.print_storage()