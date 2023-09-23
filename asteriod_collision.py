# 735. Asteroid Collision
# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

def asteroidCollision(asteroids):
    output = []
    for new_asteroid in asteroids:
        while output and new_asteroid < 0 < output[-1]:
            if output[-1] < -new_asteroid:
                output.pop()
                continue
            elif output[-1] == -new_asteroid:
                output.pop()
            break
        else:
            output.append(new_asteroid)
    return output

asteroids = [5,10,-5]
print(asteroidCollision(asteroids))

# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

# Time Complexity: O(n)
# Space Complexity: O(n)