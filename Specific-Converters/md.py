# Lighter HTML, more rare but good

import markdown

def convert_to_html(fname):
    output_file = fname.rsplit('.', 1)[0] + '.html'
    
    with open(fname, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"<html><body>{html_content}</body></html>")
    
    print(f"Converted {fname} to HTML successfully.")
    return output_file