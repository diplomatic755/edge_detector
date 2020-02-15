#!/usr/bin/env -S python3 -B
import matplotlib.pyplot as plt
import numpy as np
from skimage import feature


class Detector:
    """ Класс детектора, содержит методы обработки входного изображения,
    перевода в битовый массив, координаты точек и вывода результатов обработки
                                   Методы:
    edge() - метод реализующий фильтр Канни, необходимый для алгоритма обнаружения границ изображения
        sigma=1.            (float) -   Дисперсия первичного гауссова размытия
        low_threshold=None  (float) -   Нижняя/верхняя граница для определения гистерезиса (связывание краев)
        high_threshold=None (float) -   (если None, значения установлены на 10% / 20% от максимального значения dtype)
        mask=None      (array bool) -   Маска для ограничения фильтра в определенной области
        use_quantiles=None (bool)   -   True->low_threshold и high_threshold как квантили изображения величины кромки

    bitmap() - метод реализующий преобразование в битовый массив (в оттенках серого, массив float64 на выходе)

    points() - метод реализующий преобразование в координаты точек (на выходе кортеж из пар координат x, y в px)"""

    def __init__(self, image):
        self.image = image
        self.edges = None

    # Фильтр Канни
    def edge(self, sigma=1., low_threshold=None, high_threshold=None, mask=None, use_quantiles=None):
        edges = feature.canny(image=self.image,
                              sigma=sigma, low_threshold=low_threshold, high_threshold=high_threshold,
                              mask=mask, use_quantiles=use_quantiles)
        return edges

    # Преобразование в битовый массив
    def bitmap(self):
        bitmap_array = self.edges.astype(np.float64)
        return bitmap_array

    # Преобразование в координаты точек
    def points(self):
        x, y = np.where(self.edges)
        dots = []
        for i, j in zip(x, y):
            dots.append([i, j])
        chain = np.array(dots)
        return chain


def main():
    return None


if __name__ == '__main__':
    main()
