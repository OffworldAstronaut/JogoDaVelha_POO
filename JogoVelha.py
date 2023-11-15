# Tipagem especial 
from typing import Optional, List, Tuple
# Módulo random para necessidades aleatórias
from random import randint 

class Jogador:
    """Classe abstrata que engloba os dois tipos possíveis de jogadores: humano e computador"""
    def __init__(self, simbolo : str) -> None:
        """Instancia um objeto da classe Jogador 

        Args:
            simbolo (str): Símbolo associado ao jogador, pode ser 'X' ou 'O' 
        """        
        self.simbolo = simbolo

    def add_simbolo(self, novosimbolo : str) -> None: 
        """Atribui um novo símbolo ao jogador (setter)

        Args:
            novosimbolo (str): Novo símbolo a ser adicionado
        """        
        self.simbolo = novosimbolo

class JogadorHumano(Jogador):
    """Classe que representa um jogador humano, especialização da classe Jogador."""    
    def __init__(self, simbolo : str): 
        """Inicializa uma instância da classe

        Args:
            simbolo (str): Símbolo do jogador
        """        
        super().__init__(simbolo)
        self.simbolo = simbolo 

    def fazer_jogada(self) -> Tuple[int, int]: 
        """Possibilita o jogador humano a fazer uma jogada no tabuleiro 

        Returns:
            pos (Tuple[int, int]): Tupla contendo a posição no tabuleiro que a jogada será feita 
        """        
        print(f"Jogador: {self.simbolo}")
        pergunta_jogada = int(input("> Posição: "))

        # Seleciona a tupla que representa uma posição no tabuleiro de acordo com a posição escolhida pelo jogador
        if pergunta_jogada == 0:
            pos = (0, 0)
        elif pergunta_jogada == 1: 
            pos = (0, 1)
        elif pergunta_jogada == 2: 
            pos = (0, 2)
        elif pergunta_jogada == 3: 
            pos = (1, 0)
        elif pergunta_jogada == 4: 
            pos = (1, 1) 
        elif pergunta_jogada == 5: 
            pos = (1, 2) 
        elif pergunta_jogada == 6: 
            pos = (2, 0) 
        elif pergunta_jogada == 7: 
            pos = (2, 1) 
        else: 
            pos = (2, 2)
    
        return pos 

class JogadorComputador(Jogador):
    """Classe que representa um jogador que é um computador, especialização da classe Jogador.
    """    
    def __init__(self, simbolo : str, estrategia : str): 
        """Inicializa uma instância da classe

        Args:
            simbolo (str): Símbolo associado ao jogador 
            estrategia (str): Estratégia escolhida para a máquina
        """        
        super().__init__(simbolo)
        self.simbolo = simbolo 
        self.estrategias = ["aleatoria", "inteligente", "darksouls"]
        if estrategia in self.estrategias:
            self.estrategia = estrategia
        else: 
            self.estrategia = "aleatoria"

    def fazer_jogada(self) -> Tuple[int, int]: 
        """Possibilita o computador a fazer uma jogada no tabuleiro

        Returns:
            Tuple[int, int]: Tupla contendo a posição no tabuleiro que a jogada será feita 
        """
        # Estratégia aleatória 
        if self.estrategia == "aleatoria":
            # Escolhe aleatoriamente uma linha 
            linha_aleatoria = randint(0, 2)
            # Escolhe aleatoriamente uma coluna 
            coluna_aleatoria = randint(0, 2)
            # Gera a tupla "posição"
            pos = (linha_aleatoria, coluna_aleatoria)

        return pos

