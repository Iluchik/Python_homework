from homePackage import sum_all
from random import randint
# enter numbers like "1 2 3 4 5 6 7"
print(sum_all([int(x) for x in input().split()] or [randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)]))