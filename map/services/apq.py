class Element:
  """ A key, value and index. """
  def __init__(self, key: int, value: any, index: int):
    self._key = key
    self._value = value
    self._index = index
  
  def __eq__(self, other):
    return self._key == other._key
  
  def __lt__(self, other):
    return self._key < other._key
  
  def wipe(self):
    self._key = None
    self._value = None
    self._index = None
    

class UnsortedAPQ:
  def __init__(self) -> None:
    self.__heap = []

  def __len__(self) -> int:
    ''' Return the number of items in the APQ '''
    return len(self.__heap)

  def add_item(self, key: int, item: any):
    ''' Add a new item into the priority queue with priority key, and return its Element in the APQ '''
    next_index = len(self)
    new_el = Element(key, item, next_index)
    self.__heap.append(new_el)
    return new_el
  
  def min(self):
    ''' Return the element with the minimum key '''
    return min(self.__heap, lambda el: el._key)
  
  def remove_min(self):
    ''' Return and remove the value with the minimum key '''
    if len(self) == 0:
      return None
    
    min_index = 0

    for index in range(len(self)):
      if self.__heap[index] < self.__heap[min_index]:
        min_index = index

    self.__swap(min_index, -1) # Move item to remove into last index
    removed_el: Element = self.__heap.pop()
    return (removed_el._key, removed_el._value)
  
  def update_key(self, element: Element, new_key: int):         
    ''' update the key in element to be new_key, and re-balance the APQ '''
    element._key = new_key
    return
  
  def get_key(self, element: Element):
    ''' return the current key for element '''
    return element._key
  
  def remove(self, element: Element) -> tuple:
    ''' Remove the element from the APQ, and re-balance APQ. Returns tuple in format `(key, value)`. '''
    self.__swap(element._index, -1) # Swap last element with provided element
    self.__heap.pop()
    return (element._key, element._value)
  
  def __swap(self, x: int, y: int):
    ''' Private function to swap the index of two elements in the heap '''
    self.__heap[x], self.__heap[y] = self.__heap[y], self.__heap[x]
    self.__heap[x]._index = x
    self.__heap[y]._index = y


class BinaryHeapAPQ:
  def __init__(self) -> None:
    self.__heap = []

  def __str__(self) -> str:
    print_string = "|-"
    
    for e in self.__heap:
      print_string += f" {e._value}({e._key}) -"

    return print_string + ">"

  def __len__(self) -> int:
    ''' Return the number of items in the APQ '''
    return len(self.__heap)

  def add_item(self, key: int, item: any):
    ''' Add a new item into the priority queue with priority key, and return its Element in the APQ '''
    next_index = len(self)
    new_el = Element(key, item, next_index)
    self.__heap.append(new_el)
    self.__bubble_up(len(self) - 1)
    return new_el
  
  def min(self):
    ''' Return the element with the minimum key '''
    return self.__heap[0]
  
  def remove_min(self):
    return self.remove(self.__heap[0])
  
  def remove(self, element: Element) -> tuple:
    ''' Remove the element from the APQ, and re-balance APQ. Returns tuple in format `(key, value)`. '''
    # Swap last element with provided element and bubble el into correct position
    index = element._index
    self.__swap(index, -1) 
    popped_el = self.__heap.pop()
    
    if len(self) > 1:
      self.__bubble_down(index)

    return (popped_el._key, popped_el._value)
  
  def update_key(self, element: Element, new_key: int):         
    ''' Update the key in element to be new_key, and re-balance the APQ '''
    prev_key = element._key
    if new_key > prev_key: # Key has increased, so bubble down
      element._key = new_key
      self.__bubble_down(element._index)

    elif new_key < prev_key: # Key has decreased, so bubble up
      element._key = new_key
      self.__bubble_up(element._index)
  
  def get_key(self, element: Element):
    ''' return the current key for element '''
    return element._key
  
  def __bubble_up(self, index):
    ''' Recursively compares a given element at `index` with its parents until it reaches its correct position in the APQ '''
    if index <= 0: return
      
    parent = (index - 1) // 2

    if self.__heap[parent]._key > self.__heap[index]._key:
      self.__swap(parent, index)
      return self.__bubble_up(parent)
    else: return
  
  def __bubble_down(self, index):
    ''' Recursively compares a given element at `index` with its children until it reaches its correct position in the APQ '''
    if index >= len(self) // 2 and index < len(self):
      return
      
    min_child = self.__min_child(index)

    if (self.__heap[index]._key > self.__heap[min_child]._key):
      self.__swap(index, min_child)
      return self.__bubble_down(min_child)
    else: return

  def __min_child(self, index):
    ''' Returns the index of the minimum child for a given `index` '''
    left_child = (index * 2) + 1
    right_child = (index * 2) + 2

    if right_child >= len(self):
      return left_child
    else:
      if self.__heap[left_child]._key < self.__heap[right_child]._key:
        return left_child
      else:
        return right_child
  
  def __swap(self, x: int, y: int):
    ''' Private function to swap the index of two elements in the heap '''
    self.__heap[x], self.__heap[y] = self.__heap[y], self.__heap[x]
    self.__heap[x]._index = x
    self.__heap[y]._index = y



def test_heap():
  heap = BinaryHeapAPQ()
  ant = heap.add_item(35, 'ant')
  fox = heap.add_item(18, 'fox')
  bed = heap.add_item(14, 'bed')
  dog = heap.add_item(22, 'dog')
  egg = heap.add_item(27, 'egg')
  cat = heap.add_item(24, 'cat')

  print(str(heap))
  heap.update_key(ant, 13)
  print(str(heap))
  heap.update_key(fox, 25)
  print(str(heap))
  heap.remove_min()
  print(str(heap))

# test_heap()