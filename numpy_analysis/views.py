# Импортируем стандартный модуль для рендеринга страниц
from django.shortcuts import render
# Импортируем стандартные модули для пагинации страниц
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Подключаем модуль для фиксирования времени
import time
# Подключаем модуль для анализа numpy
import numpy as np
# Подключаем конфигурационный файл для импорта констант
from django.conf import settings


# Создаем вид для рендеринга страницы формы
def numpy_page(request):
    return render(request, 'numpy_page.html')


# Создаем вид для обработки вариантов numpy
def numpy_processing(request):
    # Обявляем глобальные переменные т.к будем работать не только с post запросами VG
    global end
    global data_numpy
    # Проверяем тип запроса формы
    if request.method == 'POST':
        # Получаем значение варианта из формы
        c = request.POST.get('choice', None)
        # Обработка варианта 1
        if c == 'c1':
            # Обявляем переменую для пагинации первой страницы
            page = request.GET.get('page', 1)
            # Фиксируем время
            start = time.time()
            # Считываем информацию из дампа
            data_numpy = np.load(settings.NUMPY_DUMP)
            # Поиск значений global_active_power что больше 5
            data_numpy = data_numpy[data_numpy['gap'] > 5]
            # Передаем series в качестве аргумента, ставим максимальное значение для 1й страницы
            paginator = Paginator(data_numpy, 1000)
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
            return render(request, 'numpy_data.html', context)
        # Обработка варианта 2
        elif c == 'c2':
            # Обявляем переменую для пагинации первой страницы
            page = request.GET.get('page', 1)
            # Фиксируем время
            start = time.time()
            # Считываем информацию из дампа
            data_numpy = np.load(settings.NUMPY_DUMP)
            # Поиск значений voltage что больше 235
            data_numpy = data_numpy[data_numpy['v'] > 235]
            # Передаем series в качестве аргумента, ставим максимальное значение для 1й страницы
            paginator = Paginator(data_numpy, 1000)
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
            return render(request, 'numpy_data.html', context)
        # Обработка варианта 3
        elif c == 'c3':
            # Обявляем переменую для пагинации первой страницы
            page = request.GET.get('page', 1)
            # Фиксируем время
            start = time.time()
            # Считываем информацию из дампа
            data_numpy = np.load(settings.NUMPY_DUMP)
            # Поиск значений global_intensity что больше 19 и меньше 20
            data_numpy = data_numpy[(data_numpy['gi'] >= 19) & (data_numpy['gi'] <= 20)]
            # Передаем series в качестве аргумента, ставим максимальное значение для 1й страницы
            paginator = Paginator(data_numpy, 1000)
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
            return render(request, 'numpy_data.html', context)
        # Обработка варианта 4
        elif c == 'c4':
            # Обявляем переменую для пагинации первой страницы
            page = request.GET.get('page', 1)
            # Фиксируем время исполнения
            start = time.time()
            # Считываем информацию из дампа
            data_numpy = np.load(settings.NUMPY_DUMP)
            # Генерируем 500000 уникальных строк
            data_numpy = data_numpy[np.random.choice(data_numpy.shape[0], 500000, replace=False)]
            # Расчет среднего значения для группы 1
            s1_average = sum(data_numpy['s1'])/500000
            # Расчет среднего значения для группы 2
            s2_average = sum(data_numpy['s2'])/500000
            # Расчет среднего значения для группы 3
            s3_average = sum(data_numpy['s3'])/500000
            # Поиск записей после 18:00
            data_numpy = data_numpy[(data_numpy['hours'] >= 18) & (data_numpy['minutes'] > 0)]
            # Из предидушего фрейма выводим те в которых global_active_power больше 6
            data_numpy = data_numpy[data_numpy['gap'] > 6]
            # Из полученого результата ищем все записи где группа 2 больше группы 1 и группы 3
            data_numpy = data_numpy[(data_numpy['s2'] > data_numpy['s1']) & (data_numpy['s2'] > data_numpy['s3'])]
            # Ищем размер полученого фрейма и делим пополам
            l = len(data_numpy) // 2
            # Делаем срез 1й части
            first_part = data_numpy[:l]
            # Из первой части выбираем каждое 3е значение
            first_part = first_part[::3]
            # Делаем срез 2й части
            second_part = data_numpy[l:]
            # Из первой части выбираем каждое 4е значение
            second_part = second_part[::4]
            # Обединяем два списка средствами numpy
            data_numpy = np.concatenate((first_part, second_part), axis=0)
            # Передаем series в качестве аргумента, ставим максимальное значение для 1й страницы
            paginator = Paginator(data_numpy, 1000)
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
            context = {'frame': p, 'time': end, 'av1': s1_average, 'av2': s2_average, 'av3': s3_average}
            # Передаем обработаные данные на страницу
            return render(request, 'numpy_data.html', context)
    # Данное условие необходимо для навигации по страницам
    else:
        # Обявляем переменую для пагинации первой страницы
        page = request.GET.get('page', 1)
        # Передаем series в качестве аргумента, ставим максимальное значение для 1й страницы
        paginator = Paginator(data_numpy, 1000)
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
        return render(request, 'numpy_data.html', context)