def chatbot():
  print("Oi eu sou o Nicolas🤓 estou aqui para informar, oferecer suporte e concientizar sobre o Transtorno do Espectro Autista() . Digite:")
  print("1 - Sobre o Autismo")
  print("2 - Graus de Autismo")
  print("3 - Tratamentos")
  print("4 - Mais Informações")

  opcao = input()

  if opcao == "1":
    sobre_autismo()
  elif opcao == "2":
    graus_autismo()
  elif opcao == "3":
    tratamentos()
  elif opcao == "4":
    mais_informacoes()
  else:
    print("Opção inválida. Tente novamente.")
    chatbot()

def sobre_autismo():
  print("O autismo, também conhecido como Transtorno do Espectro Autista (TEA), é uma condição de neurodesenvolvimento que afeta a maneira como as pessoas percebem e interagem com o mundo ao seu redor.")
  print("Pessoas com autismo podem ter dificuldades em: ")
  print("- Comunicação e interação social")
  print("- Comportamento repetitivo e interesses restritos")
  print("- Processamento sensorial")
  print("O autismo é um espectro, o que significa que a gravidade dos sintomas pode variar muito de pessoa para pessoa.")

  print("\nDeseja saber mais sobre os graus do autismo (2)?")
  print("Digite 'sim' ou 'não':")

  resposta = input()

  if resposta.lower() == "sim":
    graus_autismo()
  else:
    chatbot()

def graus_autismo():
  print("O Transtorno do Espectro Autista (TEA) é dividido em três níveis de gravidade, de acordo com os critérios do Manual Diagnóstico e Estatístico de Transtornos Mentais (DSM-5):")
  print("- Nível 1: Necessidade de Suporte Leve")
  print("- Nível 2: Necessidade de Suporte Moderado")
  print("- Nível 3: Necessidade de Suporte Severo")
  print("A determinação do nível de gravidade é feita por um profissional qualificado, com base em uma avaliação abrangente que leva em consideração as habilidades e desafios da pessoa em diferentes áreas do desenvolvimento.")

  print("\nDeseja saber mais sobre os tratamentos para o autismo (3)?")
  print("Digite 'sim' ou 'não':")

  resposta = input()

  if resposta.lower() == "sim":
    tratamentos()
  else:
    chatbot()

def tratamentos():
  print("Atualmente, não existe cura para o autismo, mas existem diversos tratamentos que podem ajudar a melhorar a qualidade de vida das pessoas com essa condição.")
  print("Alguns dos principais tratamentos incluem:")
  print("- Terapia comportamental")
  print("- Fonoaudiologia")
  print("- Fisioterapia")
  print("- Terapia ocupacional")
  print("- Medicação (em alguns casos)")
  print("É importante ressaltar que o tratamento ideal para cada pessoa com autismo deve ser individualizado, levando em consideração suas necessidades e características específicas.")

  print("\nDeseja saber mais sobre onde encontrar mais informações sobre o autismo (4)?")
  print("Digite 'sim' ou 'não':")

  resposta = input()

  if resposta.lower() == "sim":
    mais_informacoes()
  else:
    chatbot()

def mais_informacoes():
  print("Existem diversas fontes de informações confiáveis sobre o autismo, como:")
  print("- Sociedade Brasileira de Pediatria (SBP): https://www.sbp.com.br/")
  print("- Associação Brasileira do Autismo (ABRA): https://www.facebook.com/abra.autismo/?locale=pt_BR")
  print("- Centro de Valorização da Vida (CVV): https://cvv.org.br/page/2/")
  print("Você também pode encontrar informações em sites de instituições de pesquisa e órgãos governamentais.")

  print("\nObrigado por conversar comigo! Espero ter ajudado a esclarecer suas dúvidas sobre o autismo.")

chatbot()
