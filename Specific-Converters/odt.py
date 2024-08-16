# Used by LibreOffice and OpenOffice, and other open-source processors.

import subprocess

def convert_to_html(fname):
    output_file = fname.rsplit('.', 1)[0] + '.html'
    
    try:
        subprocess.run(['soffice', '--headless', '--convert-to', 'html', fname], check=True)
        print(f"Converted {fname} to HTML successfully.")
        return output_file
    except subprocess.CalledProcessError:
        print(f"Error converting {fname} to HTML.")
        return None
