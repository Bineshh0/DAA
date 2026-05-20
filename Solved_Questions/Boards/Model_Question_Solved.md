# DAA Model Question - Solved

**Full Marks: 60 | Pass Marks: 24 | Time: 3 hours**

---

## Section A (2 × 10 = 20)

### Question 1: Algorithm Analysis, RAM Model, and Asymptotic Notations (2+3+5)

#### Why Algorithm Analysis is Needed (2 marks)
Algorithm analysis is essential because:
- **Performance Prediction**: Helps predict how an algorithm will perform with different input sizes
- **Algorithm Comparison**: Allows comparison between different algorithms solving the same problem
- **Resource Optimization**: Helps in efficient utilization of time and memory resources
- **Scalability Assessment**: Determines if an algorithm is suitable for large-scale applications

#### RAM Model (3 marks)
The **Random Access Machine (RAM)** model is a theoretical model used for algorithm analysis:

**Key Features:**
- **Sequential Execution**: Instructions are executed one after another
- **Simple Operations**: Each simple operation (arithmetic, comparison, assignment) takes constant time O(1)
- **Memory Access**: Accessing any memory location takes constant time
- **No Concurrency**: Single processor with no parallel operations

**Assumptions:**
- Memory is unlimited
- Each memory word can hold any value
- No memory hierarchy (cache, main memory)

#### Asymptotic Notations (5 marks)

**1. Big-O Notation (Upper Bound)**
- Definition: f(n) = O(g(n)) if there exist positive constants c and n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀
- Example: f(n) = 3n² + 2n + 1 = O(n²)
- Represents the **worst-case** time complexity

**2. Big-Ω (Omega) Notation (Lower Bound)**
- Definition: f(n) = Ω(g(n)) if there exist positive constants c and n₀ such that f(n) ≥ c·g(n) for all n ≥ n₀
- Example: f(n) = 3n² + 2n + 1 = Ω(n²)
- Represents the **best-case** time complexity

**3. Big-Θ (Theta) Notation (Tight Bound)**
- Definition: f(n) = Θ(g(n)) if f(n) = O(g(n)) and f(n) = Ω(g(n))
- Example: f(n) = 3n² + 2n + 1 = Θ(n²)
- Represents the **average-case** or exact growth rate

---

### Question 2: Order Statistics and Worst-Case Linear Time Selection (2+8)

#### Order Statistics (2 marks)
- **Definition**: The ith order statistic of a set of n elements is the ith smallest element
- **Minimum**: 1st order statistic (i = 1)
- **Maximum**: nth order statistic (i = n)
- **Median**: Middle element; for odd n: (n+1)/2 th element; for even n: lower median at n/2

#### Worst-Case Linear Time Selection Algorithm (8 marks)

**Algorithm: SELECT(A, p, r, i)**
```
1. Divide the n elements into groups of 5
2. Find the median of each group by sorting (takes O(1) per group)
3. Recursively find the median of medians (call it x)
4. Partition the array around x
5. Let k = rank of x
6. If i = k, return x
7. If i < k, recursively select in the left partition
8. If i > k, recursively select in the right partition
```

**Steps in Detail:**

**Step 1-2**: Divide elements into ⌈n/5⌉ groups, each of 5 elements (last group may have fewer). Find median of each group.

**Step 3**: Recursively find median of the ⌈n/5⌉ medians.

**Step 4-5**: Partition using median-of-medians as pivot.

**Step 6-8**: Recurse on appropriate partition.

**Time Complexity Analysis:**
- Step 1-2: O(n) - finding medians of groups of 5
- Step 3: T(n/5) - recursive call on n/5 medians
- Step 4: O(n) - partitioning
- Step 7-8: T(7n/10) - at most 7n/10 elements in recursive call

**Recurrence**: T(n) = T(n/5) + T(7n/10) + O(n)

**Solution**: T(n) = O(n) - **Linear time in worst case**

---

### Question 3: Dynamic Programming and Floyd-Warshall Algorithm (4+6)

