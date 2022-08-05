from more_itertools import collapse

from business.pdf_service import extract_blocks_from_page, get_pdf_pages, extract_text_from_block, \
    get_block_index_by_matching_text
from core.constants import STOCKS_REGEX, XP_POSSIBLE_OBS_COLUMN_VALUES
from core.utils import extract_date_from_string, extract_from_string_using_regex


def extract_data_from_xp_pdf(pdf):
    if not is_xp_pdf(pdf):
        return

    for page in get_pdf_pages(pdf):
        page_blocks = extract_blocks_from_page(page)
        date = get_operation_date(page_blocks)
        table_rows, table_data = get_table_data(get_table_blocks(page_blocks))


def get_table_data(table_blocks):
    header = get_table_headers(table_blocks[0])
    table_blocks.pop(0)

    rows_data = list(map(get_row_data, table_blocks))

    return header, rows_data


def get_table_headers(header_block):
    block_text = extract_text_from_block(header_block)
    headers = block_text.split('\n')

    headers[2] = headers[2].split(' ', 1)
    headers[5] = headers[5].split('(*)')
    headers = list(collapse(headers))
    del headers[-1]
    del headers[0]
    headers[0] = headers[0].replace('Q ', '')
    headers.remove('Obs. ')
    headers.remove('Prazo')

    headers.append('Broker')

    return headers


def get_row_data(row_block):
    text = extract_text_from_block(row_block).split('\n')
    stock = extract_from_string_using_regex(text[3], STOCKS_REGEX)
    text[3] = stock
    text = remove_obs_column(text)
    del text[-1]
    text.append("XP INVESTIMENTOS")
    return text


def remove_obs_column(row_text):
    possible_obs_column = row_text[4]
    if (possible_obs_column in XP_POSSIBLE_OBS_COLUMN_VALUES):
        del row_text[4]

    return row_text


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
