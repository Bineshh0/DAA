import os

# Define the HTML template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Outfit:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: {primary_color};
            --secondary: {secondary_color};
            --dark: #0f172a;
            --light: #f8fafc;
            --text-dark: #1e293b;
            --text-light: #475569;
            --bg-color: #f1f5f9;
        }}
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-dark);
            line-height: 1.7;
        }}
        header {{
            background: linear-gradient(135deg, var(--dark), var(--primary));
            color: white;
            padding: 4rem 2rem;
            text-align: center;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            position: relative;
            overflow: hidden;
        }}
        header::after {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 10%, transparent 10%), radial-gradient(circle, rgba(255,255,255,0.1) 10%, transparent 10%);
            background-size: 30px 30px;
            background-position: 0 0, 15px 15px;
            opacity: 0.3;
            animation: moveBg 30s linear infinite;
        }}
        @keyframes moveBg {{
            0% {{ transform: translate(0, 0); }}
            100% {{ transform: translate(30px, 30px); }}
        }}
        h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 3.5rem;
            margin-bottom: 1rem;
            position: relative;
            z-index: 1;
        }}
        .subtitle {{
            font-size: 1.2rem;
            font-weight: 300;
            opacity: 0.9;
            position: relative;
            z-index: 1;
            max-width: 600px;
            margin: 0 auto;
        }}
        .container {{
            max-width: 900px;
            margin: -3rem auto 3rem;
            padding: 0 1.5rem;
            position: relative;
            z-index: 2;
        }}
        .question-card {{
            background: white;
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05), 0 4px 6px -2px rgba(0,0,0,0.025);
            border-left: 6px solid var(--secondary);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}
        .question-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);
            border-left-width: 10px;
        }}
        .tag {{
            display: inline-block;
            padding: 0.35rem 0.8rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
            background-color: var(--light);
            color: var(--primary);
            border: 1px solid rgba(0,0,0,0.05);
        }}
        .question {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.4rem;
            font-weight: 700;
            color: var(--dark);
            margin-bottom: 1rem;
        }}
        .answer {{
            font-size: 1.05rem;
            color: var(--text-light);
            position: relative;
        }}
        .answer p {{
            margin-bottom: 0.75rem;
        }}
        .answer p:last-child {{
            margin-bottom: 0;
        }}
        .highlight {{
            background-color: rgba(16, 185, 129, 0.1);
            color: var(--secondary);
            padding: 0.1rem 0.3rem;
            border-radius: 4px;
            font-family: monospace;
            font-weight: 600;
        }}
        .nav-links {{
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 3rem;
            flex-wrap: wrap;
        }}
        .nav-link {{
            padding: 0.75rem 1.5rem;
            background: white;
            color: var(--dark);
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            transition: all 0.2s;
            border: 2px solid transparent;
        }}
        .nav-link:hover {{
            border-color: var(--primary);
            color: var(--primary);
        }}
        .nav-link.active {{
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }}
        .unit-header {{
            font-family: 'Outfit', sans-serif;
            font-size: 2rem;
            color: var(--dark);
            margin: 3rem 0 1.5rem;
            border-bottom: 3px solid var(--primary);
            padding-bottom: 0.5rem;
            display: inline-block;
        }}
    </style>
</head>
<body>
    <header>
        <h1>{title}</h1>
        <p class="subtitle">{subtitle}</p>
    </header>
    
    <div class="container">
        <div class="nav-links">
            <a href="daa_viva_simple.html" class="nav-link {active_simple}">1. Simple Recurring</a>
            <a href="daa_viva_advanced.html" class="nav-link {active_advanced}">2. Advanced Syllabus</a>
            <a href="daa_viva_out_of_box.html" class="nav-link {active_oob}">3. Out of the Box</a>
        </div>
        
        {content}
    </div>
