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
        
det_2 = """
<h2>2.1 Basic Algorithms</h2>
<div class="box">
    <h3>GCD (Greatest Common Divisor) via Iteration</h3>
    <p>Using the iterative Euclidean algorithm:</p>
<pre>
def GCD(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a
</pre>
    <p><strong>Complexity:</strong> Time $O(\\log(\\min(a, b)))$, Space $O(1)$. It shrinks logarithmically because the remainder $a \\% b$ is always less than $a/2$.</p>

    <h3>Fibonacci via Iteration</h3>
    <p>Calculates the $N$-th Fibonacci number without deep recursion overhead.</p>
<pre>
def fib(n):
    if n <= 1: return n
    prev2, prev1 = 0, 1
    for i in range(2, n+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return current
</pre>
    <p><strong>Complexity:</strong> Time $O(N)$, Space $O(1)$.</p>
</div>

<h2>2.2 Sequential Search</h2>
<div class="box">
    <p>Iterates through every element from beginning to end to find the target.</p>
    <p><strong>Worst Case Time:</strong> $O(N)$ (Element is at the end or not present).<br>
    <strong>Best Case Time:</strong> $O(1)$ (Element is at the 1st position).<br>
    <strong>Average Time:</strong> $O(N/2)$ which simplifies to $O(N)$.</p>
</div>

<h2>2.3 Sorting Algorithms</h2>
<div class="box">
    <h3>1. Bubble Sort</h3>
    <p>Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. Largest elements bubble to the surface at the end.</p>
    <p><strong>Worst/Average Time:</strong> $O(N^2)$. <strong>Best Time:</strong> $O(N)$ (if optimized with a boolean swap flag on an already sorted array).</p>

    <h3>2. Selection Sort</h3>
    <p>Finds the minimum element from the unsorted part and puts it at the beginning.</p>
    <p><strong>Worst/Average/Best Time:</strong> All exactly $O(N^2)$. Even if the array is sorted, it still scans the entire remaining list to verify minimums.</p>

    <h3>3. Insertion Sort</h3>
    <p>Builds the final sorted array one item at a time. It compares the current element backwards against already sorted ones and inserts it into the correct position.</p>
    <p><strong>Worst/Average Time:</strong> $O(N^2)$ (Array reversed).<br>
    <strong>Best Time:</strong> $O(N)$ (Array already sorted - inner loop instantly terminates without shifting). Extremely efficient for small datasets.</p>
</div>
"""

con_2 = """
<h2>Summary: Iterative Algorithms</h2>
<ul>
    <li><strong>GCD Algorithm:</strong> Uses $a, b$ modulo substitutions. Space: $O(1)$. Time: $O(\\log(\\min(a,b)))$. Extremely fast.</li>
    <li><strong>Fibonacci:</strong> Iterative > Recursive. $O(N)$ Time. $O(1)$ Space. The recursive approach takes $O(2^n)$ Time which is intractable!</li>
    <li><strong>Linear/Sequential Search:</strong> Simple <code>for</code> loop. Constant $O(1)$ space. Worst case $O(N)$. Doesn't require array to be sorted.</li>
    <li><strong>Bubble Sort:</strong> $O(N^2)$. Compares and swaps adjacent pairs. Optimized version halts if no swaps occurred in a pass.</li>
    <li><strong>Selection Sort:</strong> $O(N^2)$ always. Scans strictly for the global minimum for the next index position. Least number of Memory Swaps ($O(N)$ swaps maximum).</li>
    <li><strong>Insertion Sort:</strong> $O(N^2)$. Acts like sorting playing cards in your hand. Best case is $O(N)$ if nearly sorted. Often used in hybrid algorithms for small chunks.</li>
</ul>
"""

imp_2 = """
<h2>Board & Pre-Board Important Questions</h2>

<div class="step">
    <h3>Q1. Write the algorithm for insertion sort and explain its time complexity. (5 Marks) [Boards]</h3>
    <p><strong>Answer:</strong></p>
<pre>
INSERTION-SORT(A)
    for j = 2 to A.length
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key // Scan backward
            A[i+1] = A[i]          // Shift right
            i = i - 1
        A[i+1] = key               // Insert
</pre>
    <p><strong>Complexity Explanation:</strong></p>
    <ul>
        <li><strong>Best Case Time: $\\Omega(N)$</strong>. When the array is already sorted, the `while` loop condition `A[i] > key` fails immediately on the first check. The inner loop doesn't execute, resulting in exactly $N-1$ constant time comparisons.</li>
        <li><strong>Worst Case Time: $O(N^2)$</strong>. When the array is sorted in reverse order, every new element `j` requires scanning and shifting all $j-1$ previous elements. This forms an arithmetic progression sum $\\frac{N(N-1)}{2}$, which simplifies to $O(N^2)$.</li>
        <li><strong>Space Complexity: $O(1)$</strong>. It sorts completely in-place.</li>
    </ul>
</div>
"""

adv_2 = """
<h2>Advanced Algorithms: Python's Timsort & Hardware Optimization</h2>
<div class="box">
    <h3>Why Insertion Sort Defeats Advanced Algorithms in Real Life</h3>
    <p>You learned that Merge Sort and Quick Sort are $O(N \\log N)$, completely dominating Insertion Sort's $O(N^2)$. So why does the V8 JavaScript Engine, Python's sorted(), and Java's Arrays.sort() rely heavily on Insertion Sort under the hood?</p>
    <ul>
        <li><strong>Timsort:</strong> Timsort leverages the fact that real-world data contains pre-sorted sub-arrays (called "runs"). It splits a massive array into tiny chunks of 32 or 64 elements, uses <strong>Insertion Sort</strong> to perfectly sort those tiny chunks, and then uses Merge Sort to sew them together!</li>
        <li><strong>Constant Overhead & Caching:</strong> $O(N \\log N)$ comes with huge constant hardware overheads (recursion stack setup, object tracking). For small $N$ (e.g., $N < 50$), the overhead crushes the CPU. Furthermore, Insertion Sort operates perfectly sequentially backwards, ensuring a 100% L1 Cache Hit Rate because it never jumps randomly. The hardware executes it instantly.</li>
    </ul>

    <h3>Branch Predictor Failure in Sorting</h3>
    <p>CPUs "guess" which branch an `if` statement will take to execute instructions in advance (Lookahead pipelines). If you sort random data, the CPU's branch predictor guesses `A[i] > key` correctly only 50% of the time, resulting in massive hardware penalty stalls! If the data is almost sorted, the branch predictor reaches near 100% accuracy, making iterative comparisons blazing fast at the microarchitecture level.</p>
</div>
"""

build_file("Unit_2_1_Detailed_Notes.html", "Unit 2 Detailed Notes", "Unit 2: Iterative Algorithms", det_2)
build_file("Unit_2_2_Concise_Revision.html", "Unit 2 Revision Note", "Unit 2: Quick Revision", con_2)
build_file("Unit_2_3_Important_Questions.html", "Unit 2 Questions", "Unit 2: Board & Pre-board Analysis", imp_2)
build_file("Unit_2_4_Advanced_Study.html", "Unit 2 Advanced Note", "Unit 2: Advanced Real-World Context", adv_2)
print("Unit 2 generation complete.")
