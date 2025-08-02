import logging

def skriv_till_sheet(rad: list, blad_namn="Mat"):
    logging.info(f"(TESTLÄGE) Skulle skriva till blad '{blad_namn}': {rad}")
