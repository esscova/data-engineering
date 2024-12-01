from utils import Extractor
from typing import List, Dict

class User(Extractor):
    def __init__(self, url: str='https://api.escuelajs.co/api/v1/users' ):
        super().__init__(url)
    
    def get_data(self) -> List[Dict]:
        return self.data
    
users = User().get_data()
