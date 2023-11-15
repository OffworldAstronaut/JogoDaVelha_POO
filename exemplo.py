# Importa todas as classes necessárias 
from JogoVelha import JogadorComputador, JogadorHumano, JogoVelha

# Dois jogadores humanos
jogador_1 = JogadorHumano("X")
jogador_2 = JogadorHumano("O") 

# Cria o primeiro jogo 
jogo1 = JogoVelha(jogador_1, jogador_2)

# Executa o primeiro jogo 
jogo1.jogar()

# Um jogador humano e uma máquina 
jogador_3 = JogadorComputador("X", "aleatoria")
jogador_4 = JogadorHumano("O") 

# Cria o segundo jogo 
jogo2 = JogoVelha(jogador_3, jogador_4)

# Executa o segundo jogo 
jogo2.jogar()