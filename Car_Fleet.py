class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list()
        stack = list()
        for index in range(len(position)):
            cars.append([position[index], speed[index]])
        
        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        print(cars)
        
        for pos, spd in cars:
            stack.append((target-pos)/spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
