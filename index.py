class Player:
    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATECANTE
        self.situation = "NORMAL"  # ou "EXPULSO"
        self.participate_in_game = False # ou True

    def showInfo(self):
        return f'Camisa {self.number} - {self.name} | {self.position}'

    def hasSendOff(self):
        return bool(self.situation == 'EXPULSO')

    def getParticipation(self):
        return self.participate_in_game

    def setPlayerParticipation(self, value):
        self.participate_in_game = value

    def setExpulsion(self):
        self.situation = 'EXPULSO'

def readList(list, title, withIndex):
    print(title)
    for index, item in enumerate(list):
        if withIndex:
            print(f'{index+1}) {item.showInfo()}')
        else:
            print(item.showInfo())


def generatePlayerByInfoArr(infoArr):
    number = infoArr[0]
    name = infoArr[1]
    position = infoArr[2]

    return Player(name, number, position)


def populatePlayerList(list = []):
    if len(list) == 0:
        with open('convocados.txt') as file:
            filePlayers = file.read().split('\n')

            for filePlayer in filePlayers:
                infoArr = filePlayer.split(':')

                player = generatePlayerByInfoArr(infoArr)
                list.append(player)
        
        print('Arquivo foi lido com sucesso!\nAgora voce ja pode escalar o seu time.')
    else:
        print('Voce ja escolheu essa opcao!\nPor favor, escolha outra opcao do menu.')

def selectPlayers(playersList, selectedPlayersList, reservedPlayersList):
    playersOptions = []

    if len(selectedPlayersList) != 0 and len(reservedPlayersList) != 0:
        print('Voce ja escolheu essa opcao!\nPor favor, escolha outra opcao do menu.')
    elif len(playersList) == 0:
        print('Voce nao leu o arquivo!\nPor favor, primeiro selecione a primeira opcao do menu')
    else:
        for player in playersList:
            playersOptions.append(player)


        for i in range(11):
            print(f'Selecione os jogadores para jogar a partida:\n')
            print(f'Jogadores disponiveis:')

            readList(playersOptions, 'Jogadores disponiveis', True)

            selectedIndex = int(input('Selecione um jogador:')) - 1
            selectedPlayer = playersOptions[selectedIndex]
            
            selectedPlayer.setPlayerParticipation(True)
            selectedPlayersList.append(selectedPlayer) 
            playersOptions.pop(selectedIndex)
        
        for player in playersOptions:
            reservedPlayersList.append(player)
        

        print('Time escalado com sucesso!')


def substution(selectedPlayersList, reservedPlayersList):
    if len(selectedPlayersList) == 0 and len(reservedPlayersList) == 0:
        print('Voce primeiro tem que escalar o time.\nSelecione a segunda opcao do menu')
    else:
        readList(selectedPlayersList, 'Jogadores em campo:', True)

        oldPlayerIndex = int(input('Selecione um jogador para substituir:')) - 1

        readList(reservedPlayersList, 'Jogadores no banco:', True)

        newPlayerIndex = int(input('Selecione um jogador para entrar em campo:')) - 1

        oldPlayer = selectedPlayersList[oldPlayerIndex]
        newPlayer = reservedPlayersList[newPlayerIndex]

        newPlayer.setPlayerParticipation(True)

        selectedPlayersList.pop(oldPlayerIndex)
        selectedPlayersList.insert(oldPlayerIndex, newPlayer)
        
        reservedPlayersList.pop(newPlayerIndex)
        reservedPlayersList.insert(newPlayerIndex, oldPlayer)

        print('Substituição feita com sucesso!')


def expulsion(selectedPlayersList, reservedPlayersList): 
    if len(selectedPlayersList) == 0 and len(reservedPlayersList) == 0:
        print('Voce primeiro tem que escalar o time.\nSelecione a segunda opcao do menu')
    else: 
        readList(selectedPlayersList, 'Jogadores em campo:', True)

        playerIndex = int(input('Selecione o jogador que sera expulso: ')) - 1
        player = selectedPlayersList[playerIndex]

        player.setExpulsion()
  
        selectedPlayersList.pop(playerIndex)
        reservedPlayersList.append(player)

        print('Expulsão feita com sucesso!')

def savePlayerInFile(playersList, selectedPlayersList, reservedPlayersList):
    if len(selectedPlayersList) == 0 and len(reservedPlayersList) == 0:
        print('Voce primeiro tem que escalar o time.\nSelecione a segunda opcao do menu')
    else: 
        file = open("todosjogadores.txt", "a")
        textToFile = []

        textToFile.append('=== RESUMO DA PARTIDA ===\n')

        textToFile.append('+++ Todos os jogadores +++\n')
        for player in playersList:
            textToFile.append(f'* {player.showInfo()}\n')

        textToFile.append('\n')
        
        textToFile.append('+++ Jogadores que terminaram o jogo escalado +++\n')
        for player in selectedPlayersList:
            textToFile.append(f'* {player.showInfo()}\n')
        
        textToFile.append('\n')
        
        textToFile.append('+++ Jogadores que participaram do jogo +++\n')
        for player in selectedPlayersList:
            textToFile.append(f'* {player.showInfo()}\n')
        for player in reservedPlayersList:
            if player.getParticipation():
                textToFile.append(f'* {player.showInfo()}\n')

        textToFile.append('\n')

        textToFile.append('+++ Jogadores que foram expulsos +++\n')
        for player in reservedPlayersList:
            if player.hasSendOff():
                textToFile.append(f'* {player.showInfo()}\n')

        textToFile.append('\n')

        textToFile.append('+++ Jogadores que foram para o banco de reserva +++\n')
        for player in reservedPlayersList:
            if player.getParticipation():
                textToFile.append(f'* {player.showInfo()}\n')

        file.writelines(textToFile)
        print('O resumo da partida foi salvo dentro do arquivo "todosjogadores.txt"!')
        







menu = '''
MENU
======
1- Ler arquivo de jogadores
2- Escalar time
3- Realizar Substiuição
4- Expulsão
5- Imprimir escalação
'''


def init():
    option = ''
    players = []
    selectedPlayers = []
    reservedPlayers = []

    while option != 'fim':
        print(menu)
        option = input('Selecione uma opção do menu:')
        print('\n################################\n')
        if option == '1':
            populatePlayerList(players)
            pass
        elif option == '2':
            selectPlayers(players, selectedPlayers, reservedPlayers)
        elif option == '3':
            substution(selectedPlayers, reservedPlayers)
        elif option == '4':
            expulsion(selectedPlayers, reservedPlayers)
        elif option == '5':
            savePlayerInFile(players, selectedPlayers, reservedPlayers)
        elif option.lower() == 'fim':
            break

        print('\n################################\n')


init()