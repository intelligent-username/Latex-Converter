# Microsoft Word from 2007 onward and Google Docs

from docx import Document
from bs4 import BeautifulSoup

def convert_to_html(fname):
    output_file = fname.rsplit('.', 1)[0] + '.html'
    
    doc = Document(fname)
    html = "<html><body>"
    
    for para in doc.paragraphs:
        html += f"<p>{para.text}</p>"
    
    html += "</body></html>"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Converted {fname} to HTML successfully.")
    return output_file
