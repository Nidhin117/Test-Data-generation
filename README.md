# Test-Data-generation
Test Data Generation using Genetic Algorithms
Two programs were considered for this project- Jacobi symbol and Cipolla function.
Genetic algorithm was used to generate test data with maximum code coverage.

Targets Identified in the code:
❖ Jacobi Symbol: <br/>
• We have selected 5 target statements to achieve complete code coverage of the given jacboi symbol program. <br/>
• Target 1 is the statement: “raise ValueError("'K' has to be positive and 'n' has to be an odd integer.")” <br/>
• Target 2 is the statement: “jacobi = -jacobi” which is inside the if condition “if r == 3 or r == 5:” <br/>
• Target 3 is the statement:” jacobi = -jacobi” which is inside the if condition “if k % 4 == 3 and n % 4 == 3:” <br/>
• Target 4 and 5 are statements “return jacobi” and “return 0” respectively. <br/>
• We have not considered the statement “r = n % 8” as a target because when we try to reach target 2, this statement will eventually get executed. <br/>
• Likewise, statement “k %= n” is also not considered a target as when target 3 is reached, this statement will get executed eventually. <br/>
• 5 different variations of jacboi function have been created to calculate the fitness of each of these targets and they are saved in 5 different files: p1target1, p1target2, p1target3, p1target4, p1target5.
<br/> <br/>
❖ Cipolla Function: <br/>
• We have selected 7 target statements in order to achieve complete code coverage of the given Cipolla function program. <br/>
• Target 1 is the statement: “print("A")” <br/>
• Target 2 is the statement: “print("B")” which is inside the if condition “ls(omega2) == p-1:” <br/>
• Target 3 is the statement:” print("C")” which is outside the if condition “ls(omega2) == p-1:” <br/>
• Target 4 is the statement:” print("D")” which is inside the if condition “if (nn & 1) == 1” <br/>
• Target 5 is the statement:” print("F")” which is inside the if condition “if r.y != 0” <br/>
• Target 6 is the statement:” print("G")” which is inside the if condition “((r.x * r.x) % p) != n:” <br/>
• Target 7 is the final statement “return Triple(r.x, p - r.x, True)”. <br/>
• We have not considered the statement “print("E")” as a target because when we try to reach target 4, this statement will eventually get executed. <br/>
• 7 different variations of cipolla function have been created to calculate the fitness of each of these targets and they are saved in 5 different files:  <br/> p2target1, p2target2, p2target3, p2target4, p2target5, p2target6, p2target7
