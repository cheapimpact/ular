import random

score = 0
# print("bilangan ", a, " + ", b, " = ", c)
while True:
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = a + b
    c_str = repr(c)
    c2 = int(c_str[-1])
    c3 = c2 % 2
    # print(c, " ", c2, " ", c3)
    print(a, " + ", b, " = ")
    guess = int(input())
    if guess == c3:
        print("mantap")
        score += 1
    else:
        print("gg, score 0: ", score)
        break
