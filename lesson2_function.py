import math


def move(x,y,step,angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi / 6)
print(x,y)

def quadratic(a,b,c):
    x = math.sqrt(b**2 - 4 * a *c)
    x1 = (-b + x) /( 2 * a)
    x2 = (-b - x) /( 2 * a)
    return x1,x2


def mul(*nums):
    result = 1
    if len(nums) == 0:
        raise TypeError("")
    else:
        for num in nums:
            result = result * num
    return result



try:
    mul(1)
    print("测试失败")
except TypeError:
    print("测试成功")