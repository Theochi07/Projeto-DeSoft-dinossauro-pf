# Dino Rush

Sabe o dinossauro que aparece no Google Chrome quando a internet cai? O Dino Rush é a nossa versão dele, feita em Python com **pygame** para o Projeto Final de Design de Software.

## Autores
- João Henrique Gusmão
- Theo Chi
- Gabriel Dias

## Como funciona
O dinossauro corre sozinho, e o seu trabalho é desviar do que aparece pela frente:
- **Cactos**: aperte a **SETA PARA CIMA** para pular.
- **Pterodáctilos** (a partir da fase 2): segure a **SETA PARA BAIXO** para abaixar.

A cada 200 pontos você passa de fase e o jogo acelera, até a fase 10.
De 30 em 30 segundos surge um **escudo azul (S)**. Pegou, o dino aguenta uma batida.
Chegou a **2500 pontos**? Você venceu.

Tem tela de menu, de instruções, de game over e de vitória. Dá para pausar com a tecla **P**, e o jogo guarda o recorde enquanto estiver aberto.
As pernas do dino, as asas do pterodáctilo e as nuvens são animadas, e tem música de fundo e efeitos sonoros.

## Como jogar
1. Instale o pygame (só precisa fazer isso uma vez):
   ```
   pip install pygame-ce
   ```
   (O `pygame-ce` funciona igualzinho ao `pygame` e já tem versão pronta para o Python mais novo.)
2. Na pasta do projeto, rode o arquivo **dino_rush.py**:
   ```
   python dino_rush.py
   ```
Rode sempre a partir da pasta principal do projeto, a mesma onde está o `dino_rush.py`.

## Como o código está organizado
Cada parte do jogo tem a sua pasta, e cada tela tem o seu arquivo:

```
dino_rush.py               -> ARQUIVO QUE DEVE SER EXECUTADO (abre a janela e troca entre as telas)
config.py                  -> constantes: tamanho da janela, física, dificuldade, cores e estados

tela/menu.py               -> tela de início
tela/instrucoes.py         -> tela de instruções
tela/jogo.py               -> tela do jogo (loop principal da partida)
tela/game_over.py          -> tela de fim de jogo
tela/vitoria.py            -> tela de vitória

mecanica/movimento.py      -> pulo, gravidade, abaixar e movimento dos obstáculos
mecanica/colisao.py        -> verifica se dois objetos se encostam
mecanica/fases.py          -> fase atual, velocidade de cada fase e intervalo entre obstáculos

personagem/dino.py         -> criar o dinossauro, carregar a imagem e desenhar
personagem/personagem.png  -> imagem do T-Rex
obstaculos/obstaculos.py   -> criar e desenhar cactos, pterodáctilos e o escudo
cenario/cenario.py         -> céu, sol, nuvens, chão e textos
sons/sons.py               -> efeitos sonoros e música de fundo (os .wav ficam nessa pasta)
```

Por dentro, o jogo é feito de funções, listas e dicionários. O dinossauro e cada obstáculo são dicionários.

## Quem fez o quê
| Integrante | Pastas e arquivos |
|---|---|
| João Henrique Gusmão | `tela/` (um commit por tela) |
| Theo Chi | `mecanica/`, `personagem/`, `obstaculos/` |
| Gabriel Dias | `cenario/`, `sons/`, `config.py`, `dino_rush.py`, `README.md` |

## Créditos
- `personagem/personagem.png`: T-Rex original em pixel art, desenhado para o jogo. Quer trocar o personagem? É só colocar outro PNG com fundo transparente no lugar desse arquivo.
- `pulo.wav`, `fase.wav`, `batida.wav` e `musica.wav`: gerados por programa pelo grupo.