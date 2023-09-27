import pytest
from pyds_a.data_structures.linked_list import LinkedList  # Import your LinkedList implementation

def test_empty_linked_list():
    ll = LinkedList()
    assert ll.is_empty() is True
    assert ll.size() == 0

def test_linked_list_insert():
    ll = LinkedList()
    ll.insert(1)
    assert ll.size() == 1
    assert ll.search(1) is True

def test_linked_list_delete():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.delete(1)
    assert ll.size() == 1
    assert ll.search(1) is False
    assert ll.search(2) is True

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
    assert ll.is_empty() is True
    assert ll.search(1) is False
    assert ll.search(2) is False

if __name__ == "__main__":
    pytest.main()
