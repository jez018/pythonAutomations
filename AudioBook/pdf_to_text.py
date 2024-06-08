from pypdf import PdfReader

def pdf_to_text(pdf_file_loc='test_file.pdf'):

    pdf_file_name = pdf_file_loc

    reader = PdfReader(pdf_file_name)

    pages_content = []
    for page in reader.pages:
        # extracting text from page
        text = page.extract_text()
        splitted_text = text.splitlines()
        pages_content.append(splitted_text)

    return pages_content


