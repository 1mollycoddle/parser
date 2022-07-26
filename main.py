import re
import datetime
from datetime import timedelta, datetime

text = "Сходить      покушать   на    неделе в 13:13"


def instance(item):
    ob = re.sub(r'\s+', ' ', item)
    return ob


Mondays = ['в понедельник', 'каждый понедельник', 'понедельник', 'Понедельник', 'по понедельникам', 'понедельник']
Tuesdays = ['во вторник', 'каждый вторник', 'вторник', 'Вторник', 'по вторникам']
Wendsdays = ['в среду', 'каждую среду', 'среда', 'Среда', 'по средам', 'среду']
Thursdays = ['в четверг', 'каждый четверг', 'четверг', 'Четверг', 'по четвергам']
Fridays = ['в пятницу', 'каждую пятницу', 'пятница', 'Пятница', 'по пятницам']
Saturdays = ['в субботу', 'каждую субботу', 'суббота', 'Суббота', 'по субботам']
Sundays = ['в воскресенье', 'каждое воскресенье', 'воскресенье', 'Воскресенье', 'по воскресеньям']
WEEK = [Mondays, Tuesdays, Wendsdays, Thursdays, Fridays, Saturdays, Sundays]
week_array = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье']
months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
          'декабря']

day_array = ['дня', 'день', 'дней']
key = ['минут', 'минуты', 'часа', 'часов', 'число']
minutes_array = ['минут', 'минуты', 'минуту']
hours_array = ['часа', 'часов', 'час']
time_key = [
    'через', 'Через', 'каждые', 'Каждые', 'каждое', 'Каждое', 'каждый', 'Каждый',
    'каждую', 'Каждую', 'в', 'В', 'к', 'К'
]
params_array = ['каждые', 'Каждые', 'каждое', 'Каждое', 'каждый', 'Каждый', 'каждую', 'Каждую']

days = [
    'понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу',
    'воскресенье',
]
cherez = ['Через', 'через']

check = ['через', 'завтра', 'утром', 'на', 'по']

smth = ['неделе', 'году', 'год', 'неделю', 'месяце', 'месяц']

now = datetime.now()
weekday_today = now.weekday()
day_week_current = datetime.isoweekday(datetime.now())


