import fitz

def open_pdf(file_path):
    return fitz.open(file_path)

def get_pdf_pages(pdf):
    total_pages = pdf.page_count
    return [pdf.load_page(i) for i in range(total_pages)]

def extract_blocks_from_page(page):
    return page.get_text("blocks", sort=True)


def extract_text_from_block(block):
    return block[4]


def extract_text_from_blocks(blocks):
    text = []

    for block in blocks:
        text.append(extract_text_from_block(block))

    return text