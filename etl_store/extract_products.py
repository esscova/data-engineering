from utils import Extractor
from typing import List, Dict

class Product(Extractor):
    def __init__(self, url: str='https://api.escuelajs.co/api/v1/products' ):
        super().__init__(url)
    
    def get_data(self) -> List[Dict]:
        return self.data
    
products = Product().get_data()