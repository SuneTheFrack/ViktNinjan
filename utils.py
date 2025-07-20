# utils.py
# Hjälpfunktioner för loggmoduler

from datetime import datetime

def get_datum_tid(data):
    now = datetime.now()
    
    # Om datum inte anges → använd dagens datum
    datum = data.get("datum")
    if not datum:
        datum = now.strftime("%Y-%m-%d")

    # Om tid saknas eller är "nu" → använd aktuell tid
    tid = data.get("tid")
    if not tid or str(tid).lower() == "nu":
        tid = now.strftime("%H:%M")

    return datum, tid
