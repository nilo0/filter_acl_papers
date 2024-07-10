import os
from typing import List
from openai import OpenAI
from acl_papers.prompt import system_prompt


MODEL="gpt-3.5-turbo"


def analyse_abstract(abstract:str, model:str):
  
  OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

  client = OpenAI(api_key=OPENAI_API_KEY)


  message = [
        {"role":"system", "content":system_prompt},
        {"role":"user", "content":f"Abstract: {abstract}"}
  ]

  OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
  client = OpenAI(api_key=OPENAI_API_KEY)

  completion = client.chat.completions.create(
    model=model,
    messages=message,
    temperature=0, 
    max_tokens=150
    )
  
  return completion.choices[0].message.content
