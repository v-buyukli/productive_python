from random import choice, seed

import pytest

from ..fluent_python.frenchdeck import Card, FrenchDeck, spades_high


def test_card_creation():
    card = Card('7', 'diamonds')
    assert card.rank == '7'
    assert card.suit == 'diamonds'


def test_frenchdeck_len():
    deck = FrenchDeck()
    assert len(deck) == 52


def test_frenchdeck_indexing():
    deck = FrenchDeck()
    first_card = deck[0]
    last_card = deck[-1]
    assert first_card.rank == '2'
    assert first_card.suit == 'spades'
    assert last_card.rank == 'A'
    assert last_card.suit == 'hearts'


def test_frenchdeck_choice():
    seed(10)
    deck = FrenchDeck()
    random_card = choice(deck)  # nosec
    assert isinstance(random_card, Card)


def test_frenchdeck_slicing():
    deck = FrenchDeck()
    sliced_deck = deck[:3]
    assert len(sliced_deck) == 3


def test_frenchdeck_iteration():
    deck = FrenchDeck()
    for card in deck:
        assert isinstance(card, Card)


def test_frenchdeck_reversed():
    deck = FrenchDeck()
    for card in reversed(deck):
        assert isinstance(card, Card)


def test_frenchdeck_contains():
    deck = FrenchDeck()
    hearts_queen = Card('Q', 'hearts')
    not_in_deck = Card('7', 'beasts')
    assert hearts_queen in deck
    assert not_in_deck not in deck


def test_frenchdeck_sorting():
    deck = FrenchDeck()
    sorted_deck = sorted(deck, key=spades_high)
    assert len(deck) == len(sorted_deck)
    assert str(sorted_deck[0]) == "Card(rank='2', suit='clubs')"
    assert str(sorted_deck[51]) == "Card(rank='A', suit='spades')"


if __name__ == '__main__':
    pytest.main()
