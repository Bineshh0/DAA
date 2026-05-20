import os
import shutil
import glob

base_dir = r"c:\Users\V16\.gemini\antigravity\scratch\5th sem\DAA"
exam_prep_dir = os.path.join(base_dir, "Exam_Prep")

unit_mapping = {
    "Unit_1": "Unit1_Foundation",
    "Unit_2": "Unit2_Iterative",
    "Unit_3": "Unit3_DivideConquer",
    "Unit_4": "Unit4_Greedy",
    "Unit_5": "Unit5_DynamicProgramming",
    "Unit_6": "Unit6_Backtracking",
    "Unit_7": "Unit7_NumberTheoretic",
    "Unit_8": "Unit8_NPCompleteness"
}

mathjax_config = """
    <script>
    MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']]
      }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
"""

html_files = glob.glob(os.path.join(exam_prep_dir, "*.html"))

for file_path in html_files:
    filename = os.path.basename(file_path)
    
    # Identify which unit this file belongs to
    target_folder = None
    for prefix, folder_name in unit_mapping.items():
        if filename.startswith(prefix):
            target_folder = folder_name
            break
            
    if target_folder:
        # Read content and fix formatting
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace the old MathJax script tag with the configured one
        old_script = '<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>'
        if old_script in content:
            content = content.replace(old_script, mathjax_config.strip())
            
        # Also clean up unescaped \\pmod if needed, but MathJax should handle it
        
        # Write to new target directory
        out_target_dir = os.path.join(base_dir, target_folder)
        os.makedirs(out_target_dir, exist_ok=True)
        out_filepath = os.path.join(out_target_dir, filename)
        
        with open(out_filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Moved & Fixed: {filename} -> {target_folder}")
        
        # Delete original file
        os.remove(file_path)

print("All files distributed and formatted successfully.")
