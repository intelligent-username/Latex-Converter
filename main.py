import importlib

# Start, give instructions, and call on initial conversion
def main():
    fname = input("Enter the name of the file you want to convert (Ensure it's in the same directory as this runner.py): ")
    
    # Make sure to check ending with the dot so the name of the file itself doesn't contain the extension  
    if fname.endswith(".tex"):
        print("This is already a LaTeX file")
        return 0

    if fname.endswith(".html"):
        return latexer(fname)
    
    print("File Received. Converting...", endswith = "")    
    htmlfile = None

    # Convert file to HTML

    if fname.endswith(".doc"):
        doc_converter = importlib.import_module("Specific-Converters.doc")
        htmlfile = doc_converter.convert_to_html(fname)

    elif fname.endwith(".docx"):
        docx_converter = importlib.import_module("Specific-Converters.docx")
        htmlfile = docx_converter.convert_to_html(fname)

    elif fname.endswith(".md"):
        md_converter = importlib.import_module("Specific-Converters.md")
        htmlfile = md_converter.convert_to_html(fname)
    
    elif fname.endswith(".pdf"):
        pdf_converter = importlib.import_module("Specific-Converters.pdf")
        htmlfile = pdf_converter.convert_to_html(fname)
    
    elif fname.endswith(".odt"):
        odt_converter = importlib.import_module("Specific-Converters.odt")
        htmlfile = odt_converter.convert_to_html(fname)
    
    elif fname.endswith(".rtf"):
        rtf_converter = importlib.import_module("Specific-Converters.rtf")
        htmlfile = rtf_converter.convert_to_html(fname)
    
    elif fname.endswith(".txt"):
        txt_converter = importlib.import_module("Specific-Converters.txt")
        htmlfile = txt_converter.convert_to_html(fname)

    else:
        print("Unsupported file format. Check REDAME.md for supported formats")

    print("...")

    if htmlfile:
            latexer(htmlfile)
    else:
            print("Failed to convert the file to HTML.")

# Convert the HTML to LaTeX, return to main
def latexer(htmlfile):
    print("Converting to final state...")

if __name__ == "__main__":
    main()
