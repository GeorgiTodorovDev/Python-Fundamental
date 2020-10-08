import math
person_elevator = int(input())
elevator_capacity = int(input())

result = math.ceil(person_elevator / elevator_capacity)
print(result)