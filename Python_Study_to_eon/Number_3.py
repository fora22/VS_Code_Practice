#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, voters):
        self.v = []
        for i in range(len(voters)):
            self.v.append(list(map(int,voters[i])))
        self.politicianNumber = len(self.v[0])
        self.victory = [0 for x in range(self.politicianNumber)] # 각 후보자의 득표수를 저장하는 리스트 + 가상의 탈락 후보자 자리를 위해 1을 더한다.
        for i in range(len(voters) - 1):
            self.checkVictory()

        return self.v[0]
        
    def checkVictory(self):
        for i in range(len(self.v)):
            self.victory[int(self.v[i][0])] = self.victory[int(self.v[i][0])] + 1

        leaving_out_pol = []
        leaving_out_pol.append(self.victory.index(min(self.victory)))
        for i in range(len(self.v)):
            self.v[i].remove(leaving_out_pol[0])

        leaving_out_pol.pop()
        
    #     k = 0
    #     self.checkVictory(k)
    #     self.victory = [0 for x in range(self.politicianNumber + 1)] # 각 후보자의 득표수를 저장하는 리스트 + 가상의 탈락 후보자 자리를 위해 1을 더한다.
    #     self.checkVictory(k)
        
    #     return self.victory

    def checkVictory(self, k):
        for i in range(len(self.v)):
            if int(self.v[i][k]) == self.politicianNumber:
                k = k + 1
                self.victory[int(self.v[i][k])] = self.victory[int(self.v[i][k])] + 1
                k = k - 1
            else:
                self.victory[int(self.v[i][k])] = self.victory[int(self.v[i][k])] + 1

        if (max(self.victory[:-1]) > (self.politicianNumber / 2)) :
            return self.victory.index(max(self.victory[:-1]))
            

        leaving_out_pol = []
        for i in range(len(self.victory) - 1): # 가상의 후보자 자리는 뺀다.
            if self.victory[i] == min(self.victory[:-1]):
                leaving_out_pol.append(i)

        for i in range(len(self.v)):
            self.v[i] = self.v[i].replace(str(leaving_out_pol[0]), str(self.politicianNumber))
        
    # def findSameValue(self):
    #     sameValue = False
    #     for i in range(len(self.victory[:-1])-1):





# voters = ["01","10","01","01","10"]
voters = ["120","102","210","021","012"]
# voters = ["10","01"]
# voters = ["3120","3012","1032","3120","2031","2103","1230","1230"]
answer = Solution()
print(answer.solution(voters))