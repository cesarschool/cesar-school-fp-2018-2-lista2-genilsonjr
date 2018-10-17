## QUESTÃO 3 ##
#
# Crie uma implementação da cifra rotacional, às vezes também chamada de cifra de César.
# 
# A cifra de César é uma simples cifra de deslocamento que se baseia na transposição 
# de todas as letras do alfabeto usando uma chave inteira entre 0 e 26. 
# O uso da chave 0 ou 26 sempre produzirá a mesma saída devido à aritmética modular. 
# A letra é deslocada para tantos valores quanto o valor da chave.
#
# A notação geral para cifras rotacionais é ROT + <chave>. A cifra rotacional mais comumente usada é a ROT13.
#
# Um ROT13 no alfabeto latino seria o seguinte:
# 	Normal:  abcdefghijklmnopqrstuvwxyz
#	Cifrado: nopqrstuvwxyzabcdefghijklm
#
# Exemplos:
#	Entrada: ROT5 omg 
#          Saída: trl
#	Entrada: ROT0 c 
#          Saída: c
#	Entrada: ROT26 Cool 
#          Saída: Cool
#	Entrada: ROT13 The quick brown fox jumps over the lazy dog. 
#          Saída: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#	Entrada: ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. 
#          Saída: The quick brown fox jumps over the lazy dog.
#
# Se um valor de entrada inválido for digitado, a seguinte mensagem 
# deve ser impressa: 'Erro'. 
# Entradas inválidas podem ser entradas que contém códigos de rotações 
# inválidos ou mensagens contendo caracteres que não estão no alfabeto. 
# Exemplos:
# 	Entrada: RARA abc Saída: Erro
# 	Entrada: ROT5 c99 Saída: Erro
#
# As entradas devem ser sempre compostas por ROT + <chave> + ' ' + 'mensagem', 
# ou seja, a cifra rotacional e a mensagem a ser cifrada separados por vírgula.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    
    texto = input('Digite a mensagem a ser encriptada ou decifrada: ')# Solicitando o texto a ser encriptado ou decriptado:

    chave = int(input('Entre com o valor da chave (deslocamento): '))# Chave a ser utilizada

    modo = input('Escolha E para encriptar ou D para decriptar o texto: ')# Determinar modo de operação (E = encriptar; D = decriptar)

    CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'# Conjunto de caracteres válidos no algoritmo

    convertido = ''# Variável para armazenar o texto criptografado (ou decifrado)

    texto = texto.upper()# Converter todo o texto em maiúsculas:
    for caractere in texto:# Código que será executdo em cada caractere do texto:
      if caractere in CARACTERES:
 
       num = CARACTERES.find(caractere) # Obter o número criptografado ou decriptado do caractere
 
       if modo == 'E':# Obter o número do caractere
         num = num + chave
       elif modo == 'D':
         num = num - chave
 
      if num >= len(CARACTERES):# Manipulando a rotação se o valor de num for maior do que o comprimento de CARACTERES ou menor que 0
        num = num - len(CARACTERES)
      elif num < 0:
        num = num + len(CARACTERES)
 
        convertido = convertido + CARACTERES[num]# Adicionar (concatenar) o caractere correspondente a num na variável convertido 
      else:
        convertido = convertido + caractere# Concatenado o caractere sem efetuar criptografia ou decifragem

    if modo == 'E':# Mostrar o texto encriptado ou decifrado na tela:
       print('O texto criptografado é ', convertido)
    if modo == 'D':
       print('O texto decriptado é ', convertido)



    
if __name__ == '__main__':
    main()
