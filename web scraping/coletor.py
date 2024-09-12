import asyncio
from services import coletar_dados, salvar_csv
from datetime import datetime
import pandas as pd

URL:str = 'https://agendadividendos.com/app/ajax/agenda.php?a=get-mes&tipo={tipo}&ano={ano}&mes={mes}tipoData=1'

HEADER:dict = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

ANO = datetime.now().year

MES = datetime.now().month

###

async def main():
    try:
        acoes = await coletar_dados(header=HEADER, url=URL, tipo=1,ano=ANO, mes=MES) 
        fiis = await coletar_dados(header=HEADER, url=URL, tipo=2,ano=ANO, mes=MES) 
        
        salvar_csv(acoes, fiis, ANO, MES)
        
    except Exception as e:
        print(f'Ocorreu um erro durante a execução - {str(e)}')

if __name__ == '__main__':
    asyncio.run(main())