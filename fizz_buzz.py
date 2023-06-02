# 412. Fizz Buzz
# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

def fizzBuzz(n):
    ans = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            ans.append("FizzBuzz")
        elif i % 3 == 0:
            ans.append("Fizz")
        elif i % 5 == 0:
            ans.append("Buzz")
        else:
            ans.append(str(i))
    return ans

    # Alternative Approach
    # ans = []
    # fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}
    # for num in range(1,n+1):
    #     num_ans_str = ""
    #     for key in fizz_buzz_dict.keys():
    #         if num % key == 0:
    #             num_ans_str += fizz_buzz_dict[key]
                
    #     if not num_ans_str:
    #         num_ans_str = str(num)
            
    #     ans.append(num_ans_str)
    # return ans

n = 5
print(fizzBuzz(n))
# Output: ["1","2","Fizz","4","Buzz"]

# Time Complexity : O(n)
# Space Complexity : O(1)