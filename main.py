from importlib import import_module
from bs4 import BeautifulSoup
import os

# Start, give instructions, and call on initial conversion
def main():
    fname = input("Enter the (exact) name of the file you want to convert (Ensure it's in the same directory as main.py and include the extension): ")
    
    # Make sure to check ending with the dot so the name of the file itself doesn't contain the extension
    if fname.endswith(".tex"):
        print("This is already a LaTeX file")
        return 0

    if fname.endswith(".html"):
        return latexer(fname)
    
    print("File Received. Converting...", end="")
    htmlfile = None

    # Convert file to HTML
    # Could have uses a loop of some sort but more efficient to just use series of elif statements

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

# Convert the HTML to LaTeX
# Then return the LaTeX file to main
def latexer(htmlfile):
    print("Converting to final state...")
    with open(htmlfile, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    latex_content = [
        "\\documentclass{article}",
        "\\usepackage[utf8]{inputenc}",
        "\\usepackage{hyperref}",
        "\\usepackage{graphicx}",
        "\\usepackage{amsmath}",
        "\\begin{document}",
        ""
    ]

    def escape_latex(text):
        chars = {
            '&': '\\&', '%': '\\%', '$': '\\$', '#': '\\#', '_': '\\_',
            '{': '\\{', '}': '\\}', '~': '\\textasciitilde{}',
            '^': '\\textasciicircum{}'
        }
        return ''.join(chars.get(c, c) for c in text)

    for tag in soup.find_all():
        if tag.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag.name[1])
            command = ['section', 'subsection', 'subsubsection', 'paragraph', 'subparagraph', 'subparagraph'][level-1]
            latex_content.append(f"\\{command}{{{escape_latex(tag.text)}}}\n")

        elif tag.name == 'p':
            latex_content.append(f"{escape_latex(tag.text)}\n\n")
        
        elif tag.name in ['ul', 'ol']:
            env = 'itemize' if tag.name == 'ul' else 'enumerate'
            latex_content.append(f"\\begin{{{env}}}")
            for li in tag.find_all('li', recursive=False):
                latex_content.append(f"\\item {escape_latex(li.text)}")
            latex_content.append(f"\\end{{{env}}}\n")
        
        elif tag.name == 'table':
            cols = len(tag.find('tr').find_all(['th', 'td']))
            latex_content.append(f"\\begin{{tabular}}{{{'|c' * cols}|}}")
            latex_content.append("\\hline")
        
            for row in tag.find_all('tr'):
                cells = row.find_all(['th', 'td'])
                latex_content.append(" & ".join(escape_latex(cell.text.strip()) for cell in cells) + " \\\\ \\hline")
            latex_content.append("\\end{tabular}\n")
        
        elif tag.name == 'a':
            href = tag.get('href', '')
            latex_content.append(f"\\href{{{href}}}{{{escape_latex(tag.text)}}}")
        
        elif tag.name == 'img':
            src = tag.get('src', '')
            alt = tag.get('alt', 'image')
            latex_content.append(f"\\includegraphics[width=0.8\\textwidth]{{{src}}}")
            latex_content.append(f"\\caption{{{escape_latex(alt)}}}")
        
        elif tag.name in ['b', 'strong']:
            latex_content.append(f"\\textbf{{{escape_latex(tag.text)}}}")
        elif tag.name in ['i', 'em']:
        
            latex_content.append(f"\\textit{{{escape_latex(tag.text)}}}")
        
        elif tag.name == 'code':
            latex_content.append(f"\\texttt{{{escape_latex(tag.text)}}}")

    latex_content.append("\\end{document}")

    output_file = htmlfile.rsplit('.', 1)[0] + '.tex'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(latex_content))

    print(f"Converted {htmlfile} to LaTeX successfully.")
    return output_file


if __name__ == "__main__":
    main()
