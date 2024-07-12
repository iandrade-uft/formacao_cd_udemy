import os
import unicodedata
import re

def normalizar_string(s):
    # Normaliza a string para decompor os caracteres acentuados
    nfkd_form = unicodedata.normalize('NFKD', s)
    # Remove os caracteres especiais
    s = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    # Substitui espaços por underline e transforma em minúsculas
    s = re.sub(r'[,\s]+', '_', s).lower()
    return s

def remomear_diretorio(dir_name):
    number, old_desc_name = dir_name.split(".")
    number = int(number)
    new_desc_name = normalizar_string(old_desc_name)
    new_dir_name = f"{number:02d}_{new_desc_name}"
    return new_dir_name



def main():
    directories=[d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]
    for dir_name in directories:
        new_dir_name = remomear_diretorio(dir_name)
        os.rename(dir_name, new_dir_name)

if __name__=="__main__":
    main()