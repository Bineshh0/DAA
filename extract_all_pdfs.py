import fitz # PyMuPDF
import os
import glob

daa_dir = r"c:\Users\V16\.gemini\antigravity\scratch\5th sem\DAA"
pdf_paths = glob.glob(os.path.join(daa_dir, "Unit*", "*.pdf")) + glob.glob(os.path.join(daa_dir, "CSC314*.pdf"))

for pdf_path in pdf_paths:
    print(f"Processing: {pdf_path}")
    doc = fitz.open(pdf_path)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    out_dir = os.path.join(os.path.dirname(pdf_path), base_name + "_extracted")
    os.makedirs(out_dir, exist_ok=True)
    
    md_file = os.path.join(out_dir, base_name + ".md")
    
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(f"# Extracted Content from {base_name}\n\n")
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            f.write(f"## Page {page_num + 1}\n\n")
            if text.strip():
                f.write(text + "\n\n")
            
            # Extract images
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_filename = f"page{page_num+1}_img{img_index}.{image_ext}"
                image_filepath = os.path.join(out_dir, image_filename)
                
                with open(image_filepath, "wb") as img_file:
                    img_file.write(image_bytes)
                
                md_img_path = image_filepath.replace("\\", "/")
                f.write(f"![Image from page {page_num+1}](file:///{md_img_path})\n\n")
    
    print(f"Done extraction for {base_name}")

