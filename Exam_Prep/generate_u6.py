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

det_6 = """
<h2>6.1 Concept of Backtracking</h2>
<div class="box">
    <p>Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time. It uses a <strong>State Space Tree</strong> constraint mechanism. Unlike naive recursion which brute-forces absolutely all paths, if Backtracking determines that building on the current partial solution cannot possibly yield a valid solution, it abandons (<strong>prunes</strong>) it immediately, reversing the last action and moving backward to try a different path.</p>
    <h3>Recursion vs Backtracking</h3>
    <ul>
        <li><strong>Recursion:</strong> Computes the function calls indiscriminately until base cases are forcefully hit.</li>
        <li><strong>Backtracking:</strong> Evaluates a boolean <em>Bounding Function (isSafe check)</em> before attempting the recursive step. If false, it completely ignores the entire subtree node branch!</li>
    </ul>
</div>

<h2>6.2 Backtracking Algorithms</h2>
<div class="box">
    <h3>N-Queen Problem</h3>
    <p>Given an N x N chessboard, place N Queens such that no two attack each other (not in same row, column, or diagonals).<br>
    <strong>Strategy:</strong> Place Queen in column 1, row 1. Proceed to column 2. Try row 1 (attacked!), row 2 (attacked!), try row 3 (Safe). Place it. If column 3 fails for all rows, abandon column 2's placement, move column 2's queen down one row, and recompute!</p>

    <h3>Subset-Sum Problem</h3>
    <p>Given an array of integer values and a target Sum $M$, find all possible subsets that accurately sum to $M$.<br>
    <strong>Bounding Function (Pruning):</strong> Let $S$ be the current running sum and $A[k]$ be the next element. If $(S + A[k] > M)$, immediately halt and prune. Do not explore the inclusion of $A[k]$. Also, ignore generating further subsets if adding every remaining element left in the array still yields $< M$.</p>

    <h3>0/1 Knapsack via Backtracking</h3>
    <p>Instead of DP Table, we explore the $2^N$ tree explicitly.<br>
    <strong>Bounding Function:</strong> If adding the next item breaches maximum Weight $W$, prune the branch immediately. To optimize further, keep a `max_profit` global tracker. If the current accumulated profit + the optimistic remaining possible profit (if we mathematically took fractions of the rest) is ALREADY mathematically less than `max_profit`, prune the branch immediately because it's a dead end!</p>
</div>
"""

con_6 = """
<h2>Summary: Backtracking</h2>
<ul>
    <li><strong>Core Concept:</strong> Depth First Search (DFS) over a logical State Space Tree combined with severe Bounding Function pruning.</li>
    <li><strong>N-Queens:</strong> Constraints check array elements left-diagonal, right-diagonal, and horizontal rows. Prunes trillions of invalid board states.</li>
    <li><strong>Subset Sum:</strong> Evaluates subsets sequentially. State Space left node = Include current. Right node = Exclude current. Prunes if running tally exceeds Target.</li>
    <li><strong>0/1 Knapsack:</strong> Uses bounding fractions. If (Current Profit + Bound Profit of remaining) $<=$ Max Found Profit, it skips explicitly calculating that whole subtree!</li>
</ul>
"""

