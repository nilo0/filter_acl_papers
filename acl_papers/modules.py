import os
import requests
import pandas as pd

from bs4 import BeautifulSoup
from typing import List, Dict



def crawling(url:str):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup


def load_or_create_df(path:str, columns:List['str']):
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
        except Exception as e:
            df = pd.DataFrame(columns=columns)

    else:
        df = pd.DataFrame(columns=columns)

    return df


def update_dataframe(path: str, columns:list, new_rows:List[Dict]):
    df = load_or_create_df(path=path, columns=columns)
    new_df = pd.DataFrame(new_rows, columns=columns)
    
    df = pd.concat([df, new_df], ignore_index=True)
    
    df.to_csv(path, index=False)


def check_relevant(text:str) -> bool:
    text_lower = text.lower()
    if "relevant" in text_lower and "irrelevant" not in text_lower:
        return True
    elif "irrelevant" in text_lower:
        return False
    else:
        return None