# Plain Text files

from html import escape

def convert_to_html(fname):
    output_file = fname.rsplit('.', 1)[0] + '.html'
    
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    html_content = f"<html><body><pre>{escape(content)}</pre></body></html>"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Converted {fname} to HTML successfully.")
    return output_file
