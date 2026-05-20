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

det_5 = """
<h2>5.1 Strategy: Dynamic Programming vs Greedy</h2>
<div class="box">
    <p><strong>Dynamic Programming (DP)</strong> solves complex optimization problems by breaking them down into simpler, overlapping subproblems. Unlike Greedy tracking only local minimums, DP computes <em>all</em> possible scenarios completely, tabulates their values to avoid redundant computation, and finally picks the optimal aggregate path.</p>
    <ul>
        <li><strong>Optimal Substructure:</strong> Optimal solution to problem contains optimal solutions to sub-problems.</li>
        <li><strong>Overlapping Subproblems:</strong> Subproblems recur heavily. Recursion computes them $2^N$ times. DP computes them exactly once, fetching from an array hereafter $O(1)$.</li>
    </ul>
    <h3>Memoization vs Tabulation Strategy</h3>
    <p><strong>Memoization (Top-Down):</strong> Writing a standard recursive function, but wrapping a cache array at the top. If `cache[n]` exists, return it, else compute. Pros: Only computes strictly required nodes. Cons: Heavy Call Stack overhead.</p>
    <p><strong>Tabulation (Bottom-Up):</strong> Fully abandoning recursion. Building a massive ND-array from size 0, 1... up to N incrementally in iterative loops. Pros: No recursion limit crashes. Cons: Computes every single cell regardless of need.</p>
</div>

<h2>5.2 DP Algorithms</h2>
<div class="box">
    <h3>Floyd-Warshall (All-Pairs Shortest Path)</h3>
    <p>Instead of running Dijkstra $V$ times, it builds a massive DP matrix. It checks if passing through an intermediate vertex $k$ creates a shorter path extending from $i$ to $j$.</p>
    <p>Formula: $D^k[i][j] = \\min(D^{k-1}[i][j], D^{k-1}[i][k] + D^{k-1}[k][j])$<br>
    <strong>Complexity:</strong> Time $O(V^3)$, Space $O(V^2)$.</p>

    <h3>0/1 Knapsack Problem</h3>
    <p>You cannot take partial items. Fractional Greedy fails. We build a DP matrix where rows = Items available, cols = Weight Capacity.<br>
    Formula: `DP[i][w] = max(DP[i-1][w], val[i] + DP[i-1][w-wt[i]])`</p>
    <p><strong>Complexity:</strong> strictly $O(N \\times W)$. Note this is <em>Pseudo-polynomial</em>. If W is $10^9$, runtime hangs.</p>

    <h3>String Editing (Edit Distance)</h3>
    <p>Converts String A to String B using insertions, deletions, and substitutions. Forms a 2D matrix comparing prefixes.</p>

    <h3>Matrix Chain Multiplication</h3>
    <p>Determines the perfectly optimal Parenthesization sequence for multiplying $N$ matrices to minimize scalar arithmetic multiplications. It calculates all split intervals $k$ across sequence length $i$ to $j$. Time: $O(N^3)$.</p>
</div>
"""

con_5 = """
<h2>Summary: Dynamic Programming</h2>
<ul>
    <li><strong>Core Pillars:</strong> Overlapping Subproblems & Optimal Substructure.</li>
    <li><strong>Approach:</strong> Tabulation (Bottom-up DP table) vs Memoization (Top-down Recursive Cache). DP executes entirely in Polynomial Time, while naïve recursion hits Exponential Time.</li>
    <li><strong>Matrix Chain:</strong> $O(N^3)$. Minimizes floating point operations natively. Formula: $M[i][j] = \\min_{k}(M[i][k] + M[k+1][j] + p_{i-1}p_k p_j)$.</li>
    <li><strong>String Editing:</strong> $O(M \\times N)$. Table compares strings. If chars match, copy diagonal `[i-1][j-1]`. Else `1 + min(delete, insert, substitute)`.</li>
    <li><strong>0/1 Knapsack:</strong> $O(N \\times W)$. Items indivisible. You either explicitly take it (add val, subtract weight index), or explicitly discard it. DP matrices store highest val tracked at all strict weight tiers.</li>
    <li><strong>Floyd-Warshall:</strong> $O(V^3)$. Computes shortest path matrix iteratively funneling routes strictly restricted through interim vertex $K=1..N$.</li>
    <li><strong>TSP (Travelling Salesman):</strong> $O(N^2 2^N)$. DP heavily reduces plain recursion from $O(N!)$, saving vast calculations, but still remains NP-hard.</li>
</ul>
"""

