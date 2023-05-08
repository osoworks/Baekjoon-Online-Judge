n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0] #[0]: 학생수, [1:]: 점수
    cnt = 0 #평균 이상인 학생수
    
    for score in nums[1:]:
        if score > avg:
            cnt += 1
            
    rate = cnt/nums[0] *100
    print('{0:0.3f}%'.format(rate))