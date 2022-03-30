def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    thing = 0
    for n in nums:
        if n == 7:
            thing+=1

    if thing > 0:
        return "True"
    else:
        return "False"

    # YOUR CODE HERE 

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

