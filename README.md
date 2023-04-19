<!DOCTYPE html>
<html lang="pt-br">
<head>
     <link rel="icon" type="image/png" href="https://i.ibb.co/4KgLqg4/WISPfavicon.png"/>
    <link href="https://i.ibb.co/rfPgX6r/apple-touch-icon.png" rel="apple-touch-icon" />
    <link href="https://i.ibb.co/QKSDBmF/apple-touch-icon-76x76.png" rel="apple-touch-icon" sizes="76x76"/>
    <link href="https://i.ibb.co/8gbgPwf/apple-touch-icon-120x120.png" rel="apple-touch-icon" sizes="120x120"/>
    <link href="https://i.ibb.co/2YV2wmH/apple-touch-icon-152x152.png" rel="apple-touch-icon" sizes="152x152"/>
    <link href="https://i.ibb.co/ssb2v69/apple-touch-icon-180x180.png" rel="apple-touch-icon" sizes="180x180"/>
    <link href="https://i.ibb.co/C6H747F/icon-hires.png" rel="icon" sizes="192x192" />
    <link href="https://i.ibb.co/X2b8Fxx/icon-normal.png" rel="icon" sizes="128x128" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black" />
    <link rel="stylesheet" href="http://code.jquery.com/mobile/1.3.0/jquery.mobile-1.3.0.min.css" />
   </head>
<body>
       <h1 class="ui-title" role="heading" aria-level="1"><center><a class="ui-link"><img src="https://i.ibb.co/n0FYr7w/WISP-logo-5050png.png" alt="WISP-logo-5050png" border="0"></a></center>     
       </h1>
    <div data-role="page" id="main">
        <div data-role="header">
            <h1>Projeto WISP</h1>
        </div>
         <div data-role="content">
            <h2>Resumo</h2>
            <p>O projeto WISP é uma aplicação em Python para microcontroladores ESP8266 que permite controlar relés através de uma interface web. Ele utiliza a biblioteca wifimgr para se conectar à rede Wi-Fi e permite o controle dos pinos de saída do ESP8266 para acionar relés.</p>
            <h3>Principais funcionalidades:</h3>
            <ol>
                <li>Conexão Wi-Fi: A conexão é estabelecida utilizando a biblioteca wifimgr, que gerencia a conexão Wi-Fi do dispositivo.</li>
                                <li>Gerenciamento de memória: O projeto utiliza gc.collect() e esp.osdebug(None) para otimizar o uso da memória disponível no microcontrolador.</li>
                <li>Controle dos pinos de saída: O projeto configura os pinos do ESP8266 como saída (output) e permite controlá-los através de requisições HTTP.</li>
                <li>Leitura de arquivos HTML: A função read_html_file lê um arquivo HTML do sistema de arquivos e retorna seu conteúdo.</li>
                <li>Manipulação de requisições HTTP: A função handle_request processa as requisições recebidas, verifica se algum comando foi enviado para controlar os relés e define a resposta HTTP a ser enviada.</li>
                <li>Servidor Web: O projeto utiliza um socket para aceitar conexões e responder às requisições HTTP. Um loop principal aceita conexões, processa as requisições chamando handle_request e envia a resposta.</li>
            </ol>
            <p>Este projeto pode ser usado como base para criar sistemas de automação residencial ou industrial, permitindo o controle de dispositivos conectados a relés através de uma interface web.</p>
        </div>
        <div data-role="footer">
            <h4>Projeto WISP &copy; 2023</h4>
        </div>
    </div>
</body>
</html>
