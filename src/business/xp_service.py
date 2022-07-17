def is_xp_pdf(pdf):
    first_page_text = pdf.get_page_text(0)
    return "XP INVESTIMENTOS" in first_page_text