# DAA_1002244502_HandsOn3

function x = f(n)
   x = 1;                          
   for i = 1:n                     
        for j = 1:n
             x = x + 1;


x = 1; will run once so it takes 1 operation O(1).
for i = 1:n   this loop runs from i=1 to i=n so it runs n iteration O(n).
for j = 1:n   For each iteration of the outer loop, the inner for loop runs from 𝑗=1 to 𝑗=𝑛, meaning it also runs n iterations for each iteration of outer loop, i.e. n*n times O(n^2).
x = x + 1;    it is executed once for each combination of 𝑖 and j. So, for each iteration of the outer loop, the inner loop runs n times, and in total, the assignment operation is executed 𝑛 × 𝑛 = 𝑛^2 times, i.e. O(n^2).

T(n) = 1 + n + n^2 + n^2
T(n) = 1 + n + 2n^2
The dominant term is n^2
Therefore runtime is O(n^2).


