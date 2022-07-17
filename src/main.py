from core.directory_utils import get_input_files
from business.pdf_service import open_pdf
from business.xp_service import extract_data_from_xp_pdf


def notas_corretagem_parser():
    files = get_input_files()
    for file in files:
        current_pdf = open_pdf(file)
        extract_data_from_xp_pdf(current_pdf)


if __name__ == "__main__":
    notas_corretagem_parser()
