from typing import Optional, Sequence, TypeVar

T = TypeVar("T")


def binary_search(items: Sequence[T], target: T) -> Optional[int]:
    """Return the index of target in a sorted sequence, or None if absent.

    Runs in O(log n) time. If target occurs more than once, any matching
    index may be returned.
    """
    low, high = 0, len(items) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    assert binary_search(data, 7) == 3
    assert binary_search(data, 1) == 0
    assert binary_search(data, 11) == 5
    assert binary_search(data, 4) is None
    assert binary_search([], 1) is None
    assert binary_search([2], 2) == 0
    assert all(binary_search(data, x) == i for i, x in enumerate(data))
    print("all checks passed")
