import pytest
from pyds_a.data_structures.linked_list import LinkedList  # Import your LinkedList implementation

def test_empty_linked_list():
    test_list = LinkedList()
    assert test_list.is_empty() is True
    assert test_list.size() == 0

def test_linked_list_insert():
    test_list = LinkedList()
    test_list.insert(1)
    assert test_list.size() == 1
    assert test_list.search(1) is True

def test_linked_list_delete():
    test_list = LinkedList()
    test_list.insert(1)
    test_list.insert(2)
    test_list.delete(1)
    assert test_list.size() == 1
    assert test_list.search(1) is False
    assert test_list.search(2) is True

def test_linked_list_get_list():
    test_list = LinkedList()
    test_list.insert(1)
    test_list.insert(2)
    test_list.insert(3)
    assert test_list.get_list() == [1, 2, 3]

def test_linked_list_clear():
    test_list = LinkedList()
    test_list.insert(1)
    test_list.insert(2)
    test_list.clear()
    assert test_list.size() == 0
    assert test_list.is_empty() is True
    assert test_list.search(1) is False
    assert test_list.search(2) is False

if __name__ == "__main__":
    pytest.main()
