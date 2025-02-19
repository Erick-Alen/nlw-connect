import pytest

from .inscritos_repository import InscritosRepository


@pytest.mark.skip("Insert in DB")
def test_insert_inscritos():
    subscriber_info = {
        "nome": "Teste",
        "email": "teste@teste.com",
        "link": "teste.com",
        "evento_id": 1,
    }
    subs_repo = InscritosRepository()
    subs_repo.insert(subscriber_info)


def test_select_subscriber():
    # Arrange
    email = "teste@teste.com"
    evento_id = 1
    repository = InscritosRepository()
    # Act
    sub = repository.select_subscriber(email, evento_id)
    print(sub)
    print(sub.nome)


def test_ranking():
    evento_id = 3
    subs_repo = InscritosRepository()
    ranking = subs_repo.get_referral_ranking(evento_id)

    for link in ranking:
        print(f'Link: {link.nome} - Total subscribers: {link.total}')
