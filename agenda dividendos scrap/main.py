import asyncio
from src.services import coletar_dados, salvar_csv
from core.configs import settings

async def main():
    try:
        acoes = await coletar_dados(
            header=settings.HEADER, 
            url=settings.URL, 
            tipo=1,
            ano=settings.ANO, 
            mes=settings.MES
        ) 
        
        fiis = await coletar_dados(
            header=settings.HEADER, 
            url=settings.URL, 
            tipo=2,
            ano=settings.ANO, 
            mes=settings.MES
        ) 
        
        salvar_csv(acoes, fiis, settings.ANO, settings.MES)
        
    except Exception as e:
        print(f'Ocorreu um erro durante a execução - {str(e)}')

if __name__ == '__main__':
    asyncio.run(main())