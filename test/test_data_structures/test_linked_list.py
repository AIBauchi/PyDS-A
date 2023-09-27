import pytest
from pyds_a.data_structures.linked_list import LinkedList  # Import your LinkedList implementation

def test_empty_linked_list():
    ll = LinkedList()
    assert ll.is_empty() == True
    assert ll.size() == 0

def test_linked_list_insert():
    ll = LinkedList()
    ll.insert(1)
    assert ll.size() == 1
    assert ll.search(1) == True

def test_linked_list_delete():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.delete(1)
    assert ll.size() == 1
    assert ll.search(1) == False
    assert ll.search(2) == True

def test_linked_list_get_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.get_list() == [1, 2, 3]

def test_linked_list_clear():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.clear()
    assert ll.size() == 0
    assert ll.is_empty() == True
    assert ll.search(1) == False
    assert ll.search(2) == False

if __name__ == "__main__":
    pytest.main()
