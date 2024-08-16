# .rft: Less complicated version of .docx

import pypandoc

def convert_to_html(fname):
    output_file = fname.rsplit('.', 1)[0] + '.html'
    
    try:
        # Convert the RTF file to HTML using pypandoc
        pypandoc.convert_file(fname, 'html', outputfile=output_file)
        print(f"Converted {fname} to HTML successfully.")
        return output_file
    except Exception as e:
        print(f"Error converting {fname} to HTML: {str(e)}")
        return None
