def listar_tarefas():
    tarefas = [
        "Configurar o repositorio Git",
        "Criar os artefatos do projeto",
        "Registrar a nova versao"
    ]

    print("Projeto Controle de Tarefas")
    print("---------------------------")

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"{numero}. {tarefa}")


if __name__ == "__main__":
    listar_tarefas()