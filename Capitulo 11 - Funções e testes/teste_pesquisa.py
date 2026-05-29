try:
    import pytest
except ImportError:
    raise ImportError("Módulo 'pytest' não encontrado. Instale com: pip install pytest") from None
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """Uma pesquisa que estará disponível para todas as funções de teste."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Teste se uma única resposta está armazenada corretamente."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Teste se três respostas individuais estão armazenadas corretamente."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses