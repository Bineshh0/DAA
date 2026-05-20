# Extracted Content from Unit 7 Number Theoretic Algorithms2024

## Page 1

Number Theoretic Algorithms (5)  
 
 
Recall Basic Number theoretic concepts 
 
 
Solving Modular Linear Equations 
 Euclid’s and Extended Euclid’s Algorithms for solving Modular Linear Equations. 
 
 
 
 
 
EXTENDED-EUCLID (a, b) 
{    if b = = 0 
     return(a,1,0)      // d,x,y 
else (d’, x’, y’) =EXTENDED-EUCLID (b, a mod b) 
 (d, x, y) = (d’, y’, x’-a/b y’) 
             return (d, x, y ) 
} 
 
 
 
 
 
 
 
 
Algorithm for Solving modular linear equations  
T(n)=O(Log(min(a,b))) 


![Image from page 1](file:///c:/Users/V16/.gemini/antigravity/scratch/5th sem/DAA/Unit7_NumberTheoretic/Unit 7 Number Theoretic Algorithms2024_extracted/page1_img0.png)

## Page 2

Finding solutions to the equation ax  b(mod n) ; 
 
 
 
 
 For 14x  30 (mod 100)  (here, a = 14, b = 30, and n = 100).  
Calling EXTENDED-EUCLID we can obtain (d, x’, y’)=(2,-7,1) 
Since d/b there exists two solutions x0 and x1 95 and 45 respectively. 
 
 
 
 
 
 
 
 
 
 
 
T(n)=O(d+Log(min(a,n))) 
 


![Image from page 2](file:///c:/Users/V16/.gemini/antigravity/scratch/5th sem/DAA/Unit7_NumberTheoretic/Unit 7 Number Theoretic Algorithms2024_extracted/page2_img0.png)

## Page 3

Algorithm for Solving Modular Exponentiation  
 
 
 
 
 
The results of MODULAR-EXPONENTIATION when computing ab ( mod n) , where a = 7, b = 
560  = [1000110000] , and n = 561. The values are shown after each execution of the for loop. The 
final result is 1. 
 
 
 
 
  
 
 
If b represented by n bits then  
T(n)=O(n)/O(logn) 
Any integer n can be  
represented by logn bits ! 


![Image from page 3](file:///c:/Users/V16/.gemini/antigravity/scratch/5th sem/DAA/Unit7_NumberTheoretic/Unit 7 Number Theoretic Algorithms2024_extracted/page3_img0.png)

![Image from page 3](file:///c:/Users/V16/.gemini/antigravity/scratch/5th sem/DAA/Unit7_NumberTheoretic/Unit 7 Number Theoretic Algorithms2024_extracted/page3_img1.png)

## Page 4

Miller-Rabin Randomized Primality Test and Analysis 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Loop in main function runs S times 
Witness function n-1 =2t.u takes logn times 
Modular exponentiation takes logn time  
 For loop runs t times  n 
so  
T(n)=S.(logn+logn+n) integer step. 
Which is very fast. 


![Image from page 4](file:///c:/Users/V16/.gemini/antigravity/scratch/5th sem/DAA/Unit7_NumberTheoretic/Unit 7 Number Theoretic Algorithms2024_extracted/page4_img0.jpeg)

![Image from page 4](file:///c:/Users/V16/.gemini/antigravity/scratch/5th sem/DAA/Unit7_NumberTheoretic/Unit 7 Number Theoretic Algorithms2024_extracted/page4_img1.png)

## Page 5

 
An example of the application of the Chinese remainder theorem, 
suppose we are given the two equations 
 
 
 
 
 
 
 
 
 


![Image from page 5](file:///c:/Users/V16/.gemini/antigravity/scratch/5th sem/DAA/Unit7_NumberTheoretic/Unit 7 Number Theoretic Algorithms2024_extracted/page5_img0.png)

![Image from page 5](file:///c:/Users/V16/.gemini/antigravity/scratch/5th sem/DAA/Unit7_NumberTheoretic/Unit 7 Number Theoretic Algorithms2024_extracted/page5_img1.png)

