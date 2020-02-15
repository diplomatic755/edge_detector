#!/usr/bin/env -S python3 -B
from skimage import io


class Picture:
    """ Класс изображений:
    filename (str) - адрес файла с изображением, в случае если не задано явно, то будет запрошена строка
    region (tuple) - границы обрабатываемого фрагмента изображения, также используется в методе crop
    as_gray (bool) - флаг, указывает открыть изображение (оттенки серого / цветное)

    crop() - метод для обрезки входного изображения
        region (tuple (UP, DOWN, LEFT, RIGHT) ) - границы обрезки входного изображения в px """

    # Конструктор-инициализатор
    def __init__(self, filename=None, region=None, as_gray=True):
        try:
            if filename is None:
                filename = "./images/1.bmp" #   Значение для примера
                #filename = input("filename->")
        except FileNotFoundError:
            print("File not found, check filename and try again")
        if region is None:
            image = io.imread(fname=filename, as_gray=as_gray)
        else:
            image = io.imread(fname=filename, as_gray=as_gray)
            image = image[region[0]: (image.shape[0] - region[1]), region[2]: (image.shape[1] - region[3])]
        self.filename, self.image = filename, image

    # Обрезка изображения
    def crop(self, region):
        return Picture(filename=self.filename, region=region)


def main():
    return None


if __name__ == '__main__':
    main()
