
# asteroids = [5,10,-5]
# positive --> right, Negative --> left
# remember [-1,10] never collide because -1 ---> left and 10 ---> right.
def asteroidCollision(asteroids):
    stack = []

    for a in asteroids:
        # reason why we are using while instead of if because consider this case
        # [5,10,-15] output would be [-15]
        while stack and a < 0 and stack[-1] > 0:
            diff = a + stack[-1]
            if diff < 0:
                stack.pop()
            elif diff > 0:
                a = 0
            else:
                a = 0
                stack.pop()
        if a:
            stack.append(a)
    return stack


asteroids = [-10, 5, 10, -5]
print(asteroidCollision(asteroids))
