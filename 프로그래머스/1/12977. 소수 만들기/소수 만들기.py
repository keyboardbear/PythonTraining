def solution(nums):
    answer = 0
    for i in range (0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                sum_num=nums[i]+nums[j]+nums[k]    
                for t in range(2,int(sum_num ** 0.5) + 1):
                    if sum_num % t ==0:
                        is_prime=False
                        break
                else:
                        answer+=1
               
                    
    return answer