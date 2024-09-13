# Scraper de Dividendos

Este projeto é um web scraper que coleta dados de dividendos e proventos de ações e fundos imobiliários (FIIs) do site "agendadividendos.com". Ele foi projetado para reunir informações sobre pagamentos futuros de dividendos e salvá-las em formato CSV.

## Funcionalidades

- Coleta de dados assíncrona para melhor desempenho
- Extrai dados tanto de ações quanto de FIIs
- Configurações personalizáveis para fácil customização
- Salva os dados em formato CSV para análise simples

## Requisitos

- Python 3.7+
- aiohttp
- BeautifulSoup4
- pandas

## Estrutura do Projeto

- `main.py`: O ponto de entrada da aplicação
- `configs.py`: Contém as configurações do sistema
- `services.py`: Inclui a funcionalidade principal para extração e processamento de dados

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/esscova/data-engineering.git
   cd data-engineering/agenda_dividendos_scraper
   ```

2. Instale os pacotes necessários:
   ```
   pip install aiohttp beautifulsoup4 pandas
   ```

## Uso

1. Certifique-se de que suas configurações em `configs.py` estão corretas.

2. Execute o script:
   ```
   python main.py
   ```

3. O script irá coletar dados para o mês e ano atuais (conforme configurado) e salvar dois arquivos CSV no diretório `data`:
   - `ACOES-{ano}-{mes}.csv`: Para dividendos de ações
   - `FIIS-{ano}-{mes}.csv`: Para dividendos de FIIs

## Configuração

Você pode modificar as seguintes configurações em `configs.py`:

- `HEADER`: O user agent para requisições HTTP
- `ANO`: O ano para o qual coletar dados (padrão: ano atual)
- `MES`: O mês para o qual coletar dados (padrão: mês atual)

## Formato dos Dados

Os dados coletados incluem os seguintes campos:

- Ticker: O código da ação ou FII
- Nome: O nome completo da empresa ou fundo
- Data_com: A data ex-dividendo
- Data_pgto: A data de pagamento
- Tipo: O tipo de pagamento (ex: dividendo, juros sobre capital próprio)
- Valor: O valor do pagamento por ação/cota

## Tratamento de Erros

O script inclui tratamento básico de erros:
- Ele imprimirá uma mensagem de erro se houver um problema durante a execução.
- Trata e registra erros relacionados à análise e conversão de dados.

## Contribuindo

Contribuições, problemas e solicitações de recursos são bem-vindos.
