# Fetch_Rewards_exercise_SDET
Coding exercise from FetchRewards in regards to SDET application   
Exercise asks for gold bars to be weighed by two bowls and find the one fake bar  
## Solution description   
Made lists for left/right bowl and goldbars than split goldbars list into two halves around the median . Splat the lower half to the left bowl   
and splat the upper half to the right bowl. Thus comparing which side is heavier and taking a big chunck out of the guessing.   
after that, it was just narrowing down the lists using logical comparisons around the median left over.   
   
### Please find the solution in **weighbars.py**