imp_5 = """
<h2>Board & Pre-Board Important Questions</h2>

<div class="step">
    <h3>Q1. Explain Matrix Chain Multiplication, write recurrence relation and find the optimal cost for chain (4 x 10) (10 x 3) (3 x 12) (12 x 20) (20 x 7). (2+8) [Pre-board 2024]</h3>
    <p><strong>Answer Plan:</strong></p>
    <ul>
        <li><strong>Explanation:</strong> Emphasize that matrix multiplication is associative but NOT commutative. Parentheses placement drastically shifts total scalar operations without altering the final content algorithm layout. Dynamic programming breaks the interval $i$ to $j$ exploring every pivot partition $k$.</li>
        <li><strong>Recurrence Relation:</strong><br>
        $m[i, j] = 0$ if $i = j$<br>
        $m[i, j] = \\min_{i \\le k < j} \\{m[i, k] + m[k+1, j] + p_{i-1} \\cdot p_k \\cdot p_j\\}$ if $i < j$</li>
        <li><strong>Numerical Calculation:</strong> Build an $N \\times N$ DP table. You have 5 dimensions $[4, 10, 3, 12, 20, 7]$. Iteratively compute lengths 2, 3, 4, 5. Show minimum costs dynamically updating $m[1..2]$ etc. Result yields optimal parens.</li>
    </ul>
</div>

<div class="step">
    <h3>Q2. Explain Dynamic Programming Approach. Differ with recursion? Floyd Warshall algorithm to compute shortest path and analyze its time complexity. (4+6) [Boards]</h3>
    <p><strong>Answer:</strong><br>
    DP is problem solving via tabular history, ensuring you solve a unique problem exactly once.<br>
    <strong>DP vs Recursion:</strong><br>
    1. DP is Bottom-Up, explicit memory state array. Recursion is Top-Down, Call Stack.<br>
    2. DP resolves in Polynomial time (efficient). Uncached Recursion handles overlapping problems repeatedly, resulting in severe Exponential Time.<br>
    <strong>Floyd-Warshall:</strong> Write the 3 nested loops. $k$ is the intermediate vertex, evaluating rows $i$ expanding to targets $j$. Matrix is strictly updated $N$ times. Due to 3 loops over $N$ vertices, total time strictly evaluates to exactly $O(V^3)$.</p>
</div>

<div class="step">
    <h3>Q3. What do you mean by memoization strategy? Compare memoization with dynamic programming. (5) [Boards]</h3>
    <p><strong>Answer:</strong><br>
    Memoization is caching the output of a deterministic recursive function directly into a HashMap or array based on its exact input parameters.<br>
    <strong>Comparison:</strong><br>
    - DP (Tabulation) computes $100\\%$ of all subproblems systematically inside iterative `for`-loops. Eager evaluation. High space density.<br>
    - Memoization evaluates 'lazy'. It exclusively computes branches triggered actively by the recursive request. It bypasses mathematically impossible logic branches directly, potentially saving table space if states are extremely sparse. Prone to Call Stack Overflow exception on vast data sets.</p>
</div>
"""

adv_5 = """
<h2>Advanced DP Memory Economics</h2>
<div class="box">
    <h3>The Viterbi Algorithm & DNA Decoding</h3>
    <p>While Matrix Chain and TSP are strictly computer science concepts, the highest peak of Dynamic Programming governs biological evolution computational discovery currently actively used today. The <strong>Viterbi Algorithm</strong> is a DP framework used to analyze Hidden Markov Models (HMMs).</p>
    <p>When sequencing raw nucleotide data (interpreting electrical noise from rapid DNA genome strands A,C,T,G sequence), Viterbi DP is executed to calculate the highest probability exact path of correct nucleotides backwards through the matrix, correcting for genetic read variations computationally. If done recursively without DP, sequencing one genome would mathematically exceed the universe's total processing lifespan!</p>

    <h3>Why 0/1 Knapsack is Fake Polynomial (Pseudo-Polynomial)</h3>
    <p>You memorize that 0/1 Knapsack is $O(N \\times W)$. This feels like Polynomial Time, putting it in Class 'P'. So why is Knapsack labeled exactly as NP-Complete Intractable?</p>
    <p>In complexity theory, inputs are measured strictly by bit length. A knapsack capacity $W=1,000,000$ requires exactly $20$ binary bits of input memory string space natively (since $2^{20} \\approx 1,000,000$). However, implementing the DP solution forces us to construct a full 2D loop computing memory locations up to $W$.<br>
    The algorithm's strict Time Execution corresponds to $2^{\\text{input bits}}$. The time grows EXPONENTIALLY relative strictly to the bit capacity representation length of $W$. So if a hacker provides $W=10^{15}$, the bit length is merely 50 bytes of JSON payload string, which crashes the server matrix DP generation, failing completely.</p>
</div>
"""

build_file("Unit_5_1_Detailed_Notes.html", "Unit 5 Detailed Notes", "Unit 5: Dynamic Programming", det_5)
build_file("Unit_5_2_Concise_Revision.html", "Unit 5 Revision Note", "Unit 5: Quick Revision", con_5)
build_file("Unit_5_3_Important_Questions.html", "Unit 5 Questions", "Unit 5: Board & Pre-board Analysis", imp_5)
build_file("Unit_5_4_Advanced_Study.html", "Unit 5 Advanced Note", "Unit 5: Bio-Informatics & NP-Deception", adv_5)
print("Unit 5 generation complete.")
