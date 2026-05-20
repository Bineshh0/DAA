import os

OUT_DIR_1 = r"c:\Users\V16\.gemini\antigravity\scratch\5th sem\DAA\Unit1_Foundation"
OUT_DIR_2 = r"c:\Users\V16\.gemini\antigravity\scratch\5th sem\DAA\Unit2_Iterative"

MM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:#0a0a0f;color:#d4d4d4;line-height:1.8;padding:20px}
.container{max-width:900px;margin:0 auto}
h1{font-size:1.8rem;background:linear-gradient(135deg,#6b9bff,#8eeaff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:5px;text-align:center}
.sub{text-align:center;color:#666;font-size:.85rem;margin-bottom:30px}
h2{color:#6b9bff;font-size:1.25rem;margin:28px 0 12px;padding:10px 16px;background:#6b9bff10;border-left:4px solid #6b9bff;border-radius:0 8px 8px 0}
h3{color:#8eeaff;font-size:1.05rem;margin:20px 0 8px}
h4{color:#aaccff;font-size:.95rem;margin:14px 0 6px}
p{margin-bottom:10px;font-size:.92rem}
ul,ol{padding-left:22px;margin-bottom:12px;font-size:.92rem}
li{margin-bottom:6px}
.def{background:#12121a;border:1px solid #1e1e30;border-radius:10px;padding:14px 18px;margin:12px 0;font-size:.9rem}
.def strong{color:#8eeaff}
.formula{background:#1a1020;border:1px solid #9b59b640;border-radius:8px;padding:10px 14px;margin:8px 0;font-family:monospace;font-size:.88rem;color:#dda0dd}
.table-wrap{overflow-x:auto;margin:12px 0}
table{width:100%;border-collapse:collapse;font-size:.85rem}
th,td{padding:10px;border:1px solid #1e1e30;text-align:left}
th{background:#1a1a2e;color:#8eeaff;font-weight:600}
tr:nth-child(even){background:#0e0e18}
.note{background:#0a1a0a;border:1px solid #6bcb7740;border-radius:8px;padding:12px;margin:10px 0;font-size:.85rem}
.note strong{color:#6bcb77}
.warn{background:#1a1a0a;border:1px solid #ffd93d40;border-radius:8px;padding:12px;margin:10px 0;font-size:.85rem}
.warn strong{color:#ffd93d}
.diagram{background:#0f0f1a;border:1px solid #4d96ff40;border-radius:10px;padding:16px;margin:14px 0;text-align:center;font-size:.85rem;color:#88aaff; white-space:pre}
code{background:#1a1a2e;padding:2px 6px;border-radius:4px;font-size:.85rem;color:#ff8888}
</style>
<script>
MathJax = {
  tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] }
};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{TITLE}}</title>
""" + MM_CSS + """
</head>
<body>
    <div class="container">
        <h1>📘 {{H1}}</h1>
        <p class="sub">Detailed Notes — CSC 314 Design and Analysis of Algorithms | Exam Orientated</p>
        {{CONTENT}}
    </div>
</body>
</html>"""

def build_file(directory, filename, title, h1, content):
    html = HTML_TEMPLATE.replace("{{TITLE}}", title).replace("{{H1}}", h1).replace("{{CONTENT}}", content)
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as f:
        f.write(html)

det_1 = r"""
<!-- INTRODUCTION -->
<h2>1.1 Introduction to Algorithm Analysis</h2>

<div class="def">
    <strong>Algorithm</strong>: Derived from 9th-century mathematician Al-Khwarizmi. It is a strictly finite set of well-defined rules/instructions for solving a specific computational problem.<br>
    The study of <em>Algorithm Analysis</em> is evaluating the performance metrics (Time complexity and Space complexity) of these instructions before compiling code to determine overall viability.
</div>

<h3>Five Properties of an Algorithm</h3>
<p>For an instruction set to be formally considered a computational "Algorithm", it must possess:</p>
<ol>
    <li><strong>Finiteness:</strong> The algorithm must absolutely terminate after a finite number of steps. It cannot be an infinite looping structure.</li>
    <li><strong>Definiteness:</strong> Each step must be precisely defined. Actions specified must be rigorously unambiguous (no "flip a coin" or "maybe execute X").</li>
    <li><strong>Possesses Inputs:</strong> An algorithm receives zero or more quantities externally supplied prior to execution.</li>
    <li><strong>Possesses Outputs:</strong> An algorithm produces at least one computed quantity that has a structural relation to the inputs.</li>
    <li><strong>Effectiveness:</strong> All operations must be sufficiently basic such that a person could theoretically trace it exactingly with pen and paper in finite time.</li>
</ol>

<div class="warn">
    <strong>⚠️ Critical Exam Detail:</strong> Algorithms and "Programs" are not identical! A server operating system is a <em>program</em> but not an algorithm, because an OS deliberately runs endlessly without Finiteness (terminating).
</div>

<!-- RAM MODEL -->
<h2>1.2 Random Access Machine (RAM) Model</h2>

<p>The <strong>RAM Model</strong> is the foundational abstract theoretical machine utilized by computer scientists to analyze mathematical algorithm complexity devoid of specific hardware constraints.</p>

<div class="table-wrap">
    <table>
        <tr><th>RAM Model Assumption</th><th>Description</th></tr>
        <tr><td><strong>Single Processor</strong></td><td>Instructions execute sequentially, one after another, lacking parallel threads.</td></tr>
        <tr><td><strong>Infinite Memory</strong></td><td>Assumes memory banks are infinitely large, nullifying OutOfMemory exceptions.</td></tr>
        <tr><td><strong>Constant Execution Cost</strong></td><td>Basic arithmetic (+, -, *, /) and logic operations take exactly $O(1)$ constant time step.</td></tr>
        <tr><td><strong>Constant Memory Cost</strong></td><td>Fetching data from memory cell $0$ costs the exact same $1$ unit of time as fetching from cell $9,999,999$.</td></tr>
        <tr><td><strong>No Memory Hierarchy</strong></td><td>Blindly ignores the real-life existence of L1/L2 Caches and physical Page Faults.</td></tr>
    </table>
</div>

<!-- ASYMPTOTIC NOTATIONS -->
<h2>1.3 Asymptotic Notations ⭐ (VERY IMPORTANT)</h2>

<p>Asymptotic notations are formal mathematical tools utilizing functions to describe how the runtime of an algorithm fundamentally scales as input size $N$ skyrockets towards infinity. These bounding behaviors are crucial for establishing performance guarantees.</p>

<h3>1. Big-Oh ($O$) — Strict Upper Bound (Worst Case)</h3>
<div class="def">
    <strong>Definition:</strong> Describes the maximum possible execution bounds. The function $f(n)$ will never exceed the growth rate of $g(n)$ past a specific boundary $n_0$.
</div>
<div class="formula">
    $O(g(n)) = \{f(n) : \exists c > 0, n_0 > 0 \text{ such that } 0 \le f(n) \le c \cdot g(n) \text{ for all } n \ge n_0\}$
</div>
<ul>
    <li>Proves that an algorithm's worst case is "at most" $g(n)$.</li>
    <li><em>Example:</em> For $f(n) = 3n^2 + 5n$, we select $g(n) = n^2$. By setting $c = 8$ and $n_0 = 1$, we prove $3n^2 + 5n \le 8n^2$. Thus, $f(n) \in O(n^2)$.</li>
    <li>Graphically, the curve of $c \cdot g(n)$ permanently covers and stays above the curve of $f(n)$.</li>
</ul>

<h3>2. Big-Omega ($\Omega$) — Strict Lower Bound (Best Case)</h3>
<div class="def">
    <strong>Definition:</strong> Establishes the absolute guaranteed minimum growth rate constraint.
</div>
<div class="formula">
    $\Omega(g(n)) = \{f(n) : \exists c > 0, n_0 > 0 \text{ such that } 0 \le c \cdot g(n) \le f(n) \text{ for all } n \ge n_0\}$
</div>
<ul>
    <li>Proves an algorithm is fundamentally "at least" $g(n)$ slow.</li>
    <li>Graphically, the curve of $c \cdot g(n)$ permanently stays completely below $f(n)$.</li>
</ul>

<h3>3. Big-Theta ($\Theta$) — Exact Tight Bound (Average Case)</h3>
<div class="def">
    <strong>Definition:</strong> Represents the precise tight convergence where $f(n)$ is identically proportional to $g(n)$, acting concurrently as both the upper limit and the lower limit.
</div>
<div class="formula">
    $\Theta(g(n)) = \{f(n) : \exists c_1, c_2 > 0, n_0 > 0 \text{ such that } 0 \le c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \text{ for all } n \ge n_0\}$
</div>
<ul>
    <li>This is the most highly-valued notation because it is the most informative. If an algorithm is $\Theta(N^2)$, you absolutely know exactly how it behaves in all standardized vectors.</li>
</ul>

<h3>4. Little-oh ($o$) & Little-omega ($\omega$)</h3>
<p>Unlike Big-Oh and Big-Omega which allow for $f(n)$ to be exactly equal ($=$) to $g(n)$, the "Little" notations demand <strong>strict inequality</strong> mapping.</p>
<ul>
    <li><strong>Little-oh ($o$):</strong> Strictly upper bounds ($<$). The limit as $n \to \infty$ of $f(n)/g(n)$ must mathematically evaluate exactly to 0. (e.g. $2n \in o(n^2)$ is true, but $2n^2 \in o(n^2)$ is false).</li>
    <li><strong>Little-omega ($\omega$):</strong> Strictly lower bounds ($>$). Limit of $f(n)/g(n)$ evaluates to infinity.</li>
</ul>


<!-- SOLVING RECURRENCES -->
<h2>1.4 Solving Recurrences</h2>
<p>When an algorithm leverages "Divide & Conquer" recursion, tracing absolute iteration complexity requires solving algebraic recurrence equations. Let the complexity be formulated as: <code>T(n) = a*T(n/b) + f(n)</code></p>

<h3>Method 1: Master Theorem</h3>
<p>A formulaic shortcut for solving perfectly balanced geometric recurrences. <br>
Let $a \ge 1$ (branches spawned), $b > 1$ (shrink ratio of branch size), and $f(n)$ be the cost of partition/merging at that level.</p>

<div class="note">
    <strong>Core Mechanic:</strong> You must calculate polynomial $n^{\log_b a}$ and directly compare its weight against the $f(n)$ merging cost!
</div>

<ol>
    <li><strong>Case 1 (Heavy Leaves):</strong> If the branching complexity exponentially dwarfs the combining complexity. Mathematically: $f(n) = O(n^{\log_b a - \epsilon})$. <br>
        <strong>Solution:</strong> $T(n) = \Theta(n^{\log_b a})$.</li>
    <li><strong>Case 2 (Perfect Balance):</strong> If the merging cost perfectly matches the branching scaling exactly. Mathematically: $f(n) = \Theta(n^{\log_b a})$.<br>
        <strong>Solution:</strong> $T(n) = \Theta(n^{\log_b a} \cdot \log n)$.</li>
    <li><strong>Case 3 (Heavy Root):</strong> If the merging step $f(n)$ requires drastically more computational effort than the leaf branching. Mathematically: $f(n) = \Omega(n^{\log_b a + \epsilon})$.<br>
        <strong>Solution:</strong> $T(n) = \Theta(f(n))$.</li>
</ol>


<h3>Method 2: Recursion Tree</h3>
<p>Applied when Master Theorem fails (e.g. unequal sub-branches like $T(n) = T(n/3) + T(2n/3) + n$).</p>
<div class="diagram">
                 f(n)                           => Level Cost: f(n)
               /       \
      T(n/2)              T(n/2)                => Level Cost: f(n/2) + f(n/2)
      /   \               /    \
T(n/4)  T(n/4)       T(n/4)  T(n/4)             => Level Cost: 4 * f(n/4)
</div>
<p><strong>Steps:</strong> Draw tree hierarchy, evaluate the sequential cost across each horizontal level, and compute the total geometric sum mathematically to isolate the upper bounds.</p>
"""

build_file(OUT_DIR_1, "Unit_1_1_Detailed_Notes.html", "Unit 1 Detailed Notes", "Unit 1: Foundation of Algorithm Analysis", det_1)

# Now Unit 1 Important Questions
imp_1 = r"""
<!-- IMPORTANT QUESTIONS -->
<h2>Unit 1 Board & Pre-board Analysis</h2>

<div class="warn">
    <strong>⚠️ Analytical Insight:</strong> This chapter exclusively guarantees questions strictly revolving around defining the 3 Asymptotic Notations natively and mathematically resolving Recurrence Relations using the Master Method. Prepare accordingly.
</div>

<div class="step">
    <h3>Q1. Why do you need algorithm analysis? Discuss about RAM model. Also discuss about Big Oh, Big Omega and Big theta with corresponding examples. (2+3+5 = 10 Marks) [Boards]</h3>
    <br>
    <strong>Requirement 1: Need for Analysis</strong>
    <ul>
        <li><strong>Predictability:</strong> We analyze algorithms to precisely estimate runtime bounds independent of varying hardware logic, shielding deployments from critical infinite execution.</li>
        <li><strong>Resource Engineering:</strong> Evaluates optimization vectors (Space-Time tradeoff limits).</li>
    </ul>
    
    <strong>Requirement 2: RAM Model Framework</strong>
    <p>The "Random Access Machine" is the generalized math construct utilized to normalize comparisons. It dictates that every basic execution (add, sub, allocate) takes identically $1$ uniform time step $O(1)$. Simultaneously, it mandates infinite memory lacking cache boundaries, thus discarding real-world L1/L2 Cache latency variables from pure algorithmic evaluation.</p>
    
    <strong>Requirement 3: Asymptotic Definitions</strong>
    <p>See Detailed Notes for formal definitions equations. For examples:</p>
    <ul>
        <li><strong>Big-Oh ($O$):</strong> Upper bound constraint limit. Consider $7n^2 + 20$. Pick bounding $g(n) = n^2$. For $c=8, n_0=20$, $7n^2 + 20 \le 8n^2$. Therefore it is absolutely $O(n^2)$.</li>
        <li><strong>Big-Omega ($\Omega$):</strong> Lower bound structure. If $T(N)$ is best case, $7n^2 + 20 \ge 7n^2$ for all positive $n$, thus $\Omega(n^2)$.</li>
        <li><strong>Big-Theta ($\Theta$):</strong> Tight lock convergence. Since it scales identically constrained between $7n^2$ and $8n^2$, the complexity formally locks at $\Theta(n^2)$.</li>
    </ul>
</div>

<div class="step">
    <h3>Q2. State and solve by Master method: T(n) = 7T(n/2) + n² (5 Marks) [Pre-board 2023]</h3>
    <p>Using the standard Master Theorem format: $T(n) = aT(n/b) + f(n)$</p>
    <p>Here mathematically extracted values are: $a = 7$, $b = 2$, and $f(n) = n^2$.</p>
    <p><strong>Step 1: Compute Branch Weight Limit</strong></p>
    <div class="formula">
        $n^{\log_b a} = n^{\log_2 7} \approx n^{2.807}$
    </div>
    <p><strong>Step 2: Comparison Execution</strong></p>
    <p>We directly compare $f(n) = n^2$ against the weight $n^{2.807}$. Since $n^2$ is asymptotically far smaller than $n^{2.807}$, this explicitly falls under <strong>Case 1 (Heavy Leaves Scenario)</strong>. The cost of generating branches exponentially overwhelms the $O(n^2)$ effort to merge them.</p>
    <p><strong>Step 3: Resolution</strong></p>
    <p>Under Case 1, $f(n) = O(n^{\log_b a - \epsilon})$. The boundary complexity is natively dictated by the leaf nodes.</p>
    <div class="answer">Final Answer: $T(n) = \Theta(n^{\log_2 7})$</div>
</div>

<div class="step">
    <h3>Q3. Solve by Master Method: T(n) = 3T(n/2) + n AND T(n) = 2T(n/4) + √n (2.5 + 2.5) [Boards]</h3>
    <p><strong>Equation A Resolution: $T(n) = 3T(n/2) + n$</strong></p>
    <ul>
        <li>$a=3, b=2, f(n)=n^1$</li>
        <li>Calculate scalar weight: $n^{\log_2 3} \approx n^{1.58}$</li>
        <li>Compare $n^1$ vs $n^{1.58}$. The scalar $n^{1.58}$ dominates. This is exclusively <strong>Case 1</strong>.</li>
        <li><span style="color:#6bcb77; font-weight:bold;">Result: $\Theta(n^{\log_2 3})$</span></li>
    </ul>

    <p><strong>Equation B Resolution: $T(n) = 2T(n/4) + \sqrt{n}$</strong></p>
    <ul>
        <li>$a=2, b=4, f(n)=n^{0.5}$</li>
        <li>Calculate scalar weight: $n^{\log_4 2} = n^{0.5}$ (Since $4^{0.5} = 2$)</li>
        <li>Compare $n^{0.5}$ vs $n^{0.5}$. The scales are <strong>identically matched!</strong> Result falls squarely into <strong>Case 2 (Perfect Balance)</strong>.</li>
        <li>Under Case 2, we multiply the boundary directly by a logarithmic scaling dimension $\log n$.</li>
        <li><span style="color:#6bcb77; font-weight:bold;">Result: $\Theta(\sqrt{n} \log n)$</span></li>
    </ul>
</div>

<div class="step">
    <h3>Q4. Solve by Recursion tree: T(n) = 3T(n/4) + Θ(n²) (5 Marks) [Pre-board 2023]</h3>
    <p><strong>Trace Logistics:</strong></p>
    <p>We build a theoretical mathematical tree mapping all operation costs.</p>
    <ul>
        <li>Level 0 Root Cost: $n^2$</li>
        <li>Level 1 splits into exactly 3 sub-nodes, each inheriting sub-problem dimension $(n/4)$. Cost per node: $(n/4)^2 = n^2/16$. Total Level 1 aggregate cost: $3 \times (n^2/16) = \frac{3}{16}n^2$.</li>
        <li>Level 2 splits into 9 sub-nodes. Dimension $(n/16)$. Cost per node: $(n/16)^2 = n^2/256$. Total Level 2 aggregate cost: $9 \times (n^2/256) = \frac{9}{256}n^2 = (\frac{3}{16})^2 n^2$.</li>
    </ul>
    <p><strong>Geometric Formulation:</strong></p>
    <p>The total time function creates an infinite summation series:<br>
    $T(n) = n^2 + \frac{3}{16}n^2 + (\frac{3}{16})^2n^2 + \dots$<br>
    $T(n) = n^2 \sum_{i=0}^{\log_4 n} (\frac{3}{16})^i$</p>
    <p>Because the geometric internal ratio $(3/16)$ is strictly less than 1, the series intrinsically converges upon an absolute bounded constant multiplier.</p>
    <div class="answer">Final Verification: $T(n) = \Theta(n^2)$</div>
</div>
"""
build_file(OUT_DIR_1, "Unit_1_3_Important_Questions.html", "Unit 1 Questions", "Unit 1: Board Exam Past Papers", imp_1)


det_2 = r"""
<!-- INTRODUCTION -->
<h2>2.1 Iterative Foundational Algorithms</h2>

<div class="def">
    <strong>Iterative Approach:</strong> Algorithms that utilize structural loops (`while`, `for`) to repeat execution blocks modifying state variables until constraints are fulfilled, effectively circumventing Call Stack limits experienced during native recursion.
</div>

<h3>1. GCD (Greatest Common Divisor) - Iterative Euclid</h3>
<p>The native iterative Euclidean algorithm operates efficiently by acknowledging that $GCD(a, b) = GCD(b, a \text{ mod } b)$. It iteratively shrinks variables devoid of recursive nesting limits.</p>
<pre>
FUNCTION iterative_euclid_gcd(A, B):
    while B != 0:
        remainder = A mod B
        A = B
        B = remainder
    return A
</pre>
<p><strong>Analytical Complexity:</strong> The modulo operator guarantees that variable sizes severely drop by over half natively within two iteration boundaries. Time Complexity mathematically evaluates exactly to $O(\log(\min(A,B)))$ utilizing <strong>only $O(1)$ constant physical space</strong>!</p>

<h3>2. Iterative Fibonacci Generator</h3>
<p>Standard recursive Fibonacci requires an intractable $O(2^n)$ computing time, making sequence extraction functionally impossible past $n=45$. Iterative generation directly resolves overlapping constraints entirely.</p>
<pre>
FUNCTION iterative_fib(N):
    if N <= 1: return N
    array F = size(N+1)
    F[0] = 0
    F[1] = 1
    for i = 2 to N:
        F[i] = F[i-1] + F[i-2]
    return F[N]
</pre>
<p><strong>Analytical Complexity:</strong> Loop executes specifically $N-1$ linear cycles resulting in strictly $O(N)$ polynomial duration execution utilizing explicitly $O(N)$ contiguous array memory structures.</p>

<!-- SEARCHING -->
<h2>2.2 Searching Methodologies (Sequential Search)</h2>

<div class="box">
    <p><strong>Linear / Sequential Search:</strong> Iteratively traverses entirely across the memory array boundary evaluating absolute positional variables until target is located.</p>
    <ul>
        <li><strong>Best Case Time: $\Omega(1)$</strong> (The target integer instantly manifests physically at array index $0$).</li>
        <li><strong>Worst Case Time: $O(N)$</strong> (Target completely absent or resides identically at absolute final index position $N-1$).</li>
        <li><strong>Average Case Time: $\Theta(N)$</strong> (On average, uniformly random distributions result in targeting $N/2$ position. Dropping mathematical fraction constants scales to exactly $N$).</li>
    </ul>
    <p><em>Distinct Advantage:</em> Completely independent of element structure. Unlike Binary Search spanning $O(\log N)$ limit constraints requiring meticulously pre-sorted arrays, sequential search parses unsorted volatile vectors natively.</p>
</div>

<!-- SORTING -->
<h2>2.3 Primary Sorting Protocols</h2>

<h3>A. Bubble Sort</h3>
<p>Structurally cascades the maximal integer values to the final memory bounds iteratively via exhaustive adjacent pair-wise comparisons.</p>
<div class="formula">
    Swaps $a[j]$ and $a[j+1]$ natively whenever $a[j] > a[j+1]$. Inner boundary strictly dynamically restricts to $N-i-1$.
</div>
<ul>
    <li><strong>Worst/Average Time:</strong> $O(N^2)$.</li>
    <li><strong>Space Complexity:</strong> $O(1)$ Constant (In-place sorting architecture).</li>
</ul>

<h3>B. Selection Sort</h3>
<p>Executes global minimum scans. Physically searches the complete array boundary specifically resolving the singular absolute internal minimum integer, subsequently swapping that integer explicitly into sequential sorted index $i$.</p>
<ul>
    <li><strong>All Cases Time Constraint:</strong> Exactly $\Theta(N^2)$ perpetually! Regardless of optimal sorted arrays, it structurally mandates exhaustive $N^2$ scans asserting minimum validation.</li>
    <li><strong>Space Complexity:</strong> $O(1)$.</li>
    <li><em>Note:</em> Requires the absolute mathematical lowest metric of data swaps natively possible ($O(N)$ swaps bounded maximum).</li>
</ul>

<h3>C. Insertion Sort ⭐</h3>
<p>Executes identical mechanism logic to human card players sorting their physical playing hand sequentially. Systematically iterates target integers natively extracting them from sequence and tracing linearly backwards displacing all sorted elements until exact scalar convergence location is discovered.</p>
<pre>
FUNCTION insertion_sort(A):
    for j = 1 to length(A) - 1:
        key = A[j]
        i = j - 1
        while i >= 0 AND A[i] > key:    // Trace Backwards limit
            A[i+1] = A[i]               // Execute Right Shift overwrite
            i = i - 1
        A[i+1] = key                    // Deposit Target into location
</pre>
<ul>
    <li><strong>Superlative Best Case:</strong> $\Omega(N)$ (If pre-sorted array, `while` condition instantly terminates, inner-loop breaks entirely, resolving precisely into strict $N$ execution sequences).</li>
    <li><strong>Worst Case Time:</strong> $O(N^2)$ (Reverse structured data input causes total loop compounding. $(N \times (N-1)) / 2$ evaluates asymptotically to native squared polynomial).</li>
</ul>
"""

build_file(OUT_DIR_2, "Unit_2_1_Detailed_Notes.html", "Unit 2 Detailed Notes", "Unit 2: Iterative Algorithms", det_2)

imp_2 = r"""
<!-- IMPORTANT QUESTIONS -->
<h2>Unit 2 Board & Pre-board Analysis</h2>

<div class="warn">
    <strong>⚠️ Analytical Insight:</strong> The majority of structural board questions from Iterative Algorithms strictly revolve around explicitly defining the Insertion Sort algorithm and dissecting its operational boundaries. Selection/Bubble is almost completely ignored!
</div>

<div class="step">
    <h3>Q1. Write the algorithm for insertion sort and explain its time complexity. (5 Marks) [Boards]</h3>
    <br>
    <strong>Requirement 1: Algorithm Code</strong>
<pre>
INSERTION-SORT(Array A)
    for j = 1 to A.length - 1
        key = A[j]
        i = j - 1
        
        // Scan backward through sorted partition
        while i >= 0 and A[i] > key
            A[i + 1] = A[i]    // Shift elements right
            i = i - 1
            
        A[i + 1] = key         // Insert explicitly into correct tier
</pre>

    <strong>Requirement 2: Complexity Analysis Derivation</strong>
    <p>To acquire maximum marks, you absolutely MUST break the structural complexity bounds individually demonstrating algorithm adaptability.</p>
    <ul>
        <li><strong>Best Case Mathematical Analysis [$\Omega(N)$]</strong><br>
        If the memory input vector is fully pre-sorted sequentially $[1, 2, 3, 4, 5]$, the fundamental evaluating while condition `A[i] > key` functionally evaluates to `False` entirely on the absolute first check every external iteration. No internal rightwards shifting executes physically. The secondary internal nested while-loop aborts instantly. Consequently, the external algorithm traverses natively precisely $N-1$ basic linear increments. Final theoretical constraint maps exactly to polynomial magnitude $\Omega(N)$.</li>
        
        <li><strong>Worst Case Mathematical Analysis [$O(N^2)$]</strong><br>
        If the sequence structure vectors completely reverse $[9, 8, 7, 6, 5]$, when evaluating index $j$, the internal mechanism traces recursively fundamentally backwards completely evaluating and physically overwriting every singular element located spanning interval sequence $0$ to $j-1$. The absolute cumulative summation evaluates directly to structural form $1 + 2 + 3 + \dots + N-1$. Using Arithmetic sequence geometric mathematics, $Sum = N(N-1)/2$. Discarding static integers, we isolate structural limit $O(N^2)$.</li>
        
        <li><strong>Space Constraint Properties [$O(1)$]</strong><br>
        Because memory overrides operate structurally strictly internally displacing index assignments in-place without generating cloned arrays explicitly, it completely functions natively inside $1$ constant allocation boundary. Space requirement resolves strictly to optimal scaling limit $O(1)$.</li>
    </ul>
</div>
"""
build_file(OUT_DIR_2, "Unit_2_3_Important_Questions.html", "Unit 2 Questions", "Unit 2: Board Exam Past Papers", imp_2)

print("Generated exactly following MM constraints. Task complete.")