class JogoVelha: 
    """Classe principal. Aplica todas as outras classes para fazer com que o jogo seja executado. 
    """    
    def __init__(self, j1 : Jogador, j2 : Jogador) -> None:
        """Instancia um jogo-da-velha entre dois jogadores 

        Args:
            j1 (Jogador): 'Jogador 1', o primeiro jogador
            j2 (Jogador): 'Jogador 2', o segundo jogador 
        """        
        # lista que armazena os dois jogadores  
        self.jogadores = [j1, j2]
        # objeto Tabuleiro: o jogo não existe sem o tabuleiro 
        self.tabuleiro = Tabuleiro() 
        # variável para marcar de qual turno é a vez: 0 se for o jogador um e 1 se for o jogador 2; -1 é o caso inicial
        self.turno = -1

    def jogador_atual(self) -> Jogador:
        """Retorna o jogador que deverá jogar agora

        Returns:
            Jogador: Objeto "Jogador", que deverá jogar agora
        """
        if self.turno == -1:
            # Ao começar o jogo, o jogador 1 tem a vez, sempre 
            self.turno = 0
            return self.jogadores[0]

        elif self.turno == 0: 
            # se a vez era do jogador 1, a vez agora é do jogador 2 
            self.turno = 1 
            return self.jogadores[1]
        else: 
            # se a vez era do jogador 2, a vez agora é do jogador 1  
            self.turno = 0 
            return self.jogadores[0]
        
    def jogar(self) -> None:
        """Simula o jogo propriamente dito. 
        """        
        while True: 
            # Seleciona o jogador atual 
            j_atual = self.jogador_atual()
            while True:
                # Imprime o tabuleiro na tela 
                self.tabuleiro.imprimir_tabuleiro()
                # Pede a jogada ao jogador atual por meio da classe Jogador (fazer_jogada)
                jogada_atual = j_atual.fazer_jogada()
                # Marca a jogada no tabuleiro, se a casa escolhida estiver vazia
                if self.tabuleiro.verificar_casa_vazia(jogada_atual):
                    self.tabuleiro.marcar_casa(jogada_atual, j_atual.simbolo)
                    break
                # Caso contrário (casa prenchida), o usuário será notificado e terá que escolher outra jogada 
                else:
                    print("Essa casa já está preenchida!")
                    print()

            # Se as condições de vitória para o jogador 1 estiverem sido satisfeitas, anuncie sua vitória
            if self.checar_fim_de_jogo() == "j1": 
                print("FIM DE JOGO!")
                print(f"VITÓRIA DE {self.jogadores[0].simbolo}!")
                print()
                self.tabuleiro.imprimir_tabuleiro()
                break

            # Se as condições de vitória para o jogador 2 estiverem sido satisfeitas, anuncie sua vitória
            elif self.checar_fim_de_jogo() == "j2": 
                print("FIM DE JOGO!")
                print(f"VITÓRIA DE {self.jogadores[1].simbolo}!")
                print()
                self.tabuleiro.imprimir_tabuleiro()
                break

            # Se as condições de empate estiverem sido satisfeitas, anucie o empate 
            elif self.checar_fim_de_jogo() == "empate": 
                print("FIM DE JOGO!")
                print("EMPATE!")
                print()
                self.tabuleiro.imprimir_tabuleiro()
                break

    def checar_fim_de_jogo(self) -> Optional[str]:
        """Checa se o jogo acabou, retornando também o resultado caso verdade. 

        Returns:
            vitoria (Optional[str]): Marca a vitória ou empate do jogo atual: "j1", "j2" ou "empate"
        """
        # Lista dos jogadores 
        jogadores = self.jogadores 
        # Lista dos símbolos dos jogadores 
        simbolos_j = [jogadores[0].simbolo, jogadores[1].simbolo]
        # Variável para marcar o resultado do jogo, padrão "None"
        vitoria = None

        # condições de vitória para o jogador 1 (linhas)

        cond1_vitoria_j1 = self.tabuleiro.casas[0] == [simbolos_j[0], simbolos_j[0], simbolos_j[0]]
        cond2_vitoria_j1 = self.tabuleiro.casas[1] == [simbolos_j[0], simbolos_j[0], simbolos_j[0]]
        cond3_vitoria_j1 = self.tabuleiro.casas[2] == [simbolos_j[0], simbolos_j[0], simbolos_j[0]]

        # condições de vitória para o jogador 1 (colunas)

        cond4_vitoria_j1 = self.tabuleiro.casas[0][0] == simbolos_j[0] and self.tabuleiro.casas[1][0] == simbolos_j[0] and self.tabuleiro.casas[2][0] == simbolos_j[0]
        cond5_vitoria_j1 = self.tabuleiro.casas[0][1] == simbolos_j[0] and self.tabuleiro.casas[1][1] == simbolos_j[0] and self.tabuleiro.casas[2][1] == simbolos_j[0]
        cond6_vitoria_j1 = self.tabuleiro.casas[0][2] == simbolos_j[0] and self.tabuleiro.casas[1][2] == simbolos_j[0] and self.tabuleiro.casas[2][2] == simbolos_j[0]

        # condições de vitória para o jogador 1 (diagonais)

        cond7_vitoria_j1 = self.tabuleiro.casas[0][0] == simbolos_j[0] and self.tabuleiro.casas[1][1] == simbolos_j[0] and self.tabuleiro.casas[2][2] == simbolos_j[0]
        cond8_vitoria_j1 = self.tabuleiro.casas[0][2] == simbolos_j[0] and self.tabuleiro.casas[1][1] == simbolos_j[0] and self.tabuleiro.casas[2][0] == simbolos_j[0]

        # condições de vitória para o jogador 2 (linhas)

        cond1_vitoria_j2 = self.tabuleiro.casas[0] == [simbolos_j[1], simbolos_j[1], simbolos_j[1]]
        cond2_vitoria_j2 = self.tabuleiro.casas[1] == [simbolos_j[1], simbolos_j[1], simbolos_j[1]]
        cond3_vitoria_j2 = self.tabuleiro.casas[2] == [simbolos_j[1], simbolos_j[1], simbolos_j[1]]

        # condições de vitória para o jogador 2 (colunas)

        cond4_vitoria_j2 = self.tabuleiro.casas[0][0] == simbolos_j[1] and self.tabuleiro.casas[1][0] == simbolos_j[1] and self.tabuleiro.casas[2][0] == simbolos_j[1]
        cond5_vitoria_j2 = self.tabuleiro.casas[0][1] == simbolos_j[1] and self.tabuleiro.casas[1][1] == simbolos_j[1] and self.tabuleiro.casas[2][1] == simbolos_j[1]
        cond6_vitoria_j2 = self.tabuleiro.casas[0][2] == simbolos_j[1] and self.tabuleiro.casas[1][2] == simbolos_j[1] and self.tabuleiro.casas[2][2] == simbolos_j[1]

        # condições de vitória para o jogador 2 (diagonais)

        cond7_vitoria_j2 = self.tabuleiro.casas[0][0] == simbolos_j[1] and self.tabuleiro.casas[1][1] == simbolos_j[1] and self.tabuleiro.casas[2][2] == simbolos_j[1]
        cond8_vitoria_j2 = self.tabuleiro.casas[0][2] == simbolos_j[1] and self.tabuleiro.casas[1][1] == simbolos_j[1] and self.tabuleiro.casas[2][0] == simbolos_j[1]

        # arrays que armazenam as chaves True-False 

        cond_vitorias_j1 = [cond1_vitoria_j1, cond2_vitoria_j1, cond3_vitoria_j1, cond4_vitoria_j1, 
                            cond5_vitoria_j1, cond6_vitoria_j1, cond7_vitoria_j1, cond8_vitoria_j1]

        cond_vitorias_j2 = [cond1_vitoria_j2, cond2_vitoria_j2, cond3_vitoria_j2, cond4_vitoria_j2, 
                            cond5_vitoria_j2, cond6_vitoria_j2, cond7_vitoria_j2, cond8_vitoria_j2]
        
        # condições para verificar se houve vitória 

        # Se alguma das condições de vitória estiver sido satisfeita, o jogador 1 ganhou 
        if True in cond_vitorias_j1: 
            vitoria = "j1"

        # Se alguma das condições de vitória estiver sido satisfeita, o jogador 2 ganhou
        elif True in cond_vitorias_j2: 
            vitoria = "j2"

        # Se nenhuma das duas foi satisfeita e o tabuleiro estiver completamente preenchido, é um empate 
        elif self.tabuleiro.verificar_preenchimento(): 
            vitoria = "empate"

        return vitoria 

