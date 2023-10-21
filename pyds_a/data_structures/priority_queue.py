"""
Author: Your Name

Priority Queue Implementation (using a Binary Heap)

This priority queue is implemented using a binary heap data structure, where elements with lower priority (higher values) are dequeued first.
"""

class PriorityQueue:
    """
    Priority queue based on a binary heap data structure.
    Elements with higher priority (lower values) are dequeued first.
    """

    def __init__(self):
        """
        Initializes an empty priority queue.
        """
        self.heap = []

    def __len__(self) -> int:
        """
        Returns the number of elements in the priority queue.
        """
        return len(self.heap)

    def is_empty(self) -> bool:
        """
        Checks if the priority queue is empty.
        """
        return len(self) == 0

    def enqueue(self, data, priority: int):
        """
        Inserts an element with the given priority into the priority queue.

        Args:
            data: The element to enqueue.
            priority: The priority of the element.

        Returns:
            The modified priority queue.
        """
        entry = (priority, data)
        self.heap.append(entry)
        self._heapify_up(len(self.heap) - 1)
        return self

    def dequeue(self):
        """
        Removes and returns the element with the highest priority from the queue.

        Returns:
            The element with the highest priority.
        """
        if len(self) == 0:
            raise IndexError("Priority queue is empty")

        if len(self) == 1:
            return self.heap.pop()[1]

        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return top[1]

    def _heapify_up(self, index):
        # Internal method to maintain the heap property during insertion.
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent_index][0]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        # Internal method to maintain the heap property during deletion.
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if (
                left_child_index < len(self)
                and self.heap[left_child_index][0] < self.heap[smallest][0]
            ):
                smallest = left_child_index

            if (
                right_child_index < len(self)
                and self.heap[right_child_index][0] < self.heap[smallest][0]
            ):
                smallest = right_child_index

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
