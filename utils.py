# utils.py
# Hjälpfunktioner för loggmoduler

from datetime import datetime

def get_datum_tid(data):
    now = datetime.now()
    
    # Datum: om saknas → dagens datum
    datum = data.get("datum")
    if not datum or str(datum).lower() == "nu":
        datum = now.strftime("%Y-%m-%d")

    # Tid: om saknas eller är "nu" → aktuell tid
    tid = data.get("tid")
    if not tid or str(tid).lower() == "nu":
        tid = now.strftime("%H:%M")

    return datum, tid
