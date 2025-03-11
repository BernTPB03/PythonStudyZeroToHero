import json
import random

tasks = []
data_file = "tasks.json"

def load_tasks():
    global tasks
    try:
        with open(data_file, "r", encoding="utf-8") as file:  # Especificando a codificação
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

def save_tasks():
    with open(data_file, "w", encoding="utf-8") as file:  # Especificando a codificação
        json.dump(tasks, file, indent=4)

def add_task():
    task = input("Digite a nova tarefa: ")
    tasks.append({"task": task, "completed": False})
    save_tasks()
    print("Tarefa adicionada com sucesso!")

def list_tasks():
    if not tasks:
        print("Nenhuma tarefa pendente.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{idx}. {status} {task['task']}")

def complete_task():
    list_tasks()
    try:
        index = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks()
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def delete_task():
    list_tasks()
    try:
        index = int(input("Digite o número da tarefa a remover: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks()
            print(f"Tarefa '{removed['task']}' removida.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    load_tasks()
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        choice = input("Escolha uma opção: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# Jogo de Adivinhação
def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    while True:
        try:
            chute = int(input("Adivinhe o número (entre 1 e 100): "))
            tentativas += 1
            if chute < numero_secreto:
                print("Muito baixo!")
            elif chute > numero_secreto:
                print("Muito alto!")
            else:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                break
        except ValueError:
            print("Digite um número válido.")


# Conversor de Unidades
def conversor_unidades():
    unidades = {
        "1": ("Quilômetros para Milhas", 0.621371),
        "2": ("Milhas para Quilômetros", 1.60934),
        "3": ("Quilos para Libras", 2.20462),
        "4": ("Libras para Quilos", 0.453592),
        "5": ("Celsius para Fahrenheit", lambda c: (c * 9 / 5) + 32),
        "6": ("Fahrenheit para Celsius", lambda f: (f - 32) * 5 / 9)
    }

    print("Escolha uma conversão:")
    for key, (desc, _) in unidades.items():
        print(f"{key}. {desc}")
    opcao = input("Digite a opção desejada: ")
    if opcao in unidades:
        valor = float(input("Digite o valor: "))
        descricao, fator = unidades[opcao]
        if callable(fator):
            resultado = fator(valor)
        else:
            resultado = valor * fator
        print(f"{descricao}: {resultado}")
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    while True:
        print("\n1. Gerenciador de Tarefas")
        print("2. Jogo de Adivinhação")
        print("3. Conversor de Unidades")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            menu()
        elif opcao == "2":
            jogo_adivinhacao()
        elif opcao == "3":
            conversor_unidades()
        elif opcao == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")
