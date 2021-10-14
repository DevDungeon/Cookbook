#!/usr/bin/env python
"""
Modified from original at https://www.geeksforgeeks.org/how-to-extract-images-from-pdf-in-python/
pip install fitz frontend pymupdf
"""
import fitz
import io
from PIL import Image

pdf_file = fitz.open("test.pdf")
  
for page_index in range(len(pdf_file)):    
    page = pdf_file[page_index]
    image_list = page.getImageList()
      
    if image_list:
        print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
    else:
        print("[!] No images found on page", page_index)
    for image_index, img in enumerate(page.getImageList(), start=1):
        
        # get the XREF of the image
        xref = img[0]
          
        # extract the image bytes
        base_image = pdf_file.extractImage(xref)
        image_bytes = base_image["image"]
          
        # get the image extension
        image_ext = base_image["ext"]
        with open(f'{page_index}_{image_index}.{image_ext}', 'wb') as f:
            f.write(image_bytes)

