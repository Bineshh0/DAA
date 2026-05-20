import os

OUT_DIR = r"c:\Users\V16\.gemini\antigravity\scratch\5th sem\DAA\Exam_Prep"

CSS = """
<style>
  body { font-family: 'Segoe UI', sans-serif; max-width: 900px; margin: 30px auto; padding: 0 20px; line-height: 1.6; color: #222; background: #fdfdfd; }
  h1 { text-align: center; color: #1a1a2e; border-bottom: 3px solid #16213e; padding-bottom: 10px; }
  h2 { color: #16213e; background: #e8eaf6; padding: 10px 14px; border-left: 5px solid #1a237e; margin-top: 40px; }
  h3 { color: #283593; margin-top: 20px; border-bottom: 1px dashed #ccc; padding-bottom: 5px; }
  table { border-collapse: collapse; margin: 15px 0; width: 100%; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
  th, td { border: 1px solid #bbb; padding: 10px 14px; text-align: left; }
  th { background: #e0e0e0; font-weight: bold; }
  .step, .box { background: #fff; border: 1px solid #ddd; padding: 15px 20px; margin: 10px 0; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
  .answer { background: #e8f5e9; padding: 10px 15px; border-left: 5px solid #2e7d32; margin: 15px 0; font-weight: bold; font-size: 1.1em; color: #1b5e20; }
  ul, ol { margin: 10px 0 10px 25px; padding-left: 10px; }
  li { margin-bottom: 8px; }
  code { background: #eee; padding: 2px 6px; border-radius: 4px; font-family: monospace; color: #d32f2f; }
  pre { background: #f4f4f4; padding: 15px; font-family: monospace; border: 1px solid #ccc; border-radius: 5px; overflow-x: auto; font-size: 1.1em; color: #0d47a1; }
</style>
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{TITLE}}</title>
""" + CSS + """
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    <h1>{{H1}}</h1>
    {{CONTENT}}
</body>
</html>"""

