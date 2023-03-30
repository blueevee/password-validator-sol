import re


def minSize(password, length):
    """"
        Verifica se a senha possui a quantidade mínima de dígitos
    """
    return length <= len(password)   

def minUppercase(password, amount_letters):
    """"
        Verifica se a senha possui a quantidade mínima de letras maiúsculas 
    """
    upper_letters = sum(letter.isupper() for letter in password)
    return amount_letters <= upper_letters  

def minLowercase(password, amount_letters):
    """"
        Verifica se a senha possui a quantidade mínima de letras minúsculas 
    """
    lower_letters = sum(letter.islower() for letter in password)
    return amount_letters <= lower_letters    

def minDigit(password, amount_numbers):
    """"
        Verifica se a senha possui a quantidade mínima de dígitos númericos 
    """
    numbers = sum(letter.isdigit() for letter in password)
    return amount_numbers <= numbers    

def minSpecialChars(password, special_chars):
    """"
        Verifica se a senha possui a quantidade mínima de caracteres especiais 
    """
    chars = len(re.findall(r"[!@#\$%\^&\*\(\)-\+\\{}\[\]\/]", password))
    return special_chars <= chars  

def noRepeted(password, value):
    """"
        Verifica se a senha possui caracteres repetidos em sequência 
    """
    pattern = re.compile(r'([\w!@#\$%\^&\*\(\)-\+\\{}\[\]\/&])\1*')
    groups = [match.group() for match in pattern.finditer(password)]
    return not len(max(groups, key=len)) > 1