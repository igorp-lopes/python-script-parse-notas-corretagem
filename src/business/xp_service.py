from more_itertools import collapse

from business.pdf_service import extract_text_from_block, \
    get_block_index_by_matching_text
from core.utils import extract_date_from_string


def get_table_headers(header_block):
    block_text = extract_text_from_block(header_block)
    headers = block_text.split('\n')

    headers[2] = headers[2].split(' ', 1)
    headers[5] = headers[5].split('(*)')
    headers.pop()
    headers = list(collapse(headers))

    return headers


def get_table_blocks(all_blocks):
    table_start_index = get_block_index_by_matching_text(all_blocks, 'Negócios realizados')
    table_end_index = get_block_index_by_matching_text(all_blocks, 'NOTA DE NEGOCIAÇÃO')
    return all_blocks[table_start_index:table_end_index]


def is_xp_pdf(pdf):
    first_page_text = pdf.get_page_text(0)
    return "XP INVESTIMENTOS" in first_page_text


def get_operation_date(blocks):
    date_block = list(
        filter(lambda block: extract_date_from_string(extract_text_from_block(block)) is not None, blocks))
    return extract_date_from_string(extract_text_from_block(date_block[1]))
