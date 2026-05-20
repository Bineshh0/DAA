# Design and Analysis of Algorithms (DAA)

**Tribhuvan University**  
Institute of Science and Technology  
Bachelor of Science in Computer Science and Information Technology

---

| | |
|---|---|
| **Course Title:** | Design and Analysis of Algorithms |
| **Course No:** | CSC314 |
| **Semester:** | V |
| **Nature of Course:** | Theory + Lab |
| **Full Marks:** | 60 + 20 + 20 |
| **Pass Marks:** | 24 + 8 + 8 |
| **Credit Hours:** | 3 |

---

## Course Description

This course introduces basic elements of the design and analysis of computer algorithms. Topics include asymptotic notations and analysis, divide and conquer strategy, greedy methods, dynamic programming, basic graph algorithms, NP completeness, and approximation algorithms. For each topic, beside in depth coverage, one or more representative problems and their algorithms shall be discussed.

## Course Objective

Analyze the asymptotic performance of algorithms. Demonstrate a familiarity with major algorithm design techniques. Apply important algorithmic design paradigms and methods of analysis. Solve simple to moderately difficult algorithmic problems arising in applications. Able to demonstrate the hardness of simple NP complete problems.

---

## Course Contents

### Unit 1: Foundation of Algorithm Analysis (4 Hrs.)
1.1. Algorithm and its properties, RAM model, Time and Space Complexity, detailed analysis of algorithms (like factorial algorithm), Concept of Aggregate Analysis  
1.2. Asymptotic Notations: Big-O, Big-Ω and Big-Θ Notations their Geometrical Interpretation and Examples  
1.3. Recurrences: Recursive Algorithms and Recurrence Relations, Solving Recurrences (Recursion Tree Method, Substitution Method, Application of Masters Theorem)

---

### Unit 2: Iterative Algorithms (4 Hrs.)
2.1. Basic Algorithms: Algorithm for GCD, Fibonacci Number and analysis of their time and space complexity  
2.2. Searching Algorithms: Sequential Search and its analysis  
2.3. Sorting Algorithms: Bubble, Selection, and Insertion Sort and their Analysis

---

### Unit 3: Divide and Conquer Algorithms (8 Hrs.)
3.1. Searching Algorithms: Binary Search, Min-Max finding and their Analysis  
3.2. Sorting Algorithms: Merge Sort and Analysis, Quick Sort and Analysis (Best Case, Worst Case and Average Case), Heap Sort (Heapify, Build Heap and Heap Sort Algorithms and their Analysis), Randomized Quick sort and its Analysis  
3.3. Order Statistics: Selection in Expected Linear Time, Selection in Worst Case Linear Time and their Analysis

---

### Unit 4: Greedy Algorithms (6 Hrs.)
4.1. Optimization Problems and Optimal Solution, Introduction of Greedy Algorithms, Elements of Greedy Strategy  
4.2. Greedy Algorithms: Fractional Knapsack, Job sequencing with Deadlines, Kruskal's Algorithm, Prims Algorithm, Dijkstra's Algorithm and their Analysis  
4.3. Huffman Coding: Purpose of Huffman Coding, Prefix Codes, Huffman Coding Algorithm and its Analysis

---

### Unit 5: Dynamic Programming (8 Hrs.)
5.1. Greedy Algorithms vs Dynamic Programming, Recursion vs Dynamic Programming, Elements of DP Strategy  
5.2. DP Algorithms: Matrix Chain Multiplication, String Editing, Zero-One Knapsack Problem, Floyd Warshall Algorithm, Travelling Salesman Problem and their Analysis  
5.3. Memorization Strategy, Dynamic Programming vs Memoization

---

### Unit 6: Backtracking (5 Hrs.)
6.1. Concept of Backtracking, Recursion vs Backtracking  
6.2. Backtracking Algorithms: Subset-sum Problem, Zero-one Knapsack Problem, N-queen Problem and their Analysis

---

### Unit 7: Number Theoretic Algorithms (5 Hrs.)
7.1. Number Theoretic Notations, Euclid's and Extended Euclid's Algorithms and their Analysis  
7.2. Solving Modular Linear Equations, Chinese Remainder Theorem, Primality Testing, MillerRabin Randomized Primality Test and their Analysis

---

### Unit 8: NP Completeness (5 Hrs.)
8.1. Tractable and Intractable Problems, Concept of Polynomial Time and Super Polynomial Time Complexity  
8.2. Complexity Classes: P, NP, NP-Hard and NP-Complete  
8.3. NP Complete Problems, NP Completeness and Reducibility, Cook's Theorem, Proofs of NP Completeness (CNF SAT), Vertex Cover and Subset Sum  
8.4. Approximation Algorithms: Concept, Vertex Cover Problem, Subset Sum Problem

---

## Laboratory Works

This course can be learnt in effective way only if we give focus in practical aspects of algorithms and techniques discussed in class. Therefore student should be able to implement the algorithms and analyze their behavior.

For the laboratory work, students should implement the following algorithms in C/C++ and perform their analysis for time and space complexity:

1. Basic iterative algorithms: GCD algorithm, Fibonacci Sequences, Sequential and Binary Search
2. Basic iterative sorting algorithms: Bubble Sort, Selection Sort, Insertion Sort
3. Binary Search with Divide and Conquer approach
4. Merge Sort, Heap Sort, Quick Sort, Randomized Quick Sort
5. Selection Problem with Divide and Conquer approach
6. Fractional Knapsack Problem, Job sequencing with deadline, Kruskal's algorithm, Prims algorithm, Dijkstra's Algorithm
7. Implement the dynamic programming algorithms
8. Algorithms using Backtracking approach
9. Implement approximation Algorithms

---

## Text Books

1. Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, "Introduction to algorithms", Third Edition, The MIT Press, 2009
2. Ellis Horowitz, SartajSahni, SanguthevarRajasekaran, "Computer Algorithms", Second Edition, Silicon Press, 2007
3. Kleinberg, Jon, and Eva Tardos, "Algorithm Design", Addison Wesley, First Edition, 2005

---

## Model Question

**Full Marks: 60 | Pass Marks: 24 | Time: 3 hours**

### Section A
*Attempt any two questions. (2 × 10 = 20)*

1. Why do you need the algorithm analysis? Discuss about RAM model for analysis of algorithms. Also discuss about Big Oh, Big Omega and Big theta with examples. (2+3+5)

2. Discuss the order statistics. Explain about the worst case linear time selection algorithm and analyze its time complexity. (2+8)

3. Explain in brief about the Dynamic Programming Approach for algorithm design. How it differs with recursion? Explain the Floyd Warshall algorithm to compute the all pair shortest path in graph and analyze its time complexity. (4+6)

### Section B
*Attempt any eight questions. (8 × 5 = 40)*

4. Write the algorithm for Binary Search with divide and conquer approach and explain its complexity. (5)

5. Solve the following recurrence relations using master method. (2.5+2.5)
   - a. T(n) = 3T(n/2) + n
   - b. T(n) = 2T(n/4) + √n

6. What is prefix code? Explain Huffman algorithm to compute the prefix codes. (5)

7. Write the algorithm for insertion sort and explain its time complexity. (5)

8. What do you mean by memoization strategy? Compare memoization with dynamic programming. (5)

9. Explain backtracking with suitable example. (5)

10. Explain the Euclid's method to solve the modular linear equations with example. (5)

11. Explain in brief about the complexity classes P, NP and NP Complete. (5)

12. Write short notes on:
    - a. Tractable and Intractable Problems
    - b. Approximation Algorithms
