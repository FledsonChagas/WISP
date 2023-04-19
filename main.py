# Importação das bibliotecas necessárias
import wifimgr
import gc
import machine
import esp
from machine import Pin
try:
    import usocket as socket
except:
    import socket

# Conexão à rede Wi-Fi usando a biblioteca wifimgr
wlan = wifimgr.get_connection()

# Caso não consiga estabelecer a conexão, o programa ficará preso em um loop infinito
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass

print("ESP OK")

# Gerenciamento de memória
gc.collect()
esp.osdebug(None)

# Criação da lista de pinos do ESP8266 como saída (output)
pins = [Pin(i, Pin.OUT) for i in [5, 4, 0, 2, 14, 12, 13, 15]]

# Função para ler o conteúdo do arquivo HTML
def read_html_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return None

# Função para tratar a requisição recebida
def handle_request(request):
    # Itera sobre a lista de pinos e verifica se algum comando foi enviado para controlar os relés
    for i, pin in enumerate(pins, start=1):
        pin_on = request.find(f'/?relay{i}=1')
        pin_off = request.find(f'/?relay{i}=0')
        if pin_on == 6:
            print(f'RELAY {i} ON')
            pin.value(1)
        if pin_off == 6:
            print(f'RELAY {i} OFF')
            pin.value(0)

    # Lê o conteúdo do arquivo HTML e define a resposta HTTP
    html_content = read_html_file("index.html")
    
    if html_content is not None:
        response = "HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n" + html_content
    else:
        response = "HTTP/1.1 500 Internal Server Error\nContent-Type: text/plain\nConnection: close\n\nError reading HTML file"
    
    return response

# Configuração do socket para aceitar conexões
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 80))
    s.listen(5)

except OSError as e:
    machine.reset()

# Loop principal para aceitar conexões e responder às requisições
while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('Content = %s' % request)
        
        # Chama a função handle_request para processar a requisição e obter a resposta
        response = handle_request(request)
        
        # Envia a resposta e fecha a conexão
        conn.sendall(response.encode())
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')
