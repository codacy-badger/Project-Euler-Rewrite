from problem import Problem


class DistinctPowers(Problem):
    @Problem.solution()
    def brute_force(self):
        # Good ol fashion set comprehension
        return len({a ** b for a in range(2, 101) for b in range(2, 101)})