def setDate(thing):
    cherez_houres = ''
    cherez_minute = ''
    day = now.day
    month = now.month
    mins = '12:00'
    hours = ''
    minutes = ''
    obs = ''
    time = ''
    year = now.year
    text = thing.split()
    day_week_compare = 0
    try:
        for item in text:

            # ------ days of the week check
            if item in Mondays:
                day_week = 'Monday'
                day_week_compare = 1
            elif item in Tuesdays:
                day_week = 'Tuesday'
                day_week_compare = 2
            elif item in Wendsdays:
                day_week = 'Wendsday'
                day_week_compare = 3
            elif item in Thursdays:
                day_week = 'Thursday'
                day_week_compare = 4
            elif item in Fridays:
                day_week = 'Friday'
                day_week_compare = 5
            elif item in Saturdays:
                day_week = 'Saturday'
                day_week_compare = 6
            elif item in Sundays:
                day_week = 'Sunday'
                day_week_compare = 7

            if day_week_compare:
                if day_week_compare > day_week_current:
                    day = int(now.day) + (day_week_compare - day_week_current)

                elif day_week_compare <= day_week_current:
                    day = int(now.day) + (day_week_compare - day_week_current + 7)

            '''if item in days:
                day = item
                for i in range(len(day)):
                    if day == day[i]:
                        day = datetime.weekday(day)


                if all(x not in time_key for x in text[text.index(item):]):
                    break'''

            # ------ day + month check
            try:
                if item.isdigit() and text[text.index(item) + 1] in months:
                    # print(thing)
                    day = str(item)
                    for i in range(len(months)):
                        if text[text.index(item) + 1] == months[i]:
                            month = i + 1

                    if now.month > month:
                        year = 2023
                    # month = ''.join(thing.split()[thing.split().index(item) + 1])
                    # if all(x not in time_key for x in text[text.index(item):]):
                    # break

            except Exception as ex:
                print(ex)

            if item in cherez:
                # через час
                if text[text.index(item) + 1] in hours_array:

                    mins = now + timedelta(hours=1)

                    mins = mins.time()

                    hours = mins.hour
                    minutes = mins.minute
                    if now.time() > mins:
                        day = now + timedelta(days=1)
                        day = day.day

                    if len(str(minutes)) < 2:
                        minutes = '0' + str(minutes)
                    if len(str(hours)) < 2:
                        hours = '0' + str(hours)
                    mins = str(hours) + ':' + str(minutes)

                # через день
                if text[text.index(item) + 1] in day_array:
                    day = now + timedelta(days=2)  # now.today
                    day = day.day
                    mins = '12:00'

                # через минуту
                if text[text.index(item) + 1] in minutes_array:
                    mins = now + timedelta(minutes=1)
                    mins = mins.time()
                    hours = mins.hour
                    if len(str(minutes)) < 2:
                        minutes = '0' + str(minutes)
                    if len(str(hours)) < 2:
                        hours = '0' + str(hours)

                    if now.time() > mins:
                        day = now + timedelta(days=1)
                        day = day.day
                    mins = str(hours) + ':' + str(minutes)

                # через 22 минуты
                if text[text.index(item) + 2] in minutes_array:
                    a = now + timedelta(minutes=int(text[text.index(item) + 1]))
                    a = a.time()
                    hours = a.hour
                    minutes = a.minute
                    if len(str(minutes)) < 2:
                        minutes = '0' + str(minutes)
                    if len(str(hours)) < 2:
                        hours = '0' + str(hours)
                    mins = str(hours) + ':' + str(minutes)
                    if now.time() > a:
                        day = now + timedelta(days=1)
                        day = day.day

                # через 2 дня(через 10 дней)
                if text[text.index(item) + 2] in day_array:
                    day = now + timedelta(days=int(text[text.index(item) + 1]))
                    day = day.day
                    mins = '12:00'

                # через 2 часа
                if text[text.index(item) + 2] in hours_array:  # and text[text.index(item) + 3].isdigit() == False:
                    mins = now + timedelta(hours=int(text[text.index(item) + 1]))
                    mins = mins.time()
                    hours = mins.hour
                    minutes = mins.minute
                    if len(str(minutes)) < 2:
                        minutes = '0' + str(minutes)
                    if len(str(hours)) < 2:
                        hours = '0' + str(hours)
                    if now.time() > mins:
                        day = now + timedelta(days=1)
                        day = day.day
                    mins = str(hours) + ':' + str(minutes)

                # через 2 часа 30 минут
                if text[text.index(item) + 2] in hours_array and text[text.index(item) + 3].isdigit():
                    mins = now + timedelta(hours=int(text[text.index(item) + 1]),
                                           minutes=int(text[text.index(item) + 3]))
                    mins = mins.time()
                    hours = mins.hour
                    minutes = mins.minute
                    if len(str(minutes)) < 2:
                        minutes = '0' + str(minutes)
                    if len(str(hours)) < 2:
                        hours = '0' + str(hours)
                    if now.time() > mins:
                        day = now + timedelta(days=1)
                        day = day.day
                    mins = str(hours) + ':' + str(minutes)

            if 'утром' in item:
                mins = '09:00'

            if 'днем' in item:
                mins = '15:00'
            if 'вечером' in item:
                mins = '18:00'

            if 'завтра' in item:
                day = now.today() + timedelta(days=1)
                day = day.day
                mins = '12:00'
                '''mins = now.time()
                hours = mins.hour
                minutes = mins.minute
                if len(str(minutes)) < 2:
                    minutes = '0' + str(minutes)
                if len(str(hours)) < 2:
                    hours = '0' + str(hours)
                mins = str(hours) + ':' + str(minutes)'''

            if 'неделе' in item:
                day = now + timedelta(days=2)  # now.today
                day = day.day
                mins = '12:00'

            '''if item in check:
                obs = ' '.join(thing.split()[thing.split().index(item):thing.split().index(item) + 2])
                if all(x not in time_key for x in thing.split()[thing.split().index(item):]):
                    break'''

            # год
            if item.isdigit() and (2000 <= int(item)):
                year = item

            # --------- mins
            if ':' in item:
                mins = item
                time = datetime.strptime(mins, '%H:%M')

                if ((time.time() <= now.time()) and (day == now.day)):
                    day = now.today() + timedelta(days=1)
                    day = day.day

            # params check
            if item in params_array:
                obs = "REPEAT_ALWAYS"
                if text[text.index(item) + 1] in week_array:
                    obs = 'REPEAT_ALWAYS'
                    day = text[text.index(item) + 1]

                if text[text.index(item) + 1].isdigit() and text[text.index(item) + 2] == 'число':
                    obs = 'REPEAT_ALWAYS'
                    day = text[text.index(item) + 1]

                if text[text.index(item) + 1] == 'год':
                    obs = 'REPEAT_ALWAYS'
                    day = now.day



    except Exception as ex:
        print(ex)
    return [day, month, year, mins, obs]


