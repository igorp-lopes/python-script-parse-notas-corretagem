import fitz


def open_pdf(file_path):
    return fitz.open(file_path)


def get_pdf_pages(pdf):
    total_pages = pdf.page_count
    return (pdf.load_page(i) for i in range(total_pages))


def extract_blocks_from_page(page, sort=True):
    return page.get_text("blocks", sort)


def get_block_index_by_matching_text(blocks, text_to_match):
    for index, block in enumerate(blocks):
        if text_to_match in extract_text_from_block(block):
            return index
        
    return None


def extract_text_from_block(block):
    return block[4]


def extract_text_from_blocks(blocks):
    return [extract_text_from_block(block) for block in blocks]
