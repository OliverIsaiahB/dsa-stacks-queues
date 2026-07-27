"""A MONOTONIC stack keeps its contents in sorted order by popping anything that
would break the order. It solves 'next greater element' and span problems in
a single amortized O(n) pass — a technique interviewers love."""
from __future__ import annotations


def next_greater(nums: list[int]) -> list[int]:
    """For each element, the next element to its right that is strictly greater,
    or -1 if none. One pass using a decreasing monotonic stack of INDICES."""
    result = [-1] * len(nums)
    stack: list[int] = []                # indices of values awaiting their answer
    for i, value in enumerate(nums):
        # pop every index whose value is now beaten by the current value
        while stack and nums[stack[-1]] < value:
            j = stack.pop()
            result[j] = value            # value is j's next greater element
        stack.append(i)                  # i waits for ITS next greater
    return result                        # anything left on the stack stays -1


def daily_temperatures(temps: list[int]) -> list[int]:
    """How many days until a warmer temperature, per day (0 if never)."""
    answer = [0] * len(temps)
    stack: list[int] = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j            # distance to the warmer day
        stack.append(i)
    return answer
