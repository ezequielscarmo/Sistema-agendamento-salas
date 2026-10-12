# Sistema de Agendamento de Salas
# Projeto Engenharia de Software - Ezequiel do Carmo

salas = []

def cadastrar_sala(nome):
    salas.append({"nome": nome, "agendamentos": []})
    print(f"Sala {nome} cadastrada!")

def agendar_sala(nome_sala, horario):
    for sala in salas:
        if sala["nome"] == nome_sala:
            if horario in sala["agendamentos"]:
                print(f"ERRO: {nome_sala} ja ocupada as {horario}")
                return False
            sala["agendamentos"].append(horario)
            print(f"Sala {nome_sala} agendada para {horario}")
            return True
    print("Sala nao encontrada")
    return False

# Testes
cadastrar_sala("Sala 101")
agendar_sala("Sala 101", "14:00")
agendar_sala("Sala 101", "14:00")  # testa conflito
