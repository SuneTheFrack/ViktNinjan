# utils.py
# Hjälpfunktioner för loggmoduler

from datetime import datetime

def get_datum_tid(data):
    """
    Returnerar datum och tid i rätt format.
    Om datum eller tid saknas i inkommande data (ex: från GPT),
    används nuvarande datum och/eller tid.
    
    Parametrar:
        data (dict): JSON-data från request
    
    Returnerar:
        tuple: (datum, tid) i format ("YYYY-MM-DD", "HH:MM")
    """
    now = datetime.now()
    datum = data.get("datum", now.strftime("%Y-%m-%d"))
    tid = data.get("tid", now.strftime("%H:%M"))
    return datum, tid
