import random
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib
import numpy as np


def plot_polygon(polygons, width: int, height: int):
    """
    Plot list of polygons

    :param polygons numpy.darray: list of polygons
    :param width int: width of image
    :param height int: height of image
    """

    shapes = []
    for p in polygons:

        po = Polygon(np.array(list(zip(p[::2], p[1::2]))), True)
        shapes.append(po)

    fig, axs = plt.subplots()
    p = PatchCollection(shapes, cmap=matplotlib.cm.jet, alpha=0.4)
    axs.add_collection(p)

    axs.set_xlim([0, width])
    axs.set_ylim([0, height])
    axs.xaxis.tick_top()
    axs.yaxis.tick_left()
    axs.invert_yaxis()

    plt.show()


if __name__ == "__main__":
    polygons = [
        [
            100,
            100,
            200,
            100,
            200,
            200,
            100,
            200,
            50,
            150,
        ],
        [
            100,
            100,
            200,
            100,
            200,
            200,
            100,
            200,
            50,
            300,
        ],
        [
            811.212424585916,
            1394.320065769296,
            815.9339919719415,
            1364.4942767728717,
            894.721575414084,
            1376.9667342307039,
            890.0000080280585,
            1406.7925232271282,
        ],
    ]
    plot_polygon_on_empty(polygons, 5832, 7963)
