from survey import AnonymousSurvey


# Defina uma pergunta e faça uma pesquisa.
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Mostre a pergunta e armazene as respostas à pergunta.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Mostre os resultados da pesquisa.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()