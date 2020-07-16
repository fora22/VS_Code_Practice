#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, s):
        self.s_String = []
        self.result = []
        for s_number in s:
            self.s_String.append(int(s_number))

        for k in range(int(len(self.s_String) / 2)):
            self.checkString(k+1, k)
        # for n in range(1, len(self.s_String) + 1, 1):

        lenResult = []
        for i in range(len(self.result)):
            lenResult.append(len(self.result[i]))

        if len(lenResult) == 0:
            return 0
        else:
            return max(lenResult)

    def checkString(self, n, p):
        if len(self.s_String) == (2 * n):
            leftSum = sum(self.s_String[: + n])
            rightSum = sum(self.s_String[n:n + n])
            if leftSum == rightSum:
                self.result.append(self.s_String[:n] + self.s_String[n:n + n])
        else:
            for i in range(len(self.s_String) - (n + p)):
                leftSum = sum(self.s_String[i:i + n])
                rightSum = sum(self.s_String[i + n:i + n + n])
                if leftSum == rightSum:
                    self.result.append(self.s_String[i:i + n] + self.s_String[i + n:i + n + n])

            


s = "12321"
# s = "74233285"
# s = "1"
answer = Solution()
print(answer.solution(s))
