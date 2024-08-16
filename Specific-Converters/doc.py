# .doc: Pre-2007 Microsoft Word and other legacy systems use this

# .doc: Pre-2007 Microsoft Word and other legacy systems use this

import pypandoc

def convert_to_html(fname):
    output_file = fname.rsplit('.', 1)[0] + '.html'
    
    try:
        pypandoc.convert_file(fname, 'html', outputfile=output_file)
        print(f"Converted {fname} to HTML successfully.")
        return output_file
    except Exception as e:
        print(f"Error converting {fname} to HTML: {str(e)}")
        return None
