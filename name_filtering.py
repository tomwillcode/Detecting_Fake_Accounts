import spacy
import re
import numpy as np
import pandas as pd
nlp = spacy.load("en_core_web_sm")

def split_string(text):
    # Split the text on spaces and underscores
    substrings = re.split(r'\s+|_', text)

    # Remove empty strings from the list
    substrings = [substr.lower() for substr in substrings if substr]

    return substrings

def get_names(text_list):
  returned_list = []
  for i in text_list:
    doc = nlp(i)
    if len(doc.ents) > 0 and doc.ents[0].label_ == 'PERSON':
      returned_list.append(i.lower())
  return(returned_list)

def return_name_list(input_string):
  name_list = split_string(input_string)
  return ''.join(get_names(name_list))

def get_name_list(df):
    first_names = list(df[pd.isnull(df['First_Name']) != True]['First_Name'].str.lower())
    last_names = list(df[pd.isnull(df['Last_Name']) != True]['Last_Name'].str.lower())
    return first_names + last_names

def get_names2(text_list, official_names):
    first_last = [i for i in text_list if i in official_names]
    return first_last

