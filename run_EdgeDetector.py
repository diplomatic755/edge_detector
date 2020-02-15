import matplotlib.pyplot as plt
import numpy as np

import skimage.io
from scipy import interpolate
from EdgeDetector import Detector
from images import Picture


cut_region = (450, 50, 100, 100)  # Границы обрезки изображения
space = 25  # Сколько будет пропускаться точек при интерполяции

Photo1 = Picture(filename="./images/1.bmp")
skimage.io.imsave(fname="./results/source_image.bmp", arr=Photo1.image)

Photo1 = Photo1.crop(region=cut_region)
skimage.io.imsave(fname="./results/cropped_image.bmp", arr=Photo1.image)

try:
    Image = Detector(image=Photo1.image)
    Image.edges = Image.edge(sigma=1.4)
    bitmap_image = Image.bitmap()
    skimage.io.imsave(fname="./results/bitmap_image.bmp",
                      arr=bitmap_image, check_contrast=False)

    # Картинка для диплома
    fig0, (ax0, ax1) = plt.subplots(nrows=2, ncols=1, dpi=600)
    ax0.imshow(Image.image, cmap=plt.cm.gray)
    ax0.axis("on")
    ax0.set_title("Исходное изображение", fontsize=15)

    ax1.imshow(bitmap_image, cmap=plt.cm.gray)
    ax1.axis("on")
    ax1.set_title("Оператор Канни, $\sigma=1.4$", fontsize=15)
    fig0.tight_layout()
    plt.savefig(fname="./results/filtered.png",
                dpi=600, facecolor='w', edgecolor='w', format='png')
    plt.show()

    # Массив точек границы, подготовка (сортировка по возр X, прорежение точек)
    chain = Image.points()
    chain = chain[chain[:, 1].argsort()]
    x_axis = chain[::space, 1]
    y_axis = chain[::space, 0].max() - chain[::space, 0]

    # Интерполяция сплайном Акимы
    f = interpolate.Akima1DInterpolator(x=x_axis, y=y_axis)
    x_new = np.arange(x_axis.min(), x_axis.max(), 1)
    y_new = f(x_new)

    # График, точки границы + кривая сплайна интерполяции
    fig1 = plt.figure(dpi=600)
    ax2 = fig1.subplots()
    ax2.scatter(x=x_axis, y=y_axis, s=5, color='red', label="Точки границы")
    ax2.plot(x_new, y_new, color='blue', label="Сплайн")
    ax2.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
               ncol=2, mode="expand", borderaxespad=0.)
    ax2.set_aspect(aspect=1)
    plt.savefig(fname="./results/plot_graph.png",
                dpi=600, facecolor='w', edgecolor='w', format='png')
    plt.show()

    # Сплайн и точки наложенные на изображение
    fig2, ax3 = plt.subplots(dpi=600)
    ax3.imshow(Image.image)
    ax3.plot(x_new, chain[::space, 0].max() - y_new, color='black',
             alpha=0.6, linewidth=3, label="Сплайн")
    ax3.scatter(x=chain[::space, 1], y=chain[::space, 0],
                s=9, color='red', label="Точки")
    ax3.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
               ncol=2, mode="expand", borderaxespad=0.)
    plt.savefig(fname="./results/layered_pic.png",
                dpi=600, facecolor='w', edgecolor='w', format='png')
    plt.show()

except(EOFError, KeyboardInterrupt):
    print("\nStop")
