import aiohttp
from datetime import datetime
from bs4 import BeautifulSoup as bs
from typing import List, Dict, Optional
import pandas as pd

def extrair_dados_da_linha(row:bs) -> Optional[Dict[str,str]]:
    """
    Função para extrair dados de uma linha da tabela
    """
    cols = row.find_all('td')
    
    if not cols:
        return None
    
    ativo_tag = cols[0].find('a')
    nome_tag = cols[0].find('span', class_='text-muted')

    if ativo_tag and nome_tag:
        ticker = ativo_tag.get_text(strip=True)
        nome = nome_tag.get_text(strip=True)
        data_com = cols[1].get_text(strip=True)
        data_pgto = cols[2].get_text(strip=True)
        tipo = cols[3].get_text(strip=True)
        valor_str = cols[4].get_text(strip=True).replace('.', '').replace(',', '.')

        try:
            valor = float(valor_str)
        except ValueError:
            print(f'Erro ao converter o valor:{valor_str}')
            valor = 0.0

        def expandir_ano(data:str):
            dia, mes, ano = data.split('/')
            if len(ano) == 2:
                ano = '20'+ ano
            return f'{dia}/{mes}/{ano}'
        
        try:
            data_com = datetime.strptime(expandir_ano(data_com), '%d/%m/%Y').date()
            data_pgto = datetime.strptime(expandir_ano(data_pgto), '%d/%m/%Y').date()
        except ValueError as e:
            print(f'Erro ao converter a data: {e}')
            return None
        
        return {
            'Ticker': ticker,
            'Nome': nome,
            'Data_com': data_com,
            'Data_pgto': data_pgto,
            'Tipo': tipo,
            'Valor': valor
        }
    return None


async def coletar_dados(header:dict, url:str, tipo:int, ano:int, mes:int) -> List[Dict[str,str]]:
    """
    Esta funcao coleta e processa os dados de dividendos e proventos para o ano, mes e tipo (1 = ações ou 2 = fiis) fornecidos.
    """
    url = url.format(tipo=tipo, ano=ano, mes=mes)

    async with aiohttp.ClientSession(headers=header) as session:
        async with session.get(url=url) as response:
            if response.status != 200:
                return []
            
            site = await response.text()
            site = bs(site, 'html.parser')

            data = []
            rows = site.find_all('tr')

            for row in rows:
                dado = extrair_dados_da_linha(row)
                if dado:
                    data.append(dado)
    return data

def salvar_csv(acoes, fiis,ano,mes):
    acoes_df = pd.DataFrame(acoes)
    fiis_df = pd.DataFrame(fiis)

    # converter para data
    for df in [acoes_df, fiis_df]:
        df['Data_com'] = pd.to_datetime(df['Data_com'])
        df['Data_pgto'] = pd.to_datetime(df['Data_pgto'])

    # persistir dados
    acoes_df.to_csv(f'data/ACOES-{ano}-{mes}.csv', index=False, sep=',')
    fiis_df.to_csv(f'data/FIIS-{ano}-{mes}.csv', index=False, sep=',')