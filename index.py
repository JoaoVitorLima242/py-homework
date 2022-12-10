class Player:
    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position
        self.played_in_game = False

    def showInfo(self):
        return f'Camisa {self.number} - {self.name} | {self.position}'

    def setPlayerParticipation(self, value):
        self.played_in_game = value

def readList(list, title):
    print(title)
    for item in list:
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

            for index, player in enumerate(playersOptions):
                print(f'{index+1}) {player.showInfo()}')

            selectedIndex = int(input('Selecione um jogador:')) - 1
            selectedPlayer = playersOptions[selectedIndex]

            selectedPlayersList.append(selectedPlayer) 
            playersOptions.pop(selectedIndex)
        
        for player in playersOptions:
            reservedPlayersList.append(player)


def init():
    option = ''
    players = []
    selectedPlayers = []
    reservedPlayers = []

    while option != 'fim':
        print('''
MENU
======
1- Ler arquivo de jogadores
2- Escalar time
3- Realizar Substiuição
4- Expulsão
5- Imprimir escalação
''')
        option = input('Selecione uma opção do menu:')
        print('\n################################\n')
        if option == '1':
            populatePlayerList(players)
            pass
        elif option == '2':
            selectPlayers(players, selectedPlayers, reservedPlayers)
        elif option == '5':
            readList(players, 'LISTA DE JOGADORES')
            readList(selectedPlayers, 'LISTA DE JOGADORES ESCALADOS')
            readList(reservedPlayers, 'LISTA DE JOGADORES RESERVA')
        elif option.lower() == 'fim':
            break

        print('\n################################\n')


init()