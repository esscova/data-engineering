from datetime import datetime

class Settings:
    URL:str = 'https://agendadividendos.com/app/ajax/agenda.php?a=get-mes&tipo={tipo}&ano={ano}&mes={mes}tipoData=1'

    HEADER:dict = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    ANO = datetime.now().year

    MES = datetime.now().month

settings = Settings()