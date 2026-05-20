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

det_8 = """
<h2>8.1 Tractable vs Intractable Problems</h2>
<div class="box">
    <p><strong>Tractable Problems:</strong> Problems that can be definitively solved in Polynomial Time (i.e. $O(N^k)$). Examples: Sorting $O(N \\log N)$, Matrix Multiplication $O(N^3)$.</p>
    <p><strong>Intractable Problems:</strong> Problems that strictly require Super-Polynomial Time (Exponential $O(2^N)$ or Factorial $O(N!)$) on all known computational algorithms. If input size scales, they crash the computer. Examples: 0/1 Knapsack, TSP.</p>
</div>

<h2>8.2 Complexity Classes</h2>
<div class="box">
    <h3>P (Polynomial Time)</h3>
    <p>Problems that can be structurally <strong>SOLVED</strong> by a determinisitic computer in Polynomial time. (e.g. Dijkstra, Binary Search).</p>

    <h3>NP (Non-deterministic Polynomial)</h3>
    <p>Problems whose solutions cannot currently be <em>found</em> quickly, but if someone hands you a solution, you can mathematically <strong>VERIFY</strong> if that solution is correct strictly in Polynomial time natively. (e.g., Checking if a given TSP path is $< 1000$ miles takes $O(N)$, but computing the shortest path from scratch takes exponential time).</p>

    <h3>NP-Hard</h3>
    <p>A problem is NP-Hard if every other problem strictly in NP can be mathematically translated (<strong>reduced</strong>) to it in Polynomial time. They are at least as hard as the hardest problems in NP! Interestingly, an NP-Hard problem itself doesn't even have to belong to the NP class (it doesn't have to be verifiable).</p>

    <h3>NP-Complete</h3>
    <p>The VIP intersection zone! A problem is NP-Complete if it fulfills both conditions simultaneously: <strong>(1) It is in NP, AND (2) It is NP-Hard</strong>.</p>
</div>

<h2>8.3 Reduction & Cook's Theorem</h2>
<div class="box">
    <p><strong>Polynomial Reducibility:</strong> If you can rewrite Problem A so that an algorithm for Problem B solves it mathematically in Polynomial Time, then $A \\le_P B$.</p>
    <h3>Cook's Theorem</h3>
    <p>Proved Stephen Cook (1971): The <strong>Boolean Satisfiability Problem (CNF-SAT)</strong> is mathematically the first explicitly proven NP-Complete problem. Every solitary computation problem belonging to NP can be explicitly re-written as a massive logical AND/OR Boolean formulation.</p>
</div>

<h2>8.4 Approximation Algorithms</h2>
<div class="box">
    <p>When encountering NP-Hard problems in reality, finding the exact perfect optimal solution is fundamentally impossible due to heat death of the universe math constraints. So we trade absolute exactness for massive speed! Approximation algorithms output answers that are mathematically bounded to be "close enough" to the optimum, incredibly fast (in Polynomial time).</p>
    
    <h3>Vertex Cover Approximation (2-Approximation)</h3>
    <p><strong>Problem:</strong> Find the smallest set of vertices that explicitly touch EVERY edge in a graph. Exact finding is NP-C.</p>
    <p><strong>Approximation:</strong> Pick a random edge $(u, v)$. Immediately add both vertices to your cover. Delete all edges connected to either $u$ or $v$. Repeat un-covered edge grabs until the graph is empty. This blindly crude algorithm structurally guarantees that the final cover is exactly $\\le 2 \\times$ the size of the true Optimal cover! Runs in $O(V+E)$.</p>

    <h3>Subset Sum Approximation (FPTAS)</h3>
    <p>Uses a mathematical scaling factor to trim trailing decimals off the subset possibilities tree, ensuring the combinatorial list of subsets doesn't logically explode to $2^N$. It bounds the output stringently to an error tolerance of exactly $(1 + \\epsilon)$.</p>
</div>
"""

con_8 = """
<h2>Summary: NP Completeness</h2>
<ul>
    <li><strong>Tractable:</strong> Operates efficiently. Solvable in $O(N^K)$. Class $P$.</li>
    <li><strong>Intractable:</strong> Incomputable efficiently. Requires $O(2^N)$ CPU brute-forcing.</li>
    <li><strong>NP Class:</strong> Solutions are verifiable in Polynomial time. We don't guarantee solving them fast, but checking them is instant.</li>
    <li><strong>NP-Hard vs Complete:</strong> If all NP problems reduce to $X$, $X$ is NP-Hard. If $X$ is additionally inside NP (is verifiable), $X$ upgrades instantly to NP-Complete status.</li>
    <li><strong>Cook's Theorem:</strong> CNF-SAT was proved as the original foundational bedrock NP-Complete problem.</li>
    <li><strong>Approximation:</strong> Accept failure to find exactly $100\\%$ perfect answer. Get a confirmed $90\\%$ accurate answer in 2 milliseconds instead of 5 billion years. E.g. Vertex Cover picks arbitrary edges yielding a confirmed maximum $200\\%$ error bound factor.</li>
</ul>
"""

