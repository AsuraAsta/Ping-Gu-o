import subprocess  
import platform

#Subprocess ele tem uam funcao de abrir o cmd ou terminal e rodar um comando nele sem que o user veja
#Já o Platform ele tem uma funcao para identificar em ql sistema eu estou

ip = "8.8.8.8"
def ping_ip (ip):
    sistema = platform.system()  #Declarei a variavel sistemas e disse a pra busca pelo platforma.system em qual sistema op eu estou 
    if sistema == "Windows":
        parametro = "-n"
    else: 
        parametro = "-c"   
    comando = ["ping", parametro, "1", ip] #Declarei essa variavel para poder passar os termos que vao ser jogados no cmd .
    resultado = subprocess.run(comando, capture_output=True) #Variavel vai jopgar no cmd via subprocess os tem na var comando e vai capturar oq sair de la pelo capture_output
    print(resultado)
