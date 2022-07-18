from business.pdf_service import extract_text_from_block
from core.utils import extract_date_from_string


def is_xp_pdf(pdf):
    first_page_text = pdf.get_page_text(0)
    return "XP INVESTIMENTOS" in first_page_text


def get_operation_date(blocks):
    date_block = list(
        filter(lambda block: extract_date_from_string(extract_text_from_block(block)) is not None, blocks))
    return extract_date_from_string(date_block[1])
