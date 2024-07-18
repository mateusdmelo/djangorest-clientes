import re
from validate_docbr import CPF


def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)


def nome_valido(nome):
    return nome.isalpha()


def rg_valido(num_rg):
    return len(num_rg) == 9


def celular_valido(num_celular):
    """Verifica se o celular é válido (xx) xxxxx-xxxx"""
    pattern = r'^\(\d{2}\) \d{5}-\d{4}$'
    return re.match(pattern, num_celular) is not None