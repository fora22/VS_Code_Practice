#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, voters):
        self.v = []
        for i in range(len(voters)):
            self.v.append(list(map(int,voters[i])))
        self.politicianNumber = len(self.v[0])

        while True:
            self.victory = [int(self.politicianNumber / 2) for x in range(self.politicianNumber)] # 각 후보자의 득표수를 저장하는 리스트 + 가상의 탈락 후보자 자리를 위해 1을 더한다.
            polticianVictory = self.checkVictory()
            if polticianVictory > -1:
                break

        return polticianVictory


    def delMin(self):
        for politician, victoryNumber in enumerate(self.victory):
            if victoryNumber == min(self.victory):
                [x.remove(politician) for x in self.v]
                break
            
    def checkVictory(self):
        for i in range(len(self.v)):
            if self.victory[int(self.v[i][0])] == None:
                self.victory[int(self.v[i][0])] = 1
            else:     
                self.victory[int(self.v[i][0])] = self.victory[int(self.v[i][0])] + 1
             

        if (self.victory.count(max(self.victory)) == 1) and (max(self.victory) > int(len(self.v) / 2)):
            return self.victory.index(max(self.victory))
        else:
            if self.victory.count(min(self.victory)) != 1:
                for i in range(self.victory.count(min(self.victory))):
                    self.delMin()
            else:
                self.delMin()
        
        return -1
    





# voters = ["01","10","01","01","10"]
# voters = ["120","102","210","021","012"]
# voters = ["10","01"]
voters = ["3120","3012","1032","3120","2031","2103","1230","1230"]
answer = Solution()
print(answer.solution(voters))