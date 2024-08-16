# .odt: Used by LibreOffice and OpenOffice, and other open-source processors.

from odf.opendocument import load
from odf.text import P
from odf import teletype

def convert_to_html(fname):
    # Load the .odt file
    doc = load(fname)
    
    # Extract text content
    paragraphs = doc.getElementsByType(P)
    html_content = "<html><body>"
    
    for paragraph in paragraphs:
        text = teletype.extractText(paragraph)
        html_content += f"<p>{text}</p>"
    
    html_content += "</body></html>"
    
    # Write to HTML file
    output_file = fname.rsplit('.', 1)[0] + '.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Converted {fname} to HTML successfully.")
    return output_file