def getTime(item):
    try:
        for object in item.split(' '):

            try:

                if object in time_key or object.isdigit() or (
                        object in check and item.split()[item.split().index(object) + 1] in smth):
                    time_case = ' '.join(item.split()[item.split().index(object):])
                    info = setDate(time_case)
                    state = 'SUCCESS'
                    text = (' '.join(item.split()[:item.split().index(object)]) if item.split()[0] not in smth \
                                                                                   and item.split()[0] not in days \
                                                                                   and item.split()[0] not in time_key \
                                                                                   and item.split() not in cherez \
                                else '*'.join([x for x in item.split() if x not in time_key \
                                               and x not in days \
                                               and x not in cherez \
                                               and x not in smth
                                               and x.isdigit() == False \
                                               and x not in day_array \
                                               and x not in hours_array \
                                               and x not in minutes_array]))

                    try:
                        data = {'STATUS': state,
                                'DATE': {
                                    'year': info[2],
                                    'month': info[1],
                                    'day': info[0],
                                    'time': {
                                        'hours': info[3].split(':')[0],
                                        'minutes': info[3].split(':')[1]
                                    },
                                    'PARAMS': info[-1]},
                                'текст': text
                                }
                    except:

                        data = {'STATUS': state,
                                'DATE': {
                                    'year': info[2],
                                    'month': info[1],
                                    'day': info[0],
                                    'time': {
                                        'hours': '',
                                        'minutes': ''
                                    },
                                    'PARAMS': info[-1]},
                                'text': text
                                }

                    return data

            except Exception as ex:
                print(ex)
                state = 'ERROR'
                data = {'STATUS': state}
                return data

    except:
        pass


text_0 = "Начать собираться в 4:31"
text_1 = "Проснуться, улыбнуться, почистить зубы и помыться в 07:13"
text_2 = "Съездить на дачу 17 мая в 16:15"
text_3 = 'Подписать служебку у начальника 13 декабря 2021 года в 16:15'
text_4 = "Убраться в квартире через 90 минут"
text_5 = "Позвонить друзьям через 3 часа"
text_6 = "Приготовить покушать на 2-3 дня 3 сентября 2022 года в 06:01"
text_7 = "Перевод локального компьютера в режим гибернации завтра"
text_8 = "Выключить 13 декабря в 20:17"
text_9 = "Перевод локального компьютера в режим гибернации через 2 дня"
text_10 = 'Служебку подписать на питон 12 ноября утром'
text_11 = 'Служебку подписать на питон в четверг в 20:17'
text_12 = 'Служебку подписать на питон в среду'
text_13 = 'Служебку в отдел кадров в среду в 13:13'
text_14 = "В пятницу уроки"
text_15 = 'Поскольку все записи имеют один и тот же шаблон, внести данные, которые хотите извлечь из пары скобок 13 декабря 2022 года в 16:15'

text_16 = "Напомни про гречку через 14 минут"
text_17 = "Через 50 минут таймер установаить. дерзай"
text_18 = "Основы_Python_в_четверг_15:00 3 сентября 2022 года"
text_19 = " Основы_Python_в_четверг_15:00 в среду 15:00 "
text_20 = "13 1311"
text_21 = 1231
text_22 = "Сходить покушать на неделе в 13:13"
text_23 = "del_qustion_answer*как дела?*норма, как сам?"
text_24 = "Сходить покушать на неделе"
text_25 = "В следующем месяце Подписать служебку "
text_26 = "\d\de23 2\3 3r3556"
text_27 = "Подписать служебку по выходным"
text_28 = "Сходить в сауну каждое 28 число"
text_29 = "Подписать служебку по выходным в 20:19"
text_30 = "поздравить с др маму через год в 20:18"
text_31 = "поздравить с др маму через час"
text_32 = "тренировка каждый час в 20:19"
text_33 = "Подписать служебку 23 февраля"
text_34 = "Тренировка каждый четверг"
text_35 = "Тренировка каждый год"

for item in list(range(0, 36)):
    try:
        print('-------------------')
        text = instance(globals()[f'text_{item}'])
        print(getTime(text))
        print(globals()[f'text_{item}'].strip())
    except:
        pass
