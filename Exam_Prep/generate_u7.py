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

det_7 = """
<h2>7.1 Euclid's and Extended Euclid Algorithms</h2>
<div class="box">
    <h3>Euclid's GCD</h3>
    <p>Finds the Greatest Common Divisor of two numbers $a$ and $b$. Recursively uses the property: $\\gcd(a, b) = \\gcd(b, a \\pmod b)$. Base case is $b = 0$.</p>

    <h3>Extended Euclidean Algorithm</h3>
    <p>Not only finds $d = \\gcd(a,b)$, but also finds coefficients $x$ and $y$ such that $a \\cdot x + b \\cdot y = d$. Formally known as Bezout's Identity. It is heavily used in cryptography strictly to find the Modulo Multiplicative Inverse $d$ of RSA keys.</p>
</div>

<h2>7.2 Solving Modular Linear Equations</h2>
<div class="box">
    <p>Equation format: $aX \\equiv b \\pmod n$.</p>
    <p><strong>Solution Existence:</strong> The equation only has a valid integer solution if $b$ is perfectly divisible by $d$, where $d = \\gcd(a, n)$. If it exists, there will be exactly $d$ distinct modular solutions.</p>
    <p><strong>Method:</strong></p>
    <ol>
        <li>Find $d = \\gcd(a, n)$ using Extended Euclid. Also gives coefficients $x'$ and $y'$ such that $a \\cdot x' + n \\cdot y' = d$.</li>
        <li>Initial base solution: $x_0 = x' \cdot (b/d) \\pmod n$.</li>
        <li>The full sequence of $d$ modular solutions are generated using: $x_i = (x_0 + i \\cdot (n/d)) \\pmod n$ for $i = 0, 1 \\dots d-1$.</li>
    </ol>

    <h3>Chinese Remainder Theorem (CRT)</h3>
    <p>Solves systems of simultaneous congruences. <br>
    $x \\equiv a_1 \\pmod{m_1}$<br>
    $x \\equiv a_2 \\pmod{m_2}$<br>
    ...<br>
    Condition: The moduli $m_1, m_2...$ MUST be pairwise coprime.</p>

    <h3>Primality Testing</h3>
    <p><strong>Miller-Rabin Randomized Test:</strong> Instead of checking division up to $\\sqrt{N}$ ($O(N^{0.5})$), it uses modular exponentiation properties related to Fermat's Little Theorem. As a randomized algorithm, it tests a random base $A$. If it returns "composite", $N$ is 100% composite. If it returns "prime", $N$ is probably prime. By running the test $k$ times independently, the error probability shrinks exponentially to $4^{-k}$. This enables analyzing $2048$-bit RSA keys in mere milliseconds.</p>
</div>
"""

con_7 = """
<h2>Summary: Number Theoretic Algorithms</h2>
<ul>
    <li><strong>Euclidean Algorithm:</strong> Time $O(\\log(\\min(A,B)))$. Divides larger by smaller repeatedly substituting remainder.</li>
    <li><strong>Extended Euclidean:</strong> Returns $(d, x, y)$ resolving $ax + by = d$. Useful for modular inverse resolving.</li>
    <li><strong>Modular Linear Eq ($aX \\equiv b \\pmod n$):</strong> Solvable strictly if $\\gcd(a, n)$ divides $b$. Total solutions = $\\gcd(a,n)$. Employs Extended Euclidean $x$ variable.</li>
    <li><strong>Chinese Remainder Theorem:</strong> Solves independent remainder equations. Total Modulus $M = m_1 \\cdot m_2 \\cdot \\dots$. To solve each segment computationally calculate Inverse $M_i$.</li>
    <li><strong>Miller-Rabin Primality:</strong> Probabilistic Monte Carlo algorithm. Operates exponentially faster than Trial Division. Error rate drops drastically over $K$ repeated iteration cycles. Forms backbone foundation of RSA protocol cryptography security.</li>
</ul>
"""

