"""Задание 1. Подсчёт общего времени в минутах."""


def calculate_minutes(time_string):
    total_minutes = 0
    for interval in time_string.split(','):
        for value in interval.split():
            if 'h' in value:
                total_minutes += int(value.replace('h', '')) * 60
            elif 'm' in value:
                total_minutes += int(value.replace('m', ''))
            elif 's' in value:
                total_minutes += int(value.replace('s', '')) // 60
    return total_minutes


if __name__ == '__main__':
    time_values = '1h 45m,360s,25m,30m 120s,2h 60s'
    total_minutes = calculate_minutes(time_values)
    print(total_minutes)