#### Dynamic Programming Approach (4 marks)

**Concept**: Dynamic Programming (DP) is an algorithmic paradigm that solves complex problems by:
1. Breaking them into simpler overlapping subproblems
2. Storing solutions to subproblems to avoid redundant computation
3. Building up solutions to larger problems from smaller ones

**Elements of DP:**
- **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems
- **Overlapping Subproblems**: Same subproblems are solved multiple times

**DP vs Recursion:**
| Recursion | Dynamic Programming |
|-----------|-------------------|
| Top-down approach | Bottom-up approach |
| May solve same subproblem multiple times | Stores solutions (memoization/tabulation) |
| Can be exponential | Polynomial time |
| Uses call stack | Uses table/array |

#### Floyd-Warshall Algorithm (6 marks)

**Purpose**: Finds shortest paths between all pairs of vertices in a weighted graph.

**Algorithm:**
```
FLOYD-WARSHALL(W)
    n = W.rows
    D⁰ = W
    for k = 1 to n
        for i = 1 to n
            for j = 1 to n
                d[i][j]^k = min(d[i][j]^(k-1), d[i][k]^(k-1) + d[k][j]^(k-1))
    return D^n
```

**Key Idea**: d[i][j]^k = shortest path from i to j using only vertices {1, 2, ..., k} as intermediate vertices.

**Example:**
```
Initial Distance Matrix:
     1    2    3    4
1    0    3    ∞    7
2    8    0    2    ∞
3    5    ∞    0    1
4    2    ∞    ∞    0

After k=1, k=2, k=3, k=4 iterations, we get all-pairs shortest paths.
```

**Time Complexity**: O(n³) - three nested loops each running n times

**Space Complexity**: O(n²) - for the distance matrix

---

## Section B (8 × 5 = 40)

### Question 4: Binary Search with Divide and Conquer (5 marks)

**Algorithm:**
```
BINARY-SEARCH(A, low, high, key)
    if low > high
        return -1  // Not found
    mid = (low + high) / 2
    if A[mid] == key
        return mid
    else if A[mid] > key
        return BINARY-SEARCH(A, low, mid-1, key)
    else
        return BINARY-SEARCH(A, mid+1, high, key)
```

**Complexity Analysis:**
- Each comparison eliminates half the remaining elements
- Recurrence: T(n) = T(n/2) + O(1)
- Time Complexity: **O(log n)**
- Space Complexity: O(log n) for recursive, O(1) for iterative

---

### Question 5: Solving Recurrences Using Master Method (2.5+2.5)

**Master Theorem**: For T(n) = aT(n/b) + f(n)
- Compare f(n) with n^(log_b(a))

**a) T(n) = 3T(n/2) + n**
- a = 3, b = 2, f(n) = n
- n^(log₂3) = n^1.585
- f(n) = n = O(n^(1.585-ε)) for some ε > 0
- **Case 1 applies**: T(n) = **Θ(n^(log₂3)) ≈ Θ(n^1.585)**

**b) T(n) = 2T(n/4) + √n**
- a = 2, b = 4, f(n) = √n = n^0.5
- n^(log₄2) = n^0.5
- f(n) = Θ(n^(log₄2))
- **Case 2 applies**: T(n) = **Θ(√n · log n)**

---

### Question 6: Prefix Code and Huffman Algorithm (5 marks)

**Prefix Code**: A code where no codeword is a prefix of another codeword. This ensures unique decodability.

**Huffman Algorithm:**
```
HUFFMAN(C)
    n = |C|
    Q = C  // Min priority queue based on frequency
    for i = 1 to n-1
        allocate new node z
        z.left = x = EXTRACT-MIN(Q)
        z.right = y = EXTRACT-MIN(Q)
        z.freq = x.freq + y.freq
        INSERT(Q, z)
    return EXTRACT-MIN(Q)  // Root of tree
```

**Example**: Characters with frequencies: a(45), b(13), c(12), d(16), e(9), f(5)
- Build tree bottom-up by combining lowest frequency nodes
- Assign 0 for left edge, 1 for right edge
- Result: Variable length codes with shorter codes for frequent characters

