import re

def remove_space_white(string,atr):
   return re.sub(r'\s{1,}',atr ,string.strip())