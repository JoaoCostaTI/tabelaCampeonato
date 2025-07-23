#Lista com os times
times = [
    {
      "posicao": 1,
      "nome": "Cruzeiro",
      "pontos": 45,
      "jogos": 15,
      "vitorias": 10,
      "empates": 3,
      "derrotas": 2,
      "gols_pro": 27,
      "gols_contra": 9,
      "saldo": 18
    },
    {
      "posicao": 2,
      "nome": "Flamengo",
      "pontos": 30,
      "jogos": 14,
      "vitorias": 9,
      "empates": 3,
      "derrotas": 2,
      "gols_pro": 27,
      "gols_contra": 5,
      "saldo": 22
    },
    {
      "posicao": 3,
      "nome": "Bragantino",
      "pontos": 27,
      "jogos": 15,
      "vitorias": 8,
      "empates": 3,
      "derrotas": 4,
      "gols_pro": 18,
      "gols_contra": 15,
      "saldo": 3
    },
    {
      "posicao": 4,
      "nome": "Palmeiras",
      "pontos": 26,
      "jogos": 13,
      "vitorias": 8,
      "empates": 2,
      "derrotas": 3,
      "gols_pro": 16,
      "gols_contra": 11,
      "saldo": 5
    },
    {
      "posicao": 5,
      "nome": "Botafogo",
      "pontos": 25,
      "jogos": 14,
      "vitorias": 7,
      "empates": 4,
      "derrotas": 3,
      "gols_pro": 17,
      "gols_contra": 7,
      "saldo": 10
    }
  ]

#estrutura para cadastro dos times
dadosTimes = {}

#Formatação da tabela
def tabelaFormatada():
    print(" -"*33)
    print(f'|{"Classificação":<20} {"P":^5}{"J":^5}{"V":^5}{"E":^5}{"D":^5}{"GP":^5}{"GC":^5}{"SG":^5}{"%":^5}|')
    print(" -"*33)

tabelaFormatada()

for time in times:
    #Calculando aproveitamento
    pontosPossiveis = time['jogos'] * 3
    pontosConquistados = time["pontos"]
    aproveitamento = int((pontosConquistados / pontosPossiveis) * 100)

    print(f'|{time["posicao"]:<1} {time["nome"]:<19}{time["pontos"]:^5}{time["jogos"]:^5}{time["vitorias"]:^5}{time["empates"]:^5}{time["derrotas"]:^5}{time["gols_pro"]:^5}{time["gols_contra"]:^5}{time["saldo"]:^5}{aproveitamento:^5}')