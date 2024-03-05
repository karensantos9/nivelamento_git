def soma(a,b):
    operacaosoma = a + b
    return operacaosoma
    

def subtração (sub1,sub2):
    operacaosubt = (sub1 - sub2)
    return operacaosubt

def divisao (di1,di2):
    operacaodivisao = (di1 / di2)
    return operacaodivisao

def multiplicacao (mul1, mul2):
    operacaomult = mul1 * mul2
    return operacaomult

def potenciacao (pot1,pot2):
    operacaopoten = (pot1**pot2)
    return operacaopoten


def fatorial (fatorial):
    i= 1
    fator = 1
    if fatorial == 0:
        return 1
    else:
        for i in range ( 1, fatorial +1):
            fator *= i
        return fator


while True:
    print("-----calculadora------")
    print ("1 - soma")
    print ("2 - subtração")
    print ("3 - divisão")
    print ("4 - multiplicação")
    print ("5 - potenciação")
    print ("6 - fatorial")
    print ("7 - sair da calculadora")
    
    
    operação = (input("qual operação deseja relizar? "))
    
    
    if operação in ('1', '2', '3', '4', '5'):
        num1 = int (input ("qual o número? "))
        num2 = int (input ("qual o número? "))
        if operação == '1':
            resposta1 = soma(num1,num2)
            print (f"-----o resultado da soma é:{resposta1}----") 
        elif operação == '2':
            resposta2 = subtração (num1,num2)
            print (f"-----o rsultado da subtração é: {resposta2}-----")
        elif operação =='3':
            resposta3 = divisao (num1,num2)
            print (f"---- a resposta da divisão é: {resposta3}----")
        elif operação == '4':
            resposta4 = multiplicacao(num1,num2)
            print (f"-----a resposta da multiplicação é:{resposta4}-----")
        elif operação == '5':
            resposta5 = potenciacao(num1,num2)
            print (f" -----a resposta da potenciação é: {resposta5}-----")
            
            
    elif operação in ('6'):
            num10 = int (input ("qual o número? "))
            resposta6 = fatorial(num10)
            print (f"-----a resposta é {resposta6}-----")
            
    else:
        print("-------tchau-------")
        
    
    
        
        
