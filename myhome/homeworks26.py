import math

team1_num = 7
team2_num = 8
score_1 = 50
score_2 = 54
team1_time = 23456.7
team2_time = 12345.6
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
if team1_time / score_1 > team2_time / score_2:
    challenge_result = 'Победили Волшебники данных'
elif team1_time / score_1 < team2_time / score_2:
    challenge_result = 'Победили Мастера кода'
else:
    challenge_result = 'Ничья'
print('В команде Мастера кода участников: %s!' % (team1_num))
print('И того сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {} с!'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задачи')
print(f'Сегодня было решено {tasks_total} задачи в среднем по {time_avg:5.1f} на задачу')
print(f'Среднее время решения на одного участника Мастера кода'
      f' {team1_time / score_1:5.1f}')
print(f'Среднее время решения на одного участника Волшебники данных'
      f' {team2_time / score_2:5.1f}')
print(challenge_result)


