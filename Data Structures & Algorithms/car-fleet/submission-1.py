class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        n = len(speed)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort(key = lambda x: x[0], reverse = True)
        for i in range(n):
            curr = (target - cars[i][0])/ cars[i][1]
            if not stack:
                stack.append(curr)
            elif stack[-1] >= curr:
                continue
            else:
                stack.append(curr)
        return len(stack)