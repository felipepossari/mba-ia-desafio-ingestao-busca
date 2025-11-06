from search import search_prompt
from ingest import check_variables


def main():
    check_variables()
    print("Faça sua pergunta: (Pressione Ctrl+D para sair)\n")
    while True:
        question = input("PERGUNTA: ")
        result_message = search_prompt(question)
        if not result_message:
            raise RuntimeError("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        print(f"RESPOSTA: {result_message.content}")
        print("_" * 50)


if __name__ == "__main__":
    main()