imp_6 = """
<h2>Board & Pre-Board Important Questions</h2>

<div class="step">
    <h3>Q1. Explain backtracking with suitable example. (5) [Boards]</h3>
    <p><strong>Answer:</strong><br>
    Backtracking systematically searches for a solution to a problem among all available options by building candidates piece by piece. If a candidate is determined to be invalid midway, it is abandoned ("backtracked"). <br>
    <strong>Example (N-Queens via `isSafe()` bound):</strong></p>
<pre>
SOLVE-N-QUEENS(board, col)
    if col >= N: return true
    for row = 0 to N-1
        if isSafe(board, row, col):
            board[row][col] = 1        // Place
            if (SOLVE-N-QUEENS) return true
            board[row][col] = 0        // Backtrack
    return false
</pre>
</div>

<div class="step">
    <h3>Q2. Explain problem optimization, how 0/1 Knapsack problem can be solved by backtracking approach? Show necessary calculation of state space tree. W=8, n=6, profits=[13,14,24,25,18,10], weight=[2,3,6,5,4,1] (2+8) [Pre-board 2023]</h3>
    <p><strong>Answer Plan:</strong></p>
    <ul>
        <li><strong>Problem Optimization:</strong> Utilizing global upper bounds to instantly terminate recursive tree growth downward.</li>
        <li><strong>Backtracking Logic:</strong> Define node function $BT(weight\\_idx, cur\\_prof, cur\\_wt)$.</li>
        <li><strong>Calculation:</strong> Sort by Profit/Weight Ratio first! Ratio array = [6.5, 4.6, 4, 5, 4.5, 10]. Sorted sequence: Item6, Item1, Item4, Item2, Item5, Item3.<br>
        Start Tree at Root (W=0, P=0).<br>
        Left child (Take Item 6): W=1, P=10. Right child (Skip 6): W=0, P=0.<br>
        Follow left. Take Item 1. W=3, P=23.<br>
        Take Item 4. W=8, P=48. FULL! Bound limits hit. Right side branches prune.<br>
        The required explicit tree drawing should demonstrate branches cleanly cutting off when $W > 8$.</li>
    </ul>
</div>

<div class="step">
    <h3>Q3. Explain how backtracking is used for subset sum problem explain with example. (5) [Pre-board 2024]</h3>
    <p><strong>Answer:</strong><br>
    The Subset Sum problem builds a binary tree where left lines assign $X_i = 1$ (include) and right lines assign $X_i = 0$ (exclude). <br>
    <strong>Bounding:</strong><br>
    Suppose Set S = {2, 3, 5, 6, 8} Target M = 10.<br>
    Root -> Include 2 (sum=2) -> Include 3 (sum=5) -> Include 5 (sum=10). We print solution `{2, 3, 5}`!<br>
    Then Backtrack to (sum=5), Include 6 (sum=11 > 10). Here the bounding function detects failure. IT PRUNES the branch immediately, avoiding further additions below it.</p>
</div>
"""

adv_6 = """
<h2>Advanced Theoretical Analysis</h2>
<div class="box">
    <h3>Optimization via Constraint Satisfaction Problems (CSPs)</h3>
    <p>In modern AI systems, plain Backtracking is extremely weak. Backtracking naively attempts the very next valid option in sequential order. In <strong>Constraint Satisfaction Problems (CSPs)</strong> (used in Sudoku solvers, Google Maps graph routing, and Logistics), AI algorithms use two profound upgrades:</p>
    <ul>
        <li><strong>Minimum Remaining Values (MRV) Heuristic:</strong> Instead of picking "Column 2" next in N-Queens, the algorithm scans the entire board and actively picks the variable that has the <em>fewest</em> legal remaining options. If a column only has 1 safe tile left, it assigns it immediately. This aggressively shrinks the backtracking tree depth.</li>
        <li><strong>Forward Checking:</strong> Whenever the algorithm assigns $X_1$, it instantly scans $X_2, X_3... X_n$ and crosses out incompatible domains exactly at that given moment. If any future variable's domain becomes empty $0$, the algorithm catches the impending failure $N$ layers early and backtracks immediately! This eliminates millions of wasted node computations that naive backtracking blindly falls into.</li>
    </ul>
</div>
"""

build_file("Unit_6_1_Detailed_Notes.html", "Unit 6 Detailed Notes", "Unit 6: Backtracking", det_6)
build_file("Unit_6_2_Concise_Revision.html", "Unit 6 Revision Note", "Unit 6: Quick Revision", con_6)
build_file("Unit_6_3_Important_Questions.html", "Unit 6 Questions", "Unit 6: Board & Pre-board Analysis", imp_6)
build_file("Unit_6_4_Advanced_Study.html", "Unit 6 Advanced Note", "Unit 6: CSP AI Heuristics", adv_6)
print("Unit 6 generation complete.")
