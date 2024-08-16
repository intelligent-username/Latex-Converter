# .rft: Less complicated version of .docx
# *Note: Currently doesn't work :(()) because of missing pandoc? Pandoc might be broken b/c it's installed but error says "missing file"

import pypandoc

def convert_to_html(fname):
    output_file = fname.rsplit('.', 1)[0] + '.html'
    
    try:
        # Convert the RTF file to HTML using pypandoc
        pypandoc.convert_file(fname, 'html', outputfile=output_file)
        print(f"Converted {fname} to HTML successfully.")
        return output_file
    except Exception as e:
        print(f"\nError converting {fname} to HTML: \n\n--------{str(e)}\n---------")
        return None
