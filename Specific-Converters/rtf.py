# Less complicated version of .docx

import subprocess

def convert_to_html(fname):
    output_file = fname.rsplit('.', 1)[0] + '.html'
    
    try:
        subprocess.run(['unoconv', '-f', 'html', '-o', output_file, fname], check=True)
        print(f"Converted {fname} to HTML successfully.")
        return output_file
    except subprocess.CalledProcessError:
        print(f"Error converting {fname} to HTML.")
        return None