imp_7 = """
<h2>Board & Pre-Board Important Questions</h2>

<div class="step">
    <h3>Q1. Write and trace recursive Extended Euclidean algorithm. (2+3) [Pre-board 2024]</h3>
    <p><strong>Algorithm:</strong></p>
<pre>
EXTENDED-GCD(a, b)
    if b == 0
        return (a, 1, 0)
    (d, x', y') = EXTENDED-GCD(b, a % b)
    return (d, y', x' - floor(a/b) * y')
</pre>
</div>

<div class="step">
    <h3>Q2. Solve using CRT: $x \\equiv 2 \\pmod 3, x \\equiv 4 \\pmod 5, x \\equiv 5 \\pmod 7$ (5 Marks) [Pre-board 2023]</h3>
    <p><strong>Answer Trace:</strong><br>
    Given: $a_1=2, a_2=4, a_3=5$. Moduli: $m_1=3, m_2=5, m_3=7$.<br>
    Check coprimes: GCD is 1 for all pairs. Valid.<br>
    Calculate $M = 3 \\times 5 \\times 7 = 105$.<br>
    $M_1 = 105/3 = 35$. $M_2 = 105/5 = 21$. $M_3 = 105/7 = 15$.<br>
    Mod Inverses:<br>
    $y_1 = 35^{-1} \\pmod 3 \\Rightarrow 2y_1 \\equiv 1 \\pmod 3 \\Rightarrow y_1 = 2$.<br>
    $y_2 = 21^{-1} \\pmod 5 \\Rightarrow 1y_2 \\equiv 1 \\pmod 5 \\Rightarrow y_2 = 1$.<br>
    $y_3 = 15^{-1} \\pmod 7 \\Rightarrow 1y_3 \\equiv 1 \\pmod 7 \\Rightarrow y_3 = 1$.<br>
    Formula: $X = (a_1 M_1 y_1 + a_2 M_2 y_2 + a_3 M_3 y_3) \\pmod M$<br>
    $X = (2 \\cdot 35 \\cdot 2) + (4 \\cdot 21 \\cdot 1) + (5 \\cdot 15 \\cdot 1)$<br>
    $X = 140 + 84 + 75 = 299$<br>
    $299 \\pmod{105} = 89$.<br>
    <span class="answer">Final Solution: $\\mathbf{X = 89}$</span>
    </p>
</div>

<div class="step">
    <h3>Q3. Explain Euclid's method to solve modular linear equations with an example. (5) [Boards]</h3>
    <p><strong>Explanation:</strong> Resolving $aX \\equiv b \\pmod n$. Utilize the Extended-Euclidean function to extract $d=\\gcd(a,n)$ and coefficient variable $x'$. Confirm divisibility ($b \\pmod d == 0$). Define initial variable $x_0 = x' \\times (b/d) \\pmod n$. The array of legitimate answers maps out across adding $+ (n/d)$ iteratively.</p>
</div>
"""

adv_7 = """
<h2>Advanced Theoretical Analysis: AKS Primality & Crypto</h2>
<div class="box">
    <h3>Why is Miller-Rabin Probability Acceptable?</h3>
    <p>If you generate a prime number for securing billions of dollars in a banking database using RSA, relying on a "probability" test seems dangerous. What if Miller-Rabin mistakenly flags a composite number as Prime (a false-positive) and the Bank's encryption key is structurally broken?</p>
    <p>If the test is run 40 times natively ($k=40$), the probability of a false-positive is $4^{-40}$, which is approximately $\\approx 8.27 \\times 10^{-25}$. The chance of a stray cosmic ray flipping a memory transistor in the bank's CPU and corrupting the key physically is mathematically trillions of times higher than Miller-Rabin failing. Therefore, probabilistic testing is considered effectively absolute truth in the encryption industry.</p>

    <h3>The AKS Primality Breakthrough (2002)</h3>
    <p>For decades, Computer Science struggled to find a deterministic absolute proof test faster than Trial Division. Up until 2002, we relied solely on probabilistic tests (Miller-Rabin). Then three Indian researchers (Agrawal, Kayal, Saxena) dropped a bombshell paper proving definitively that <strong>"PRIMES is in P"</strong>!</p>
    <p>The <strong>AKS Primality Test</strong> was the first algorithm to calculate deterministic prime identity entirely theoretically in unconditional polynomial time $O(\\log^{12} N)$. While a historic computational breakthrough proving non-probabilistic P-class evaluation, the heavy math polynomials render it ironically <em>slower</em> than Miller-Rabin practically. But mathematically, its invention revolutionized understanding Polynomial Complexity Class boundaries!</p>
</div>
"""

build_file("Unit_7_1_Detailed_Notes.html", "Unit 7 Detailed Notes", "Unit 7: Number Theoretic Algorithms", det_7)
build_file("Unit_7_2_Concise_Revision.html", "Unit 7 Revision Note", "Unit 7: Quick Revision", con_7)
build_file("Unit_7_3_Important_Questions.html", "Unit 7 Questions", "Unit 7: Board & Pre-board Analysis", imp_7)
build_file("Unit_7_4_Advanced_Study.html", "Unit 7 Advanced Note", "Unit 7: P-Class Boundaries & Crypto Maths", adv_7)
print("Unit 7 generation complete.")
