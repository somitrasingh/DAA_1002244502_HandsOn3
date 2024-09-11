## Question 3

### Big-O (Upper Bound)
The top constraint is O(n²), because the time complexity grows quadratically. This indicates that as n increases, the function's runtime won't increase more quickly than n².

### Big-Omega (Lower Bound)
The function executes at least n² operations,therefore lower bound is Ω(n²).

### Big-Theta (Tight Bound)
Since both the upper and lower bounds are n², therefore the tight bound is Θ(n²).


## Question 4

Yes, since y = i + j is added to each iteration, there will be a tiny increase in runtime. Still, since this is a constant-time operation, O(n²) is the overall time complexity. The growth rate won't alter, but the actual runtime will.

## Question 5
No, the results from #1 are based on the asymptotic behavior of the algorithm, and since adding y = i + j is just an additional constant-time operation, it does not change the time complexity from O(n²).
