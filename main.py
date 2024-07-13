import smtplib
import os

login_yan = os.getenv("LOGIN_email")
password_yan = os.getenv("PASSWORD_email")
my_variable2='https://dvmn.org/referrals/urMnATzNCfF8oEHI9PGEXyUbDYhe6qgLX4ktypEp/'
my_variable3='Пётр'
my_variable4='Александр'
my_email = 'setpoints@yandex.ru'
his_email = 'alekskubarev10@mail.ru'
message_adv = """Привет, {0}! {1} приглашает тебя на сайт {2}!

{2} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {2}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {2}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(my_variable3,my_variable4,my_variable2)
letter_adv = """\
From: {0} 
To: {1} 
Subject:Приглашение!
Content-Type: text/plain; charset="UTF-8";

{2}""".format(my_email, his_email, message_adv)
letter_adv = letter_adv.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login_yan, password_yan)
server.sendmail(my_email, his_email, letter_adv)
server.quit()
