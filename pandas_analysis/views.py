# Импортируем стандартный модуль для рендеринга страниц
from django.shortcuts import render
# Импортируем стандартные модули для пагинации страниц
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Подключаем модуль для фиксирования времени
import time
# Подключаем модуль для анализа pandas
import pandas as pd
# Подключаем конфигурационный файл для импорта констант
from django.conf import settings
'''
Модуль для создания дампов. Будет использован только для pandas, поскольку модуль намного медленее работает чем numpy VG

Пример кода для создания дампа
dt = pd.read_csv('base.txt', index_col=False,  delimiter=';', names=['date', 'hours', 'minutes', 'seconds', 'gap', 'grp', 'v', 'gi', 's1', 's2', 's3'])
dt.to_pickle('pandas.pickle', compression='infer')
'''
import pickle


# Создаем вид для рендеринга главной страници
def index(request):
    return render(request, 'home.html')


# Создаем вид для рендеринга страницы формы
def pandas_page(request):
    return render(request, 'pandas_page.html')


# Создаем вид для обработки вариантов pandas
def pandas_processing(request):
    # Обявляем глобальные переменные т.к будем работать не только с post запросами
    global end
    global pandas_data
    # Проверяем тип запроса формы
    if request.method == "POST":
        # Получаем значение варианта из формы
        c = request.POST.get('choice', None)
        # Обработка варианта 1
        if c == 'c1':
            # Обявляем переменую для пагинации первой страницы
            page = request.GET.get('page', 1)
            # Фиксируем время
            start = time.time()
            # Считываем информацию из дампа
            pandas_data = pd.read_pickle(settings.PANDAS_DUMP, compression='infer')
            # Поиск значений global_active_power что больше 5
            pandas_data = pandas_data[pandas_data['gap'] > 5]
            # Полученый фрейм конвертируем в список и передаем в качестве аргумента, также ставим мааксимальное количесто строк на одной странице
            paginator = Paginator(pandas_data.values.tolist(), 1000)
            # Фиксируем время исполнения
            end = time.time() - start
            try:
                # Получаем значения для первой страницы
                p = paginator.page(page)
                # Обработка исключений при не целых значениях пагинатора
            except PageNotAnInteger:
                # В этом случае выводим страницу 1
                p = paginator.page(1)
                # Обработка исключений для пустых страниц
            except EmptyPage:
                # Выводим только пагинацию
                p = paginator.page(paginator.num_pages)
            # Создаем словарь со значениями
            context = {'frame': p, 'time': end}
            # Передаем обработаные данные на страницу
            return render(request, 'pandas_data.html', context)
        # Обработка варианта 2
        elif c == 'c2':
            # Обявляем переменую для пагинации первой страницы
            page = request.GET.get('page', 1)
            # Фиксируем время
            start = time.time()
            # Считываем информацию из дампа
            pandas_data = pd.read_pickle(settings.PANDAS_DUMP, compression='infer')
            # Поиск значений voltage что больше 235
            pandas_data = pandas_data[pandas_data['v'] > 235]
            # Для вольтажа был создан отдельный дамп, поскольку поиск всех значений требовал бы больше ресурсов сервера
            with open(settings.VOLTAGE_DUMP, 'rb') as handle:
                # Присваиваем значение для пагинатора
                paginator = pickle.load(handle)
            # Фиксируем время
            end = time.time() - start
            try:
                # Получаем значения для первой страницы
                p = paginator.page(page)
                # Обработка исключений при не целых значениях пагинатора
            except PageNotAnInteger:
                # В этом случае выводим страницу 1
                p = paginator.page(1)
                # Обработка исключений для пустых страниц
            except EmptyPage:
                # Выводим только пагинацию
                p = paginator.page(paginator.num_pages)
            # Создаем словарь со значениями
            context = {'frame': p, 'time': end}
            # Передаем обработаные данные на страницу
            return render(request, 'pandas_data.html', context)
        # Обработка варианта 3
        elif c == 'c3':
            # Обявляем переменую для пагинации первой страницы
            page = request.GET.get('page', 1)
            # Фиксируем время
            start = time.time()
            # Считываем информацию из дампа
            pandas_data = pd.read_pickle(settings.PANDAS_DUMP, compression='infer')
            # Поиск значений global_intensity что больше 19 и меньше 20
            pandas_data = pandas_data[(pandas_data['gi'] >= 19) & (pandas_data['gi'] <= 20)]
            # Полученый фрейм конвертируем в список и передаем в качестве аргумента, также ставим мааксимальное количесто строк на одной странице
            paginator = Paginator(pandas_data.values.tolist(), 1000)
            # Фиксируем время
            end = time.time() - start
            try:
                # Получаем значения для первой страницы
                p = paginator.page(page)
                # Обработка исключений при не целых значениях пагинатора
            except PageNotAnInteger:
                # В этом случае выводим страницу 1
                p = paginator.page(1)
                # Обработка исключений для пустых страниц
            except EmptyPage:
                # Выводим только пагинацию
                p = paginator.page(paginator.num_pages)
            # Создаем словарь со значениями
            context = {'frame': p, 'time': end}
            # Передаем обработаные данные на страницу
            return render(request, 'pandas_data.html', context)
        # Обработка варианта 4
        elif c == 'c4':
            # Обявляем переменую для пагинации первой страницы
            page = request.GET.get('page', 1)
            # Фиксируем время
            start = time.time()
            # Считываем информацию из дампа
            pandas_data = pd.read_pickle(settings.PANDAS_DUMP, compression='infer')
            # Генерируем 500000 уникальных строк
            pandas_data = pandas_data.sample(n=500000, replace=True)
            # Расчет среднего значения для группы 1
            s1_average = sum(pandas_data['s1'])/500000
            # Расчет среднего значения для группы 2
            s2_average = sum(pandas_data['s2'])/500000
            # Расчет среднего значения для группы 3
            s3_average = sum(pandas_data['s3'])/500000
            # Поиск записей после 18:00
            pandas_data = pandas_data[(pandas_data['hours'] >= 18) & (pandas_data['minutes'] > 0)]
            # Из предидушего фрейма выводим те в которых global_active_power больше 6
            pandas_data = pandas_data[pandas_data['gap'] > 6]
            # Из полученого результата ищем все записи где группа 2 больше группы 1 и группы 3
            pandas_data = pandas_data[(pandas_data['s2'] > pandas_data['s1']) & (pandas_data['s2'] > pandas_data['s3'])]
            # Ищем размер полученого фрейма и делим пополам
            l = len(pandas_data) // 2
            # Делаем срез 1й части
            first_part = pandas_data[:l]
            # Из первой части выбираем каждое 3е значение
            first_part = first_part[::3]
            # Делаем срез 2й части
            second_part = pandas_data[l:]
            # Из второй части выбираем каждое 4е значение
            second_part = second_part[::4]
            # Создаем список из полученых частей
            f = [first_part, second_part]
            # Обединяем 2 части в 1
            pandas_data = pd.concat(f)
            # Полученый фрейм конвертируем в список и передаем в качестве аргумента, также ставим мааксимальное количесто строк на одной странице
            paginator = Paginator(pandas_data.values.tolist(), 1000)
            # Фиксируем время
            end = time.time() - start
            try:
                # Получаем значения для первой страницы
                p = paginator.page(page)
                # Обработка исключений при не целых значениях пагинатора
            except PageNotAnInteger:
                # В этом случае выводим страницу 1
                p = paginator.page(1)
                # Обработка исключений для пустых страниц
            except EmptyPage:
                # Выводим только пагинацию
                p = paginator.page(paginator.num_pages)
            # Создаем словарь со значениями
            context = {'frame': p, 'time': end, 'av1': s1_average, 'av2': s2_average, 'av3': s3_average}
            # Передаем обработаные данные на страницу
            return render(request, 'pandas_data.html', context)
    # Данное условие необходимо для навигации по страницам
    else:
        # Обявляем переменую для пагинации первой страницы
        page = request.GET.get('page', 1)
        # Получаем фрейм из глобальной переменной и преобразовуем в список
        paginator = Paginator(pandas_data.values.tolist(), 1000)
        try:
            # Получаем значения для первой страницы
            p = paginator.page(page)
            # Обработка исключений при не целых значениях пагинатора
        except PageNotAnInteger:
            # В этом случае выводим страницу 1
            p = paginator.page(1)
            # Обработка исключений для пустых страниц
        except EmptyPage:
            # Выводим только пагинацию
            p = paginator.page(paginator.num_pages)
        # Создаем словарь со значениями
        context = {'frame': p, 'time': end}
        # Передаем обработаные данные на страницу
        return render(request, 'pandas_data.html', context)