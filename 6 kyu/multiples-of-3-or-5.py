def solution(number):
    nums = []
    if number<=0:
        return 0
    for i in range(1,number):
        nums.append(i)
    result = [x for x in nums if x%3==0 or x%5==0]
    return sum(result)