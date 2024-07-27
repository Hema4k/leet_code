from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(positionSpeed, reverse=True):
            arrival = (target - p) / s
            stack.append(arrival)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                # If the top element arrives faster than the next element
                stack.pop()

        return len(stack)