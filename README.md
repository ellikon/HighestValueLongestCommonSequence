# HighestValueLongestCommonSequence

Name: Luis Goicoechea - UFID:3500-9213

Name: Robert Miller - UFID:6705-1188

## Instructions to compile/build code 
Code was written using Python 3.12

## Instructions to run program
If using a console you can navigate to the /src folder where the files are and use the command "python3 HVLCS.py ..\data\xxxxx where xxxxx is the name of the file you would like to use and is in the /data folder." (Replace '\' with '/' if using Linux or macOS)


## Assumptions
The input files will have k in the first line where k >= 1. There will then be **k** number of lines, each with a character and value pair separated by a space " ". After all character and value pairs there will be two more lines each containing a string corresponding to A and B which will then be compared. File should have the '.in' file extension

The output file will have the result for highest value in the first line and in the second line will contain one of the possible subsequences that would result in that highest value. The file will use the same file name as the input but changing the '.in. extension to '.out'

## Question 1: Empirical Comparison
Graph for the runtime of 10 input files with increasing length of strings A and B
<img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/097dabaf-863b-48b1-aba5-6715f8553f58" />


## Question 2: Recurrence Equation

This recurrence equation is the basis for calculating the highest possible value of a common subsequence between two strings. This function can be built upon to later find the exact sequence itself based on the values chosen at each step.

$$
OPT(i, j) = 
\begin{cases} 
0 & \text{if } i = 0 \text{ or } j = 0 \\
v(c_i) + OPT(i-1, j-1) & \text{if } A_i = B_j \\
max(OPT(i - 1, j), OPT(i, j - 1)) & \text{otherwise}
\end{cases}
$$

This recurrence function and its base cases are correct becuase if either i or j are 0, then they are out of range of the strings and should just return 0. If a character from both A and B matches, then the value of that character must be added to the max possible value of strings A and B that don't contain that character. If the characters don't equal each other, then it must return the max between taking a character from A or B.

## Question 3: Big-Oh

This is the pseudocode for an algorithm that computes the length of the HVLCS of given strings A and B.

```
LET V be a dictionary of characters and their values

INITIALIZE 2D array L of size length(A) + 1 by length(B) + 1 with values 0
INITIALIZE 2D array M of size length(A) + 1 by length(B) + 1 with values 0

FOR i=1 to length(A)
	FOR j=1 to length(B)
		IF A[i-1] = B[j-1]
			M[i][j] = V[A[i-1]] + M[i-1][j-1]
			L[i][j] = 1 + L[i-1][j-1]
		ELSE
			M[i][j] = max(M[i-1][j], M[i][j-1])
			IF M[i][j] = M[i-1][j]
				L[i][j] = L[i-1][j]
			ELSE
				L[i][j] = L[i][j-1]

RETURN L[length(A), length(B)]
```

Because this function has a for loop that runs for each character in B, nested in a for loop that runs for each character in A, this algorithm has a runtime of O(A*B) where A is the length of string A, and B is the length of string B.