class Tabuleiro: 
    """Simula o tabuleiro do jogo.
    """    
    # números disponíveis das casas do tabuleiro 
    numeros_casas = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # inicializa um objeto tabuleiro criando uma matriz numpy
    def __init__(self) -> None: 
        # Cria primeiro uma lista de números de 0 a 8 e depois tranforma essa lista numa matriz 3 x 3 
        self.casas = [
            [0, 1, 2],
            [3, 4, 5], 
            [6, 7, 8]
        ]

    def verificar_casa_vazia(self, pos: Tuple[int, int]) -> bool:  
        """Verifica se uma dada casa do tabuleiro está vazia

        Args:
            pos (Tuple[int, int]): Tupla contendo a posição do tabuleiro a ser verificada

        Returns:
            bool: booleano indicando se a casa está vazia (True) ou não (False)
        """        
        if self.pegar_tabuleiro()[pos[0]][pos[1]] not in Tabuleiro.numeros_casas: 
            return False
        
        else: 
            return True

    def marcar_casa(self, pos : Tuple[int, int], simbolo : str) -> bool: 
        """Marca uma determinada casa do tabuleiro com o símbolo do jogador

        Args:
            pos (Tuple[int, int]): Posição a ser marcada 
            simbolo (str): Símbolo do jogador que está jogando
        """        
        # Marca uma casa com o símbolo do jogador. Deve verificar se a casa selecionada está vazia 
        self.casas[pos[0]][pos[1]] = simbolo

    def pegar_tabuleiro(self) -> List[List[str]]:
        """Retorna o tabuleiro em formato de uma lista de listas, com cada sub-lista sendo uma linha do tabuleiro

        Ex.: 

        [
            [X, O, X], 
            [X, O, O], 
            [O, X, O]
        ]

        Returns:
            lista_tabuleiro (List[List[str]]): Tabuleiro no formato desejado
        """        
        # Retorna o tabuleiro no formato de uma lista de listas, onde cada sub-lista é uma linha do tabuleiro 
        # Ex: 
        # [
        # [X, O, X],
        # [X, O, O], 
        # [O, X, O]
        # ]
        lista_tabuleiro = self.casas
        return lista_tabuleiro

    def imprimir_tabuleiro(self) -> None: 
        """Imprime o tabuleiro na tela para o jogador, de forma organizada
        """        
        # imprime o tabuleiro na tela de forma organizada 
        print(
            f"""

              |      |
          {self.pegar_tabuleiro()[0][0]}   |   {self.pegar_tabuleiro()[0][1]}  |   {self.pegar_tabuleiro()[0][2]}
              |      |
        ---------------------
              |      |
          {self.pegar_tabuleiro()[1][0]}   |   {self.pegar_tabuleiro()[1][1]}  |   {self.pegar_tabuleiro()[1][2]}
              |      |
        ---------------------
              |      |
           {self.pegar_tabuleiro()[2][0]}  |   {self.pegar_tabuleiro()[2][1]}  |   {self.pegar_tabuleiro()[2][2]}
              |      |
            
            """)

    def verificar_preenchimento(self) -> bool: 
        """Verifica se o tabuleiro está completamente preenchido, uma condição necessária para determinar se o jogo está empatado

        Returns:
            bool: Booleano indicando se o tabuleiro está completamente preenchido ou não (True, se sim, False, caso contrário)
        """        
        # variáveis booleanas para verificar o preenchimento de cada linha 
        linha1_preenchida = not self.verificar_casa_vazia((0, 0)) and not self.verificar_casa_vazia((0, 1)) and not self.verificar_casa_vazia((0, 2))
        linha2_preenchida = not self.verificar_casa_vazia((1, 0)) and not self.verificar_casa_vazia((1, 1)) and not self.verificar_casa_vazia((1, 2))
        linha3_preenchida = not self.verificar_casa_vazia((2, 0)) and not self.verificar_casa_vazia((2, 1)) and not self.verificar_casa_vazia((2, 2))

        # se o tabuleiro inteiro estiver preenchido (todas as variáveis verdadeiras), marque o tabuleiro como preenchido
        if linha1_preenchida and linha2_preenchida and linha3_preenchida:
            return True

        else: 
            return False