imp_8 = """
<h2>Board & Pre-Board Important Questions</h2>

<div class="step">
    <h3>Q1. Explain in brief about the complexity classes P, NP and NP Complete. (5 Marks) [Boards]</h3>
    <p><strong>Answer:</strong></p>
    <ul>
        <li><strong>P (Polynomial):</strong> The set of all decision problems solvable by a deterministic machine in polynomial time $O(n^k)$. Considered the class of efficiently computable problems.</li>
        <li><strong>NP (Non-deterministic Polynomial):</strong> The set of problems where, if the answer is "Yes", a deterministic machine can <em>check and verify</em> the proof in polynomial time. P is a structural subset of NP ($P \\subseteq NP$).</li>
        <li><strong>NP-Complete:</strong> The set of the absolute hardest problems operating strictly inside NP. They must structurally be in NP, and all other problems in NP must mathematically reduce to them in polynomial time. If a solitary NP-complete problem is ever solved efficiently, the entire NP class formally collapses into P.</li>
    </ul>
</div>

<div class="step">
    <h3>Q2. Define Complexity classes, how to prove CNF-SAT is NP Complete? (5 Marks) [Pre-boards]</h3>
    <p><strong>Answer:</strong><br>
    Proof structure explicitly invokes <strong>Cook's Theorem</strong>. 
    <br>Step 1: Prove it is in NP. Given a boolean truth string assignment, verifying that all OR-clauses internally evaluate to True takes linear time $O(N)$.
    <br>Step 2: Prove it is NP-Hard. Cook demonstrated rigorously that the operation of <em>any non-deterministic Turing machine computation graph</em> can be mathematically rewritten exactly as a gigantic Boolean logic formula. Thus every verification problem analytically reduces exclusively to SAT processing.</p>
</div>

<div class="step">
    <h3>Q3. What types of approach is approximation? How vertex cover is solved by this approach? (1+4) [Pre-boards]</h3>
    <p><strong>Answer:</strong><br>
    <strong>Approximation Approach:</strong> Instead of seeking the absolute absolute minimum (which requires exponential recursion $O(2^N)$ for NP-hard situations), approximation trades optimization accuracy for immense polynomial calculation speed. It guarantees the solution falls within a mathematical bounded ratio $\\rho$ relative to the optimal answer.<br>
    <strong>Vertex Cover Solution:</strong> The algorithm continuously picks arbitrary remaining edges and forcibly adds BOTH endpoint vertices to the output cover set, discarding all neighbor edges. Since the optimal solution inherently MUST have meticulously picked at least one of those two endpoints to legally cover that specific edge anyway, the absolute worst-case scenario occurs when our algorithm redundantly picks two vertices when one would have flawlessly sufficed. Hence, the resulting set is strictly bounded safely <strong>within a factor of exactly 2</strong> of the optimal minimum.</p>
</div>
"""

adv_8 = """
<h2>Advanced Theoretical Extrapolations</h2>
<div class="box">
    <h3>The Millennium Prize & Crypto Collapse</h3>
    <p>The <strong>P vs NP problem</strong> is one of the seven Clay Mathematics Institute Millennium Prize problems (solving it awards $1,000,000). The general consensus is $P \\neq NP$. However, if someone theoretically proved $P = NP$, they would instantly shatter the basis of modern internet cryptography structure!</p>
    <p>RSA and AES implicitly rely on integer factorization and symmetric extraction being strictly NP operations (intractable to solve, fast to verify). If $P = NP$, an algorithm exists mathematically natively reversing SHA-256 hashes and RSA keys instantaneously in polynomial time, completely destroying all cryptocurrency and banking ledgers entirely.</p>

    <h3>Quantum Computing & NP-Completeness Bypassing</h3>
    <p>While standard computers struggle over super-polynomial exponential scaling, Quantum Computers access the <strong>BQP (Bounded-error Quantum Polynomial-time)</strong> complexity class. Using <strong>Shor's Algorithm</strong>, a quantum computer manipulates Qubit superposition phase-interference properties to factorize massive integers natively in absolute polynomial time $O((\\log N)^3)$.</p>
    <p>This explicitly means that Integer Factorization (the cornerstone anchor of RSA cryptography) is mathematically solvable efficiently by a quantum machine, moving it entirely out of the Intractable category into computational solvability! However, currently, mathematicians actively emphasize that Quantum Computers theoretically <em>cannot</em> cleanly resolve general NP-Complete problems (like Traveling Salesman), indicating that BQP represents a unique overlapping orbital ring offset distinctly from the standard P vs NP class Venn diagram geometry!</p>
</div>
"""

build_file("Unit_8_1_Detailed_Notes.html", "Unit 8 Detailed Notes", "Unit 8: NP Completeness", det_8)
build_file("Unit_8_2_Concise_Revision.html", "Unit 8 Revision Note", "Unit 8: Quick Revision", con_8)
build_file("Unit_8_3_Important_Questions.html", "Unit 8 Questions", "Unit 8: Board & Pre-board Analysis", imp_8)
build_file("Unit_8_4_Advanced_Study.html", "Unit 8 Advanced Note", "Unit 8: P vs NP & Quantum Crypto-Collapse", adv_8)
print("Unit 8 generation complete.")