def build_file(filename, title, h1, content):
    html = HTML_TEMPLATE.replace("{{TITLE}}", title).replace("{{H1}}", h1).replace("{{CONTENT}}", content)
    with open(os.path.join(OUT_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(html)
        
det_3 = """
<h2>3.1 Divide and Conquer Paradigm</h2>
<div class="box">
    <p>A recursive algorithm design paradigm that solves a problem by applying three steps:</p>
    <ul>
        <li><strong>Divide:</strong> Break the main problem into several smaller sub-problems of the same type.</li>
        <li><strong>Conquer:</strong> Solve the sub-problems recursively. If they are small enough, solve them directly (base case).</li>
        <li><strong>Combine:</strong> Merge the solutions of the sub-problems to form the solution to the original problem.</li>
    </ul>
    <h3>Binary Search</h3>
    <p>Finds the target in a sorted list by halving the search space recursively.</p>
    <p><strong>Recurrence:</strong> $T(N) = T(N/2) + O(1)$. <strong>Time:</strong> $O(\\log N)$.</p>
    <h3>Min-Max Finding</h3>
    <p>Instead of $2N - 2$ comparisons iteratively, we split the array in half, find min/max in left and right, and compare. Total comparisons drop to $3N/2 - 2$.</p>
</div>

<h2>3.2 Sorting Algorithms</h2>
<div class="box">
    <h3>Merge Sort</h3>
    <p>Splits the list exactly in half until 1 element remains. Merges the halves recursively.</p>
    <p><strong>Recurrence:</strong> $T(N) = 2T(N/2) + O(N)$.<br>
    <strong>Time:</strong> $O(N \\log N)$ always. <strong>Space:</strong> $O(N)$ auxiliary array.</p>
    
    <h3>Quick Sort</h3>
    <p>Divides based on a Pivot element, ensuring elements on the left are smaller and on the right are larger.</p>
    <p><strong>Worst Case Time:</strong> $O(N^2)$ (When sorted natively and Pivot is 1st element. Partition is highly skewed $N-1$ and $1$).<br>
    <strong>Average Best Time:</strong> $O(N \\log N)$. <strong>Space:</strong> $O(\\log N)$ recursion stack.</p>
    
    <h3>Heap Sort</h3>
    <p>Treats array as a Complete Binary Tree. Builds a Max-Heap where parent > children.</p>
    <ol>
        <li><strong>BuildHeap:</strong> Call `Heapify` on all non-leaf nodes. Time: $O(N)$.</li>
        <li><strong>HeapSort:</strong> Swap the root (max element) with the last node, reduce array size, and call `Heapify` top-down to repair property. Time: $O(N \\log N)$.</li>
    </ol>
    <p><strong>Complexity:</strong> $O(N \\log N)$ worst-case. In-place, Space: $O(1)$.</p>
</div>

<h2>3.3 Order Statistics</h2>
<div class="box">
    <p>Finding the $i$-th smallest element in an unordered array. If $i = 1$, it's Minimum. If $i = N/2$, it's Median.</p>
    <h3>Selection in Expected Linear Time (Quick Select)</h3>
    <p>Randomly pick a pivot. Partition the list. If pivot lands at index $k$, and $i = k$, you are done! If $i < k$, search only the left partition.<br>
    <strong>Time:</strong> $O(N)$ average, but $O(N^2)$ worst-case.</p>

    <h3>Worst Case Linear Time Selection (Median of Medians)</h3>
    <p>Forces a good pivot to guarantee worst-case $O(N)$ partitioning limit.</p>
    <ol>
        <li>Divide $N$ elements into groups of 5.</li>
        <li>Find median of each group (takes $O(1)$). You get $\\lceil N/5 \\rceil$ medians.</li>
        <li>Recursively invoke the algorithm to find the Median of the $N/5$ medians. Call this $X$.</li>
        <li>Use $X$ as the Partition Pivot!</li>
    </ol>
    <p><strong>Recurrence:</strong> $T(n) = T(n/5) + T(7n/10) + O(n)$. Total Time: strictly $O(N)$.</p>
</div>
"""

con_3 = """
<h2>Summary: Divide and Conquer Algorithms</h2>
<ul>
    <li><strong>Concept:</strong> Divide $\\rightarrow$ Conquer $\\rightarrow$ Combine. Reduces time bounds exponentially.</li>
    <li><strong>Binary Search:</strong> $O(\\log N)$. Halves the scope. Array must be sorted.</li>
    <li><strong>Merge Sort:</strong> $O(N \\log N)$. Always splits array in exact half. Stable sort. Heavily memory dependent ($O(N)$ space required).</li>
    <li><strong>Quick Sort:</strong> $O(N \\log N)$ on average. In-place. Not stable. Vulnerable to $O(N^2)$ worst-case if pivot selection is skewed.</li>
    <li><strong>Randomized Quicksort:</strong> Stops hackers from inputting adversarial edge cases by selecting the pivot via RNG. Averages $O(N \\log N)$ guaranteed.</li>
    <li><strong>Heap Sort:</strong> Creates complete binary tree using array indexes ($2i$ left, $2i+1$ right). Root is max. Constant Space $O(1)$, Time $O(N \\log N)$.</li>
    <li><strong>Min-Max:</strong> Divide & conquer reduces brute force comparisons from $2n-2$ to $3n/2 - 2$.</li>
    <li><strong>Order Statistics (Worst Case Linear $O(N)$):</strong> The Median of Medians approach groups into 5s to avoid $O(N^2)$ QuickSelect crashes, guaranteeing 30/70 partitioning.</li>
</ul>
"""

imp_3 = """
<h2>Board & Pre-Board Important Questions</h2>

<div class="step">
    <h3>Q1. Write Heap Sort algorithm, explain with an example, and analyze complexity (6+2+2) [Pre-board 2024]</h3>
    <p><strong>Algorithmic Steps:</strong></p>
    <pre>
1. BUILD-MAX-HEAP(A)
      For i = floor(length/2) down to 1:
          MAX-HEAPIFY(A, i)
2. HEAPSORT(A)
      For i = length(A) down to 2:
          Exchange A[1] with A[i]
          heap_size = heap_size - 1
          MAX-HEAPIFY(A, 1)
    </pre>
    <p><strong>Complexity Analysis:</strong><br>
    - Building the heap originally takes $O(N)$ time.<br>
    - The main loop runs $N-1$ times, and in each iteration, extracting the root and sinking the new root down (Heapify) takes $O(\\log N)$.<br>
    - Total Time Complexity: $O(N \\log N)$. Space is $O(1)$.</p>
</div>

<div class="step">
    <h3>Q2. Explain Merge sort with recurrence relation and analysis its complexity. (5 Marks) [Pre-board 2024]</h3>
    <p><strong>Answer:</strong><br>
    Merge Sort recursively divides the array of $n$ elements into two sub-arrays of size $n/2$, sorts them independently, and merges the sorted arrays in $O(n)$ time.<br>
    <strong>Recurrence Relation:</strong> $T(n) = 2T(n/2) + cn$<br>
    Using the Master Method: $a=2, b=2, f(n)=n$.<br>
    $n^{\\log_2 2} = n^1 = n$.<br>
    Since $f(n)$ optimally matches $n^{\\log_b a}$ (Case 2), the overall complexity is exactly $\\Theta(N \\log N)$.</p>
</div>

<div class="step">
    <h3>Q3. Discuss the order statistics. Explain worst-case linear time selection algorithm and time complexity. (2+8) [Boards]</h3>
    <p><strong>Answer Plan:</strong></p>
    <ul>
        <li><strong>Order Statistics:</strong> Define finding the i-th smallest element. Median is $\\lceil N/2 \\rceil$.</li>
        <li><strong>Algorithm:</strong> Write SELECT(A, p, r, i). Detail the "group by 5" and "median of medians" pivot selection.</li>
        <li><strong>Complexity Analysis:</strong> State recursion $T(n) = T(n/5) + T(7n/10) + c \\cdot n$. The total sum equals $n$. So worst-case is strictly $O(N)$ linear time.</li>
    </ul>
</div>
"""

adv_3 = """
<h2>Advanced Industry Usage: Defeating DoS Attacks</h2>
<div class="box">
    <h3>1. QuickSort Denial-of-Service Vulnerability</h3>
    <p>Normally, programming languages default sorting arrays to QuickSort because it's very cache-friendly. However, hackers realized that if they feed web servers specific reverse-engineered malformed input data, they can trigger QuickSort's $O(n^2)$ worst-case. This forces the server's CPU to max out for minutes just to sort a small 100,000 item list, effectively executing an Algorithmic Denial of Service (DoS) attack.</p>
    <p><strong>The Fix: IntroSort (Introspective Sort)</strong><br>
    Modern libraries (C++ `std::sort`, Rust `sort`) use a hybrid algorithm called IntroSort. It starts by using QuickSort for its blazing speed. BUT, if the recursion depth exceeds $2 \\cdot \\log_2 N$, the algorithm formally "introspects" (realizes it's being hacked or fed extremely bad data), and instantly switches entirely to <strong>Heap Sort</strong>. Heap Sort guarantees $O(N \\log N)$ execution regardless of data skew!</p>

    <h3>2. "Median of Medians" Why the magic number 5?</h3>
    <p>In the Worst-Case Linear Time Selection algorithm, why do we group elements in sets of 5? Why not 3 or 7?</p>
    <p>If we group by 3, the recurrence becomes $T(n/3) + T(2n/3) + O(n)$. Notice that $n/3 + 2n/3 = n$. The work isn't shrinking fast enough, and the total complexity expands mathematically to $O(N \\log N)$, failing the "Linear Time" requirement. <br>
    Grouping by 5 correctly reduces the branches to $n/5$ and $7n/10$. The sum is $9n/10$. Since $9/10 < 1$, it strictly converges geometrically bounding execution at $O(N)$. While grouping by 7 or 9 also achieves $O(N)$, grouping by 5 possesses the smallest known constant factor multiplying the asymptotic notation.</p>
</div>
"""

build_file("Unit_3_1_Detailed_Notes.html", "Unit 3 Detailed Notes", "Unit 3: Divide and Conquer", det_3)
build_file("Unit_3_2_Concise_Revision.html", "Unit 3 Revision Note", "Unit 3: Quick Revision", con_3)
build_file("Unit_3_3_Important_Questions.html", "Unit 3 Questions", "Unit 3: Board & Pre-board Analysis", imp_3)
build_file("Unit_3_4_Advanced_Study.html", "Unit 3 Advanced Note", "Unit 3: Security Vectors & Deep Math", adv_3)
print("Unit 3 generation complete.")
