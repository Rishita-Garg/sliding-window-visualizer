from collections import deque

def sliding_window_max(nums, k):
    if not nums or k == 0:
        return []

    result = []
    window = deque()

    for i, n in enumerate(nums):
        while window and nums[window[-1]] < n:
            window.pop()
        window.append(i)

        if window[0] == i - k:
            window.popleft()

        if i >= k - 1:
            result.append(nums[window[0]])

    return result
