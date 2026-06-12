class AnonymousSurvey:
    """Colete respostas anônimas para uma pergunta de pesquisa."""

    def __init__(self, question):
        """Armazene uma pergunta e prepare-se para armazenar as respostas."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Mostre a pergunta da pesquisa."""
        print(self.question)

    def store_response(self, new_response):
        """Armazene uma única resposta à pesquisa."""
        self.responses.append(new_response)
        
    def show_results(self):
        """Mostre todas as respostas que foram dadas."""
        print("Resultados da pesquisa:")
        for response in self.responses:
            print(f"- {response}")