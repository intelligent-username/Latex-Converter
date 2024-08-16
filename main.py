from importlib import import_module
from bs4 import BeautifulSoup
import os

# Start, give instructions, and call on initial conversion
def main():
    fname = input("Enter the name of the file you want to convert (Ensure it's in the same directory as this runner.py): ")
    
    # Make sure to check ending with the dot so the name of the file itself doesn't contain the extension  
    if fname.endswith(".tex"):
        print("This is already a LaTeX file")
        return 0

    if fname.endswith(".html"):
        return latexer(fname)
    
    print("File Received. Converting...", end="")    
    htmlfile = None

    # Convert file to HTML
    # Could use loop of some sort but more efficient to just use series of elif statements

    if fname.endswith(".doc"):
        doc_converter = import_module("Specific-Converters.doc")
        htmlfile = doc_converter.convert_to_html(fname)

    elif fname.endswith(".docx"):
        docx_converter = import_module("Specific-Converters.docx")
        htmlfile = docx_converter.convert_to_html(fname)

    elif fname.endswith(".md"):
        md_converter = import_module("Specific-Converters.md")
        htmlfile = md_converter.convert_to_html(fname)
    
    elif fname.endswith(".pdf"):
        pdf_converter = import_module("Specific-Converters.pdf")
        htmlfile = pdf_converter.convert_to_html(fname)
    
    elif fname.endswith(".odt"):
        odt_converter = import_module("Specific-Converters.odt")
        htmlfile = odt_converter.convert_to_html(fname)
    
    elif fname.endswith(".rtf"):
        rtf_converter = import_module("Specific-Converters.rtf")
        htmlfile = rtf_converter.convert_to_html(fname)
    
    elif fname.endswith(".txt"):
        txt_converter = import_module("Specific-Converters.txt")
        htmlfile = txt_converter.convert_to_html(fname)

    else:
        print("Unsupported file format. Check REDAME.md for supported formats")

    print("...")

    if htmlfile:
        latexer(htmlfile)
    else:
        print("Failed to convert the file to HTML.")
        return

# Convert the HTML to LaTeX, return to main
def latexer(htmlfile):
    print("Converting to final state...")
    
    with open(htmlfile, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    latex_content = "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\begin{document}\n\n"
    
    for tag in soup.find_all():
        if tag.name == 'h1':
            latex_content += f"\\section{{{tag.text}}}\n\n"
        elif tag.name == 'h2':
            latex_content += f"\\subsection{{{tag.text}}}\n\n"
        elif tag.name == 'p':
            latex_content += f"{tag.text}\n\n"
        elif tag.name == 'ul':
            latex_content += "\\begin{itemize}\n"
            for li in tag.find_all('li'):
                latex_content += f"\\item {li.text}\n"
            latex_content += "\\end{itemize}\n\n"
        elif tag.name == 'ol':
            latex_content += "\\begin{enumerate}\n"
            for li in tag.find_all('li'):
                latex_content += f"\\item {li.text}\n"
            latex_content += "\\end{enumerate}\n\n"
        elif tag.name == 'table':
            cols = len(tag.find('tr').find_all(['th', 'td']))
            latex_content += f"\\begin{{tabular}}{{{'|c' * cols}|}}\n\\hline\n"
            for row in tag.find_all('tr'):
                cells = row.find_all(['th', 'td'])
                latex_content += " & ".join(cell.text for cell in cells) + " \\\\ \\hline\n"
            latex_content += "\\end{tabular}\n\n"
    
    latex_content += "\\end{document}"
    
    output_file = htmlfile.rsplit('.', 1)[0] + '.tex'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    print(f"Converted {htmlfile} to LaTeX successfully.")
    return output_file


if __name__ == "__main__":
    main()
