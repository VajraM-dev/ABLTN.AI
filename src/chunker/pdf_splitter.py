from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(dir_path, input_path, pages_per_split, output_prefix="split"):
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)

    for i in range(0, total_pages, pages_per_split):
        writer = PdfWriter()
        end_page = min(i + pages_per_split, total_pages)

        for j in range(i, end_page):
            writer.add_page(reader.pages[j])

        output_path = f"{output_prefix}_{i//pages_per_split + 1}.pdf"
        with open(os.path.join(dir_path, "src", "pdf_splits", output_path), "wb") as output_file:
            writer.write(output_file)

        print(f"Created: {output_path} ({end_page - i} pages)")