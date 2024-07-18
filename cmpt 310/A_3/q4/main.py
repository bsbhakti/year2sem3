from searchGeneric import Searcher
# from searchProblem import problem
# from searchProblem import problem1
from searchBranchAndBound import DF_branch_and_bound

# searcher1 = Searcher(problem1)
# print(searcher1.search() ) # find first solution
from cspExamples import test_csp
from searchGeneric import Searcher
from cspConsistency import Search_with_AC_from_CSP
from cspConsistency import select
from stripsCSPPlanner import con_plan

from searchGeneric import Searcher
from stripsProblem import delivery_domain
from cspConsistency import Search_with_AC_from_CSP, Con_solver
from stripsProblem import Planning_problem, problem0, problem1, problem2, blocks1, blocks2, blocks3,myproblem

# Problem 0
# con_plan(problem0,1) # should it succeed?
# con_plan(problem0,2) # should it succeed?
# con_plan(problem0,3) # should it succeed?
# To use search to enumerate solutions
#searcher0a = Searcher(Search_with_AC_from_CSP(CSP_from_STRIPS(problem0, 1)))
#print(searcher0a.search())  # returns path to solution

## Problem 1
# con_plan(problem1,5) # should it succeed?
# con_plan(problem1,4) # should it succeed?
## To use search to enumerate solutions:
#searcher15a = Searcher(Search_with_AC_from_CSP(CSP_from_STRIPS(problem1, 5)))
#print(searcher15a.search())  # returns path to solution
# problem3 = Planning_problem(delivery_domain, 
                            # {'SWC':True, 'RHC':False}, {'SWC':False})

print(con_plan(myproblem,4))  # Horizon of 2
# con_plan(problem3,3)  # Horizon of 3