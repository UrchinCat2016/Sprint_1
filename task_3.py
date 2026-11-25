"""Задание 3. Чемпионы мира по футболу."""


def print_champions(world_champions, country):
    for year, champion in world_champions.items():
        print(year, '-', champion)
    if country in world_champions.values():
        print(country, 'становилась чемпионом мира по футболу в 21 веке!')
    else:
        print(country, 'не выигрывала чемпионат мира по футболу в 21 веке.')


if __name__ == '__main__':
    world_champions = {
        2002: 'Бразилия',
        2006: 'Италия',
        2010: 'Испания',
        2014: 'Германия',
        2018: 'Франция',
    }
    world_champions[2022] = 'Аргентина'
    country = 'Италия'
    print_champions(world_champions, country)
