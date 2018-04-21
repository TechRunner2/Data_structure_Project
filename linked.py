class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):
      self._element = element
      self._next = next

  #------------------------------- queue methods -------------------------------
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0                          # number of queue elements

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise 'Queue is empty'
    return self._head._element              # front aligned with head of list

  def get(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise 'Queue is empty'
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                     # special case as queue is empty
      self._tail = None                     # removed head had been the tail
    return answer

  def put(self, e):
    """Add an element to the back of queue."""
    newest = self._Node(e, None)            # node will be new tail node
    if self.is_empty():
      self._head = newest                   # special case: previously empty
    else:
      self._tail._next = newest
    self._tail = newest                     # update reference to tail node
    self._size += 1

  def print_linked(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    t = self._Node(None, None)
    t = self._head

    if self.is_empty():
      raise 'Queue is empty'
    else:
       for i in range(self._size):
            if i != None:
                print('i = ', i, '\telement = ', t._element)
            t = t._next
    
  def insert_linked(self, room_no, e):
      t = self._Node(None, None)
      newest = self._Node(e, None)
    
      if self.is_empty():
         self._head = newest
         self._tail = newest                     # update reference to tail node
      elif room_no == 0:
         newest._next = self._head
         self._head = newest
      elif room_no == self._size:
         newest._next = None
         self._tail._next = newest
         self._tail = newest
      else:
         for i in range(self._size):
            if i == 1:
               t = self._head
            if i == room_no:
               print('i=',i,'\troom_no=',room_no)
               print('t->element = ',t._element)
               newest._next = t._next
               print('newest->next->element = ',newest._next._element)
               t._next = newest
               print('t->next->element = ',t._next._element)

            if i != 0:
               t=t._next
      self._size += 1