---

### Question 7: Insertion Sort Algorithm and Complexity (5 marks)

**Algorithm:**
```
INSERTION-SORT(A)
    for j = 2 to A.length
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
```

**Time Complexity:**
- **Best Case**: O(n) - array already sorted
- **Worst Case**: O(n²) - array sorted in reverse
- **Average Case**: O(n²)

**Space Complexity**: O(1) - in-place sorting

---

### Question 8: Memoization Strategy and Comparison with DP (5 marks)

**Memoization**: A top-down technique that stores results of expensive function calls and returns cached result when same inputs occur again.

**Comparison:**

| Memoization | Dynamic Programming |
|-------------|-------------------|
| Top-down approach | Bottom-up approach |
| Recursive with caching | Iterative with table |
| Solves only needed subproblems | Solves all subproblems |
| Uses recursion stack | No recursion overhead |
| Lazy evaluation | Eager evaluation |

**Example (Fibonacci):**
- Memoization: fib(n) with memo array, computed on demand
- DP: Build table from fib[0] to fib[n] iteratively

---

### Question 9: Backtracking with Example (5 marks)

**Concept**: Backtracking is a systematic way of trying out different sequences of decisions until finding one that works. When a decision leads to a dead end, we backtrack and try another.

**N-Queens Example:**
```
SOLVE-N-QUEENS(board, col)
    if col >= N
        return true  // All queens placed
    for row = 0 to N-1
        if isSafe(board, row, col)
            board[row][col] = 1  // Place queen
            if SOLVE-N-QUEENS(board, col+1)
                return true
            board[row][col] = 0  // Backtrack
    return false
```

**Key Properties:**
- Explores solution space systematically
- Prunes branches that can't lead to solution
- Uses recursion with state restoration

---

### Question 10: Euclid's Method for Modular Linear Equations (5 marks)

**Problem**: Solve ax ≡ b (mod n)

**Extended Euclidean Algorithm:**
```
EXTENDED-GCD(a, b)
    if b = 0
        return (a, 1, 0)
    (d, x', y') = EXTENDED-GCD(b, a mod b)
    return (d, y', x' - ⌊a/b⌋ × y')
```

**Example**: Solve 14x ≡ 30 (mod 100)
1. Find gcd(14, 100) = 2
2. Since 2 | 30, solution exists
3. Use Extended GCD: 14(-7) + 100(1) = 2
4. Multiply: 14(-105) ≡ 30 (mod 100)
5. Solutions: x ≡ -105 ≡ 45 (mod 50)

---

### Question 11: Complexity Classes P, NP, NP-Complete (5 marks)

**P (Polynomial Time):**
- Problems solvable in polynomial time O(n^k)
- Examples: Sorting, searching, shortest path

**NP (Non-deterministic Polynomial):**
- Problems whose solutions can be **verified** in polynomial time
- Examples: SAT, Hamiltonian cycle, subset sum

**NP-Complete:**
- Hardest problems in NP
- Every NP problem can be reduced to any NP-Complete problem in polynomial time
- If any NP-Complete problem is solved in polynomial time, P = NP
- Examples: 3-SAT, Vertex Cover, Clique

**Relationship**: P ⊆ NP, NP-Complete ⊆ NP

---

### Question 12: Short Notes (2.5+2.5)

**a) Tractable and Intractable Problems**
- **Tractable**: Problems solvable in polynomial time (P class). Practical for large inputs.
- **Intractable**: Problems requiring super-polynomial time (exponential). Not practical for large inputs.
- **Examples**: Sorting is tractable; Traveling Salesman (exact) is intractable.

**b) Approximation Algorithms**
- Algorithms that find **near-optimal** solutions for NP-hard optimization problems
- Provide **performance guarantee** (approximation ratio)
- Trade optimality for efficiency
- **Example**: Vertex Cover 2-approximation - always finds solution within 2× optimal
- Used when exact algorithms are too slow for practical use
