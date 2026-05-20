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
        
det_4 = """
<h2>4.1 Elements of Greedy Strategy</h2>
<div class="box">
    <p>A greedy algorithm makes the local optimal choice at every step with the hope that these local optimal choices will lead to a globally optimal solution. It never reconsiders previous choices (no backtracking).</p>
    <ul>
        <li><strong>Greedy Choice Property:</strong> A global optimum can be logically built by making a series of local optimum choices.</li>
        <li><strong>Optimal Substructure:</strong> An optimal solution to the problem contains optimal solutions to its sub-problems.</li>
    </ul>
</div>

<h2>4.2 Classic Greedy Algorithms</h2>
<div class="box">
    <h3>Fractional Knapsack</h3>
    <p>We can take fractions of items. Strategy: Sort items descending by value-to-weight ratio (Value/Weight). Take as much of the highest ratio item as possible until the capacity is full.</p>
    <p><strong>Complexity:</strong> $O(N \\log N)$ strictly due to the prerequisite sorting.</p>

    <h3>Job Sequencing with Deadlines</h3>
    <p>Given $N$ jobs, each with a deadline and a profit (earned if completed before deadline), schedule them to maximize profit.</p>
    <p><strong>Strategy:</strong> Sort jobs descending by profit. Track the days available using boolean slots. Always assign the job to the latest completely possible empty slot on or before its deadline.</p>

    <h3>Prim's Algorithm (Minimum Spanning Tree)</h3>
    <p>Starts from an arbitrary starting vertex. Keeps tracking the minimum weight edge that connects an unvisited vertex to the already visited MST set. Grabs the cheapest edge iteratively.</p>
    <p><strong>Complexity:</strong> $O(E \\log V)$ using a Min Priority Queue (Binary Heap).</p>

    <h3>Kruskal's Algorithm (Minimum Spanning Tree)</h3>
    <p>Considers Edges rather than vertices. Sorts all edges by strict ascending weight. Iteratively adds edges to the spanning forest as long as they don't form a Cycle.</p>
    <p><strong>Complexity:</strong> $O(E \\log E)$ due to sorting the edges, and requires a Disjoint-Set (Union-Find) data structure to verify cycles.</p>

    <h3>Dijkstra's Shortest Path Algorithm</h3>
    <p>Finds shortest paths from a single source vertex to all other vertices. Continually relaxes outward edges from the currently closest unvisited node.</p>
    <p><strong>Complexity:</strong> $O((V+E) \\log V)$ utilizing a Min-Heap. Extremely similar to Prim's, but it computes the *cumulative* distance from the source instead of just the edge weight itself.</p>
</div>

<h2>4.3 Huffman Coding (Prefix Codes)</h2>
<div class="box">
    <p>An optimal prefix-free binary encoding for data compression. Frequencies of characters determine their bit length (frequent characters get short paths, rare characters get long paths).</p>
    <p>No code is a prefix of another (e.g. if '0' is `'a'`, no other code can start with '0').</p>
    
    <p><strong>Algorithm:</strong></p>
    <ul>
        <li>Sort characters as leaf nodes in a Min-Priority Queue by their occurrence frequency.</li>
        <li>Extract the two lowest frequencies, merge them under a parent node with a combined frequency, and re-insert the parent back in.</li>
        <li>Repeat until $1$ tree remains. Left branch paths = 0, Right branch paths = 1.</li>
    </ul>
    <p><strong>Complexity:</strong> $O(N \\log N)$ to construct the tree.</p>
</div>
"""

con_4 = """
<h2>Summary: Greedy Algorithms</h2>
<ul>
    <li><strong>Concept:</strong> "Take what looks best exactly right now". Does not look at the entirety of future consequences. Fast, but doesn't always guarantee global best unless specific properties are met.</li>
    <li><strong>Fractional vs 0/1 Knapsack:</strong> Greedy works <em>only</em> on Fractional. 0/1 Knapsack requires Dynamic Programming because you can't split fractions, meaning a currently logical greedy choice might trap you into wasting 90% of total knapsack capacity later.</li>
    <li><strong>Job Sequencing:</strong> Sort by profit. Assign to the latest possible free slot from Deadline down to 0. Time: $O(N^2)$ worst case without Disjoint sets.</li>
    <li><strong>Kruskal's MST:</strong> Sort edges ascending. Keep adding if no cycle forms. Relies on Union-Find algorithm. Best for Sparse Graphs. Time $O(E \\log E)$.</li>
    <li><strong>Prim's MST:</strong> Grows out from a source vertex like a network infection capturing the nearest cheapest unvisited node. Resolves exactly like Dijkstra. Best for Dense Graphs. Time $O(E \\log V)$.</li>
    <li><strong>Dijkstra's Algo:</strong> Source shortest path. Cannot handle negative weights. $O((E+V)\\log V)$. Relaxes edge $(u,v)$ if $dist[v] > dist[u] + weight(u,v)$.</li>
    <li><strong>Huffman Coding:</strong> Lossless data compression. Combines lowest frequency leaves repetitively to build a bottom-up binary tree.</li>
</ul>
"""

