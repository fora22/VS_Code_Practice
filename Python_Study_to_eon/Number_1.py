#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, scores):
        self.meanList = []
        scores.sort()           # 점수들 정렬
        if len(scores) == 1:    # 점수 데이터가 한개일 경우 return
            return max(scores)

        for k in range(0, (len(scores) // 2)+1):
            if len(scores[k:len(scores) - k]) == 0:
                break
            self.meanList.append(sum(scores[k:len(scores) - k]) / len(scores[k:len(scores) - k]))   # score의 k번째로 낮은 점수와 score의 k번째로 높은 점수의 평균

        return max(self.meanList)






    #     for k in range(len(scores)):
    #         if  (len(scores) == 1):
    #             temp = self.checkInt(sum(scores)) / (len(scores))
    #             self.meanList.append(temp)
    #             break
    #         # scores.pop(0) # score의 k번째로 낮은 점수
    #         # scores.pop(-1) # score의 k번째로 높은 점수
    #         if (len(scores) == 0):
    #             break       # 빈 리스트일 경우 break
    #         temp = self.checkInt(sum(scores)) / (len(scores))
    #         self.meanList.append(temp) 
    #         self.checkMean()
        
    #     return max(self.meanList)

    # def checkMean(self):
    #     if len(self.meanList) != 1:
    #         self.meanList.remove(min(self.meanList))

    # def checkInt(self,x):
    #     if int(x) == x:
    #         return x
    #     else:
    #         round(x, 9)

# from random import *
# scores = []
# for i in range(50):
#     scores.append(randint(1, 50))

scores = [1,2,3,2,2]        
# scores = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]    
# scores = [1,1,999,999,1000,1000]
# p = []
# for i in range(950,1000,1):
#     p.append(i)
# print(p)
# scores = p   
answer = Solution()
print(answer.solution(scores))
