"""Дополнительное задание 1. Удаление дублей с учётом критичности."""


def remove_duplicates(tickets):
    unique_tickets = {}
    seen = []
    for level in sorted(tickets):
        unique_tickets[level] = []
        for ticket in tickets[level]:
            if ticket not in seen:
                unique_tickets[level].append(ticket)
                seen.append(ticket)
    return unique_tickets


def build_tickets_by_type(types, tickets):
    unique_tickets = remove_duplicates(tickets)
    tickets_by_type = {}
    for level, level_tickets in unique_tickets.items():
        tickets_by_type[types[level]] = level_tickets
    return tickets_by_type


if __name__ == '__main__':
    types = {
        1: 'Блокирующий',
        2: 'Критический',
        3: 'Значительный',
        4: 'Незначительный',
        5: 'Тривиальный',
    }
    tickets = {
        1: ['API_45', 'API_76', 'E2E_4'],
        2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
        3: ['E2E_45', 'API_45', 'E2E_2'],
        4: ['E2E_9', 'API_76'],
        5: ['E2E_2', 'API_61'],
    }
    tickets_by_type = build_tickets_by_type(types, tickets)
    print(tickets_by_type)
