from abc import ABC, abstractmethod
from typing import List, Dict
import requests
from loguru import logger

class Extractor(ABC):
    def __init__ (self, url: str) -> None:
        self.url = url
        self.data = self.__fetch_data(self.url)
    
    def __fetch_data(self, url: str) -> List[Dict]:
        try:
            logger.info('Buscando dados...')
            response = requests.get(url)

            if response.status_code != 200:
                logger.error(f'Erro ao buscar dados: {response.status_code}')
                return []  
            
            logger.info('Dados buscados com sucesso!')
            data = response.json()
            
            return data

        except Exception as e:
            logger.error(f'Erro ao buscar dados: {e}')
            return []

    @abstractmethod
    def get_data(self) -> List[Dict]:
        pass

class Sale:
    ...