
# ==========================================
# PROJECTO: PASSWORD CHECKER
# OBJECTIVO: Validador de palavras-passe
# ==========================================
import re
import getpass

# 1. Solicite ao utilizador uma palavra-passe.
PALAVRA_PASSE= getpass.getpass("Digite a sua palavra-passe: ")

# 2. Verifique se possui pelo menos 8 caracteres.
tamanho = len(PALAVRA_PASSE)
Oitocaracteres = tamanho >= 8

# 3. Verifique se contém pelo menos uma letra maiúscula.
palavraMaiscula=any(letra.isupper() for letra in PALAVRA_PASSE)
# print(palavraMaiscula)
    

# 4. Verifique se contém pelo menos uma letra minúscula.
palavraMinuscula=any(letra.islower() for letra in PALAVRA_PASSE)
# print(palavraMinuscula)

# 5. Verifique se contém pelo menos um número.
temNumero= any( letra.isnumeric() for letra in PALAVRA_PASSE)
# print(temNumero)
# 6. Verifique se contém pelo menos um carácter especial.
#    Exemplos: @, #, $, !, %
caracteresEspecial = bool(re.search(r"[^a-zA-Z0-9]", PALAVRA_PASSE))

def analisar_password():
    criterios = [Oitocaracteres, palavraMaiscula, palavraMinuscula, temNumero,caracteresEspecial]
    total = sum(criterios)
    classificacao="Nenhuma"
    if total<=2:
        classificacao="Fraca"
    elif total<=4 and total >=3:
        classificacao="Média"
    elif total == 5:
        classificacao="Forte"
    relatorio = {
    "tamanho": Oitocaracteres,
    "maiuscula": palavraMaiscula,
    "minuscula": palavraMinuscula,
    "numero": temNumero,
    "especial": caracteresEspecial,
    "pontuacao": total,
    "classificacao": classificacao
        
    }
    return relatorio
relatorios= analisar_password()
for chave, valor in relatorios.items():
    print(chave,":",valor)
 