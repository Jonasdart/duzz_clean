### O Duzz Clean: (Referência à Does Clean)

O Sistema Duzz Clean é um controlador de higiene de veículos, baseando seu controle na quilometragem rodada e outras análises coletadas ao decorrer do dia.
O veículo é cadastrado no sistema por placa, modelo, marca etc.

O sistema conta com um raspberry Zero (controller) que faz a comunicação com os dispersores no momento que o app, conectado ao controller via Bluetooth, solicita nova higienização.

O app irá fazer a coleta dos dados de navegação (Metragem rodada) via GPS e solicitar que uma API calcule a proxima limpeza, levando em consideração o momento da limpeza anterior.

Este app ainda pode ser usado para agendar ou verificar informações das limpezas realizadas, escolher qual ambiente do carro higiênizar e, entre outras coisas, solicitar limpeza imediata. Totalmente aplicável, por exemplo, aos motoristas de aplicativos que ao encerrrar corrida não têm a possibilidade de higienizar todo veículo ou somente o banco que foi utilizado pois já está com outro passageiro para encontrar.

### Duzz Clean Interfaces:
    -> Motorista
    -> Passageiro

#### Duzz Clean Motorista Features:

    -> Limpeza automatizada via dispenser controlado por raspberry ou raspberry + arduino
    
    -> Fazer o controle via smartphone.

    -> Receber notificações sobre suas limpezas recomendadas dependendo da metragem rodada. Ou seja, após certa quantidade de km's rodados (Parâmetro do próprio usuário), o sistema recomendará nova higienização.
    
    -> Receber interações e enteragir com o passageiro
    
    -> Acompanhar seu Rating e recomendações dos passageiros.
    
    -> Acompanhar os dados de limpeza via aplicativo, para saber quantas foram realizadas ou quanto resta de limpeza no refil.

#### Duzz Clean Passageiro Features:

    -> Poderá acompanhar quando foram realizadas as últimas limpezas utilizando Duzz Clean lendo QR code que o motorista pode colar no veículo;

    -> Avaliar a limpeza do veículo;
    
    -> Solicitar higienização do veículo antes mesmo de entrar no mesmo, tendo oportunidade de interação com o motorista.

    -> Ler notificações dos aplicativos de viagens, como "Uber", "99", etc. para identificar a placa e modelo do carro e informar, de maneira instantânea, se este carro possui o sistema de higienização automatizada da duzz e quando foi a última limpeza realizada.