</body>
</html>
"""

def generate_card(tag, question, answer):
    paragraphs = ''.join([f'<p>{p.strip()}</p>' for p in answer.split('\n\n') if p.strip()])
    return f"""
        <div class="question-card">
            <span class="tag">{tag}</span>
            <div class="question">{question}</div>
            <div class="answer">{paragraphs}</div>
        </div>
    """

# Extensive and Exhaustive list of questions.

# --- 1. SIMPLE QUESTIONS ---
simple_qs = [
    # Unit 1
    ("Unit 1: Foundation", "What is an algorithm?", "An algorithm is a finite set of instructions that, if followed, accomplishes a particular task. It must have Input, Output, Definiteness, Finiteness, and Effectiveness."),
    ("Unit 1: Foundation", "What is the RAM model in algorithm analysis?", "The Random Access Machine (RAM) model is a theoretical machine used to analyze algorithms. In this model, instructions are executed one after another, and each basic operation (like +, -, *, /, memory access) takes exactly one step (or constant time)."),
    ("Unit 1: Foundation", "Define Time Complexity and Space Complexity.", "Time complexity is the total time required by the algorithm to run as a function of the input size. Space complexity is the total memory space required by the algorithm to run as a function of the input size."),
    ("Unit 1: Foundation", "What is Big-O notation?", "Big-O notation represents the upper bound of the running time of an algorithm. It gives the worst-case complexity, meaning the algorithm will take no more time than this."),
    ("Unit 1: Foundation", "What is Big-Omega (Ω) notation?", "Big-Omega notation represents the lower bound of the running time. It gives the best-case complexity, meaning the algorithm will take at least this much time."),
    ("Unit 1: Foundation", "What is Big-Theta (Θ) notation?", "Big-Theta represents both the upper and lower bounds. It means the algorithm's running time grows exactly at the same rate as the function, providing a tight bound."),
    ("Unit 1: Foundation", "What is a Recurrence Relation?", "It is an equation or inequality that describes a function in terms of its value on smaller inputs. Used to define the time complexity of recursive algorithms."),
    ("Unit 1: Foundation", "Name the methods to solve Recurrence Relations.", "1. Substitution Method\n2. Recursion Tree Method\n3. Master Method"),

    # Unit 2
    ("Unit 2: Iterative", "What is the time complexity of GCD using Euclid's algorithm?", "The time complexity is <span class='highlight'>O(log(min(a, b)))</span>."),
    ("Unit 2: Iterative", "What is Sequential Search (Linear Search) and its time complexity?", "It is a basic search algorithm that checks every element in a list one by one until the target is found. Time complexity is <span class='highlight'>O(n)</span>."),
    ("Unit 2: Iterative", "What is Bubble Sort?", "A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. Complexity is <span class='highlight'>O(n²)</span>."),
    ("Unit 2: Iterative", "What is Selection Sort?", "It divides the list into a sorted and an unsorted region. It repeatedly selects the smallest element from the unsorted region and swaps it with the leftmost unsorted element. Complexity is <span class='highlight'>O(n²)</span>."),
    ("Unit 2: Iterative", "What is Insertion Sort?", "It builds the final sorted array one item at a time by picking elements from the unsorted part and inserting them at their correct position in the sorted part. Complexity is <span class='highlight'>O(n²)</span>."),

    # Unit 3
    ("Unit 3: Divide & Conquer", "What are the three steps in Divide and Conquer?", "1. Divide: Break the problem into smaller subproblems.\n2. Conquer: Solve subproblems recursively.\n3. Combine: Merge the subproblem solutions to form the final solution."),
    ("Unit 3: Divide & Conquer", "What is the time complexity of Binary Search?", "Best case: <span class='highlight'>O(1)</span>. Average and Worst case: <span class='highlight'>O(log n)</span>."),
    ("Unit 3: Divide & Conquer", "What is the recurrence relation for Merge Sort?", "<span class='highlight'>T(n) = 2T(n/2) + O(n)</span>. It solves to <span class='highlight'>O(n log n)</span>."),
    ("Unit 3: Divide & Conquer", "How does Quick Sort work?", "It picks an element as pivot and partitions the given array around the picked pivot by placing smaller elements to the left and larger to the right, then recursively applies this to the sub-arrays."),
    ("Unit 3: Divide & Conquer", "What is the worst-case and best-case time complexity of Quick Sort?", "Best case: <span class='highlight'>O(n log n)</span>. Worst case: <span class='highlight'>O(n²)</span> (when array is already sorted or reverse sorted)."),
    ("Unit 3: Divide & Conquer", "What is Heap Sort?", "A comparison-based sorting algorithm based on Binary Heap data structure. First, we build a Max-Heap from the data, then repeatedly extract the maximum element and place it at the end of the array. Complexity: <span class='highlight'>O(n log n)</span>."),

    # Unit 4
    ("Unit 4: Greedy", "What is a Greedy Algorithm?", "An algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most immediate (local) benefit, aiming for a global optimum."),
    ("Unit 4: Greedy", "What is Fractional Knapsack problem?", "Given weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value. We are allowed to break items (take fractions). Solved using Greedy approach."),
    ("Unit 4: Greedy", "What does Dijkstra's Algorithm do?", "It solves the single-source shortest path problem for a graph with non-negative edge weights, producing a shortest path tree."),
    ("Unit 4: Greedy", "What are Kruskal's and Prim's Algorithms used for?", "They are Greedy algorithms used to find the Minimum Spanning Tree (MST) of a connected, undirected graph."),
    ("Unit 4: Greedy", "What is Huffman Coding?", "A lossless data compression algorithm that assigns variable-length codes to input characters, with shorter codes assigned to more frequent characters. It uses a Greedy approach to build a prefix tree."),

    # Unit 5
    ("Unit 5: Dynamic Programming", "What is Dynamic Programming?", "A method for solving optimization problems by breaking them down into simpler overlapping subproblems and storing the results of these subproblems to avoid redundant computation."),
    ("Unit 5: Dynamic Programming", "How is DP different from Divide and Conquer?", "Divide and Conquer breaks problems into independent subproblems. DP breaks problems into overlapping subproblems, meaning the same subproblems are solved repeatedly, so it stores their results (memoization/tabulation)."),
    ("Unit 5: Dynamic Programming", "What is the 0/1 Knapsack Problem?", "Similar to fractional knapsack, but you cannot break items. You either take the whole item or leave it. It is solved using DP, not Greedy."),
    ("Unit 5: Dynamic Programming", "What does Floyd Warshall algorithm find?", "It finds shortest paths between all pairs of vertices in a weighted graph. Complexity is <span class='highlight'>O(V³)</span>."),

    # Unit 6
    ("Unit 6: Backtracking", "What is Backtracking?", "An algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point in time (pruning)."),
    ("Unit 6: Backtracking", "Name two classic problems solved by Backtracking.", "1. N-Queens Problem\n2. Subset-Sum Problem"),

    # Unit 7
    ("Unit 7: Number Theoretic", "What does the Extended Euclidean Algorithm do?", "Besides finding the GCD of integers a and b, it also finds coefficients x and y such that <span class='highlight'>ax + by = gcd(a, b)</span>."),
    ("Unit 7: Number Theoretic", "What is the Miller-Rabin test?", "A randomized primality test that determines whether a given number is likely prime or definitely composite."),

    # Unit 8
    ("Unit 8: NP Completeness", "Define Tractable and Intractable problems.", "Tractable problems can be solved in polynomial time (P). Intractable problems cannot be solved in polynomial time (they take super-polynomial/exponential time)."),
    ("Unit 8: NP Completeness", "What is the class P?", "The set of decision problems that can be solved by a deterministic Turing machine in polynomial time."),
    ("Unit 8: NP Completeness", "What is the class NP?", "The set of decision problems for which a 'yes' solution can be verified by a deterministic Turing machine in polynomial time (or solved by a non-deterministic Turing machine in polynomial time)."),
    ("Unit 8: NP Completeness", "What is an NP-Complete problem?", "A problem is NP-Complete if it is in NP, and every other problem in NP can be reduced to it in polynomial time. (e.g., Boolean Satisfiability (SAT)).")
]

# --- 2. ADVANCED QUESTIONS ---
advanced_qs = [
    # Unit 1
    ("Unit 1: Foundation", "How does Aggregate Analysis differ from the Accounting Method?", "In Aggregate Analysis, we find the total cost T(n) for a sequence of n operations and calculate the amortized cost as T(n)/n for all operations. In the Accounting Method, we overcharge cheap operations to store 'credit', which is later used to pay for expensive operations."),
    ("Unit 1: Foundation", "What are the limitations of the Master Theorem?", "It cannot solve recurrences if:\n1. T(n) is not monotone (e.g., T(n) = sin(n))\n2. f(n) is not a polynomial (e.g., f(n) = 2^n)\n3. b cannot be expressed as a constant (e.g., T(n) = T(n/log n))\n4. The gap between f(n) and n^(log_b a) is not polynomial (e.g., log factors exist that don't fit the extended cases)."),

    # Unit 2
    ("Unit 2: Iterative", "Why is Insertion Sort considered better than Selection Sort and Bubble Sort in practice?", "Because Insertion Sort is highly adaptive. If the array is almost sorted, its time complexity drops to <span class='highlight'>O(n)</span>. It also has very low overhead and excellent cache locality, making it the algorithm of choice for small or nearly-sorted datasets (e.g., used internally by Python's Timsort or C++'s std::sort for small partitions)."),

    # Unit 3
    ("Unit 3: Divide & Conquer", "How do we achieve O(n) Worst Case time for the Selection Problem (Order Statistics)?", "By using the Median of Medians algorithm. Instead of picking a random pivot like in Quick Select, we divide the array into groups of 5, find the median of each group, and then recursively find the median of those medians to use as the pivot. This guarantees a good split and <span class='highlight'>O(n)</span> worst-case time."),
    ("Unit 3: Divide & Conquer", "Why is Randomized Quick Sort's Expected time complexity O(n log n)?", "By picking a random pivot, the probability of consistently picking the extreme elements is incredibly small. On average, the pivot will split the array in a ratio no worse than 1/4 to 3/4, which leads to a recursion tree of depth <span class='highlight'>O(log n)</span>, thus <span class='highlight'>O(n log n)</span> overall."),

    # Unit 4
    ("Unit 4: Greedy", "Explain the difference in data structures used for Prim's vs Kruskal's algorithm.", "Prim's uses a Priority Queue (Min-Heap) to quickly find the minimum weight edge connected to the growing MST. Kruskal's uses a Disjoint Set (Union-Find) data structure to detect cycles when adding edges sorted by weight."),
    ("Unit 4: Greedy", "Why does Job Sequencing with Deadlines use a Greedy approach?", "It sorts jobs in descending order of profit, and then greedily assigns each job to the latest possible free time slot before its deadline. This maximizes profit because we always prioritize high-profit jobs and reserve early slots for other jobs."),

    # Unit 5
    ("Unit 5: Dynamic Programming", "What are the core elements of a Dynamic Programming strategy?", "1. Optimal Substructure: The optimal solution to the main problem is composed of optimal solutions to its subproblems.\n2. Overlapping Subproblems: The algorithm visits the same subproblems repeatedly. DP solves each subproblem once and saves its answer in a table."),
    ("Unit 5: Dynamic Programming", "Explain Matrix Chain Multiplication.", "It's a DP algorithm that determines the most efficient way to multiply a sequence of matrices. We don't actually perform the multiplications; we just decide the parenthesization (order) that minimizes the total scalar multiplications, finding the optimal split point <span class='highlight'>k</span> for every sub-chain."),
    ("Unit 5: Dynamic Programming", "Differentiate between Memoization and Tabulation.", "Memoization (Top-Down): Uses recursion. Checks if the result is in the cache before making a recursive call. Saves computing time but has recursion stack overhead.\nTabulation (Bottom-Up): Iterative approach. Solves all subproblems starting from the smallest, filling up an n-dimensional array. No recursion overhead."),

    # Unit 6
    ("Unit 6: Backtracking", "How does the Bounding Function work in Backtracking?", "The bounding function evaluates whether the current partial solution can lead to a valid final solution. If it violates problem constraints (e.g., placing a Queen where it's under attack, or sum exceeds target in Subset Sum), the bounding function returns false, and the algorithm prunes that branch of the state space tree."),

    # Unit 7
    ("Unit 7: Number Theoretic", "What is the Chinese Remainder Theorem (CRT)?", "CRT states that if you know the remainders of a number 'x' when divided by several pairwise coprime integers, you can uniquely determine 'x' modulo the product of those integers. It's used to solve systems of modular linear equations."),
    ("Unit 7: Number Theoretic", "Why is Primality Testing important and how does Miller-Rabin work?", "It's vital for generating large keys in Cryptography (like RSA). Miller-Rabin is a probabilistic test based on Fermat's Little Theorem. It uses a random base 'a'. If it declares a number composite, it's 100% composite. If it declares it prime, there's a small probability of error (1/4), which we make negligible by running it 'k' times (<span class='highlight'>(1/4)^k</span> error rate)."),

    # Unit 8
    ("Unit 8: NP Completeness", "What is Cook's Theorem?", "Cook's Theorem (or Cook-Levin Theorem) states that the Boolean Satisfiability Problem (SAT) is NP-Complete. It was the first problem proven to be NP-Complete. It proved that any NP problem can be reduced to SAT in polynomial time by representing the computation of a Non-Deterministic Turing Machine as a boolean formula."),
    ("Unit 8: NP Completeness", "What is Polynomial Reducibility?", "Problem A is polynomially reducible to Problem B if we can write an algorithm that transforms any instance of A into an instance of B in polynomial time, such that the answer to B is the answer to A. This is used to prove NP-Completeness."),
    ("Unit 8: NP Completeness", "What is an Approximation Algorithm?", "When an optimization problem is NP-Hard, we cannot find an exact optimal solution in polynomial time. An approximation algorithm runs in polynomial time and finds a solution that is close to the optimal solution. The 'approximation ratio' guarantees how close the result is (e.g., a 2-approximation algorithm for Vertex Cover).")
]

# --- 3. OUT OF THE BOX QUESTIONS ---
oob_qs = [
    ("Concept Application", "Can Binary Search be used on an unsorted array?", "No. Binary Search strictly requires a monotonic property (usually sorted). Without it, we cannot safely discard half of the search space because the target element could be on either side."),
    ("Real World Algorithm", "In a real-world web server managing millions of connections, which sorting algorithm is used for the connection list?", "Usually none of the basic ones. They might use a highly tuned hybrid like Timsort (Merge + Insertion), or more likely, they use a data structure that keeps elements naturally sorted upon insertion, like a Balanced Binary Search Tree (Red-Black Tree) or a Priority Queue (Heap)."),
    ("Edge Case: Dijkstra", "Why exactly does Dijkstra fail with negative weight edges?", "Dijkstra marks a node as 'visited/finalized' once it is popped from the priority queue, assuming no shorter path to it will ever be found. A negative edge can create a shortcut that makes a path shorter *after* a node has been finalized, violating Dijkstra's greedy assumption. Use Bellman-Ford instead."),
    ("Edge Case: DP", "Is Merge Sort a Dynamic Programming algorithm?", "No. While it uses Divide and Conquer, Merge Sort's subproblems are entirely independent; they do not overlap. You never sort the exact same sub-array twice. DP requires overlapping subproblems to benefit from memoization/tabulation."),
    ("Greedy vs DP", "If you are giving change for Rs. 40 using coins of Rs. 25, 20, 10, 5. Will the greedy algorithm work?", "No! Greedy would pick 25, then 10, then 5 (3 coins). But the optimal answer is two 20s (2 coins). This is why Greedy fails for general coin change, and we must use Dynamic Programming. Greedy only works for specific coin systems (like standard US/Nepal currency)."),
    ("Complexity Tricks", "Is an O(2^n) algorithm always completely useless?", "Not entirely. For extremely small values of n (e.g., n < 20), an O(2^n) algorithm will run in fractions of a second. If the problem constraints guarantee that n will always be tiny, a brute force exponential algorithm is perfectly acceptable and often easier to write than a complex polynomial one."),
    ("NP-Hard Logic", "If someone claims they wrote an algorithm that solves the Travelling Salesman Problem (TSP) exactly in O(n^3) time, what does that imply?", "If true, it would be the greatest mathematical breakthrough of the century. TSP is NP-Hard. Solving it in polynomial time (<span class='highlight'>O(n^3)</span>) would prove that P = NP, meaning all NP problems (including cracking all modern encryption) could be solved efficiently."),
    ("Randomization", "Would you ever prefer a Randomized Algorithm in a critical life-support medical system?", "Usually, no. Medical systems require strict determinism and absolute worst-case guarantees. Even if a randomized algorithm is faster on average, the infinitesimally small chance of it hitting its worst-case (or failing) is unacceptable where human lives are at stake."),
    ("Memory vs Time", "What is a 'Space-Time Tradeoff'?", "It is the concept where you can reduce the time an algorithm takes by using more memory, or reduce memory usage by taking more time. Example: Dynamic Programming uses extra memory (tabulation arrays) to drastically reduce the time complexity from exponential to polynomial."),
    ("Graph Theory Application", "How does the Internet route packets? Which algorithm?", "Routing protocols like OSPF use Dijkstra's Algorithm to find the shortest path based on link bandwidth. BGP uses a distance-vector approach similar to the Bellman-Ford algorithm to find routes across different autonomous networks.")
]


def group_by_unit(questions_list):
    grouped = ""
    current_unit = ""
    for tag, q, a in questions_list:
        if tag != current_unit:
            grouped += f"<h2 class='unit-header'>{tag}</h2>\n"
            current_unit = tag
        grouped += generate_card(tag, q, a)
    return grouped


# Generate simple HTML
simple_content = group_by_unit(simple_qs)
simple_html = HTML_TEMPLATE.format(
    title="DAA Viva: Exhaustive Simple Questions",
    subtitle="A comprehensive list of fundamental questions covering every unit of your syllabus.",
    primary_color="#3b82f6",
    secondary_color="#10b981",
    active_simple="active",
    active_advanced="",
    active_oob="",
    content=simple_content
)

# Generate advanced HTML
advanced_content = group_by_unit(advanced_qs)
advanced_html = HTML_TEMPLATE.format(
    title="DAA Viva: Exhaustive Advanced Questions",
    subtitle="In-depth conceptual questions from every chapter, testing true understanding.",
    primary_color="#8b5cf6",
    secondary_color="#f59e0b",
    active_simple="",
    active_advanced="active",
    active_oob="",
    content=advanced_content
)

# Generate OOB HTML
oob_content = "\n".join([generate_card(*q) for q in oob_qs]) # OOB doesn't strictly fit units
oob_html = HTML_TEMPLATE.format(
    title="DAA Viva: Out of the Box Questions",
    subtitle="Tricky, application-based, edge-case, and critical thinking questions.",
    primary_color="#ec4899",
    secondary_color="#06b6d4",
    active_simple="",
    active_advanced="",
    active_oob="active",
    content=oob_content
)

# Write files
import os
base_path = r"c:\Users\V16\.gemini\antigravity\scratch\5th sem\DAA\Exam_Prep"
os.makedirs(base_path, exist_ok=True)

with open(os.path.join(base_path, "daa_viva_simple.html"), "w", encoding="utf-8") as f:
    f.write(simple_html)

with open(os.path.join(base_path, "daa_viva_advanced.html"), "w", encoding="utf-8") as f:
    f.write(advanced_html)

with open(os.path.join(base_path, "daa_viva_out_of_box.html"), "w", encoding="utf-8") as f:
    f.write(oob_html)

print("Exhaustive files generated successfully!")
