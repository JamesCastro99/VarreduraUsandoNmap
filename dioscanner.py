import nmap

scanner = nmap.PortScanner()

print("Seja Bem Vindo ao DIOScanner")
print('<', '-' * 30, '>')

ip = input("Digite o IP a ser varrido: ")
print("O IP digitado foi: ", ip)
type(ip)

menu = input("""\n Escolha o tipo de varredura a ser realizada
            1 -> Varredura do Tipo SYN
            2 -> Varredura do Tipo UDP
            3 -> Varredura do Tipo Intensa
            Digite a opção escolhida: """)
print("\nA opção escolhida foi", menu)

if menu == '1':
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1 - 1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())
elif menu == '2':
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1 - 1024', '-v sU')
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['udp'].keys())
elif menu == '3':
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1 - 1024', '-v sC')
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())
else:
    print("Escolha uma opção correta!!!")