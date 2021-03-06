from problem import Problem


class SelfPowers(Problem):
    @Problem.solution()
    def solution(self):
        return str(self.series(1000))[-10:]
        
    @classmethod
    def series(cls, n):
        return sum(i**i for i in range(1, n))
