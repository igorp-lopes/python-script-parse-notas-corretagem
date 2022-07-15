from core.directory_utils import get_input_files
from pdfParserService.pdfParserService import open_pdf


def notas_corretagem_parser():
    files = get_input_files()
    for file in files:
        open_pdf()


if __name__ == "__main__":
    notas_corretagem_parser()