# -*- coding: utf-8 -*-
import os

OUT_DIR = r"c:\Users\V16\.gemini\antigravity\scratch\5th sem\DAA\Exam_Prep"
os.makedirs(OUT_DIR, exist_ok=True)

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
  .diagram { background: #fff; border: 2px dashed #aaa; padding: 20px; text-align: center; margin: 15px 0; font-family: monospace; white-space: pre; overflow-x: auto; font-size: 0.9em; }
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
        
# =======================================================
# UNIT 1 CONTENT
# =======================================================

det_1 = """
<h2>1.1 Algorithm and its Properties</h2>
<div class="box">
    <strong>Algorithm:</strong> A finite sequence of unambiguous instructions for solving a problem. 
    <ul>
        <li><strong>Finiteness:</strong> Must terminate after a finite number of steps.</li>
        <li><strong>Definiteness:</strong> Each step must be precisely defined.</li>
        <li><strong>Input:</strong> Zero or more quantities supplied externally.</li>
        <li><strong>Output:</strong> At least one quantity is produced.</li>
        <li><strong>Effectiveness:</strong> Operations must be basic enough to be done exactly and in finite time.</li>
    </ul>
</div>

<h2>1.2 RAM Model (Random Access Machine)</h2>
<div class="box">
    <p>The standard theoretical model for algorithm analysis. It assumes a single-processor computer where instructions are executed sequentially. </p>
    <ul>
        <li><strong>Constant Time:</strong> Basic operations (arithmetic, logical, data movement, control) take O(1) time.</li>
        <li><strong>Memory:</strong> Infinite memory where accessing any memory cell takes exactly 1 time step.</li>
        <li><strong>No Memory Hierarchy:</strong> The RAM model ignores real-world complexities like L1/L2 Cache, TLBs, and paging overhead. This is a critical simplification.</li>
    </ul>
</div>

<h2>1.3 Asymptotic Notations</h2>
<div class="box">
    <p>Describes the growth rate of algorithms as input size n approaches infinity. It ignores constant factors and lower-order terms.</p>
    
    <h3>1. Big-Oh ($O$) - Upper Bound</h3>
    <p>$O(g(n)) = \\{f(n) : \\exists c > 0, n_0 > 0$ such that $0 \\le f(n) \\le c.g(n)$ for all $n \\ge n_0\\}$</p>
    <p><em>Meaning:</em> $f(n)$ grows at most as fast as $g(n)$. It bounds the worst-case time complexity.</p>

    <h3>2. Big-Omega ($\\Omega$) - Lower Bound</h3>
    <p>$\\Omega(g(n)) = \\{f(n) : \\exists c > 0, n_0 > 0$ such that $0 \\le c.g(n) \\le f(n)$ for all $n \\ge n_0\\}$</p>
    <p><em>Meaning:</em> $f(n)$ grows at least as fast as $g(n)$. It bounds the best-case time complexity.</p>

    <h3>3. Big-Theta ($\\Theta$) - Tight Bound</h3>
    <p>$\\Theta(g(n)) = \\{f(n) : \\exists c_1, c_2 > 0, n_0 > 0$ such that $0 \\le c_1.g(n) \\le f(n) \\le c_2.g(n)$ for all $n \\ge n_0\\}$</p>
    <p><em>Meaning:</em> $f(n)$ grows exactly as fast as $g(n)$.</p>
</div>

<h2>1.4 Solving Recurrences</h2>
<div class="box">
    <h3>The Master Theorem</h3>
    <p>Provides a direct solution for recurrences of the form: <br>
    <strong>$$T(n) = aT(n/b) + f(n)$$</strong> <br>
    where $a \\ge 1, b > 1$ and $f(n)$ is an asymptotically positive function.</p>
    
    <ol>
        <li><strong>Case 1 (Heavy Leaves):</strong> If $f(n) = O(n^{\\log_b a - \\epsilon})$ for some $\\epsilon > 0$, then $T(n) = \\Theta(n^{\\log_b a})$.</li>
        <li><strong>Case 2 (Balanced):</strong> If $f(n) = \\Theta(n^{\\log_b a})$, then $T(n) = \\Theta(n^{\\log_b a} \\log n)$.</li>
        <li><strong>Case 3 (Heavy Root):</strong> If $f(n) = \\Omega(n^{\\log_b a + \\epsilon})$ for some $\\epsilon > 0$, and if $a f(n/b) \\le c f(n)$ for some $c < 1$ and sufficiently large $n$, then $T(n) = \\Theta(f(n))$.</li>
    </ol>
</div>
"""

con_1 = """
<h2>Summary: Foundation of Algorithm Analysis</h2>
<ul>
    <li><strong>Algorithm Properties:</strong> Finiteness, Definiteness, Input, Output, Effectiveness.</li>
    <li><strong>RAM Model:</strong> Single processor, sequential execution, memory access = $O(1)$, operations = $O(1)$, ignores Cache/Hardware latency.</li>
    <li><strong>Asymptotic Limits:</strong></li>
    <ul>
        <li>$O(g(n))$: Upper bound (Worst Case). $f(n) \\le c \\cdot g(n)$.</li>
        <li>$\\Omega(g(n))$: Lower bound (Best Case). $f(n) \\ge c \\cdot g(n)$.</li>
        <li>$\\Theta(g(n))$: Tight bound. $c_1 g(n) \\le f(n) \\le c_2 g(n)$.</li>
    </ul>
    <li><strong>Master Theorem:</strong> For $T(n) = aT(n/b) + f(n)$. Compare $f(n)$ with $n^{\\log_b a}$.</li>
    <ul>
        <li>If $n^{\\log_b a}$ is larger $\\Rightarrow T(n) = \\Theta(n^{\\log_b a})$</li>
        <li>If they are equal $\\Rightarrow T(n) = \\Theta(n^{\\log_b a} \\log n)$</li>
        <li>If $f(n)$ is larger $\\Rightarrow T(n) = \\Theta(f(n))$</li>
    </ul>
    <li><strong>Recursion Tree:</strong> A visual tree of costs. Sum the costs across all levels to find total recurrence complexity. Used when Master Theorem doesn't perfectly fit.</li>
</ul>
"""

imp_1 = """
<h2>Board & Pre-Board Important Questions</h2>

<div class="step">
    <h3>Q1. Why do you need algorithm analysis? Discuss about RAM model. Also discuss about Big Oh, Big Omega and Big theta with examples. (2+3+5) [Boards]</h3>
    <p><strong>Answer Plan:</strong></p>
    <ul>
        <li><strong>Need:</strong> To predict performance, compare bounds, optimize memory/time resources.</li>
        <li><strong>RAM Model:</strong> Explain the Infinite Memory, Single Processor, $O(1)$ instruction mapping. Explain why we use it (mathematical simplicity).</li>
        <li><strong>Notations:</strong> Write definitions for $O, \\Omega, \\Theta$. Provide geometric bounding graphs logic and an example like $3n^2 + 2n = O(n^2)$.</li>
    </ul>
</div>

<div class="step">
    <h3>Q2. State and solve by Master method: $T(n) = 7T(n/2) + n^2$. (5 Marks) [Pre-board 2023]</h3>
    <p><strong>Answer:</strong><br>
    Form: $T(n) = aT(n/b) + f(n)$<br>
    Here $a = 7, b = 2, f(n) = n^2$.<br>
    Calculate $n^{\\log_b a}$: $n^{\\log_2 7} \\approx n^{2.8}$.<br>
    Compare $f(n) = n^2$ with $n^{2.8}$.<br>
    Since $n^2 = O(n^{2.8 - \\epsilon})$ (where $\\epsilon=0.8$), we fall into <strong>Case 1</strong>.<br>
    <span class="answer">Result: $T(n) = \\Theta(n^{\\log_2 7})$</span></p>
</div>

<div class="step">
    <h3>Q3. Solve by Master Method: $T(n) = 3T(n/2) + n$ AND $T(n) = 2T(n/4) + \\sqrt{n}$. (2.5 + 2.5) [Boards]</h3>
    <p><strong>1st Equation:</strong> $a=3, b=2, f(n)=n$. $n^{\\log_2 3} = n^{1.58}$. Since $n < n^{1.58}$, Case 1 applies. Result: $\\Theta(n^{\\log_2 3})$.</p>
    <p><strong>2nd Equation:</strong> $a=2, b=4, f(n)=n^{0.5}$. $n^{\\log_4 2} = n^{0.5}$. Since they are exactly equal ($f(n) = \\Theta(n^{\\log_b a})$), Case 2 applies. Result: $\\Theta(\\sqrt{n} \\log n)$.</p>
</div>

<div class="step">
    <h3>Q4. Solve by Recursion tree: $T(n) = 3T(n/4) + \\Theta(n^2)$. (5 Marks) [Pre-board 2023/2024]</h3>
    <p><strong>Answer:</strong><br>
    Draw a tree: Root cost is $n^2$.<br>
    3 branches at depth 1, each costing $(n/4)^2 = n^2/16$. Total level cost: $\\frac{3}{16}n^2$.<br>
    At depth 2, 9 nodes costing $n^2/256$. Total level cost: $(\\frac{3}{16})^2 n^2$.<br>
    Total Cost Series is $n^2 \\sum_{i=0}^{\\infty} (3/16)^i$. Since $(3/16) < 1$, the geometric series converges to a constant.<br>
    <span class="answer">Result: $T(n) = \\Theta(n^2)$</span></p>
</div>
"""

adv_1 = """
<h2>Advanced Real-World Algorithm Analysis</h2>
<div class="box">
    <h3>1. CPU Cache Limitations of the RAM Model</h3>
    <p>The standard RAM model assumes all memory access costs $O(1)$. In real, modern computing, CPUs use a complex multi-tiered cache hierarchy (L1, L2, L3). A Cache Hit costs ~1 nanosecond, while a Main Memory Cache Miss (RAM access) can cost ~100 nanoseconds - a 100x penalty!</p>
    <p><strong>Cache-Aware Algorithms:</strong> Algorithms are now designed acknowledging "Spatial Locality" (accessing memory in contiguous blocks is faster because CPU fetches whole cache lines, e.g. 64 bytes) and "Temporal Locality". This is why an $O(n^2)$ algorithm with perfect memory locality can sometimes outperform an $O(n \\log n)$ algorithm with randomized, sparse pointer jumps (like large Linked Lists) due to constant Cache misses.</p>

    <h3>2. Akra-Bazzi Theorem</h3>
    <p>The Master Theorem you study is a simplified subset. The <strong>Akra-Bazzi Theorem</strong> is the advanced, generalized mathematical method used in theoretical algorithm design to solve divide-and-conquer recurrences with extremely uneven sub-problem sizes.<br>
    For example, $T(n) = T(n/3) + T(2n/3) + n$. The Master Theorem completely fails here because sub-problems ($1/3$ and $2/3$) are asymmetrical. Akra-Bazzi uses calculus integration directly over the recursion functions to derive tight bounds!</p>

    <h3>3. Amortized Analysis</h3>
    <p>Instead of looking at the worst case of a single operation, <strong>Amortized Analysis</strong> looks at the worst-case performance of an entire sequence of operations. For example, a Dynamic Array (e.g., Python Lists or Java ArrayList) inserting an element is usually $O(1)$. However, when it hits max capacity, it must resize and copy everything, taking $O(n)$ time. Amortized analysis proves that averaging this rare $O(n)$ penalty across $n$ elements means the amortized time remains exactly $O(1)$ per operation.</p>
</div>
"""

build_file("Unit_1_1_Detailed_Notes.html", "Unit 1 Detailed Notes", "Unit 1: Foundation of Algorithm Analysis", det_1)
build_file("Unit_1_2_Concise_Revision.html", "Unit 1 Revision Note", "Unit 1: Quick Revision", con_1)
build_file("Unit_1_3_Important_Questions.html", "Unit 1 Questions", "Unit 1: Board & Pre-board Analysis", imp_1)
build_file("Unit_1_4_Advanced_Study.html", "Unit 1 Advanced Note", "Unit 1: Advanced Hardware & Math Formulations", adv_1)

print("Unit 1 generation complete.")