imp_4 = """
<h2>Board & Pre-Board Important Questions</h2>

<div class="step">
    <h3>Q1. Explain greedy paradigm how prims algorithm uses this approach. (3+2 Marks) [Pre-board 2024]</h3>
    <p><strong>Answer:</strong><br>
    <strong>Greedy Paradigm:</strong> It is a problem-solving approach where we make the locally optimal choice at each stage with the hope of eventually reaching a global optimal solution. It lacks backtracking. <br>
    <strong>How Prim's uses it:</strong> In Prim's algorithm, we have an MST set (the visited vertices) and unvisited vertices. The 'Greedy' action is iterating across all cross-edges connecting these two sets, and indiscriminately picking the bridge edge that has the absolute minimum weight. It instantly accepts this cheapest local edge without calculating alternative future branching paths.</p>
</div>

<div class="step">
    <h3>Q2. Explain Dijkstra's shortest path algorithm and its complexity. (3+2 Marks) [Pre-board 2023]</h3>
    <p><strong>Answer Algorithm:</strong></p>
    <pre>
DIJKSTRA(Graph G, Source S):
   1. set dist[v] = infinity for all v, dist[S] = 0
   2. Q = MinPriorityQueue(all vertices keyed by dist)
   3. while Q is not empty:
   4.     u = ExtractMin(Q)
   5.     for each neighbor v of u:
   6.         if dist[u] + weight(u,v) < dist[v]:  // RELAXATION
   7.              dist[v] = dist[u] + weight(u,v)
   8.              DecreaseKey(Q, v, dist[v])
    </pre>
    <p><strong>Complexity:</strong><br>
    The algorithm extracts minimum $V$ times ($O(V \\log V)$). It relaxes edges $E$ times ($O(E \\log V)$). The total complexity is mathematically scaled to $O((V + E) \\log V)$ using a binary min-heap.</p>
</div>

<div class="step">
    <h3>Q3. What is prefix code? Explain Huffman algorithm to compute the prefix codes. (5 Marks) [Boards]</h3>
    <p><strong>Answer:</strong><br>
    A <strong>Prefix Code</strong> is a variable-length binary code where it is guaranteed that no codeword forms the starting prefix sequence of any other valid codeword. This explicitly eliminates all ambiguity during binary string decoding without needing spaces or commas.<br>
    <strong>Algorithm Explanation:</strong> Start with an array of distinct characters mapped to frequencies in a queue. Pluck the two smallest values, attach them as children to a synthetic master Parent node containing their sum frequency. Re-insert this Parent into the queue. Repeat iteratively until only the final tree root is left. To generate the codes, trace paths from the root to the leaf, assigning '0' for left-child steps and '1' for right.</p>
</div>
"""

adv_4 = """
<h2>Advanced Theoretical Analysis</h2>
<div class="box">
    <h3>Why does Greedy fail the discrete 0-1 Knapsack problem?</h3>
    <p>Consider a Knapsack with Capacity 50. Items (Weight, Value): Item A (10, $60, Ratio 6), Item B (20, $100, Ratio 5), Item C (30, $120, Ratio 4).</p>
    <p><strong>Greedy Choice:</strong> Picks highest ratio first. It will select Item A (Ratio 6). Weight used = 10, space left = 40. Then it picks Item B. Total weight = 30, space left = 20. It cannot fit Item C ($30 > 20$). The algorithm halts. <strong>Total Val: $160</strong>.</p>
    <p><strong>Globally Optimal Reality:</strong> If it entirely ignored the "Greedy Metric" and skipped Item A completely, it could select Item B (20) and Item C (30). Total weight = 50. Capacity perfectly filled. <strong>Total Val: $220.</strong></p>
    <p>Greedy assumes a fully fluid (fractional) continuum! If items are solid indivisible discrete chunks, one greedy action permanently locks out larger interlocking combinations.</p>

    <h3>Modern World: Deflate & Huffman</h3>
    <p>Huffman coding alone isn't used today. Instead, modern software relies on `DEFLATE`, the core algorithm powering `.ZIP` files, `.PNG` images, and HTTP web traffic. DEFLATE combines two algorithms:</p>
    <ul>
        <li><strong>LZ77:</strong> Eliminates duplicate recurring phrases in a file via sliding window pointers.</li>
        <li><strong>Huffman Coding:</strong> Takes the result of LZ77 and compresses the alphabetic distribution. By stripping out grammatical duplicates first, the entropy drops severely, allowing the Greedy Huffman algorithm to build incredibly dense prefix trees compared to plain text!</li>
    </ul>
</div>
"""

build_file("Unit_4_1_Detailed_Notes.html", "Unit 4 Detailed Notes", "Unit 4: Greedy Algorithms", det_4)
build_file("Unit_4_2_Concise_Revision.html", "Unit 4 Revision Note", "Unit 4: Quick Revision", con_4)
build_file("Unit_4_3_Important_Questions.html", "Unit 4 Questions", "Unit 4: Board & Pre-board Analysis", imp_4)
build_file("Unit_4_4_Advanced_Study.html", "Unit 4 Advanced Note", "Unit 4: Advanced Optimizations", adv_4)
print("Unit 4 generation complete.")
