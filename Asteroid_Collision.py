'''
We are given an array asteroids of integers representing asteroids in a row. 
The indices of the asteriod in the array represent their relative position in space.
For each asteroid, the absolute value represents its size, 
and the sign represents its direction 
(positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
'''


def asteroidCol(asteroids):
    stack=[]
    for ast in asteroids:
        # Assume current asteroid survives unless destroyed
        alive = True

        # Collision can only happen if stack top is right-moving (+) 
        # and current asteroid is left-moving (-)
        while alive and stack and stack[-1] > 0 and ast < 0:
            if stack[-1] < -ast:
                # Top asteroid is smaller → it explodes
                stack.pop()
                # Continue checking with new top of stack
                continue
            elif stack[-1] == -ast:
                # Both are same size → both explode
                stack.pop()
            # In both equal and larger cases, current asteroid is destroyed
            alive = False

        if alive:
            stack.append(ast)
    return stack



# asteroids = [5,10,-5]
# asteroids = [8,-8]
asteroids = [10,2,-5]
print(asteroidCol(asteroids))