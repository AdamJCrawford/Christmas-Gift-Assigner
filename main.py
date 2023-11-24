from random import shuffle, randint
from typing import Iterable


def gift_assigner(people: list[str]) -> Iterable[list[str]]:
    """
    Basically all we have to do it to create a derangement. That is, each person should be assigned to 1 person but no one should be assigned to themselves. Based on: https://www.youtube.com/watch?v=5kC5k5QBqcc

    Args:
        people (list[str]): List of people that will be giving/recieving gifts.

    Returns:
        Iterable[list[str]]: Iterable of 2 lists that contain all the gift assignments. The first list contains the order of the "givers" and the second list contains the order of the "receivers". Giver[n] is the person responsible for gifting reciever[n].
    """
    shuffle(people)
    top_cards = people[:]
    bottom_cards = people[:]

    # List rotatation based on random pivot. ie if the pivot is 1 the list [1, 2, 3, 4, 5] will become [2, 3, 4, 5, 1]
    random_rotation = randint(0, len(people) - 1)
    bottom_cards = bottom_cards[random_rotation:] + bottom_cards[:random_rotation]

    return zip(top_cards, bottom_cards)


if __name__ == "__main__":
    crawford = ["Adam", "Ben", "Criss", "Debbie", "Grammy", "Josh"]
    etcheverry_modesto = ["Mike", "Rose"]
    etcheverry_texas = ["Larry"]
    hanson_elderado_hills = ["Chris", "Kathy"]
    hanson_los_angels = ["Anna", "Brian"]
    hanson_sacramento = ["Kevin", "Sasha"]
    hanson_sj = ["Matt", "Rachel"]
    mccarty = ["Abe", "Bill", "Elizabeth"]

    family = (
        crawford
        + etcheverry_modesto
        + etcheverry_texas
        + hanson_elderado_hills
        + hanson_los_angels
        + hanson_sacramento
        + hanson_sj
        + mccarty
    )

    gift_assignments = gift_assigner(family)

    for giver, receiver in gift_assignments:
        print(f"{giver} will give a gift to {receiver}")
