team1_num = input('Количество участников команды Мастера кода: ')
team2_num = input('Количество участников команды Волшебники Данных: ')
score_1 = int(input('Количество задач, которые решила команда Мастера кода: '))
score_2 = int(input('Количество задач, которые решила команда Волшебники Данных: '))
team1_time = float(input('Время, которое команда Мастера кода потратила на решение всех задач: '))
team2_time = float(input('Время, которое команда Волшебники Данных потратила на решение всех задач: '))
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
challenge_result = result
tasks_total = score_1 + score_2
time_avg = ((team1_time / score_1) + (team2_time / score_2)) / 2
print('В команде Мастера кода участников: %s!' % (team1_num))
print('Итого сегодня в командах участников: %(t1)s и %(t2)s!' % {'t1': team1_num, 't2': team2_num})

print('Команда Волшебники данных решила задач: {score}!'.format(score=score_2))
print('Волшебники данных решили задачи за {time} с!'.format(time=team2_time))

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!.')

