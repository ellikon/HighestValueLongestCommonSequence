# HighestValueLongestCommonSequence

## Question 2: Recurrence Equation

This recurrence equation is the basis for calculating the highest possible value of a common subsequence between two strings. This function can be built upon to later find the exact sequence itself based on the values chosen at each step.

$$
OPT(i, j) = 
\begin{cases} 
0 & \text{if } i < 0 \text{ or } j < 0 \\
v(c_i) + OPT(i-1, j-1) & \text{if } A_i = B_j \\
max(OPT(i - 1, j), OPT(i, j - 1))
\end{cases}
$$

This recurrence function and its base cases are correct becuase if either i or j are below 0, then they are out of range of the strings and should just return 0. If a character from both A and B matches, then the value of that character must be added to the max possible value of strings A and B that don't contain that character. If the characters don't equal each other, then it must return the max between taking a character from A or B.
