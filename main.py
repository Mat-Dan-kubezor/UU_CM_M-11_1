import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm

class Requests:
    url = 'https://tinkoff.ru'  # Указываем URL, на который будем отправлять GET-запрос

    response = requests.get(url)  # Отправляем GET-запрос по указанному URL

    if response.status_code == 200:  # Проверяем статус-код ответа

        data = response.url  # Если статус-код 200 (OK), получаем данные из ответа
        print(f'Статус ответа: OK [код 200]')

    else:
        print('Ошибка при выполнении запроса')  # В случае ошибки выводим сообщение



class Panda:
    # Загрузка данных из текстового файла
    data = pd.read_fwf(r'C:\Users\kubezor\PycharmProjects\pythonProject20\text.txt')

    # Отображение первых 5 строк данных
    print(data.head())



class Numpy:
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Создаем массив
    sum = np.sum(arr)   # Суммируем его элементы
    flip = np.flip(arr) # Элементы массива в обратном порядке

    print(arr)
    print(sum)
    print(flip)


class Matplotlib:
    plt.style.use('_mpl-gallery')

    # Make data
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    # Plot the surface
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

    ax.set(xticklabels=[],
           yticklabels=[],
           zticklabels=[])

    plt.show()



class Pillow:
    image = Image.open(r'C:\Users\kubezor\PycharmProjects\pythonProject20\n8FSqKUlSlY.jpg')
    resized_image = image.resize((800, 600))
    resized_image.save('n8FSqKUlSlY.jpg')

    image.save('n8FSqKUlSlY.jpg')
    image.save('n8FSqKUlSlY.gif')