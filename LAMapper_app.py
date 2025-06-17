# version 0.2.0 beta

import numpy as np
import pandas as pd
import matplotlib
# matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
from matplotlib import colors
plt.style.use('bmh')
from openpyxl import load_workbook
import copy
import math
from mpl_toolkits.axes_grid1 import make_axes_locatable
from shiny import App, Inputs, Outputs, Session, render, ui, reactive
from matplotlib.widgets import RectangleSelector
from matplotlib.widgets import PolygonSelector
from skimage.draw import line # type: ignore
from skimage.draw import polygon # type: ignore
from skimage import color
import ast
import networkx as nx
from scipy import stats
import os
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.cm
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch
import requests
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
import seaborn as sns
import pyarrow as pa # type: ignore
import pyarrow.parquet as pq # type: ignore
from shiny._main import run_app
from shinywidgets import output_widget, render_widget  
import plotly # type: ignore
import plotly.express as px
import plotly.graph_objects as go # type: ignore
from plotly.graph_objs import Figure
from shiny.types import ImgData
from skimage import io
import cmcrameri.cm as cmc # type: ignore
from PIL import Image
import json
import io
import seaborn as sns
import matplotlib.transforms as transforms # type: ignore
from matplotlib.patches import Ellipse # type: ignore
import numpy.ma as ma # type: ignore
import cv2 # type: ignore

# from shiny.types import ImgData

def return_cm_data():
    cm_data = [[0.2422, 0.1504, 0.6603],
    [0.2444, 0.1534, 0.6728],
    [0.2464, 0.1569, 0.6847],
    [0.2484, 0.1607, 0.6961],
    [0.2503, 0.1648, 0.7071],
    [0.2522, 0.1689, 0.7179],
    [0.254, 0.1732, 0.7286],
    [0.2558, 0.1773, 0.7393],
    [0.2576, 0.1814, 0.7501],
    [0.2594, 0.1854, 0.761],
    [0.2611, 0.1893, 0.7719],
    [0.2628, 0.1932, 0.7828],
    [0.2645, 0.1972, 0.7937],
    [0.2661, 0.2011, 0.8043],
    [0.2676, 0.2052, 0.8148],
    [0.2691, 0.2094, 0.8249],
    [0.2704, 0.2138, 0.8346],
    [0.2717, 0.2184, 0.8439],
    [0.2729, 0.2231, 0.8528],
    [0.274, 0.228, 0.8612],
    [0.2749, 0.233, 0.8692],
    [0.2758, 0.2382, 0.8767],
    [0.2766, 0.2435, 0.884],
    [0.2774, 0.2489, 0.8908],
    [0.2781, 0.2543, 0.8973],
    [0.2788, 0.2598, 0.9035],
    [0.2794, 0.2653, 0.9094],
    [0.2798, 0.2708, 0.915],
    [0.2802, 0.2764, 0.9204],
    [0.2806, 0.2819, 0.9255],
    [0.2809, 0.2875, 0.9305],
    [0.2811, 0.293, 0.9352],
    [0.2813, 0.2985, 0.9397],
    [0.2814, 0.304, 0.9441],
    [0.2814, 0.3095, 0.9483],
    [0.2813, 0.315, 0.9524],
    [0.2811, 0.3204, 0.9563],
    [0.2809, 0.3259, 0.96],
    [0.2807, 0.3313, 0.9636],
    [0.2803, 0.3367, 0.967],
    [0.2798, 0.3421, 0.9702],
    [0.2791, 0.3475, 0.9733],
    [0.2784, 0.3529, 0.9763],
    [0.2776, 0.3583, 0.9791],
    [0.2766, 0.3638, 0.9817],
    [0.2754, 0.3693, 0.984],
    [0.2741, 0.3748, 0.9862],
    [0.2726, 0.3804, 0.9881],
    [0.271, 0.386, 0.9898],
    [0.2691, 0.3916, 0.9912],
    [0.267, 0.3973, 0.9924],
    [0.2647, 0.403, 0.9935],
    [0.2621, 0.4088, 0.9946],
    [0.2591, 0.4145, 0.9955],
    [0.2556, 0.4203, 0.9965],
    [0.2517, 0.4261, 0.9974],
    [0.2473, 0.4319, 0.9983],
    [0.2424, 0.4378, 0.9991],
    [0.2369, 0.4437, 0.9996],
    [0.2311, 0.4497, 0.9995],
    [0.225, 0.4559, 0.9985],
    [0.2189, 0.462, 0.9968],
    [0.2128, 0.4682, 0.9948],
    [0.2066, 0.4743, 0.9926],
    [0.2006, 0.4803, 0.9906],
    [0.195, 0.4861, 0.9887],
    [0.1903, 0.4919, 0.9867],
    [0.1869, 0.4975, 0.9844],
    [0.1847, 0.503, 0.9819],
    [0.1831, 0.5084, 0.9793],
    [0.1818, 0.5138, 0.9766],
    [0.1806, 0.5191, 0.9738],
    [0.1795, 0.5244, 0.9709],
    [0.1785, 0.5296, 0.9677],
    [0.1778, 0.5349, 0.9641],
    [0.1773, 0.5401, 0.9602],
    [0.1768, 0.5452, 0.956],
    [0.1764, 0.5504, 0.9516],
    [0.1755, 0.5554, 0.9473],
    [0.174, 0.5605, 0.9432],
    [0.1716, 0.5655, 0.9393],
    [0.1686, 0.5705, 0.9357],
    [0.1649, 0.5755, 0.9323],
    [0.161, 0.5805, 0.9289],
    [0.1573, 0.5854, 0.9254],
    [0.154, 0.5902, 0.9218],
    [0.1513, 0.595, 0.9182],
    [0.1492, 0.5997, 0.9147],
    [0.1475, 0.6043, 0.9113],
    [0.1461, 0.6089, 0.908],
    [0.1446, 0.6135, 0.905],
    [0.1429, 0.618, 0.9022],
    [0.1408, 0.6226, 0.8998],
    [0.1383, 0.6272, 0.8975],
    [0.1354, 0.6317, 0.8953],
    [0.1321, 0.6363, 0.8932],
    [0.1288, 0.6408, 0.891],
    [0.1253, 0.6453, 0.8887],
    [0.1219, 0.6497, 0.8862],
    [0.1185, 0.6541, 0.8834],
    [0.1152, 0.6584, 0.8804],
    [0.1119, 0.6627, 0.877],
    [0.1085, 0.6669, 0.8734],
    [0.1048, 0.671, 0.8695],
    [0.1009, 0.675, 0.8653],
    [0.0964, 0.6789, 0.8609],
    [0.0914, 0.6828, 0.8562],
    [0.0855, 0.6865, 0.8513],
    [0.0789, 0.6902, 0.8462],
    [0.0713, 0.6938, 0.8409],
    [0.0628, 0.6972, 0.8355],
    [0.0535, 0.7006, 0.8299],
    [0.0433, 0.7039, 0.8242],
    [0.0328, 0.7071, 0.8183],
    [0.0234, 0.7103, 0.8124],
    [0.0155, 0.7133, 0.8064],
    [0.0091, 0.7163, 0.8003],
    [0.0046, 0.7192, 0.7941],
    [0.0019, 0.722, 0.7878],
    [0.0009, 0.7248, 0.7815],
    [0.0018, 0.7275, 0.7752],
    [0.0046, 0.7301, 0.7688],
    [0.0094, 0.7327, 0.7623],
    [0.0162, 0.7352, 0.7558],
    [0.0253, 0.7376, 0.7492],
    [0.0369, 0.74, 0.7426],
    [0.0504, 0.7423, 0.7359],
    [0.0638, 0.7446, 0.7292],
    [0.077, 0.7468, 0.7224],
    [0.0899, 0.7489, 0.7156],
    [0.1023, 0.751, 0.7088],
    [0.1141, 0.7531, 0.7019],
    [0.1252, 0.7552, 0.695],
    [0.1354, 0.7572, 0.6881],
    [0.1448, 0.7593, 0.6812],
    [0.1532, 0.7614, 0.6741],
    [0.1609, 0.7635, 0.6671],
    [0.1678, 0.7656, 0.6599],
    [0.1741, 0.7678, 0.6527],
    [0.1799, 0.7699, 0.6454],
    [0.1853, 0.7721, 0.6379],
    [0.1905, 0.7743, 0.6303],
    [0.1954, 0.7765, 0.6225],
    [0.2003, 0.7787, 0.6146],
    [0.2061, 0.7808, 0.6065],
    [0.2118, 0.7828, 0.5983],
    [0.2178, 0.7849, 0.5899],
    [0.2244, 0.7869, 0.5813],
    [0.2318, 0.7887, 0.5725],
    [0.2401, 0.7905, 0.5636],
    [0.2491, 0.7922, 0.5546],
    [0.2589, 0.7937, 0.5454],
    [0.2695, 0.7951, 0.536],
    [0.2809, 0.7964, 0.5266],
    [0.2929, 0.7975, 0.517],
    [0.3052, 0.7985, 0.5074],
    [0.3176, 0.7994, 0.4975],
    [0.3301, 0.8002, 0.4876],
    [0.3424, 0.8009, 0.4774],
    [0.3548, 0.8016, 0.4669],
    [0.3671, 0.8021, 0.4563],
    [0.3795, 0.8026, 0.4454],
    [0.3921, 0.8029, 0.4344],
    [0.405, 0.8031, 0.4233],
    [0.4184, 0.803, 0.4122],
    [0.4322, 0.8028, 0.4013],
    [0.4463, 0.8024, 0.3904],
    [0.4608, 0.8018, 0.3797],
    [0.4753, 0.8011, 0.3691],
    [0.4899, 0.8002, 0.3586],
    [0.5044, 0.7993, 0.348],
    [0.5187, 0.7982, 0.3374],
    [0.5329, 0.797, 0.3267],
    [0.547, 0.7957, 0.3159],
    [0.5609, 0.7943, 0.305],
    [0.5748, 0.7929, 0.2941],
    [0.5886, 0.7913, 0.2833],
    [0.6024, 0.7896, 0.2726],
    [0.6161, 0.7878, 0.2622],
    [0.6297, 0.7859, 0.2521],
    [0.6433, 0.7839, 0.2423],
    [0.6567, 0.7818, 0.2329],
    [0.6701, 0.7796, 0.2239],
    [0.6833, 0.7773, 0.2155],
    [0.6963, 0.775, 0.2075],
    [0.7091, 0.7727, 0.1998],
    [0.7218, 0.7703, 0.1924],
    [0.7344, 0.7679, 0.1852],
    [0.7468, 0.7654, 0.1782],
    [0.759, 0.7629, 0.1717],
    [0.771, 0.7604, 0.1658],
    [0.7829, 0.7579, 0.1608],
    [0.7945, 0.7554, 0.157],
    [0.806, 0.7529, 0.1546],
    [0.8172, 0.7505, 0.1535],
    [0.8281, 0.7481, 0.1536],
    [0.8389, 0.7457, 0.1546],
    [0.8495, 0.7435, 0.1564],
    [0.86, 0.7413, 0.1587],
    [0.8703, 0.7392, 0.1615],
    [0.8804, 0.7372, 0.165],
    [0.8903, 0.7353, 0.1695],
    [0.9, 0.7336, 0.1749],
    [0.9093, 0.7321, 0.1815],
    [0.9184, 0.7308, 0.189],
    [0.9272, 0.7298, 0.1973],
    [0.9357, 0.729, 0.2061],
    [0.944, 0.7285, 0.2151],
    [0.9523, 0.7284, 0.2237],
    [0.9606, 0.7285, 0.2312],
    [0.9689, 0.7292, 0.2373],
    [0.977, 0.7304, 0.2418],
    [0.9842, 0.733, 0.2446],
    [0.99, 0.7365, 0.2429],
    [0.9946, 0.7407, 0.2394],
    [0.9966, 0.7458, 0.2351],
    [0.9971, 0.7513, 0.2309],
    [0.9972, 0.7569, 0.2267],
    [0.9971, 0.7626, 0.2224],
    [0.9969, 0.7683, 0.2181],
    [0.9966, 0.774, 0.2138],
    [0.9962, 0.7798, 0.2095],
    [0.9957, 0.7856, 0.2053],
    [0.9949, 0.7915, 0.2012],
    [0.9938, 0.7974, 0.1974],
    [0.9923, 0.8034, 0.1939],
    [0.9906, 0.8095, 0.1906],
    [0.9885, 0.8156, 0.1875],
    [0.9861, 0.8218, 0.1846],
    [0.9835, 0.828, 0.1817],
    [0.9807, 0.8342, 0.1787],
    [0.9778, 0.8404, 0.1757],
    [0.9748, 0.8467, 0.1726],
    [0.972, 0.8529, 0.1695],
    [0.9694, 0.8591, 0.1665],
    [0.9671, 0.8654, 0.1636],
    [0.9651, 0.8716, 0.1608],
    [0.9634, 0.8778, 0.1582],
    [0.9619, 0.884, 0.1557],
    [0.9608, 0.8902, 0.1532],
    [0.9601, 0.8963, 0.1507],
    [0.9596, 0.9023, 0.148],
    [0.9595, 0.9084, 0.145],
    [0.9597, 0.9143, 0.1418],
    [0.9601, 0.9203, 0.1382],
    [0.9608, 0.9262, 0.1344],
    [0.9618, 0.932, 0.1304],
    [0.9629, 0.9379, 0.1261],
    [0.9642, 0.9437, 0.1216],
    [0.9657, 0.9494, 0.1168],
    [0.9674, 0.9552, 0.1116],
    [0.9692, 0.9609, 0.1061],
    [0.9711, 0.9667, 0.1001],
    [0.973, 0.9724, 0.0938],
    [0.9749, 0.9782, 0.0872],
    [0.9769, 0.9839, 0.0805]]

    return cm_data
cm_data = return_cm_data()
parula_map = LinearSegmentedColormap.from_list('parula', cm_data)
matplotlib.colormaps.register(name="parula", cmap=parula_map)

def mpl_to_plotly(cmap, pl_entries=255):
    h = np.linspace(0, 1, pl_entries)
    colors = cmap(h)[:, :3]
    return [[round(v, 2), f'rgb({",".join([str(int(c*255)) for c in color])})'] for v, color in zip(h, colors)]

batlow_plotly = mpl_to_plotly(cmc.batlow, pl_entries=255)
batlow_plotly2 = [[0.0, 'rgba(0,0,0,0.0)'], [0.0, 'rgb(2,26,89)'], [0.01, 'rgb(3,28,89)'], [0.01, 'rgb(4,29,90)'], [0.02, 'rgb(5,31,90)'], [0.02, 'rgb(5,32,90)'], [0.02, 'rgb(6,34,90)'], [0.03, 'rgb(7,35,91)'], [0.03, 'rgb(8,37,91)'], [0.04, 'rgb(8,38,91)'], [0.04, 'rgb(9,40,91)'], [0.04, 'rgb(10,41,92)'], [0.05, 'rgb(10,43,92)'], [0.05, 'rgb(11,44,92)'], [0.06, 'rgb(11,46,92)'], [0.06, 'rgb(12,47,93)'], [0.06, 'rgb(12,48,93)'], [0.07, 'rgb(12,50,93)'], [0.07, 'rgb(13,51,93)'], [0.07, 'rgb(13,52,93)'], [0.08, 'rgb(13,53,94)'], [0.08, 'rgb(14,55,94)'], [0.09, 'rgb(14,56,94)'], [0.09, 'rgb(14,57,94)'], [0.09, 'rgb(15,58,94)'], [0.1, 'rgb(15,59,95)'], [0.1, 'rgb(15,60,95)'], [0.11, 'rgb(15,61,95)'], [0.11, 'rgb(16,63,95)'], [0.11, 'rgb(16,64,95)'], [0.12, 'rgb(16,65,95)'], [0.12, 'rgb(16,66,96)'], [0.13, 'rgb(17,67,96)'], [0.13, 'rgb(17,68,96)'], [0.13, 'rgb(17,69,96)'], [0.14, 'rgb(17,70,96)'], [0.14, 'rgb(18,71,96)'], [0.15, 'rgb(18,71,97)'], [0.15, 'rgb(18,72,97)'], [0.15, 'rgb(19,73,97)'], [0.16, 'rgb(19,74,97)'], [0.16, 'rgb(19,75,97)'], [0.17, 'rgb(20,76,97)'], [0.17, 'rgb(20,77,97)'], [0.17, 'rgb(20,78,97)'], [0.18, 'rgb(21,79,97)'], [0.18, 'rgb(21,80,97)'], [0.19, 'rgb(22,81,98)'], [0.19, 'rgb(22,82,98)'], [0.19, 'rgb(23,83,98)'], [0.2, 'rgb(23,83,98)'], [0.2, 'rgb(24,84,98)'], [0.2, 'rgb(24,85,98)'], [0.21, 'rgb(25,86,98)'], [0.21, 'rgb(25,87,98)'], [0.22, 'rgb(26,88,98)'], [0.22, 'rgb(27,89,98)'], [0.22, 'rgb(27,90,97)'], [0.23, 'rgb(28,90,97)'], [0.23, 'rgb(29,91,97)'], [0.24, 'rgb(30,92,97)'], [0.24, 'rgb(31,93,97)'], [0.24, 'rgb(32,94,97)'], [0.25, 'rgb(33,94,96)'], [0.25, 'rgb(33,95,96)'], [0.26, 'rgb(34,96,96)'], [0.26, 'rgb(36,97,96)'], [0.26, 'rgb(37,97,95)'], [0.27, 'rgb(38,98,95)'], [0.27, 'rgb(39,99,95)'], [0.28, 'rgb(40,100,94)'], [0.28, 'rgb(41,100,94)'], [0.28, 'rgb(42,101,93)'], [0.29, 'rgb(44,102,93)'], [0.29, 'rgb(45,102,92)'], [0.3, 'rgb(46,103,92)'], [0.3, 'rgb(47,104,91)'], [0.3, 'rgb(49,104,91)'], [0.31, 'rgb(50,105,90)'], [0.31, 'rgb(51,105,89)'], [0.31, 'rgb(53,106,89)'], [0.32, 'rgb(54,107,88)'], [0.32, 'rgb(56,107,87)'], [0.33, 'rgb(57,108,87)'], [0.33, 'rgb(58,108,86)'], [0.33, 'rgb(60,109,85)'], [0.34, 'rgb(61,109,84)'], [0.34, 'rgb(63,110,84)'], [0.35, 'rgb(64,110,83)'], [0.35, 'rgb(66,111,82)'], [0.35, 'rgb(67,111,81)'], [0.36, 'rgb(69,112,80)'], [0.36, 'rgb(70,112,79)'], [0.37, 'rgb(72,113,79)'], [0.37, 'rgb(74,113,78)'], [0.37, 'rgb(75,114,77)'], [0.38, 'rgb(77,114,76)'], [0.38, 'rgb(78,115,75)'], [0.39, 'rgb(80,115,74)'], [0.39, 'rgb(81,116,73)'], [0.39, 'rgb(83,116,73)'], [0.4, 'rgb(84,117,72)'], [0.4, 'rgb(86,117,71)'], [0.41, 'rgb(88,118,70)'], [0.41, 'rgb(89,118,69)'], [0.41, 'rgb(91,119,68)'], [0.42, 'rgb(92,119,67)'], [0.42, 'rgb(94,120,66)'], [0.43, 'rgb(96,120,65)'], [0.43, 'rgb(97,121,65)'], [0.43, 'rgb(99,121,64)'], [0.44, 'rgb(101,122,63)'], [0.44, 'rgb(102,122,62)'], [0.44, 'rgb(104,122,61)'], [0.45, 'rgb(106,123,60)'], [0.45, 'rgb(107,123,59)'], [0.46, 'rgb(109,124,58)'], [0.46, 'rgb(111,124,58)'], [0.46, 'rgb(112,125,57)'], [0.47, 'rgb(114,125,56)'], [0.47, 'rgb(116,126,55)'], [0.48, 'rgb(117,126,54)'], [0.48, 'rgb(119,127,53)'], [0.48, 'rgb(121,127,53)'], [0.49, 'rgb(123,128,52)'], [0.49, 'rgb(124,128,51)'], [0.5, 'rgb(126,129,50)'], [0.5, 'rgb(130,130,49)'], [0.5, 'rgb(132,130,48)'], [0.51, 'rgb(134,131,47)'], [0.51, 'rgb(135,131,47)'], [0.52, 'rgb(137,132,46)'], [0.52, 'rgb(139,132,46)'], [0.52, 'rgb(141,133,45)'], [0.53, 'rgb(143,133,45)'], [0.53, 'rgb(145,134,44)'], [0.54, 'rgb(147,134,44)'], [0.54, 'rgb(149,135,43)'], [0.54, 'rgb(151,135,43)'], [0.55, 'rgb(153,136,43)'], [0.55, 'rgb(155,136,43)'], [0.56, 'rgb(157,136,43)'], [0.56, 'rgb(159,137,43)'], [0.56, 'rgb(161,137,43)'], [0.57, 'rgb(163,138,43)'], [0.57, 'rgb(165,138,43)'], [0.57, 'rgb(166,139,44)'], [0.58, 'rgb(168,139,44)'], [0.58, 'rgb(170,140,44)'], [0.59, 'rgb(172,140,45)'], [0.59, 'rgb(174,140,45)'], [0.59, 'rgb(176,141,46)'], [0.6, 'rgb(178,141,47)'], [0.6, 'rgb(180,141,48)'], [0.61, 'rgb(182,142,48)'], [0.61, 'rgb(184,142,49)'], [0.61, 'rgb(186,143,50)'], [0.62, 'rgb(188,143,51)'], [0.62, 'rgb(190,143,52)'], [0.63, 'rgb(192,144,53)'], [0.63, 'rgb(194,144,55)'], [0.63, 'rgb(196,144,56)'], [0.64, 'rgb(197,145,57)'], [0.64, 'rgb(199,145,58)'], [0.65, 'rgb(201,145,60)'], [0.65, 'rgb(203,146,61)'], [0.65, 'rgb(205,146,62)'], [0.66, 'rgb(206,146,64)'], [0.66, 'rgb(208,146,65)'], [0.67, 'rgb(210,147,67)'], [0.67, 'rgb(212,147,68)'], [0.67, 'rgb(213,147,70)'], [0.68, 'rgb(215,148,72)'], [0.68, 'rgb(217,148,73)'], [0.69, 'rgb(218,149,75)'], [0.69, 'rgb(220,149,77)'], [0.69, 'rgb(222,149,78)'], [0.7, 'rgb(223,150,80)'], [0.7, 'rgb(225,150,82)'], [0.7, 'rgb(226,150,84)'], [0.71, 'rgb(228,151,86)'], [0.71, 'rgb(229,151,88)'], [0.72, 'rgb(231,152,90)'], [0.72, 'rgb(232,152,92)'], [0.72, 'rgb(234,153,94)'], [0.73, 'rgb(235,153,96)'], [0.73, 'rgb(236,154,98)'], [0.74, 'rgb(237,154,100)'], [0.74, 'rgb(239,155,102)'], [0.74, 'rgb(240,156,104)'], [0.75, 'rgb(241,156,107)'], [0.75, 'rgb(242,157,109)'], [0.76, 'rgb(243,157,111)'], [0.76, 'rgb(244,158,113)'], [0.76, 'rgb(245,159,116)'], [0.77, 'rgb(246,159,118)'], [0.77, 'rgb(246,160,120)'], [0.78, 'rgb(247,161,123)'], [0.78, 'rgb(248,161,125)'], [0.78, 'rgb(248,162,127)'], [0.79, 'rgb(249,163,130)'], [0.79, 'rgb(249,164,132)'], [0.8, 'rgb(250,164,135)'], [0.8, 'rgb(250,165,137)'], [0.8, 'rgb(251,166,139)'], [0.81, 'rgb(251,167,142)'], [0.81, 'rgb(251,167,144)'], [0.81, 'rgb(252,168,146)'], [0.82, 'rgb(252,169,148)'], [0.82, 'rgb(252,170,151)'], [0.83, 'rgb(252,170,153)'], [0.83, 'rgb(252,171,155)'], [0.83, 'rgb(252,172,157)'], [0.84, 'rgb(253,173,160)'], [0.84, 'rgb(253,173,162)'], [0.85, 'rgb(253,174,164)'], [0.85, 'rgb(253,175,166)'], [0.85, 'rgb(253,176,168)'], [0.86, 'rgb(253,176,171)'], [0.86, 'rgb(253,177,173)'], [0.87, 'rgb(253,178,175)'], [0.87, 'rgb(253,179,177)'], [0.87, 'rgb(253,179,179)'], [0.88, 'rgb(253,180,181)'], [0.88, 'rgb(253,181,183)'], [0.89, 'rgb(253,181,185)'], [0.89, 'rgb(253,182,187)'], [0.89, 'rgb(252,183,190)'], [0.9, 'rgb(252,184,192)'], [0.9, 'rgb(252,184,194)'], [0.91, 'rgb(252,185,196)'], [0.91, 'rgb(252,186,198)'], [0.91, 'rgb(252,187,200)'], [0.92, 'rgb(252,187,202)'], [0.92, 'rgb(252,188,204)'], [0.93, 'rgb(252,189,207)'], [0.93, 'rgb(252,189,209)'], [0.93, 'rgb(252,190,211)'], [0.94, 'rgb(252,191,213)'], [0.94, 'rgb(252,192,215)'], [0.94, 'rgb(252,193,218)'], [0.95, 'rgb(251,193,220)'], [0.95, 'rgb(251,194,222)'], [0.96, 'rgb(251,195,224)'], [0.96, 'rgb(251,196,227)'], [0.96, 'rgb(251,196,229)'], [0.97, 'rgb(251,197,231)'], [0.97, 'rgb(251,198,233)'], [0.98, 'rgb(251,199,236)'], [0.98, 'rgb(251,200,238)'], [0.98, 'rgb(250,200,240)'], [0.99, 'rgb(250,201,243)'], [0.99, 'rgb(250,202,245)'], [1.0, 'rgb(250,203,247)'], [1.0, 'rgb(250,204,250)']]

# named_colorscales = px.colors.named_colorscales()

# parula_cmap = matplotlib.cm.get_cmap('parula')
# parula_rgb = []
# norm = matplotlib.colors.Normalize(vmin=0, vmax=255)
# for i in range(0, 255):
#     k = matplotlib.colors.colorConverter.to_rgb(parula_cmap(norm(i)))
#     parula_rgb.append(k)
# def matplotlib_to_plotly(cmap, pl_entries):
#     h = 1.0/(pl_entries-1)
#     pl_colorscale = []
#     for k in range(pl_entries):
#         C = map(np.uint8, np.array(cmap(k*h)[:3])*255)
#         pl_colorscale.append([k*h, 'rgb'+str((C[0], C[1], C[2]))])
#     return pl_colorscale
# parula = matplotlib_to_plotly(parula_rgb, 255)


elements_all = ['23Na','24Mg','27Al','29Si','31P','34S','35Cl','39K','43Ca','44Ca','45Sc','49Ti','51V','53Cr','55Mn','56Fe','57Fe',
                '59Co','60Ni','63Cu','65Cu','66Zn','69Ga','71Ga','72Ge','75As','77Se','79Br','81Br','85Rb','88Sr','89Y','90Zr','91Zr',
                '93Nb','95Mo','105Pd','107Ag','109Ag','111Cd','115In','118Sn','121Sb','125Te','127I','133Cs','137Ba','139La','140Ce',
                '141Pr','146Nd','147Sm','153Eu','157Gd','159Tb','163Dy','165Ho','166Er','169Tm','172Yb','175Lu','178Hf','181Ta','182W',
                '185Re','189Os','195Pt','197Au','202Hg','203Tl','205Tl','206Pb','207Pb','208Pb','209Bi','232Th','238U']

cmaps = ["cmc.batlow", "parula", "inferno", "plasma", "viridis", "nipy_spectral", "turbo", "Reds", "Greens", "Blues"]


def channelnorm(im, channel, vmin, vmax):
    im_copy = copy.deepcopy(im)
    c = (im_copy[:,:,channel]-vmin) / (vmax-vmin)
    c[c<0.] = 0
    c[c>1.] = 1
    im_copy[:,:,channel] = c
    return im_copy

def confidence_ellipse(x, y, ax, n_std=0.1, facecolor='none', **kwargs):
    # Convert to arrays and flatten
    x = np.asarray(x).flatten()
    y = np.asarray(y).flatten()
    # Mask invalid (NaN) values in both x and y
    valid = ~np.isnan(x) & ~np.isnan(y)
    x = x[valid]
    y = y[valid]
    if x.size == 0 or y.size == 0:
        print("No valid data for confidence ellipse.")
        return Ellipse((0, 0), width=0, height=0, facecolor=facecolor, **kwargs)
    if x.size != y.size:
        raise ValueError("x and y must be the same size")
    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.nanmean(x)
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.nanmean(y)
    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)
    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)                    


app_ui = ui.page_fluid("CODES Laser Ablation Mapper v 0.2.0 beta",
    ui.navset_tab(
        ui.nav_panel("Load Data",
                     ui.page_sidebar(
                         ui.sidebar(
                            # ui.input_text("folder", "Paste the folder path (remove quotes)"),
                            # ui.input_file("data_folder", "Select the folder containing the data files"),
                            ui.input_select("file_type", "CSV or TXT files?", choices=["TXT"]),
                            ui.input_file("data_files", "Select Data Files", multiple=True, accept=[".txt"]),
                            # ui.input_text("data_directory", "Enter the directory path for saving images and files. Before loading the files, right click a file, click 'Copy as path', and paste it here. Remove the quotes and file name."),     
                            ui.input_file("min_database", "Choose mineral database file", accept=[".xlsx", ".xls"]),                          
                            # ui.input_select("elem_list", "Choose the element list", choices=["TOF", "Pyrite", "MagPy"]),
                            ui.input_numeric("pixel_size", "Spot size (μm)", 9.0),
                            ui.input_select("aspect_ratio", "Select an aspect ratio option", choices=["Calculate aspect ratio", "Input aspect ratio"]),
                            ui.input_numeric("pixel_aspect", "Input Pixel Aspect Ratio", 1.0),
                            ui.markdown("Input scan speed and sweep time to calculate aspect ratio:"),
                            ui.input_numeric("scan_speed", "Scan speed (μm/s)", 9.0),
                            ui.input_numeric("sweep_time", "Total sweep time (ms) (343 for pyrite)", 343),
                            ui.download_button("data_cube_export", "Export maps as a data cube"),
                            ),
                        ui.output_text("done_text", inline=True),
                    ),
                ),


        ui.nav_panel("Map Calculator",
                     ui.page_sidebar(
                         ui.sidebar(
                             # ui.input_select("calc_type", "Select a calculation type", choices=["Total and Entropy", "Normal Calculation"]),
                             ui.accordion(
                                ui.accordion_panel("Normal Calculation",
                                    # ui.input_select("masked_map_calc", "Select mineral to use", choices=["All"]),
                                    ui.input_select("element_1", "Select Element 1", choices=elements_all),
                                    ui.input_select("operand", "Select Operand", choices=["/", "x", "+", "-"]),
                                    ui.input_select("element_2", "Select Element 2", choices=elements_all),
                                    ui.input_checkbox("use_log_calc", "Log Scale?", value=False),
                                    ui.input_slider("min_max_vals_calc", "Percentile Range", 0,100, [1,99], step=0.1),
                                    ui.input_select("c_map_calc", "Select color map", choices=cmaps),
                                    ui.input_action_button("disp_calc_mat", "Click to display Caculated Map"),
                                    ui.input_action_button("add_calc_mat", "Click to add calculated map to globals"),
                                    ), 
                                ui.accordion_panel("Entropy Calculation",
                                    ui.input_select("elem_4_entropy", "Select the elements to use for the total and entropy cacluations", choices=elements_all, multiple=True),
                                    ui.input_action_button("calc_entropy_map", "Calculate and Plot Shannon Entropy"),
                                    ),                                
                             id="calc_accordion",
                             )
                         ),
                         ui.output_plot("calc_plot"),
                         ui.output_text("added_calc"),
                         ui.output_plot("plot_entropy_map"),
                         
                     )
            ),

                

        ui.nav_panel("Mineral Classification",
                     ui.page_sidebar(
                            ui.sidebar(
                                ui.input_select("class_type",  "Select a classification type", choices=["None", "KMeans Classification", "Compositional Classification", "Library Matching"]),
                                ui.accordion(
                                    ui.accordion_panel(
                                        "KMeans Classification",
                                        ui.input_select("kmeans_elems", "Select Element for KMeans Classification", choices=elements_all, multiple=True),
                                        ui.input_numeric("n_clusters", "Number of Clusters", 3),
                                        ui.input_text("min_names", "Mineral Names (Separate by Commas)", ""),
                                        open=False,
                                        ),
                                    ui.accordion_panel(
                                        "Compositional Classification",
                                        ui.input_numeric("n_mins_comp", "Enter Number of Minerals for Compositional Classification (1, 2, or 3)", 1),
                                        ui.input_select("comp_elem_1", "Select Element 1", choices=elements_all),
                                        ui.input_numeric("min_conc_1", "Minimum of Element 1", 1),
                                        ui.input_numeric("max_conc_1", "Maximum of Element 1", 1e6),
                                        ui.input_text("comp_mineral_1", "Mineral 1 Name", "Mineral 1"),
                                        ui.input_select("comp_elem_2", "Select Element 2", choices=elements_all),
                                        ui.input_numeric("min_conc_2", "Minimum of Element 2", 1),
                                        ui.input_numeric("max_conc_2", "Maximum of Element 2", 1e6),
                                        ui.input_text("comp_mineral_2", "Mineral 2 Name", "Mineral 2"),
                                        ui.input_select("comp_elem_3", "Select Element 3", choices=elements_all),
                                        ui.input_numeric("min_conc_3", "Minimum of Element 3", 1),
                                        ui.input_numeric("max_conc_3", "Maximum of Element 3", 1e6),
                                        ui.input_text("comp_mineral_3", "Mineral 3 Name", "Mineral 3"),
                                        open=False,
                                        ),
                                    ui.accordion_panel(
                                        "Mineral Library Match",
                                        ui.input_select("elements_ID", "Select the elements to use for the mineral ID", choices=elements_all, multiple=True),
                                        ui.input_select("minerals_ID", "Select the minerals to consider", choices=[], multiple=True),
                                        ui.input_text("weights", "Enter the weights for each element separated by commas"),                             
                                        ui.input_numeric("ID_min_thresh", "Enter the minimum match percentage for successful ID", 70),
                                        ui.input_numeric("ID_max_thresh", "Enter the maximum match percentage for successful ID", 130),
                                        # ui.input_action_button("ID_mins", "Click to perform identification"),
                                        # ui.input_checkbox("highlight_row", "Highlight row on mineral map?", value=False),
                                        # ui.input_numeric("row_number","Row Number for Line Plot", 0),
                                        # ui.input_numeric("col_min", "Enter the minimum column index", 0),
                                        # ui.input_numeric("col_max", "Enter the maximum column index", -1),
                                        open=False,
                                        ),
                                    id="classification_accordion",
                                    ),
                                ui.download_button("download_min_means", "Download Mineral Means"),
                                ),
                            ui.input_action_button("classify_minerals", "Click to Perform Classification"),
                            ui.output_plot("plot_mineral_class"),
                            ui.div(
                                ui.output_table("mineral_class_table"),
                                style="overflow-x: auto; white-space: nowrap;"  # Add horizontal scrolling
                                ),
                            )
                     ),

        ui.nav_panel("Yield Correction", 
                     ui.page_sidebar(
                         ui.sidebar(
                             ui.input_numeric("row_number","Row Number for Line Plot", 0),
                             # ui.input_numeric("col_min", "Enter the minimum column index", 0),
                             # ui.input_numeric("col_max", "Enter the maximum column index", -1),
                             ui.input_action_button("perf_yield_cor", "Apply Yield Correction"),
                             ui.input_checkbox("use_cor_mats", "Use yield corrected values for all maps?", value=False),                             
                             ui.download_button("download_yc_means", "Download Yield Corrected Means"),
                             ui.download_button("download_yc_cube", "Download yield corrected data as a data cube."),
                            ),
                         ui.output_plot("yield_cor_plot"),
                         ui.output_plot("plot_max_percent"),
                         ui.output_plot("ycf_plot"),
                         ui.div(
                                ui.output_table("apply_yield_cor"),
                                style="overflow-x: auto; white-space: nowrap;"  # Add horizontal scrolling
                                ),
                            )
                     ),


        # ui.nav_panel("Single Map", 
        #            ui.page_sidebar(
        #                ui.sidebar(
        #                    ui.input_select("masked_map", "Select mineral to show", choices=["All"], selected=["All"], multiple=True),
        #                    ui.input_select("element", "Select Element", choices=elements_all),
        #                    ui.input_checkbox("use_log", "Log Scale?", value=False),
        #                    ui.input_select("c_map", "Select color map", choices=cmaps),
        #                    ui.input_slider("min_max_vals", "Color Percentile", 0,100, value= [1,99], step=0.1),
        #                    ui.input_numeric("colorbar_fract", "Colorbar size fraction", 0.1),
        #                    # ui.input_slider("max_val", "Maximum Percentile", 0,100, 99, step=0.1),
        #                    ui.input_text("colorbar_label", "Units:"),
        #                    ui.input_action_button("save_fig", "Save Figure"),
        #                    ),
        #                 ui.output_plot("plot", width="1000px", height="1000px"),
        #                 ui.output_text("save_figure"),
        #             )
        #            ),

        ui.nav_panel("Single Map", 
                   ui.page_sidebar(
                       ui.sidebar(
                           ui.input_select("masked_map", "Select mineral to show", choices=["All"], selected=["All"], multiple=True),
                           ui.input_select("element", "Select Element", choices=elements_all),
                           ui.input_checkbox("use_log", "Log Scale?", value=False),
                           ui.input_select("c_map", "Select color map", choices=["batlow"] + px.colors.named_colorscales(), selected="batlow"),
                           ui.input_slider("min_max_vals", "Color Percentile", 0,100, value= [1,99], step=0.1),
                        #    ui.input_numeric("colorbar_fract", "Colorbar size fraction", 0.1),
                        #    # ui.input_slider("max_val", "Maximum Percentile", 0,100, 99, step=0.1),
                        #    ui.input_text("colorbar_label", "Units:"),
                        #    ui.input_action_button("save_fig", "Save Figure"),
                           ),
                        output_widget("plot"),
                    )
                   ),

        ui.nav_panel("Image Overlay",
                     ui.page_sidebar(
                         ui.sidebar(
                             ui.input_file("imported_image", "Import a background image:", accept=[".jpg", ".png", ".jpeg", ".tif"]),
                             ui.input_select("overlay_map", "Select an element for alignment:", choices=elements_all),                             
                             ui.input_action_button("clear_points", "Clear Points"),
                             ui.input_action_button("perform_overlay", "Click to perform alignment"),                             
                             ui.input_select("overlay_result_element", "Select an element to overlay:", choices=["None yet"]),
                             ui.input_select("overlay_result_cscale", "Choose a colorscale for the overlay:", choices=["Blue-Green-Red", "batlow"]),
                             ui.input_numeric("overlay_alpha", "Opacity for overlay:", 0.5),
                             
                            ),
                        ui.markdown("Single clic to select at least three corresponding points from the imported (background) image and the alignment map. The click the button to perform the alignment."),
                        output_widget("imported"),
                        ui.output_text("imported_text"),
                        output_widget("plot_overlay"),
                        ui.output_text("overlay_text"),                        
                        ui.output_text("overlay_result_text"),
                        output_widget("overlay_result"),
                        )
                     ),



        ui.nav_panel("RGB Map", 
                   ui.page_sidebar(
                       ui.sidebar(
                           ui.input_select("masked_map_red", "Select mineral for showing in red channel", choices=["All"]),
                           # ui.input_select("cmap_ch1", "Select a Color for Ch 1", choices=cmaps, selected="Reds"),
                           ui.input_select("element_red", "Select element for red channel", choices=elements_all),
                           ui.input_slider("min_max_vals_red", "Percentile Range Red", 0,100, [1,99], step=0.1),
                           ui.input_select("masked_map_green", "Select mineral for showing in green channel", choices=["All"]),
                           # ui.input_select("cmap_ch2", "Select a Color for Ch 2", choices=cmaps, selected="Greens"),
                           ui.input_select("element_green", "Select element for green channel", choices=elements_all),
                           ui.input_slider("min_max_vals_green", "Percentile Range Green", 0,100, [1,99], step=0.1),
                           ui.input_select("masked_map_blue", "Select mineral for showing in blue channel", choices=["All"]),
                           # ui.input_select("cmap_ch3", "Select a Color for Ch 3", choices=cmaps, selected="Blues"),
                           ui.input_select("element_blue", "Select element for blue channel", choices=elements_all),
                           ui.input_slider("min_max_vals_blue", "Percentile Range Blue", 0,100, [1,99], step=0.1),
                           # ui.input_action_button("save_fig_rgb", "Save Figure"),
                           ),
                        output_widget("plot_rgb"),
                        # ui.input_numeric("rgb_legend_size", value=300),
                        output_widget("rgb_legend", width="500px", height="500px"),
                        )
                   ),


        ui.nav_panel("Multi Maps",
                     ui.page_sidebar(  
                        ui.sidebar(        
                            ui.input_select("masked_map_multi", "Select mineral to show", choices=["All"]),           
                            ui.input_select("elements", "Select Elements", choices=elements_all, multiple=True),
                            ui.input_checkbox("use_log_multi", "Log Scale?", value=True),
                            ui.input_text("colorbar_label_multi", "Units:", "ppm"),
                            ui.input_slider("min_val_multi", "Minimum Percentile", 0,100, 1, step=0.1),
                            ui.input_slider("max_val_multi", "Maximum Percentile", 0,100, 99, step=0.1),                            
                            ui.input_numeric("plots_per_row", "Plots per row", 4),
                            ui.input_numeric("fig_width", "Figure Width", 20),
                            ui.input_numeric("fig_height", "Figure Height", 20),
                            ui.input_select("cmap_multi", "Choose color map", choices=cmaps),
                            ui.input_action_button("disp_multi_plot", "Display Plot"),
                            ), 
                        ui.output_text("plot_multi"),
                        ui.output_image("plot_multi_disp")
                    ),
                   
                ),


        ui.nav_panel("ROI Selector",
                     ui.page_sidebar(
                         ui.sidebar(
                            # ui.h2("Draw a Box to Select Pixels"),
                            ui.input_select("element_plotly", "Select element", choices=elements_all),
                            ui.input_slider("min_max_vals_roi", "Color Percentile", 0,100, value= [1,99], step=0.1),
                            ui.input_select("plotly_colorscale", "Choose color map", choices=["batlow"] + px.colors.named_colorscales(), selected="batlow"),
                            ui.input_select("plotly_tool", "Selection Tool:", choices=["rectangle", "lasso"], selected="rectangle"),
                            # ui.input_action_button("btn", "Show shape info"),
                            ui.download_button("download_ROI_means", "Download ROI Means"),
                            ui.input_action_button("show_roi_means", "Show ROI Means"), 
                            ui.input_action_button("roi_to_globals", "Add ROIs to Globals"),
                            ),
                            # ui.output_plotly("image_plot", width="600px", height="600px"),
                        output_widget("image_plot", width="1000px", height="400px"),
                        # ui.output_text("print_coords"),
                        # ui.output_text("dump"),
                        ui.output_data_frame("selected_pixels"), 
                        ui.output_plot("plot_roi_means"),
                         )
                     ),

        # ui.nav_panel("ROI Selector", 
        #              ui.page_sidebar(
        #                 ui.sidebar(
        #                     ui.input_select("roi_type", "Select ROI type", choices=["Rectangle", "Polygon"]),
        #                     ui.input_select("masked_map_roi", "Select mineral for masking", choices=["All"]),
        #                     ui.input_select("element_roi", "Select Element for ROI Selections", choices=elements_all),
        #                     ui.input_action_button("make_roi_table", "Select ROI(s) from Map"),
        #                     ui.input_action_button("plot_rois", "Show Map with ROIs"),                            
        #                     # ui.input_action_button("show_roi_means", "Show ROI Means"),                            
        #                     # ui.input_action_button("roi_to_globals", "Add ROIs to Globals"),                            
        #                     ),
        #                 # ui.output_text("roi_intro"),
        #                 ui.markdown("""
        #                             ### ROI Selector
        #                             Use this tool to select regions of interest (ROIs) from your map.
        #                             1. Choose the ROI type (Rectangle or Polygon).
        #                             2. Select the mineral and element for ROI selections.
        #                             3. Click "Select ROI(s) from Map" and a new window will pop up. Start drawing.
        #                             4. Close the window to quit.
        #                             """),
        #                 ui.div(
        #                         ui.output_table("roi_table"),
        #                         style="overflow-x: auto; white-space: nowrap;"  # Add horizontal scrolling
        #                         ),
        #                 ui.output_plot("plot_roi"),
        #                 # ui.output_plot("plot_roi_means"),
        #                 ui.output_text("roi_to_globals_text"),
        #                 ),
        #             ),


        # ui.nav_panel("Draw Profiles",
        #              ui.page_sidebar(
        #                 ui.sidebar(
        #                     ui.input_select("masked_map_line", "Select mineral", choices=["All"]),
        #                     ui.input_select("element_line", "Select element for drawing the line profile", choices=elements_all),                        
        #                     ui.input_action_button("make_line_table", "Draw Line on Map"),                        
        #                     ui.input_action_button("plot_line_map", "Show Map with Line Profiles"),                        
        #                     ui.input_action_button("plot_profiles", "Show Profiles"),
        #                     ui.input_action_button("lines_to_global", "Add Lines to Globals")
        #                     ),
        #                 ui.output_text("line_intro"),
        #                 ui.div(
        #                         ui.output_table("line_table"),
        #                         style="overflow-x: auto; white-space: nowrap;"  # Add horizontal scrolling
        #                         ),
        #                 ui.output_plot("plot_lines"),
        #                 ui.output_plot("plot_profs"),
        #                 ui.output_text("lines_to_globals_text"),
        #                 ),
        #             ),

        ui.nav_panel("Pb Isotopes",
                     ui.page_sidebar(
                         ui.sidebar(
                             ui.input_numeric("thresh_206cps", "Threshold for 206Pb CPS", 10000),                                                                                    
                             ui.input_checkbox("show_error_ellipse", "Show error ellipse of valid data?", value=True),
                             ui.input_numeric("n_std_Pb", "Sigma multiplier for error ellipse", value=0.1),
                             ui.input_checkbox("show_map_mean", "Show median and standard error of all valid data?", value=True),
                             ui.input_checkbox("show_all_Pb", "Show all valid data points?", value=False),                             
                             ui.input_checkbox("show_rois_Pb", "Show means and standard errors of ROIs?", value = False),
                             ui.input_select("roi_selected_Pb", "Select ROIs to plot", choices=["None yet"], multiple=True),
                             ),
                        ui.row(
                            ui.column(3, ui.input_checkbox("show_mnt", "Show SK75 Mantle?", value=True)),
                            ui.column(3, ui.input_checkbox("show_ac", "Show SK75 Avg Crust?", value=True)),
                            ui.column(3, ui.input_checkbox("show_uc", "Show SK75 Upper Crust?", value=True)),
                            ui.column(3, ui.input_checkbox("show_stage_1", "Show stage 1 model?", value=False)),
                            ),
                        ui.row(
                            ui.output_plot("Pb_Pb_plot")
                            ),
                        ui.row(
                            ui.column(
                                6,
                                ui.input_numeric("Pb_age", "Age (Ma)", 1800, step=1),
                                ui.input_numeric("mu", "mu (238U/204Pb) Default is 9.74", 9.74, step=0.01),
                                ui.input_numeric("kappa", "kappa (232Th/238U) Default is 3.82", 3.82, step=0.01),
                                ),
                            ui.column(
                                6,
                                ui.input_checkbox("autoscale_Pb_plot", "Plot Full Scale?", value=False),
                                ui.input_slider("Pb_plot_xlims", "Plot x limits", 0,2.5, value=[0.8, 1.2], step=0.01),
                                ui.input_slider("Pb_plot_ylims", "Plot y limits", 0,4.5, value=[1.8, 3.2], step=0.01),
                                ),
                            ),                        
                        )
                     ),

        ui.nav_panel("Network Graph",
                     ui.page_sidebar(
                         ui.sidebar(
                            ui.input_select("minerals_graph", "Select mineral(s) for plotting", choices=["All"], multiple=False),
                            ui.input_checkbox("choose_elems_graph", "Choose elements for the graph?", value=False),
                            ui.input_select("elems_graph", "If the above is ticked, select elements here", choices=elements_all, multiple=True),
                            ui.input_numeric("min_conc", "Concentration Threshold (ppm)", 10),
                            ui.input_numeric("corr_threshold", "Correlation Threshold", 0.5),
                            ui.input_select("corr_type", "Correlation Type", choices=["Pearson", "Spearman"]),
                            ui.input_action_button("make_graphs", "Make Graph"),
                         ),
                         ui.output_plot("mats_graph_plot")
                        )
        ),

        ui.nav_panel("Correlation Matrix",
                     ui.page_sidebar(
                            ui.sidebar(
                            ui.input_select("minerals_corr_mat", "Select mineral(s) for plotting", choices=["All"], multiple=False),
                            ui.input_select("corr_mat_els", "Select elements for correlation matrix", choices=elements_all, multiple=True),
                            #  ui.input_numeric("min_conc_corr", "Concentration Threshold (ppm)", 10),
                            #  ui.input_numeric("corr_threshold_matrix", "Correlation Threshold", 0.5),
                            #  ui.input_numeric("corr_threshold_matrix2", "Correlation Threshold 2", 0.5),
                            ui.input_checkbox("cor_log", "Log Scale?", value=False),
                            ui.input_numeric("cor_linthresh", "Log scale linear threshold", 0.01),
                            ui.input_select("corr_type_matrix", "Correlation Type", choices=["Pearson", "Spearman"]),
                            ui.input_action_button("make_corr_matrix", "Make Correlation Matrix"),
                            ),
                         ui.output_plot("plot_corr_matrix"),
                        )
                     ),
            
        ui.nav_panel("Histogram",
                     ui.page_sidebar(
                         ui.sidebar(
                             ui.input_select("hist_type", "Select a plot type", choices=["KDE", "Histogram"], selected="KDE"),
                             ui.input_select("mineral_hist", "Select mineral(s) for plotting", choices=["All"], multiple=True, selected=["All"]),
                             ui.input_select("element_hist", "Select Element for Histogram", choices=elements_all),
                             ui.input_checkbox("use_log_hist", "Log Scale?", value=False),
                             ui.input_slider("min_max_vals_x", "Percentile range for x-axis", 0,100, [0,99.9], step=0.01),
                             ui.input_numeric("bw_adj", "Bandwidth adjustment factor for KDE", 1),
                             ui.input_text("bw_adj_multi", "Bandwidth adjustment factors for each mineral (comma separated)", "1"),
                             ui.input_numeric("num_bins", "Number of bins for histogram", 500),
                             ),
                         ui.output_plot("plot_hist"),
                        )
                     ),
        

        ui.nav_panel("Bivariate Plot",
                     ui.page_sidebar(
                        ui.sidebar(
                            ui.input_checkbox("use_rois", "Use data from ROIs?", value=False),
                            ui.input_select("roi_selected", "Select ROI(s)", choices=["None yet"], multiple=True),
                            ui.input_checkbox("use_lines", "Use data from lines?", value=False),
                            ui.input_select("line_selected", "Select line(s)", choices=["None yet"], multiple=True),
                            ui.input_select("mineral_bivariate", "Select mineral(s) for plotting", choices=["All"], multiple=True, selected=["All"]),
                            ui.input_select("element_xaxis", "Select an element for the x-axis", choices=elements_all),
                            ui.input_select("element_yaxis", "Select an element for the y-axis", choices=elements_all),
                            ui.input_checkbox("mineral_color", "Color with mineral type?", value=False),
                            ui.input_checkbox("color_map", "Color with the concentration of another element?", value=False),
                            ui.input_select("c_map_bivariate", "Select element for color", choices=cmaps),
                            ui.input_checkbox("use_log_x_axis", "Log scale for x-axis?", value=False),
                            ui.input_slider("min_max_vals_xaxis", "Percentile range for x-axis", 0,100, [1,99], step=0.1),
                            ui.input_checkbox("use_log_y_axis", "Log scale for y-axis?", value=False),
                            ui.input_slider("min_max_vals_yaxis", "Percentile range for y-axis", 0,100, [1,99], step=0.1),
                            ui.input_checkbox("use_log_color", "Log scale for color map?", value=False),
                            ui.input_slider("min_max_vals_color", "Percentile range for color map", 0,100, [1,99], step=0.1),
                            ),
                        ui.output_plot("plot_bivariate"),
                        )
                     ),

        ui.nav_panel("Deconvolution",
                     ui.page_sidebar(
                         ui.sidebar(
                             ui.input_checkbox("use_rois_decon", "Use data from ROIs", value=False),
                             ui.input_select("roi_selected_decon", "Select ROI(s)", choices=["None yet"], multiple=True),
                             ui.input_checkbox("use_lines_decon", "Use data from line proiles?", value=False),
                             ui.input_select("line_selected_decon", "Select line(s)", choices=["None yet"], multiple=True),
                             ui.input_select("decon_xaxis", "Choose an element for the x-axis", choices=elements_all),
                             ui.input_numeric("decon_ideal_val", "Enter the x-axis value for the target mineral", 100000),
                             ui.input_select("decon_yaxis", "Choose element(s) for y-axis", choices=elements_all, multiple=False),
                             ui.input_checkbox("use_log_x_axis_decon", "Log scale for x-axis?", value=False),
                             ui.input_slider("min_max_vals_xaxis_decon", "Percentile range for x-axis", 0,100, [1,99], step=0.1),
                             ui.input_checkbox("use_log_y_axis_decon", "Log scale for y-axis?", value=False),
                             ui.input_slider("min_max_vals_yaxis_decon", "Percentile range for y-axis", 0,100, [1,99], step=0.1),
                            ),
                            ui.output_plot("decon_plot"),
                            ui.output_table("decon_table")
                        ),
                     ),

        
        ui.nav_panel("PCA Analysis",
            ui.page_sidebar(
                ui.sidebar(
                    ui.input_select("pca_elements", "Select Elements for PCA", choices=elements_all, multiple=True),
                    ui.input_select("mineral_pca", "Select mineral(s) for plotting", choices=["All"], multiple=True, selected=["All"]),                    
                    ui.input_numeric("n_components", "Number of PCA Components", 2),
                    ui.input_checkbox("use_log_x_axis_pca", "Log scale for x-axis?", value=False),
                    ui.input_numeric("pca_linthresh_x", "Log scale linthresh for x-axis", 1),
                    ui.input_slider("min_max_pca_xaxis", "Percentile range for x-axis", 0,100, [1,99], step=0.01),
                    ui.input_checkbox("use_log_y_axis_pca", "Log scale for y-axis?", value=False),
                    ui.input_numeric("pca_linthresh_y", "Log scale linthresh for y-axis", 1),
                    ui.input_slider("min_max_pca_yaxis", "Percentile range for y-axis", 0,100, [1,99], step=0.01),
                    ui.input_slider("max_pca_yaxis", "Maximum percentile for y_axis", 0,100, 99, step=0.01),
                    ui.input_checkbox("pca_color_map", "Color with the concentration of another element?", value=False),
                    ui.input_select("c_map_pca", "Select element for color", choices=elements_all),
                    ui.input_slider("min_max_pca_color", "Percentile range for color map", 0,100, [1,99], step=0.1),
                    ui.input_checkbox("use_log_pca", "Log scale for color map?", value=False),
                    ),
                ui.output_plot("pca_plot"),
                # ui.output_text("pca_summary"),
                )
            ),
    
    )   
)



def server(input: Inputs, output: Outputs, session: Session):

    @reactive.calc
    def data_loader():
        global global_mats
        global global_elements
        global global_data_path

        mats = {}
        loaded_elements = []  # List to store successfully loaded elements

        # Get the list of selected files
        files = input.data_files()
        if files is None:
            print("No files selected.")
            return mats, loaded_elements
        
        global_data_path = os.path.dirname(files[0]["datapath"])
        print(global_data_path)
        # global_data_path = input.data_directory()

        # Process each selected file
        for file in files:
            file_path = file["datapath"]
            file_name = file["name"]  # Get the original file name
            element_name = os.path.splitext(file_name)[0]  # Extract element name without the extension
            if element_name.startswith("Traces "):
                element_name = element_name.replace("Traces ", "") + "_ppm"
            try:
                if file_name.endswith(".csv"):
                    mats[element_name] = np.loadtxt(file_path, delimiter=",")
                elif file_name.endswith(".txt"):
                    if element_name.endswith("_ppm"):
                        mats[element_name] = np.loadtxt(file_path) * 10000
                    else:
                        mats[element_name] = np.loadtxt(file_path)
                    # print(f"{element_name} shape = {np.shape(mats[element_name])}")
                else:
                    print(f"Unsupported file format: {file_name}")
                    continue

                loaded_elements.append(element_name)
            except Exception as e:
                print(f"Error loading file {file_name}: {e}")

        shapes = [v.shape for v in mats.values() if isinstance(v, np.ndarray)]
        if shapes:
            min_rows = min(s[0] for s in shapes)
            min_cols = min(s[1] for s in shapes)
            # Clip all mats to the minimum shape
            for k in mats:
                if isinstance(mats[k], np.ndarray) and mats[k].shape[0] >= min_rows and mats[k].shape[1] >= min_cols:
                    mats[k] = mats[k][:min_rows, :min_cols]

        global_mats = mats
        global_elements = loaded_elements

        return mats, loaded_elements
    
    # @reactive.calc
    # def data_loader():

    #     global global_mats
    #     global global_elements

    #     mats = {}
    #     loaded_elements = []  # List to store successfully loaded elements

    #     element_list = elements_all 

    #     if input.file_type() == "CSV":
    #         for elem in element_list:
    #             file_path = '{}/matrix_{}_ppm.csv'.format(global_data_path, elem)
    #             if os.path.exists(file_path):
    #                 mats[f"{elem}_ppm"] = np.loadtxt(file_path, delimiter=",")
    #                 loaded_elements.append(f"{elem}_ppm")
    #             else:
    #                 print(f"Warning: File not found: {file_path}")

    #     else:
    #         folder_ = input.data_folder()
    #         if folder_ is None:
    #             folder_path = ""
    #         else:
    #             folder_path = folder_["datapath"]
    #         for elem in element_list:
    #             file_path = "{}/Traces {}.txt".format(folder_path, elem)
    #             if os.path.exists(file_path):
    #                 mats[f"{elem}_ppm"] = np.loadtxt(file_path) * 10000
    #                 loaded_elements.append(f"{elem}_ppm")
    #             else:
    #                 print(f"Warning: File not found: {file_path}")
                    
        
    #     # elements_for_total = loaded_elements
        
    #     global_mats = mats
    #     global_elements = loaded_elements

    #     return mats, loaded_elements
    
    @reactive.calc
    @reactive.event(input.make_roi_table)
    def get_roi_data():
        
        # mats_roi, loaded_elements = data_loader()
        if input.masked_map_roi() == "All":
            if "global_mats" in globals():
                if input.use_cor_mats() == True:
                    mats_roi = ycf_cor_mats
                else:
                    mats_roi = global_mats
                loaded_elements = global_elements
            else:
                mats_roi = {}
                loaded_elements = []
        else:
            if "global_masked_mats" in globals():
                if input.use_cor_mats() == True:
                    mats_roi = ycf_cor_masked_mats[input.masked_map_roi()]
                else:
                    mats_roi = global_masked_mats[input.masked_map_roi()]
                loaded_elements = global_elements
            else:
                mats_roi = {}
                loaded_elements = []
        element_list = loaded_elements

        if mats_roi == {}:
            print("No data loaded. Please load data first.")
        else:
            data = mats_roi[input.element_roi()]

        global global_roi_dict
        global global_roi_keys


        if input.roi_type() == "Rectangle":

            # List to store multiple selected regions
            selected_coords = []
            selected_regions = []
            selected_data = []

            # Callback function to handle the selection
            def onselect(eclick, erelease):
                """
                eclick and erelease are the mouse click and release events.
                eclick contains the starting coordinates (x1, y1),
                and erelease contains the ending coordinates (x2, y2).
                """
                # Convert scaled coordinates back to matrix indices
                x1 = int(eclick.xdata)
                y1 = int(eclick.ydata)
                x2 = int(erelease.xdata)
                y2 = int(erelease.ydata)

                # Ensure indices are within bounds
                x1, x2 = max(0, x1), min(data.shape[1], x2)
                y1, y2 = max(0, y1), min(data.shape[0], y2)

                selected_coords.append([y1, y2, x1, x2])

                # Extract the selected region from the data
                region_means = {}
                region_data = {}
                region_means['coords'] = [y1, y2, x1, x2]
                region_data['coords'] = [y1, y2, x1, x2]
                region_means["region_type"] = "Rectangle"
                region_data["region_type"] = "Rectangle"
                region_means["mineral_name"] = input.masked_map_roi()
                region_data["mineral_name"] = input.masked_map_roi()
                for el in element_list:
                    if el not in mats_roi:
                        print(f"Warning: Element '{el}' not found in mats_roi.")
                        continue
                    if not np.issubdtype(mats_roi[el].dtype, np.number):
                        print(f"Skipping non-numeric element: {el}")
                        continue
                    region_data[el] = ((mats_roi[el][y1:y2, x1:x2]).flatten()).tolist()
                    region_means[el] = np.nanmean(mats_roi[el][y1:y2, x1:x2])
                    region_means[f"{el}_std"] = np.nanstd(mats_roi[el][y1:y2, x1:x2])                
                selected_regions.append(region_means)  # Add the region to the list                
                selected_data.append(region_data)

                

            # Create the plot
            fig, ax = plt.subplots()
            ax.set_facecolor("black")
            vmin_ = np.nanpercentile(data, 1)
            vmax_ = np.nanpercentile(data, 99)
            ax.imshow(data, norm=colors.SymLogNorm(linthresh=0.001, vmin=vmin_, vmax=vmax_), cmap='parula', interpolation='none')

            # Create the RectangleSelector
            rectangle_selector = RectangleSelector(
                ax, onselect, useblit=True,
                button=[1],  # Left mouse button
                minspanx=1, minspany=1,  # Minimum size of the rectangle
                spancoords='pixels',
                interactive=True)

            plt.show()

            # global global_roi_dict
            # global global_roi_keys

            return selected_coords, selected_regions, selected_data
        
        elif input.roi_type() == "Polygon":
            # List to store multiple selected regions
            selected_coords = []                    
            selected_regions = []
            selected_data = []

            # Callback function to handle the selection
            def onselect(verts):
                # Convert vertices to integer indices
                x_coords, y_coords = zip(*map(lambda v: (max(0, min(data.shape[1], int(v[0]))), 
                                                        max(0, min(data.shape[0], int(v[1])))), verts))
                
                # Get the pixel coordinates of the polygon
                rr, cc = polygon(y_coords, x_coords)
                rr = np.clip(rr, 0, data.shape[0] - 1)
                cc = np.clip(cc, 0, data.shape[1] - 1)

                # Store the coordinates
                selected_coords.append(list(zip(rr, cc)))

                # Extract the selected region from the data
                region_means = {}
                region_data = {}
                region_means['coords'] = list(zip(y_coords, x_coords))  # Store the polygon vertices
                region_data["coords"] = list(zip(y_coords, x_coords))  # Store the polygon vertices
                region_means["region_type"] = "Polygon"
                region_data["region_type"] = "Polygon"
                region_means["mineral_name"] = input.masked_map_roi()
                region_data["mineral_name"] = input.masked_map_roi()
                for el in element_list:
                    if el not in mats_roi:
                        print(f"Warning: Element '{el}' not found in mats_roi.")
                        continue
                    if not np.issubdtype(mats_roi[el].dtype, np.number):
                        print(f"Skipping non-numeric element: {el}")
                        continue
                    # Extract the pixel values within the polygon
                    mask = np.zeros(data.shape, dtype=bool)
                    mask[rr, cc] = True
                    region_data[el] = (((mats_roi[el][mask])).flatten()).tolist()
                    region_means[el] = np.nanmean(mats_roi[el][mask])
                    region_means[f"{el}_std"] = np.nanstd(mats_roi[el][mask])
                selected_regions.append(region_means)  # Add the region to the list
                selected_data.append(region_data)

        
            # Create the plot
            fig, ax = plt.subplots()
            ax.set_facecolor("black")
            vmin_ = np.nanpercentile(data, 1)
            vmax_ = np.nanpercentile(data, 99)
            ax.imshow(data, norm=colors.SymLogNorm(linthresh=0.001, vmin=vmin_, vmax=vmax_), cmap='parula', interpolation='none')
            # Create the PolygonSelector
            polygon_selector = PolygonSelector(ax, onselect, useblit=True, props=dict(color='red'))
            plt.show()

            return selected_coords, selected_regions, selected_data

        

    @reactive.calc
    @reactive.event(input.roi_to_globals)
    def make_roi_dict():
        global global_roi_dict
        global global_roi_keys

        loaded_elements = global_elements

        # df = pd.read_csv("{}/roi_data.txt".format(global_data_path), sep="\t")
        df = global_roi_data_df
        # df = pq.read_pandas("{}/roi_data.parquet".format(global_data_path)).to_pandas()
        roi_dict = {}
        roi_list = []

        for i in range(len(df)):
            region_data = {}
            for el in loaded_elements:
                if el not in df.columns or df[el].isnull().all():
                    print(f"{el} not in element list or contains only null values")
                    continue
                else:
                    value = df[el][i]
                    if isinstance(value, str):
                        sanitized_string = value.replace('nan', '0')
                    elif isinstance(value, float) and math.isnan(value):
                        sanitized_string = '0'
                    else:
                        sanitized_string = str(value)
                    try:
                        array = np.array(ast.literal_eval(sanitized_string))
                    except (ValueError, SyntaxError) as e:
                        print(f"Error parsing string to array: ROI{i}. Element: {el}. Error: {e}")
                        array = np.array([])  # Default to an empty array if parsing fails
                    region_data[el] = np.where(array == 0, np.nan, array)
            roi_dict[f"ROI{i}"] = region_data
            roi_list.append(f"ROI{i}")
        print(roi_list)
        # print(roi_dict["ROI12"])


        # if input.masked_map_line() == "All":
        #     if "global_mats" in globals():
        #         mats_roi = global_mats
        #         loaded_elements = global_elements
        #     else:
        #         mats_roi = {}
        #         loaded_elements = []
        # else:
        #     if "global_masked_mats" in globals():
        #         mats_roi = global_masked_mats[input.masked_map_line()]
        #         loaded_elements = global_elements
        #     else:
        #         mats_roi = {}
        #         loaded_elements = []
        # element_list = loaded_elements

        # if mats_roi == {}:
        #     raise ValueError("No data loaded. Please load data first.")
        # else:
        #     data = mats_roi[input.element_roi()]

        # roi_dict = {}
        # roi_list = []
        # for i in range(len(df)):
        #     if df["region_type"][i] == "Polygon":
        #         coords_rois = ast.literal_eval(df['coords'][i])
        #         x_coords = [coord[1] for coord in coords_rois]
        #         print(x_coords)
        #         y_coords = [coord[0] for coord in coords_rois]
        #         print(y_coords)
        #         rr, cc = polygon(y_coords, x_coords)
        #         rr = np.clip(rr, 0, data.shape[0] - 1)
        #         cc = np.clip(cc, 0, data.shape[1] - 1)

        #         region_data = {}
        #         for el in element_list:
        #             if el not in mats_roi:
        #                 print(f"Warning: Element '{el}' not found in mats_roi.")
        #                 continue
        #             if not np.issubdtype(mats_roi[el].dtype, np.number):
        #                 print(f"Skipping non-numeric element: {el}")
        #                 continue
        #             # Extract the pixel values within the polygon
        #             mask = np.zeros(data.shape, dtype=bool)
        #             mask[rr, cc] = True
        #             region_data[el] = mats_roi[el][mask]

        #     elif df["region_type"][i] == "Rectangle":
        #         coords_rois = ast.literal_eval(df['coords'][i])
        #         coords_rois = [int(x) for x in coords_rois]
        #         y1 = coords_rois[0]
        #         y2 = coords_rois[1]
        #         x1 = coords_rois[2]
        #         x2 = coords_rois[3]

        #         region_data = {}
        #         for el in element_list:
        #             if el not in mats_roi:
        #                 print(f"Warning: Element '{el}' not found in mats_roi.")
        #                 continue
        #             if not np.issubdtype(mats_roi[el].dtype, np.number):
        #                 print(f"Skipping non-numeric element: {el}")
        #                 continue
        #             region_data[el] = mats_roi[el][y1:y2, x1:x2]

        #     else:
        #         print(f"Warning: ROI{i+1} does not have a supported geometry. Skipping.")
        #         continue
        #     roi_dict[f"ROI{i+1}"] = region_data
        #     roi_list.append(f"ROI{i+1}")

        global_roi_dict = roi_dict
        global_roi_keys = roi_list

        return roi_dict, roi_list
            

        
    @reactive.calc
    @reactive.event(input.make_line_table)
    def get_line_data():
        # mats_roi, loaded_elements = data_loader()
        if input.masked_map_line() == "All":
            if "global_mats" in globals():
                if input.use_cor_mats() == True:
                    mats_roi = ycf_cor_mats
                else:
                    mats_roi = global_mats
                loaded_elements = global_elements
            else:
                mats_roi = {}
                loaded_elements = []
        else:
            if "global_masked_mats" in globals():
                if input.use_cor_mats() == True:
                    mats_roi = ycf_cor_masked_mats[input.masked_map_line()]
                else:
                    mats_roi = global_masked_mats[input.masked_map_line()]
                loaded_elements = global_elements
            else:
                mats_roi = {}
                loaded_elements = []
        element_list = loaded_elements

        if mats_roi == {}:
            print("No data loaded. Please load data first.")
            return None, None, None, None
        else:
            data = mats_roi[input.element_line()]

        selected_line_coords = []

        def onselect(verts):
            # Convert vertices to integer indices
            x1, y1 = map(int, verts[0])  # Start point
            x2, y2 = map(int, verts[1])  # End point

            # Ensure indices are within bounds
            x1, x2 = max(0, x1), min(data.shape[1], x2)
            y1, y2 = max(0, y1), min(data.shape[0], y2)

            # Get the pixel coordinates of the line
            rr, cc = line(y1, x1, y2, x2)
            rr = np.clip(rr, 0, data.shape[0] - 1)
            cc = np.clip(cc, 0, data.shape[1] - 1)

            # Store the coordinates
            selected_line_coords.append(list(zip(rr, cc)))

        # Create the plot
        fig, ax = plt.subplots()
        ax.set_facecolor("black")
        vmin_ = np.nanpercentile(data, 1)
        vmax_ = np.nanpercentile(data, 99)
        ax.imshow(data, norm=colors.SymLogNorm(linthresh=0.001, vmin=vmin_, vmax=vmax_), cmap='parula', interpolation='none')

        # Create the LineSelector
        polygon_selector = PolygonSelector(ax, onselect, useblit=True, props=dict(color='red'))

        plt.show()

        # Process the selected line's data
        if selected_line_coords:
            selected_line_regions = []
            selected_data = []
            for coords in selected_line_coords:
                region_values = {}
                region_data = {}
                region_values['coords'] = coords
                for el in element_list:
                    if el not in mats_roi:
                        print(f"Warning: Element '{el}' not found in mats_roi.")
                        continue
                    if not np.issubdtype(mats_roi[el].dtype, np.number):
                        print(f"Skipping non-numeric element: {el}")
                        continue
                    # Extract the pixel values along the line
                    values = np.nan_to_num(mats_roi[el][tuple(zip(*coords))], nan=0)
                    region_data[el] = values
                    region_values[el] = values.tolist()  # Convert to list for easier display
                selected_line_regions.append(region_values)
                selected_data.append(region_data)
        
            coords = selected_line_coords[0]
            line_start = coords[0]
            line_end = coords[-1]
            array = np.array([line_start, line_end]).T
            line_x = array[1]
            line_y = array[0]
            dx = (line_x[1] - line_x[0])*input.pixel_size()
            dy = (line_y[1] - line_y[0])*input.pixel_size()
            total_distance = np.sqrt(dx**2 + dy**2)


        return selected_line_coords, selected_line_regions, total_distance
    
    @reactive.calc()
    @reactive.event(input.lines_to_global)
    def make_lines_dict():
        global global_line_dict
        global global_line_keys

        loaded_elements = global_elements

        df = pd.read_csv("{}/line_data.txt".format(global_data_path), sep="\t")
        line_dict = {}
        line_list = []

        for i in range(len(df)):
            region_line_data = {}
            for el in loaded_elements:
                if el not in df.columns or df[el].isnull().all():
                    print(f"{el} not in element list or contains only null values")
                    continue
                else:
                    value = df[el][i]
                    if isinstance(value, str):
                        sanitized_string = value.replace('nan', '0')
                    elif isinstance(value, float) and math.isnan(value):
                        sanitized_string = '0'
                    else:
                        sanitized_string = str(value)
                    array = np.array(ast.literal_eval(sanitized_string))
                    region_line_data[el] = np.where(array == 0, np.nan, array)
            line_dict[f"Line{i+1}"] = region_line_data
            line_list.append(f"Line{i+1}")
        print(line_list)
        # print(line_dict["Line1"])

        global_line_dict = line_dict
        global_line_keys = line_list

        return line_dict, line_list



    
    @reactive.calc
    def calc_entropy():  
        global global_mats
        global global_elements
        if input.use_cor_mats() == True:
            mats = ycf_cor_mats
        else:
            mats = global_mats
        loaded_elements = global_elements
        included_elements = list(input.elem_4_entropy())  # Convert tuple to list

        if mats != {}:
            # Ensure all arrays in mats have the same shape
            reference_shape = list(mats.values())[0].shape
            for key, value in mats.items():
                if value.shape != reference_shape:
                    raise ValueError(f"Array for {key} does not match the reference shape {reference_shape}.")

            # Initialize an array of zeros with the same shape as the arrays in mats
            pixel_sum = np.zeros(reference_shape)


            # Iterate through the arrays in mats and add them to the pixel_sum
            for key, array in mats.items():
                if key in included_elements:
                    if np.issubdtype(array.dtype, np.number):  # Ensure the array contains numeric data
                        pixel_sum += array
                    else:
                        print(f"Skipping non-numeric array: {key}")

            # Normalize the pixel sum to create a "total" map
            mats['total'] = pixel_sum / 10000
            if 'total' not in loaded_elements:
                loaded_elements.append("total")

            # Calculate entropy for each pixel
            entropy_map = np.zeros(reference_shape)
            for key, array in mats.items():
                if key in included_elements and np.issubdtype(array.dtype, np.number):
                    # Avoid division by zero
                    proportion = array / pixel_sum
                    proportion = np.clip(proportion, 1e-25, 1)  # Avoid log(0)
                    entropy_map -= proportion * np.log2(proportion)

            # Add the entropy map to the global mats
            mats['entropy'] = entropy_map
            if 'entropy' not in loaded_elements:
                loaded_elements.append("entropy")
            global_elements = loaded_elements  # Update global_elements
            global_mats = mats  # Update the global mats dictionary

            return mats, loaded_elements

        # Default return if mats is empty
        return mats, loaded_elements
    
    @reactive.calc
    def matrix_calc():
        if input.use_cor_mats() == True:
            mats = ycf_cor_mats
        else:
            mats = global_mats
        loaded_elements = global_elements
        mat1 = mats[input.element_1()]
        mat2 = mats[input.element_2()]
        operand = input.operand()
        if operand == "+":
            calc_mat = mat1 + mat2
        elif operand == "-":
            calc_mat = mat1 - mat2
        elif operand == "x":
            calc_mat = mat1 * mat2
        elif operand == "/":
            calc_mat = mat1 / mat2
        return calc_mat
    
    @reactive.calc
    def matrix_calc_add():
        global global_mats
        global global_elements
        if input.use_cor_mats() == True:
            mats = ycf_cor_mats
        else:
            mats = global_mats
        loaded_elements = global_elements
        mats = global_mats
        mat1 = mats[input.element_1()]
        mat2 = mats[input.element_2()]
        operand = input.operand()
        if operand == "+":
            calc_mat = mat1 + mat2
        elif operand == "-":
            calc_mat = mat1 - mat2
        elif operand == "x":
            calc_mat = mat1 * mat2
        elif operand == "/":
            calc_mat = mat1 / mat2
        calc_mat_name = f"{input.element_1()} {operand} {input.element_2()}"
        loaded_elements.append(calc_mat_name)
        global_elements = loaded_elements
        
        mats[calc_mat_name] = calc_mat
        global_mats = mats
        
        return mats, loaded_elements, calc_mat_name, calc_mat
    
    @reactive.calc
    def create_mineral_masked_mats():
        """
        Create a set of dictionaries where each dictionary contains the mats masked for a particular mineral.

        Args:
            mats (dict): The global mats dictionary containing all element matrices and the "mineral_names" matrix.

        Returns:
            dict: A dictionary where keys are mineral names and values are dictionaries of masked mats.
        """

        mats, _, color_nums, mineral_colors, color_mapping, mineral_colors_mapped = data_loader_3()
        # Ensure "mineral_names" exists in mats
        if "mineral_names" not in mats:
            raise KeyError("'mineral_names' matrix is not available in mats.")

        # Get the unique mineral names
        mineral_names = np.unique(mats["mineral_names"])

        # Initialize the dictionary to store masked mats for each mineral
        mineral_masked_mats = {}

        # Iterate over each mineral name
        for mineral in mineral_names:
            # Create a mask for the current mineral
            mask = mats["mineral_names"] == mineral

            # Create a dictionary for the current mineral
            mineral_mats = {}

            # Apply the mask to each element in mats (excluding "mineral_names" and other non-numeric keys)
            for key, array in mats.items():
                if key not in ["mineral_names", "kmeans", "comp_cats"] and np.issubdtype(array.dtype, np.number):
                    # Mask the array
                    masked_array = np.where(mask, array, np.nan)
                    mineral_mats[key] = masked_array

            # Add the masked mats for the current mineral to the main dictionary
            mineral_masked_mats[mineral] = mineral_mats

        return mineral_masked_mats
    

    @reactive.calc
    def data_loader_3():
        if input.class_type() == "KMeans Classification":
            mats = global_mats
            loaded_elements = global_elements  # List to store successfully loaded elements
            elements = input.kmeans_elems()

            # Filter the selected elements for KMeans clustering
            mats_ = {elem: mats[elem] for elem in input.kmeans_elems()}
            reference_shape = list(mats_.values())[0].shape
            stacked_maps = {k: v for k, v in mats_.items() if v.shape == reference_shape}
            element_stack = np.stack(list(stacked_maps.values()), axis=-1)

            # Prepare data for clustering
            rows, cols, bands = element_stack.shape
            X = element_stack.reshape((rows * cols, bands))
            imputer = SimpleImputer(strategy="constant", fill_value=0)
            X_imputed = imputer.fit_transform(X)

            # Perform KMeans clustering
            n_clusters = input.n_clusters()
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            labels = kmeans.fit_predict(X_imputed)
            label_map = labels.reshape((rows, cols))
            mats["kmeans"] = label_map
            loaded_elements.append("kmeans")

            mineral_names_list = [name.strip() for name in input.min_names().split(",")]
            if len(mineral_names_list) == n_clusters:
                # Match mineral names to mineral categories
                mineral_categories = {i: mineral_names_list[i] for i in range(n_clusters)}
            else:
                # Dynamically create mineral categories
                mineral_categories = {i: f"Mineral {i+1}" for i in range(n_clusters)}   

            # Convert the numeric matrix to categorical labels
            mineral_names = np.vectorize(mineral_categories.get)(label_map)
            mats["mineral_names"] = mineral_names
            loaded_elements.append("mineral_names")
            print(mineral_names)

            stacked_mats = np.stack([mats[key] for key in elements], axis=0)       
            mat_total = np.nansum(stacked_mats, axis=0)
            mats["mat_total"] = mat_total
            loaded_elements.append("mat_total")
            mats_norm={}
            for element in elements:
                mats_norm[element] = (mats[element]/mat_total)*100

            silicates_df = get_std_mineral_df()

            if silicates_df.empty:
                colors_list = ["C0", "indianred", "goldenrod", "darkseagreen", "plum", "palegreen", "blue", "orange", "purple", "red", "green", "yellow", "pink"]
                mineral_colors_mapped = {i: colors_list[i % len(colors_list)] for i in range(n_clusters)}
                color_mapping = {mineral_categories[i]: mineral_colors_mapped[i] for i in range(n_clusters)}

                # Map mineral names to colors
                mineral_colors = np.vectorize(color_mapping.get)(mineral_names)

                return mats, loaded_elements, np.unique(label_map), mineral_colors, color_mapping, mineral_colors_mapped
        
            
            else:
                rows, cols = mats["mineral_names"].shape
                percent_match = np.full((rows, cols), np.nan)

                for i in range(rows):
                    for j in range(cols):
                        mineral = mats["mineral_names"][i, j]
                        # Get reference row for this mineral
                        if silicates_df.empty:
                            raise ValueError("You have not uploaded a mineral library")
                        ref_row = silicates_df[silicates_df["mineral name"] == mineral]
                        if ref_row.empty:
                            continue  # No reference for this mineral
                        # Get pixel composition for selected elements
                        pixel_vals = np.array([mats[el][i, j] for el in elements])
                        # Get reference composition for selected elements
                        ref_vals = np.array([ref_row[el].values[0] for el in elements])
                        # Normalize both to sum to 100 (avoid division by zero)
                        if np.nansum(pixel_vals) == 0 or np.nansum(ref_vals) == 0:
                            continue
                        pixel_norm = (pixel_vals / np.nansum(pixel_vals)) * 100
                        ref_norm = (ref_vals / np.nansum(ref_vals)) * 100
                        # Calculate percent match
                        diff = np.abs(pixel_norm - ref_norm)
                        percent_match[i, j] = (1 - (np.nansum(diff) / 200)) * 100
                
                mats["max_percent_match"] = percent_match

                # Dynamically create color mappings
                colors_list = ["C0", "indianred", "goldenrod", "darkseagreen", "plum", "palegreen", "blue", "orange", "purple", "red", "green", "yellow", "pink"]
                mineral_colors_mapped = {i: colors_list[i % len(colors_list)] for i in range(n_clusters)}
                color_mapping = {mineral_categories[i]: mineral_colors_mapped[i] for i in range(n_clusters)}

                # Map mineral names to colors
                mineral_colors = np.vectorize(color_mapping.get)(mineral_names)

                return mats, loaded_elements, np.unique(label_map), mineral_colors, color_mapping, mineral_colors_mapped
        
        elif input.class_type() == "Compositional Classification":
            mats = global_mats
            loaded_elements = global_elements

            # Initialize variables
            elems = []
            min_concs = []
            min_names = []

            if input.n_mins_comp() == 1:
                elems = [input.comp_elem_1()]
                min_concs = [input.min_conc_1()]
                max_concs = [input.max_conc_1()]
                min_names = [input.comp_mineral_1()]
            elif input.n_mins_comp() == 2:
                elems = [input.comp_elem_1(), input.comp_elem_2()]
                min_concs = [input.min_conc_1(), input.min_conc_2()]
                max_concs = [input.max_conc_1(), input.max_conc_2()]
                min_names = [input.comp_mineral_1(), input.comp_mineral_2()]
            elif input.n_mins_comp() == 3:
                elems = [input.comp_elem_1(), input.comp_elem_2(), input.comp_elem_3()]
                min_concs = [input.min_conc_1(), input.min_conc_2(), input.min_conc_3()]
                max_concs = [input.max_conc_1(), input.max_conc_2(), input.max_conc_3()]
                min_names = [input.comp_mineral_1(), input.comp_mineral_2(), input.comp_mineral_3()]
            else:
                raise ValueError("Invalid number of minerals selected for compositional classification.")
            
            reference_shape = list(mats.values())[0].shape
            mats["comp_cats"] = np.ones(reference_shape) * len(min_names)

            for i in range(len(elems)):
                mats["comp_cats"] = np.where((mats[elems[i]] > min_concs[i]) & (mats[elems[i]] < max_concs[i]), i, mats["comp_cats"])
            
            # Convert the numeric matrix to categorical labels
            # mineral_categories = {i: f"Mineral {i+1}" for i in range(n_clusters)}
            # mineral_names = np.vectorize(lambda x: min_names[int(x)] if x < len(min_names) else "Unclassified")(mats["comp_cats"])
            mineral_categories = {i: min_names[i] for i in range(len(min_names))}
            mineral_categories[len(min_names)] = "Unclassified"  # Default category for unclassified pixels

            mineral_names = np.vectorize(mineral_categories.get)(mats["comp_cats"])
            mats["mineral_names"] = mineral_names
            loaded_elements.append("mineral_names")
            
            # Dynamically create color mappings
            colors_list = ["C0", "indianred", "goldenrod", "darkseagreen", "plum", "palegreen", "blue", "orange", "purple", "red", "green", "yellow", "pink"]
            mineral_colors_mapped = {i: colors_list[i % len(colors_list)] for i in range(len(min_names))}
            color_mapping = {min_names[i]: mineral_colors_mapped[i] for i in range(len(min_names))}
            # Assign the last used color in colors_list to "Unclassified"
            mineral_colors_mapped[len(min_names)] = colors_list[(len(min_names)) % len(colors_list)]
            color_mapping["Unclassified"] = mineral_colors_mapped[len(min_names)]

            # Map mineral names to colors
            mineral_colors = np.vectorize(color_mapping.get)(mats["mineral_names"])

            return mats, loaded_elements, np.unique(mats["comp_cats"]), mineral_colors, color_mapping, mineral_colors_mapped
        
        elif input.class_type() == "Library Matching":
            mats = global_mats
            loaded_elements = global_elements
            elements = input.elements_ID()
            if input.weights() == "":
                weights = {elem: 1 for elem in elements}
            else:
                weights = {elem: input.weights()[i] for i, elem in enumerate(elements)}

            min_thresh = input.ID_min_thresh()
            max_thresh = input.ID_max_thresh()
            stacked_mats = np.stack([mats[key] for key in elements], axis=0)       
            mat_total = np.nansum(stacked_mats, axis=0)
            mats["mat_total"] = mat_total
            loaded_elements.append("mat_total")
            mats_norm={}
            for element in elements:
                mats_norm[element] = (mats[element]/mat_total)*weights[element]*100

            silicates_df = get_std_mineral_df()

            if silicates_df.empty:
                raise ValueError("Please import a mineral library.")
            else:

                standard_values = {}
                standard_elements = {}
                mats_norm_mineral = {}
                norm_diffs = {}
                percent_match={}
                for mineral in input.minerals_ID():
                    mats_norm_mineral[mineral] = {}
                    # mats_test_means[mineral] = {}
                    mineral_df = silicates_df.loc[silicates_df["mineral name"] == mineral]
                    # print(mineral_df)
                    mineral_df = mineral_df.reset_index(drop=True)
                    standard_values[mineral] = {}
                    standard_elements[mineral] = []
                    for elem in elements:
                        if mineral_df[elem][0] == np.nan:
                            print(f"{elem} not in {mineral}")
                            continue
                            # mats_test[mineral][elem] = np.full(mats[elem].shape, np.nan)
                            # mats_test_means[mineral][elem] = np.nanmean(mats_test[mineral][elem])
                        else:
                            standard_values[mineral][elem] = mineral_df[elem][0]
                            standard_elements[mineral].append(elem)
                            mats_norm_mineral[mineral][elem] = mats_norm[elem]
                    stacked_standard_array = np.stack([pd.to_numeric(standard_values[mineral][key], errors='coerce') for key in standard_elements[mineral]], axis=0)
                    standard_values[mineral]["total"] = np.nansum(stacked_standard_array, axis=0)
                    norm_diffs[mineral] = {}
                    for e in standard_elements[mineral]:
                        std_value_norm = (standard_values[mineral][e]/standard_values[mineral]["total"])*100
                        norm_diffs[mineral][e] = np.abs(mats_norm_mineral[mineral][e] - std_value_norm)
            
                        # print(f"{e}:{std_value_norm}")
                    norm_diffs_stacked = np.stack([norm_diffs[mineral][el] for el in standard_elements[mineral]], axis=0)
                    norm_diffs_total = np.nansum(norm_diffs_stacked, axis=0)
                    percent_match[mineral] = (1-(norm_diffs_total/200))*100
                    
                    percent_match[mineral][percent_match[mineral] < min_thresh] = np.nan
                    percent_match[mineral][percent_match[mineral] > max_thresh] = np.nan

                stacked_percent_matches = np.stack([percent_match[mineral] for mineral in input.minerals_ID()], axis=0)
                max_percent_match = np.nanmax(stacked_percent_matches, axis=0)
                mats["max_percent_match"] = max_percent_match
                # Identify slices where all values are NaN
                all_nan_mask = np.isnan(stacked_percent_matches).all(axis=0)

                # Use nanargmax for slices with valid values
                max_indices = np.full(stacked_percent_matches.shape[1:], -1, dtype=int)  # Default to -1 for all-NaN slices
                valid_indices = ~all_nan_mask
                max_indices[valid_indices] = np.nanargmax(stacked_percent_matches[:, valid_indices], axis=0)

                # Handle all-NaN slices (optional: assign a specific value or leave as -1)
                # For example, assign a specific index for "Unclassified":
                unclassified_index = len(input.minerals_ID())  # Assuming this is the index for "Unclassified"
                max_indices[all_nan_mask] = unclassified_index
                mats["max_indices"] = max_indices
                loaded_elements.append("max_indices")
                # print(max_indices)

                unique_mins = np.unique(max_indices)
                minerals_selected = list(input.minerals_ID()) + ["Unclassified"]
                mineral_list = [minerals_selected[i] for i in unique_mins]
                mineral_categories = {mineral: i for i, mineral in zip(unique_mins, mineral_list)}
                # print(mineral_categories)
                # mineral_categories["Unclassified"] = len(input.minerals_ID())
                # mineral_list = list(input.minerals_ID()) + ["Unclassified"]
                # mineral_names = np.vectorize(mineral_categories.get)(mats["max_indices"])
                mineral_names = np.vectorize(lambda idx: minerals_selected[idx])(max_indices) # Used to be called max_keys
                mats["mineral_names"] = mineral_names
                loaded_elements.append("mineral_names")
                numeric_max_key = np.vectorize(mineral_categories.get)(mineral_names)
                mats["numeric_max_key"] = numeric_max_key
                loaded_elements.append("numeric_max_key")
                # print(mineral_names)

                # unique_num_keys = np.unique(numeric_max_key)
                unique_num_keys = unique_mins
                # unique_min_cats = {mineral_list[key]: i for i,key in enumerate(unique_num_keys)}
                # print(unique_min_cats)
                # unique_min_list = list(unique_min_cats.keys())
                colors_list = ["C0", "indianred", "darkseagreen", "goldenrod", "plum", "palegreen", "blue", "orange", "purple", "red", "green", "yellow", "pink"]
                mineral_colors_mapped = {num_key: colors_list[num_key % len(colors_list)] for num_key in unique_num_keys}
                color_mapping = {minerals_selected[num_key]: colors_list[num_key % len(colors_list)] for num_key in unique_num_keys}

                # mineral_colors_mapped = {i: colors_list[i] for i in range(len(mineral_list))}
                # color_mapping = {mineral_list[num_key]: mineral_colors_mapped[num_key] for num_key in unique_num_keys}
                # print(mineral_colors_mapped)
                # print(color_mapping)
                # cmap = colors.ListedColormap([mineral_colors_mapped[key] for key in sorted(mineral_colors_mapped.keys()) if key in mineral_colors_mapped.keys()])

                # colors_list = ["C0", "indianred", "darkseagreen", "goldenrod", "plum", "palegreen", "blue", "orange", "purple", "red", "green", "yellow", "pink"]
                # mineral_colors_mapped = {i: colors_list[i % len(colors_list)] for i in range(len(mineral_names))}

                # if mineral_names.ndim > 1:
                #     mineral_names = mineral_names.flatten()
                # while len(mineral_colors_mapped) < len(mineral_names):
                    
                # mineral_colors_mapped[len(mineral_colors_mapped)] = colors_list[len(mineral_colors_mapped) % len(colors_list)]

                # # Create the color_mapping dictionary
                # color_mapping = {str(mineral_names[i]): mineral_colors_mapped[i] for i in range(len(mineral_names))}
                # # color_mapping = {str(mineral_names[i]): mineral_colors_mapped[i] for i in range(len(mineral_names))}

                mineral_colors = np.vectorize(color_mapping.get)(mineral_names)

                return mats, loaded_elements, np.unique(max_indices), mineral_colors, color_mapping, mineral_colors_mapped



    # @reactive.calc
    # # @reactive.event(input.ID_mins)
    # def ID_mins():
    #     mats = global_mats
    #     elements = input.elements_ID()
    #     if input.weights() == "":
    #         weights = {elem: 1 for elem in elements}
    #     else:
    #         weights = {elem: input.weights()[i] for i, elem in enumerate(elements)}

    #     min_thresh = input.ID_min_thresh()
    #     max_thresh = input.ID_max_thresh()
    #     stacked_mats = np.stack([mats[key] for key in elements], axis=0)       
    #     mat_total = np.nansum(stacked_mats, axis=0)
    #     mats_norm={}
    #     for element in elements:
    #         mats_norm[element] = (mats[element]/mat_total)*weights[element]*100

    #     silicates_df = get_std_mineral_df()
        
    #     standard_values = {}
    #     standard_elements = {}
    #     mats_norm_mineral = {}
    #     norm_diffs = {}
    #     percent_match={}
    #     for mineral in input.minerals_ID():
    #         mats_norm_mineral[mineral] = {}
    #         # mats_test_means[mineral] = {}
    #         mineral_df = silicates_df.loc[silicates_df["mineral name"] == mineral]
    #         # print(mineral_df)
    #         mineral_df = mineral_df.reset_index(drop=True)
    #         standard_values[mineral] = {}
    #         standard_elements[mineral] = []
    #         for elem in elements:
    #             if mineral_df[elem][0] == np.nan:
    #                 print(f"{elem} not in {mineral}")
    #                 continue
    #                 # mats_test[mineral][elem] = np.full(mats[elem].shape, np.nan)
    #                 # mats_test_means[mineral][elem] = np.nanmean(mats_test[mineral][elem])
    #             else:
    #                 standard_values[mineral][elem] = mineral_df[elem][0]
    #                 standard_elements[mineral].append(elem)
    #                 mats_norm_mineral[mineral][elem] = mats_norm[elem]
    #         stacked_standard_array = np.stack([pd.to_numeric(standard_values[mineral][key], errors='coerce') for key in standard_elements[mineral]], axis=0)
    #         standard_values[mineral]["total"] = np.nansum(stacked_standard_array, axis=0)
    #         norm_diffs[mineral] = {}
    #         for e in standard_elements[mineral]:
    #             std_value_norm = (standard_values[mineral][e]/standard_values[mineral]["total"])*100
    #             norm_diffs[mineral][e] = np.abs(mats_norm_mineral[mineral][e] - std_value_norm)
       
    #             # print(f"{e}:{std_value_norm}")
    #         norm_diffs_stacked = np.stack([norm_diffs[mineral][el] for el in standard_elements[mineral]], axis=0)
    #         norm_diffs_total = np.nansum(norm_diffs_stacked, axis=0)
    #         percent_match[mineral] = (1-(norm_diffs_total/200))*100
            
    #         percent_match[mineral][percent_match[mineral] < min_thresh] = np.nan
    #         percent_match[mineral][percent_match[mineral] > max_thresh] = np.nan
    #     # print(f"biotite: {percent_match["biotite"]}")
    #     # print(f"Calcite: {percent_match["Calcite"]}")

    #     stacked_percent_matches = np.stack([percent_match[mineral] for mineral in input.minerals_ID()], axis=0)
    #     max_percent_match = np.nanmax(stacked_percent_matches, axis=0)
    #     mats["max_percent_match"] = max_percent_match
    #     # Identify slices where all values are NaN
    #     all_nan_mask = np.isnan(stacked_percent_matches).all(axis=0)

    #     # Use nanargmax for slices with valid values
    #     max_indices = np.full(stacked_percent_matches.shape[1:], -1, dtype=int)  # Default to -1 for all-NaN slices
    #     valid_indices = ~all_nan_mask
    #     max_indices[valid_indices] = np.nanargmax(stacked_percent_matches[:, valid_indices], axis=0)

    #     # Handle all-NaN slices (optional: assign a specific value or leave as -1)
    #     # For example, assign a specific index for "Unclassified":
    #     unclassified_index = len(input.minerals_ID())  # Assuming this is the index for "Unclassified"
    #     max_indices[all_nan_mask] = unclassified_index
        

    #     mineral_names = list(input.minerals_ID()) + ["Unclassified"]
    #     max_keys = np.vectorize(lambda idx: mineral_names[idx])(max_indices)
    #     mineral_mapping = {mineral: i+1 for i, mineral in enumerate(list(input.minerals_ID()))}
    #     mineral_mapping["Unclassified"] = len(input.minerals_ID())+1
    #     numeric_max_key = np.vectorize(mineral_mapping.get)(max_keys)
    #     print(max_keys)
    #     # if "Unclassified" not in standard_values:
    #     #     standard_values["Unclassified"] = {}

    #     # standard_values["Unclassified"]["total"] = mat_total

    #     std_totals_max = np.zeros_like(max_keys, dtype=float)

    #     for i, mineral in enumerate(list(input.minerals_ID())):
    #         mineral_total = standard_values[mineral]["total"]
    #         # if np.isscalar(mineral_total):
    #         mineral_total_mat = np.full_like(max_keys, mineral_total, dtype=float)  # Broadcast scalar to array
    #         std_totals_max[max_keys == mineral] = mineral_total_mat[max_keys == mineral]
    #     unclassified_mask = (max_keys == "Unclassified")
    #     std_totals_max[unclassified_mask] = mat_total[unclassified_mask]/10000
            
    #     yield_cor_fact = (mat_total/10000)/std_totals_max
    #     print(yield_cor_fact)

    #     return numeric_max_key, mineral_names, yield_cor_fact, max_percent_match
    
    @reactive.calc
    # @reactive.event(input.update_min_list)
    def get_std_mineral_df():
        file = input.min_database()        
        if file is None:
            return pd.DataFrame()
        else:
            file_path = file[0]["datapath"]
            df = pd.read_excel(file_path)
        # df = pd.read_excel("C:/Users/joalmann/OneDrive - University of Tasmania/Documents/Sebs mineral classification/silicates.xlsx")
        return df
    
    @reactive.effect
    def update_roi_selected():
        _, roi_list = make_roi_dict()
        ui.update_select("roi_selected", choices=roi_list, selected="ROI0")
        ui.update_select("roi_selected_decon", choices=roi_list, selected="ROI0")
        ui.update_select("roi_selected_Pb", choices=roi_list, selected="ROI0")

    @reactive.effect
    def update_line_selected():
        _, line_list = make_lines_dict()
        ui.update_select("line_selected", choices=line_list, selected="Line1")
        ui.update_select("line_selected_decon", choices=line_list, selected="Line1")

    @reactive.effect
    def update_minerals_ID():
        df = get_std_mineral_df()
        if "mineral name" in df.columns:
            mineral_choices = df["mineral name"].dropna().unique().tolist()  # Ensure no NaN values
            print("Updating minerals_ID with:", mineral_choices)  # Debugging
            ui.update_select("minerals_ID", choices=mineral_choices)
        else:
            print("Error: 'mineral name' column not found in the DataFrame.")
        
    
    @reactive.effect
    def update_element_choices():
        _, loaded_elements = data_loader()  # Get the loaded elements
        ui.update_select("elem_4_entropy", choices=loaded_elements)
        ui.update_select("element", choices=loaded_elements)
        ui.update_select("overlay_map", choices=loaded_elements)
        ui.update_select("element_plotly", choices=loaded_elements)
        ui.update_select("element_red", choices=loaded_elements)
        ui.update_select("element_green", choices=loaded_elements)
        ui.update_select("element_blue", choices=loaded_elements)
        ui.update_select("elements", choices=loaded_elements)
        ui.update_select("elems_graph", choices=loaded_elements)
        ui.update_select("class_elem_1", choices=loaded_elements)
        ui.update_select("class_elem_2", choices=loaded_elements)
        ui.update_select("class_elem_3", choices=loaded_elements)
        ui.update_select("element_1", choices=loaded_elements)
        ui.update_select("element_2", choices=loaded_elements)
        ui.update_select("element_roi", choices=loaded_elements)
        ui.update_select("element_line", choices=loaded_elements)
        ui.update_select("element_graph", choices=loaded_elements)
        ui.update_select("element_xaxis", choices=loaded_elements)
        ui.update_select("element_yaxis", choices=loaded_elements)
        ui.update_select("kmeans_elems", choices=loaded_elements)
        ui.update_select("comp_elem_1", choices=loaded_elements)
        ui.update_select("comp_elem_2", choices=loaded_elements)
        ui.update_select("comp_elem_3", choices=loaded_elements)
        ui.update_select("elements_ID", choices=loaded_elements)
        ui.update_select("element_hist", choices=loaded_elements)
        ui.update_select("c_map_bivariate", choices=loaded_elements)
        ui.update_select("corr_mat_els", choices=loaded_elements)
        ui.update_select("decon_xaxis", choices=loaded_elements)
        ui.update_select("decon_yaxis", choices=loaded_elements)
        ui.update_select("pca_elements", choices=loaded_elements)
        ui.update_select("c_map_pca", choices=loaded_elements)


    @reactive.effect
    @reactive.event(input.calc_entropy_map)
    def update_element_choices():
        _, loaded_elements2 = calc_entropy()  # Get the loaded elements
        # ui.update_select("elem_4_entropy", choices=loaded_elements2)
        ui.update_select("element", choices=loaded_elements2)
        ui.update_select("element_plotly", choices=loaded_elements2)
        ui.update_select("overlay_map", choices=loaded_elements2)
        ui.update_select("element_red", choices=loaded_elements2)
        ui.update_select("element_green", choices=loaded_elements2)
        ui.update_select("element_blue", choices=loaded_elements2)
        ui.update_select("elements", choices=loaded_elements2)
        # ui.update_select("elems_graph", choices=loaded_elements2)
        ui.update_select("class_elem_1", choices=loaded_elements2)
        ui.update_select("class_elem_2", choices=loaded_elements2)
        ui.update_select("class_elem_3", choices=loaded_elements2)
        ui.update_select("element_1", choices=loaded_elements2)
        ui.update_select("element_2", choices=loaded_elements2)
        ui.update_select("element_roi", choices=loaded_elements2)
        ui.update_select("element_line", choices=loaded_elements2)
        ui.update_select("element_graph", choices=loaded_elements2)
        ui.update_select("element_xaxis", choices=loaded_elements2)
        ui.update_select("element_yaxis", choices=loaded_elements2)
        ui.update_select("decon_xaxis", choices=loaded_elements2)
        ui.update_select("decon_yaxis", choices=loaded_elements2)
        ui.update_select("kmeans_elems", choices=loaded_elements2)
        ui.update_select("comp_elem_1", choices=loaded_elements2)
        ui.update_select("comp_elem_2", choices=loaded_elements2)
        ui.update_select("comp_elem_3", choices=loaded_elements2)
        ui.update_select("element_hist", choices=loaded_elements2)
        ui.update_select("c_map_bivariate", choices=loaded_elements2)
        # ui.update_select("corr_mat_els", choices=loaded_elements2)
        ui.update_select("pca_elements", choices=loaded_elements2)
        ui.update_select("c_map_pca", choices=loaded_elements2)
    
    @reactive.effect
    @reactive.event(input.classify_minerals)
    def update_mask_choices():
        if input.class_type() == "None":
            ui.notification_show("Please choose a classification type.", type="warning")
            return
        else:
            mineral_masked_mats = create_mineral_masked_mats()
            new_choices = ["All"] + list(mineral_masked_mats.keys())
            ui.update_select("masked_map", choices=new_choices, selected=["All"])
            ui.update_select("masked_map_red", choices=new_choices)
            ui.update_select("masked_map_green", choices=new_choices)
            ui.update_select("masked_map_blue", choices=new_choices)
            ui.update_select("masked_map_multi", choices=new_choices)
            # ui.update_select("masked_map_calc", choices=new_choices)
            ui.update_select("masked_map_roi", choices=new_choices)
            ui.update_select("masked_map_line", choices=new_choices)
            ui.update_select("mineral_hist", choices=new_choices, selected=["All"])
            ui.update_select("mineral_bivariate",choices=new_choices, selected=["All"])
            ui.update_select("mineral_pca",choices=new_choices, selected=["All"])
            ui.update_select("minerals_graph",choices=new_choices, selected=["All"])
            ui.update_select("minerals_corr_mat",choices=new_choices, selected=["All"])

    @reactive.effect
    @reactive.event(input.add_calc_mat)
    def update_elem_choices_calc():
        _, loaded_elements3, _, _ = matrix_calc_add()
        ui.update_select("element", choices=loaded_elements3)
        ui.update_select("overlay_map", choices=loaded_elements3)
        ui.update_select("element_plotly", choices=loaded_elements3)
        ui.update_select("elem_4_entropy", choices=loaded_elements3)
        ui.update_select("element_red", choices=loaded_elements3)
        ui.update_select("element_green", choices=loaded_elements3)
        ui.update_select("element_blue", choices=loaded_elements3)
        ui.update_select("elements", choices=loaded_elements3)
        # ui.update_select("elems_graph", choices=loaded_elements3)
        ui.update_select("class_elem_1", choices=loaded_elements3)
        ui.update_select("class_elem_2", choices=loaded_elements3)
        ui.update_select("class_elem_3", choices=loaded_elements3)
        ui.update_select("element_1", choices=loaded_elements3)
        ui.update_select("element_2", choices=loaded_elements3)
        ui.update_select("element_roi", choices=loaded_elements3)
        ui.update_select("element_line", choices=loaded_elements3)
        ui.update_select("element_graph", choices=loaded_elements3)
        ui.update_select("element_xaxis", choices=loaded_elements3)
        ui.update_select("element_yaxis", choices=loaded_elements3)
        ui.update_select("decon_xaxis", choices=loaded_elements3)
        ui.update_select("decon_yaxis", choices=loaded_elements3)
        ui.update_select("kmeans_elems", choices=loaded_elements3)
        ui.update_select("comp_elem_1", choices=loaded_elements3)
        ui.update_select("comp_elem_2", choices=loaded_elements3)
        ui.update_select("comp_elem_3", choices=loaded_elements3)
        ui.update_select("element_hist", choices=loaded_elements3)
        ui.update_select("c_map_bivariate", choices=loaded_elements3)
        # ui.update_select("corr_mat_els", choices=loaded_elements3)
        ui.update_select("pca_elements", choices=loaded_elements3)
        ui.update_select("c_map_pca", choices=loaded_elements3)



    
    
    @reactive.calc
    def calc_asp_ratio():
        if input.aspect_ratio() == "Input aspect ratio":
            asp_ratio = input.pixel_aspect()
        if input.aspect_ratio() == "Calculate aspect ratio":
            asp_ratio = input.sweep_time()/1000*input.scan_speed()/input.pixel_size()
        return asp_ratio
    
    
    
    
    @render.text()
    def done_text():
        _, loaded_elements = data_loader()
        asp_ratio = calc_asp_ratio()
        return "Aspect ratio = {}. Maps of the following isotopes have been loaded: {}".format(asp_ratio, list(loaded_elements))

    @render.download(filename = "data_cube.csv")
    def data_cube_export():
        output = io.BytesIO()
        mats, loaded_elements = data_loader()
        spot_size = input.pixel_size()
        scan_speed = input.scan_speed()
        sweep_time = input.sweep_time()
        samp_name = "Sample"
        elements = loaded_elements
       
        mat_shape = np.shape(mats[elements[0]])
        Ypts = np.array(range(mat_shape[0]))
        Xpts = np.array(range(mat_shape[1]))
        Ypts = Ypts[-1] - Ypts
        Ypts = Ypts * spot_size
        if input.aspect_ratio() == "Calculate aspect ratio":
            Xpts = Xpts * scan_speed * sweep_time/1000
        else:
            Xpts = Xpts * spot_size
        X2D,Y2D = np.meshgrid(Xpts,Ypts)
        coords = np.column_stack((Y2D.ravel(),X2D.ravel()))
        
        data_cube_df = pd.DataFrame()
        data_cube_df['x_coord'] = coords[:,1]
        data_cube_df['y_coord'] = coords[:,0]

        def leading_number(s):
            num = ''
            for c in s:
                if c.isdigit():
                    num += c
                else:
                    break
            return int(num)

        # elements_sorted = sorted(elements, key=leading_number)
        for elem in elements:
            data_cube_df[elem] = mats[elem].reshape(-1)

        data_cube_df.to_csv(output, index=False)
        output.seek(0)
        return output
    
    
    @render.plot
    @reactive.event(input.calc_entropy_map)
    def plot_entropy_map():
        mats_, loaded_elements_ = calc_entropy()
        if "entropy" not in mats_:
            raise KeyError("'entropy' matrix is not available. Ensure calc_entropy is executed before plotting.")

        asp_ratio = calc_asp_ratio()
        fig, ax = plt.subplots()
        im = ax.imshow(mats_["entropy"], cmap="parula", 
                    extent=[0, np.shape(mats_["entropy"])[1]*input.pixel_size()*asp_ratio, 0, np.shape(mats_["entropy"])[0]*input.pixel_size()], 
                    interpolation='none', alpha=1.0)
        plt.title("Entropy Map")
        plt.colorbar(im, label="Shannon Entropy (bits)")
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.tight_layout()

    
    @render.plot
    @reactive.event(input.disp_calc_mat)
    def calc_plot():
        mat_calc = matrix_calc()
        asp_ratio = calc_asp_ratio()
        pixel_size = input.pixel_size()
        vmin_ = np.nanpercentile(mat_calc, input.min_max_vals_calc()[0])
        vmax_ = np.nanpercentile(mat_calc, input.min_max_vals_calc()[1])
        ax = plt.axes()
        ax.set_facecolor("black")
        if input.use_log_calc() == True:
            plt.imshow(mat_calc, cmap=input.c_map_calc(), norm=colors.SymLogNorm(linthresh=0.001, vmin=vmin_, vmax=vmax_), extent=[0, np.shape(mat_calc)[1] * pixel_size * asp_ratio, 0, np.shape(mat_calc)[0] * pixel_size], interpolation='none')
        if input.use_log_calc() == False:
            plt.imshow(mat_calc, cmap=input.c_map_calc(), vmin=vmin_, vmax=vmax_, extent=[0, np.shape(mat_calc)[1] * pixel_size * asp_ratio, 0, np.shape(mat_calc)[0] * pixel_size], interpolation='none')
        plt.colorbar(pad=0.01)
        plt.grid(False)
        plt.xlabel("μm")
        plt.ylabel("μm")
        plt.title("{} {} {}".format(input.element_1(), input.operand(), input.element_2()))


    @render.text
    @reactive.event(input.add_calc_mat)
    def added_calc():
        mats, loaded_elements, calc_mat_name, calc_mat = matrix_calc_add()
        print(f"DEBUG: calc_mat_name = {calc_mat_name}")
        print(f"DEBUG: loaded_elements = {loaded_elements}")
        return f"{calc_mat_name} has been added to the list of maps and can be used in other processes."

    


    # @render.text    
    # @reactive.event(input.save_calc_mat)
    # def save_figure_calc():
    #     mat_calc = matrix_calc()
    #     asp_ratio = calc_asp_ratio()
    #     pixel_size = input.pixel_size()
    #     vmin_ = np.nanpercentile(mat_calc, input.min_max_vals_calc()[0])
    #     vmax_ = np.nanpercentile(mat_calc, input.min_max_vals_calc()[1])
    #     ax = plt.axes()
    #     ax.set_facecolor("black")
    #     if input.use_log_calc() == True:
    #         plt.imshow(mat_calc, cmap=input.c_map_calc(), norm=colors.SymLogNorm(linthresh=0.001, vmin=vmin_, vmax=vmax_), extent=[0, np.shape(mat_calc)[1] * pixel_size * asp_ratio, 0, np.shape(mat_calc)[0] * pixel_size], interpolation='none')
    #     if input.use_log_calc() == False:
    #         plt.imshow(mat_calc, cmap=input.c_map_calc(), vmin=vmin_, vmax=vmax_, extent=[0, np.shape(mat_calc)[1] * pixel_size * asp_ratio, 0, np.shape(mat_calc)[0] * pixel_size], interpolation='none')
    #     plt.colorbar(pad=0.01)
    #     plt.grid(False)
    #     plt.xlabel("μm")
    #     plt.ylabel("μm")
    #     plt.title("{} {} {}".format(input.element_1(), input.operand(), input.element_2()))
    #     operand = input.operand()
    #     if operand == "+":
    #         plt.savefig("{}/{}_plus_{}.png".format(global_data_path, input.element_1(), input.element_2()), dpi=300)
    #     elif operand == "-":
    #         plt.savefig("{}/{}_minus_{}.png".format(global_data_path, input.element_1(), input.element_2()), dpi=300)
    #     elif operand == "x":
    #         plt.savefig("{}/{}_times_{}.png".format(global_data_path, input.element_1(), input.element_2()), dpi=300)
    #     elif operand == "/":
    #        plt.savefig("{}/{}_divided_by_{}.png".format(global_data_path, input.element_1(), input.element_2()), dpi=300)
    #     return "Your {} {} {} image has been saved.".format(input.element_1(), input.operand(), input.element_2())



    

    @render.plot
    @reactive.event(input.classify_minerals)    
    def plot_mineral_class():
        global global_masked_mats
        asp_ratio = calc_asp_ratio()

        if input.class_type() == "None":
            raise ValueError("Please choose a classification type.")
        
        if input.class_type() == "KMeans Classification":
            if input.kmeans_elems() == []:
                raise ValueError("No elements selected for KMeans classification.")
            mats_, loaded_elements, color_nums, mineral_colors, color_mapping, mineral_colors_mapped = data_loader_3()
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = mats_

            cmap = colors.ListedColormap([mineral_colors_mapped[key] for key in sorted(mineral_colors_mapped.keys()) if key in mineral_colors_mapped.keys()])
            fig, ax = plt.subplots()
            ax.imshow(mats["kmeans"], cmap=cmap, 
                      extent=[0, np.shape(mats["kmeans"])[1]*input.pixel_size()*asp_ratio, 0, np.shape(mats["kmeans"])[0]*input.pixel_size()], 
                      interpolation='none', alpha=1.0)
            # plt.title("KMeans Cluster Map of Elemental Composition", fontsize=14)
            # plt.colorbar(label="Cluster Label")
            plt.xticks([])
            plt.yticks([])
            plt.title("KMeans Classification")
            plt.grid(False)
            plt.tight_layout()

            legend_elements = [
                Patch(facecolor=color, edgecolor='none', label=label)
                for label, color in color_mapping.items()
            ]
            ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=8, frameon=True)

            mineral_masked_mats = create_mineral_masked_mats()
            global_masked_mats = mineral_masked_mats


        if input.class_type() == "Compositional Classification":
            mats_, loaded_elements, color_nums, mineral_colors, color_mapping, mineral_colors_mapped = data_loader_3()
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = mats_

            cmap = colors.ListedColormap([mineral_colors_mapped[key] for key in sorted(mineral_colors_mapped.keys()) if key in mineral_colors_mapped.keys()])
            fig, ax = plt.subplots()
            ax.imshow(mats["comp_cats"], cmap=cmap, 
                      extent=[0, np.shape(mats["comp_cats"])[1]*input.pixel_size()*asp_ratio, 0, np.shape(mats["comp_cats"])[0]*input.pixel_size()], 
                      interpolation='none', alpha=1.0)
            # plt.title("KMeans Cluster Map of Elemental Composition", fontsize=14)
            # plt.colorbar(label="Cluster Label")
            plt.xticks([])
            plt.yticks([])
            plt.title("Compositional Classification")
            plt.grid(False)
            plt.tight_layout()

            legend_elements = [
                Patch(facecolor=color, edgecolor='none', label=label)
                for label, color in color_mapping.items()
            ]

            ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=8, frameon=True)

            mineral_masked_mats = create_mineral_masked_mats()
            global_masked_mats = mineral_masked_mats
        
        if input.class_type() == "Library Matching":

            mats_, loaded_elements, color_nums, mineral_colors, color_mapping, mineral_colors_mapped = data_loader_3()
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = mats_

            unique_vals, inverse = np.unique(mats["max_indices"], return_inverse=True)
            plot_mat = inverse.reshape(mats["max_indices"].shape) + 1

            # print("Unique max indices: ", np.unique(plot_mat))
            # cmap = colors.ListedColormap([mineral_colors_mapped[key] for key in sorted(mineral_colors_mapped.keys()) if key in mineral_colors_mapped.keys()])
            # colors_list = ["C0", "indianred", "darkseagreen", "goldenrod", "plum", "palegreen", "blue", "orange", "purple", "red", "green", "yellow", "pink"]
            cmap = colors.ListedColormap([mineral_colors_mapped[key] for key in sorted(mineral_colors_mapped.keys()) if key in mineral_colors_mapped.keys()])
            # print("mineral_colors_mapped:", mineral_colors_mapped)
            # print("numeric_max_key unique values:", np.unique(mats["numeric_max_key"]))
            fig, ax = plt.subplots()
            ax.imshow(plot_mat, cmap=cmap,
                      extent=[0, np.shape(plot_mat)[1]*input.pixel_size()*asp_ratio, 0, np.shape(plot_mat)[0]*input.pixel_size()], 
                      interpolation='none', alpha=1.0)
            plt.xticks([])
            plt.yticks([])
            plt.title("Mineral Library Matching")
            plt.grid(False)
            plt.tight_layout()
            # print("name_max_key unique values:", np.unique(mats["mineral_names"]))
            # print("color mapping:", color_mapping)
            legend_elements = [
                    Patch(facecolor=color, edgecolor='none', label=label)
                    for label, color in color_mapping.items() if label in color_mapping.keys()
                ]
            ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.01, 1), fontsize=8, frameon=True)

            mineral_masked_mats = create_mineral_masked_mats()
            global_masked_mats = mineral_masked_mats

    @render.table
    @reactive.event(input.classify_minerals)
    def mineral_class_table():
        if input.class_type() == "None":
            raise ValueError("Please choose a classification type.")
        # Load data
        if input.class_type() == "KMeans Classification":
            mats_, _, _, _, _, _ = data_loader_3()
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = mats_
            cluster_labels = mats["kmeans"]
            mineral_names = mats["mineral_names"]
        elif input.class_type() == "Compositional Classification":
            # raise ValueError("No elements selected for Compositional classification.")
            mats_, _, _, _, _, _ = data_loader_3()
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = mats_
            cluster_labels = mats["comp_cats"]
            mineral_names = mats["mineral_names"]
        elif input.class_type() == "Library Matching":
            mats_, _, _, _, _, _ = data_loader_3()
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = mats_
            cluster_labels = mats["numeric_max_key"]
            mineral_names = mats["mineral_names"]


        # Get unique clusters
        unique_clusters = np.unique(cluster_labels)

        # Initialize a dictionary to store results
        cluster_averages = {"Cluster": [], "Mineral Name": []}

        # Add columns for each element
        for element in mats.keys():
            if element not in ["kmeans", "comp_cats", "mineral", "mineral_names", "numeric_max_key", "mat_total", "max_indices", "max_percent_match"]:  # Exclude non-element matrices
                cluster_averages[element] = []

        # Calculate mean values for each cluster
        for cluster in unique_clusters:
            cluster_averages["Cluster"].append(cluster)
            mask = cluster_labels == cluster  # Mask for the current cluster

            # Get the most common mineral name for the cluster
            mineral_name = pd.Series(mineral_names[mask].flatten()).mode().iloc[0]
            cluster_averages["Mineral Name"].append(mineral_name)

            for element in mats.keys():
                if element not in ["kmeans", "comp_cats", "mineral", "mineral_names", "numeric_max_key", "mat_total", "max_indices", "max_percent_match"]:
                    cluster_mean = np.nanmean(mats[element][mask])
                    cluster_averages[element].append(cluster_mean)
        if input.class_type() == "Compositional Classification":
            cluster_averages["Mineral Name"][-1] = "Unclassified"
        # Convert to a pandas DataFrame
        df = pd.DataFrame(cluster_averages)
        global global_cluster_means_df
        global_cluster_means_df = df

        # Save the table to an Excel file (optional)
        # df.to_excel(f"{global_data_path}/cluster_averages.xlsx", index=False)

        return df
    
    @render.download(filename = "cluster_means.xlsx")
    def download_min_means():
        output = io.BytesIO()
        global_cluster_means_df.to_excel(output, index=False)
        output.seek(0)
        return output
        

    
    @render.plot
    # @reactive.event(input.ID_mins)
    def yield_cor_plot():
        asp_ratio = calc_asp_ratio()
        # if input.class_type() == "Library Matching":
        mats, loaded_elements, color_nums, mineral_colors, color_mapping, mineral_colors_mapped = data_loader_3()
        # if input.use_cor_mats() == True:
        #     mats = ycf_cor_mats
        # else:
        #     mats = mats_
        # cmap = colors.ListedColormap([mineral_colors_mapped[key] for key in sorted(mineral_colors_mapped.keys()) if key in mineral_colors_mapped.keys()])
        cmap = colors.ListedColormap([mineral_colors_mapped[key] for key in sorted(mineral_colors_mapped.keys()) if key in mineral_colors_mapped.keys()])
        fig, ax = plt.subplots()
        if input.class_type() == "Library Matching":
            ax.imshow(mats["numeric_max_key"], cmap=cmap,
                      extent=[0, np.shape(mats["numeric_max_key"])[1]*asp_ratio, 0, np.shape(mats["numeric_max_key"])[0]],
                      interpolation='none', alpha=1.0)
            if input.row_number() <= np.shape(mats["numeric_max_key"])[0]:
                hline_pos = input.row_number()
            else:
                hline_pos = input.row_number() - np.shape(mats["numeric_max_key"])[0]
            # ax.set_xticks(np.arange(0, np.shape(mats["numeric_max_key"])[1], 1))
        if input.class_type() == "KMeans Classification":
            ax.imshow(mats["kmeans"], cmap=cmap,
                      extent=[0, np.shape(mats["kmeans"])[1]*asp_ratio, 0, np.shape(mats["kmeans"])[0]],
                      interpolation='none', alpha=1.0)
            if input.row_number() <= np.shape(mats["kmeans"])[0]:
                hline_pos = input.row_number()
            else:
                hline_pos = input.row_number() - np.shape(mats["kmeans"])[0]
            # ax.set_xticks(np.arange(0, np.shape(mats["kemans"])[1], 1))
        # plt.xticks([])
        # plt.yticks([])
        plt.title("Mineral Library Matching")
        plt.grid(False)
        plt.tight_layout()
        legend_elements = [
                Patch(facecolor=color, edgecolor='none', label=label)
                for label, color in color_mapping.items()
            ]
        ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.01, 1), fontsize=8, frameon=True)        
        ax.axhline(hline_pos, c="r", alpha=0.7)
        
        # else:
        #     raise ValueError("Classification must be done by Mineral Library Matching")

            


    @render.plot
    # @reactive.event(input.perf_yield_cor)
    def plot_max_percent():
        asp_ratio = calc_asp_ratio()
        global global_masked_mats
        global global_mats
        global ycf_global

        mats, loaded_elements, color_nums, mineral_colors, color_mapping, mineral_colors_mapped = data_loader_3()

        if input.class_type() == "Library Matching":
            elements = input.elements_ID()
        if input.class_type() == "KMeans Classification":
            elements = input.kmeans_elems()
            
        mineral_list = np.unique(mats["mineral_names"])
        silicates_df = get_std_mineral_df()

        if silicates_df.empty:
            raise ValueError("Please import a mineral library.")
        
        else:
            standard_values = {}
            standard_elements = {}
            for mineral in mineral_list:
                if mineral not in ["Unclassified"]:
                    standard_values[mineral] = {}
                    standard_elements[mineral] = []
                    mineral_df = silicates_df.loc[silicates_df["mineral name"] == mineral]
                    mineral_df = mineral_df.reset_index(drop=True)
                    for elem in elements:
                        if elem not in ["kmeans", "comp_cats", "mineral", "mineral_names", "numeric_max_key", "mat_total", "max_indices", "max_percent_match"]:
                            if mineral_df[elem][0] == np.nan:
                                print(f"{elem} not in {mineral}")
                                continue
                                # mats_test[mineral][elem] = np.full(mats[elem].shape, np.nan)
                                # mats_test_means[mineral][elem] = np.nanmean(mats_test[mineral][elem])
                            else:
                                standard_values[mineral][elem] = mineral_df[elem][0]
                                standard_elements[mineral].append(elem)
                    stacked_standard_array = np.stack([pd.to_numeric(standard_values[mineral][key], errors='coerce') for key in standard_elements[mineral]], axis=0)
                    standard_values[mineral]["total"] = np.nansum(stacked_standard_array, axis=0)

            max_keys = mats["mineral_names"]
            mat_total = mats["mat_total"]
            std_totals_max = np.zeros_like(max_keys, dtype=float)

            for mineral in mineral_list:
                if mineral not in ["Unclassified"]:
                    mineral_total = standard_values[mineral]["total"]
                    mineral_total_mat = np.full_like(max_keys, mineral_total, dtype=float)  # Broadcast scalar to array                   
                    std_totals_max[max_keys == mineral] = mineral_total_mat[max_keys == mineral]
            if "Unclassified" in max_keys:
                unclassified_mask = (max_keys == "Unclassified")
                std_totals_max[unclassified_mask] = mat_total[unclassified_mask]/10000

            yield_cor_fact = (mat_total/10000)/std_totals_max
            if "Unclassified" in max_keys:
                yield_cor_fact[max_keys == "Unclassified"] = 1

            # yield_cor_fact = np.where(yield_cor_fact == 0, np.nan, yield_cor_fact)
            
            ycf_global = yield_cor_fact

            # non_elemental_elements = ["kmeans", "comp_cats", "mineral", "mineral_names", "numeric_max_key", "mat_total", "max_indices", "max_percent_match"]
            
            # ycf_cor_mats = {}
            # for elem in loaded_elements:
            #     if elem not in ["kmeans", "comp_cats", "mineral", "mineral_names", "numeric_max_key", "mat_total", "max_indices", "max_percent_match"]:
            #         ycf_cor_mats[elem] = mats[elem]/yield_cor_fact
            # for elem in ["kmeans", "comp_cats", "mineral", "mineral_names", "numeric_max_key", "mat_total", "max_indices", "max_percent_match"]:
            #         if elem in mats.keys():
            #             ycf_cor_mats[elem] = mats[elem]

            # masked_mats = global_masked_mats

            # ycf_cor_masked_mats = {}
            # for mineral in mineral_list:
            #     ycf_cor_masked_mats[mineral] = {elem: masked_mats[mineral][elem]/yield_cor_fact for elem in loaded_elements if elem not in non_elemental_elements}

            
            # print(f"Row No.: {row_no/input.pixel_size()}")
            # col_min = int(input.col_min()/asp_ratio)
            # col_max = int(input.col_max()/asp_ratio)
            fig, axs = plt.subplots(3,1, sharex=True)
            if input.class_type() == "Library Matching":
                unique_min_no = np.unique(mats["numeric_max_key"])
                mat_shape = np.shape(mats["numeric_max_key"])
            if input.class_type() == "KMeans Classification":
                unique_min_no = np.unique(mats["kmeans"])
                mat_shape = np.shape(mats["kmeans"])
            min_no_mapping = {num_key: i for i, num_key in enumerate(unique_min_no)}
            if input.class_type() == "Library Matching":
                min_no_mat = np.vectorize(min_no_mapping.get)(mats["numeric_max_key"])
            if input.class_type() == "KMeans Classification":
                min_no_mat = np.vectorize(min_no_mapping.get)(mats["kmeans"])
            row_no = (np.shape(min_no_mat)[0]-1) - input.row_number()
            print(row_no)            
            x_var = np.linspace(0, mat_shape[1]*asp_ratio, mat_shape[1])
            axs[0].plot(x_var, min_no_mat[row_no], c="r")
            axs[0].set_ylabel("Mineral No.")
            axs[0].invert_yaxis()
            axs[1].plot(x_var, mats["max_percent_match"][row_no], c="r")
            axs[1].set_ylabel("Match %")
            axs[2].plot(x_var, yield_cor_fact[row_no], c="r")
            axs[2].set_ylabel("Yield CF")

    @render.plot
    def ycf_plot():
        asp_ratio = calc_asp_ratio()
        plt.imshow(ycf_global,
                   extent=[0, np.shape(ycf_global)[1]*asp_ratio, 0, np.shape(ycf_global)[0]],
                      interpolation='none')
        plt.title("Yield CF")
        plt.colorbar()
        plt.grid(False)
        plt.tight_layout()
        
        
    
    @render.table
    @reactive.event(input.perf_yield_cor)
    def apply_yield_cor():
        global ycf_cor_mats
        global ycf_cor_masked_mats
        # if input.class_type() == "Library Matching":

        mats, loaded_elements, color_nums, mineral_colors, color_mapping, mineral_colors_mapped = data_loader_3()
        mineral_list = np.unique(mats["mineral_names"])

        yield_cor_fact = ycf_global

        non_elemental_elements = ["kmeans", "comp_cats", "mineral", "mineral_names", "numeric_max_key", "mat_total", "max_indices", "max_percent_match"]
        non_elemental_elements += [
            k for k in mats.keys()
            if "CPS" in k or any(op in k for op in ["/", "+", "-", "*"])]

            
        ycf_cor_mats = {}
        for elem in loaded_elements:
            if elem not in non_elemental_elements:
                ycf_cor_mats[elem] = mats[elem]/yield_cor_fact
        for elem in non_elemental_elements:
                if elem in mats.keys():
                    ycf_cor_mats[elem] = mats[elem]

        masked_mats = global_masked_mats

        ycf_cor_masked_mats = {}
        for mineral in mineral_list:
            ycf_cor_masked_mats[mineral] = {elem: masked_mats[mineral][elem]/yield_cor_fact for elem in loaded_elements if elem not in non_elemental_elements}

        cor_data_means_dict = {}
        for mineral in mineral_list:
            cor_data_means_dict[mineral] = {}
            cor_data_means_dict[mineral]["mineral"] = mineral
            for elem in loaded_elements:
                if elem not in non_elemental_elements:
                    ycf_cor_masked_mats[mineral][elem][np.isinf(ycf_cor_masked_mats[mineral][elem])] = np.nan
                    if np.isnan(ycf_cor_masked_mats[mineral][elem]).all():
                        cor_data_means_dict[mineral][elem] = np.nan
                        print(f"{mineral}/{elem} contained all nans")
                    else:                        
                        cor_data_means_dict[mineral][elem] = np.nanmean(ycf_cor_masked_mats[mineral][elem])
                    cor_data_means_dict[mineral][f"{elem} 1sd"] = np.nanstd(ycf_cor_masked_mats[mineral][elem])
        
        cor_data_means_df = pd.DataFrame.from_dict(cor_data_means_dict, orient="index")
        legend_order = list(color_mapping.keys())
        cor_data_means_df = cor_data_means_df.reindex(legend_order)
        global global_cor_data_means_df
        global_cor_data_means_df = cor_data_means_df
        return cor_data_means_df

        # else:
        #     raise ValueError("Classification must be done by Mineral Library Matching")
        
    @render.download(filename = "ycf_means.xlsx")
    def download_yc_means():
        output = io.BytesIO()
        global_cor_data_means_df.to_excel(output, index=False)
        output.seek(0)
        return output


    @render.download(filename = "yield_cor_datacube.csv")
    def download_yc_cube():
        output = io.BytesIO()
        mats = ycf_cor_mats
        elements = list(mats.keys())
        spot_size = input.pixel_size()
        scan_speed = input.scan_speed()
        sweep_time = input.sweep_time()
       
        mat_shape = np.shape(mats[elements[0]])
        Ypts = np.array(range(mat_shape[0]))
        Xpts = np.array(range(mat_shape[1]))
        Ypts = Ypts[-1] - Ypts
        Ypts = Ypts * spot_size
        if input.aspect_ratio() == "Calculate aspect ratio":
            Xpts = Xpts * scan_speed * sweep_time/1000
        else:
            Xpts = Xpts * spot_size
        X2D,Y2D = np.meshgrid(Xpts,Ypts)
        coords = np.column_stack((Y2D.ravel(),X2D.ravel()))
        
        data_cube_df = pd.DataFrame()
        data_cube_df['x_coord'] = coords[:,1]
        data_cube_df['y_coord'] = coords[:,0]

        def leading_number(s):
            num = ''
            for c in s:
                if c.isdigit():
                    num += c
                else:
                    break
            return int(num)

        # elements_sorted = sorted(elements, key=leading_number)
        for elem in elements:
            data_cube_df[elem] = mats[elem].reshape(-1)

        data_cube_df.to_csv(output, index=False)
        output.seek(0)
        return output
        
    
    
 
    # @render_widget
    # def image_plot():
    #     mats = global_mats
    #     mat = mats[input.element_plotly()]
    #     x_coords = []
    #     y_coords =[]        
    #     for row in range((np.shape(mat)[0])):
    #         for col in range((np.shape(mat)[1])):
    #             x_coords.append(col)
    #             y_coords.append(row)
    #     # data_x = np.array([1,2,3,4])
    #     # data_y = np.array([5,6,7,8])
    #     # fig = px.imshow(mat)
    #     fig = px.scatter(x=x_coords, y=y_coords,
    #         color=np.log10(mat.flatten()), # Apply log10 to the color values
    #         # color_continuous_scale = parula,
    #         color_continuous_scale=input.plotly_colorscale(),  # Choose a colorscale (e.g., "Viridis", "Inferno", etc.)
    #         labels={"color": input.element_plotly()})
    #     # fig = go.Figure(data=go.Heatmap(x=x_coords, y=y_coords, z=mat.flatten()))
    #     # fig = px.imshow(mat)
    #     fig.update_traces(marker=dict(size=5, symbol="square"))
    #     fig.update_layout(dragmode="select", autosize=False)  # Enables box select
    #     # fig.update_xaxes(title="X Pixel")
    #     # fig.update_yaxes(title="Y Pixel")
    #     fig.update_yaxes(autorange='reversed')
    #     fig.update_layout(xaxis=dict(visible=False), yaxis=dict(visible=False), plot_bgcolor="white")
    #     # fig.add_trace(go.Heatmap(data=mat))
    #     w = go.FigureWidget(fig.data, fig.layout)
    #     w.data[0].on_selection(on_point_selection)
    #     w.update_layout(newselection=dict(line=dict(color="red", width=2)))
    #     return w
    selection_reactive = reactive.value(None)

    @render_widget
    def image_plot():
        asp_ratio = calc_asp_ratio()
        if input.use_cor_mats() == True:
            mats = ycf_cor_mats
        else:
            mats = global_mats 
        mat = mats[input.element_plotly()]
        mat[np.isinf(mat)] = 0
        mat[np.isnan(mat)] = 0
        color_scale = batlow_plotly if input.plotly_colorscale() == "batlow" else input.plotly_colorscale()
        x_extent = np.linspace(0, mat.shape[1]*asp_ratio, mat.shape[1])
        y_extent = np.linspace(0, mat.shape[0], mat.shape[0])
        vmin_ = np.nanpercentile(mat, input.min_max_vals_roi()[0])
        vmax_ = np.nanpercentile(mat, input.min_max_vals_roi()[1])
        fig = px.imshow(mat, x=x_extent, y=y_extent,
                        range_color=[vmin_, vmax_], 
                        color_continuous_scale=color_scale,
                        labels={"x": "pixel no.", "y": "pixel no."})

        # Set drag mode based on the selection tool
        dragmode = "select" if input.plotly_tool() == "rectangle" else "lasso"
        fig.update_layout(dragmode=dragmode, autosize=False)
        fig.update_layout(plot_bgcolor="white")
        fig.update_layout(modebar_remove=["zoom", "pan"])
        fig.update_layout(newselection=dict(line=dict(color="red", width=2)))

        # Create a FigureWidget
        w = go.FigureWidget(fig)

        w.data[0].on_selection(on_point_selection)

        return w
    
    def on_point_selection(trace, points, state):
        selection_reactive.set(state)



    # @render_widget
    # def image_plot():
    #     mats = global_mats
    #     mat = mats[input.element_plotly()]
    #     color_scale = batlow_plotly if input.plotly_colorscale() == "batlow" else input.plotly_colorscale()
    #     fig = px.imshow(mat, color_continuous_scale=color_scale)

    #     # Enable drawing rectangles
    #     fig.update_layout(
    #         dragmode='drawrect',
    #         newshape=dict(line_color="cyan"),
    #         modebar_add=["drawrect", "eraseshape"]
    #     )

    #     # Convert the figure to a FigureWidget
    #     fig_widget = go.FigureWidget(fig)

    #     # Callback to capture shapes
    #     def on_shape_change(layout, new_shapes):
    #         if "shapes" in layout:
    #             shapes_reactive.set(layout["shapes"])  # Store the shapes in the reactive value
    #             print(f"Shapes updated: {layout['shapes']}")  # Debugging output

    #     # Attach the callback to the layout's `shapes` property
    #     fig_widget.layout.on_change(on_shape_change, "shapes")

    #     return fig_widget
    
    # @reactive.Effect
    # @reactive.event(input.btn)
    # def show_shape_info():
    #     shapes = shapes_reactive.get()
    #     if shapes:
    #         shapes_json = json.dumps(shapes, indent=2)
    #         @output
    #         @render.text
    #         def dump():
    #             return shapes_json
    #     else:
    #         @output
    #         @render.text
    #         def dump():
    #             return "No shapes drawn yet."
            
        # # Create a FigureWidget
        # w = go.FigureWidget(fig)

        # # Callback to handle shape changes

        
        #     # print("NEW SHAPE ADDED")
        #     # print("DEBUG: Callback triggered")
        #     # print("DEBUG: Layout changed:", layout)
        #     # print("DEBUG: New shapes:", new_shapes)
        #     # if new_shapes:
        #     #     # Process the last shape added
        #     #     new_shape = new_shapes[-1]
        #     #     if new_shape['type'] == 'rect':
        #     #         x0, x1 = new_shape['x0'], new_shape['x1']
        #     #         y0, y1 = new_shape['y0'], new_shape['y1']
        #     #         print(f"Rectangle coordinates: x0={x0}, x1={x1}, y0={y0}, y1={y1}")

        # w.layout.on_relayout(on_shape_change)

        # return w
    
    # def on_shape_change(relayout_data):
    #     shape_reactive.set(relayout_data)

    
    # def on_shape_change(layout):
    #     # print(f"Layout from function: {layout}")
    #     print(f"from function: {layout.shapes}")


        # fig_widget = go.FigureWidget(fig)


        # # Define the callback for layout changes
        # def on_shape_change(layout, new_shapes):
        #     print(f"Layout from function: {layout}")
        #     if new_shapes:
        #         # Get the last shape added
        #         new_shape = new_shapes[-1]
        #         if new_shape['type'] == 'rect':
        #             x0, x1 = new_shape['x0'], new_shape['x1']
        #             y0, y1 = new_shape['y0'], new_shape['y1']
        #             print(f"Rectangle coordinates: x0={x0}, x1={x1}, y0={y0}, y1={y1}")

        # # Attach the callback to listen for changes in shapes
        # print(fig_widget.layout)
        # print(fig_widget.data)
        # fig_widget.layout.on_change(on_shape_change, 'shapes')

        # # fig_widget._config = fig_widget._config | {'modeButtonsToAdd': ['drawline', 'drawopenpath', 'drawclosedpath', 'drawcircle', 'drawrect', 'eraseshape']}
        # return fig_widget
    
    # def on_point_selection(trace, points, state):
    #     selection_reactive.set(state)

    @render.text
    def print_coords():
        # return "Ignore: this is a placeholder for debugging"
        if selection_reactive.get() is None:
            return "No points selected."
        else:
            x_idxs = selection_reactive.get().xrange
            y_idxs = selection_reactive.get().yrange
            return f"X coords: {x_idxs} Y coords: {y_idxs}"

    global global_roi_avgs_df
    global global_roi_data_df
    global_roi_avgs_df = pd.DataFrame()
    global_roi_data_df = pd.DataFrame()

    @render.data_frame
    def selected_pixels():
        asp_ratio = calc_asp_ratio()
        global global_roi_avgs_df
        global global_roi_data_df

        if input.use_cor_mats() == True:
            mats = ycf_cor_mats
        else:
            mats = global_mats 
        elements = global_elements
        if selection_reactive.get() is None:
            empty_df = pd.DataFrame({"Message": ["No regions selected"]})
            return empty_df
        else:
            if input.plotly_tool() == "lasso":
                x_idxs = np.array(selection_reactive.get().xs) / asp_ratio
                y_idxs = np.array(selection_reactive.get().ys)
                rr, cc = polygon(y_idxs, x_idxs)
                mat_shape = mats[elements[0]].shape
                mask = np.zeros(mat_shape, dtype=bool)
                mask[rr, cc] = True
            elif input.plotly_tool() == "rectangle":
                xmin = int(np.floor(np.min(selection_reactive.get().xrange) / asp_ratio))
                xmax = int(np.ceil(np.max(selection_reactive.get().xrange) / asp_ratio))
                ymin = int(np.floor(np.min(selection_reactive.get().yrange)))
                ymax = int(np.ceil(np.max(selection_reactive.get().yrange)))
                mat_shape = mats[elements[0]].shape
                # Clip to ensure indices are within bounds
                xmin = max(0, xmin)
                xmax = min(mat_shape[1], xmax)
                ymin = max(0, ymin)
                ymax = min(mat_shape[0], ymax)
                mask = np.zeros(mat_shape, dtype=bool)
                mask[ymin:ymax, xmin:xmax] = True
                # print("mat shape:", mats[element].shape, "mask shape:", mask.shape)

            region_data = {}
            region_data_dict = {}
            region_means = {}
            region_means["ROI"] = f"ROI{len(global_roi_avgs_df)}"
            # region_means["x_idxs"] = x_idxs
            # region_means["y_idxs"] = y_idxs
            region_data["ROI"] = f"ROI{len(global_roi_avgs_df)}"
            for element in elements:
                if np.issubdtype(mats[element].dtype, np.number):
                    region_data_el = mats[element][mask].flatten()
                    
                    # # Ensure region_data_el is numeric
                    # try:
                    #     region_data_el = np.asarray(region_data_el, dtype=np.float64)
                    # except ValueError as e:
                    #     print(f"ERROR: Non-numeric data in region_data_el for element {element}: {e}")
                    #     continue

                    # # Replace values <= 0 with np.nan
                    # region_data_el = np.where(region_data_el <= 0, np.nan, region_data_el)

                    # if region_data_el.size == 0 or np.all(np.isnan(region_data_el)):
                    #     print(f"WARNING: No valid data for element {element} in the selected region.")
                    #     continue

                    region_data[element] = region_data_el.tolist()
                    region_data_dict[element] = region_data_el
                    valid_values = region_data_el[region_data_el > 0]
                    if valid_values.size == 0:
                        region_means[element] = np.nan
                        region_means[f"{element}_1sd"] = np.nan
                    else:
                        region_means[element] = np.round(np.nanmean(valid_values), 2)
                        region_means[f"{element}_1sd"] = np.round(np.nanstd(valid_values), 2)
            region_means["N"] = np.size(region_data[element])
            if input.plotly_tool() == "lasso":
                region_data["coords_x"] = x_idxs
                region_data["coords_y"] = y_idxs
            if input.plotly_tool() == "rectangle":
                region_data["coords_x"] = [xmin, xmax]
                region_data["coords_y"] = [ymin, ymax]   
            
            # Append the new row to the DataFrame
            if region_means:
                new_row = region_means                
                df = pd.concat([global_roi_avgs_df, pd.DataFrame([new_row])], ignore_index=True)  # Append as a new row
                global_roi_avgs_df = df
                new_data_row = region_data
                global_roi_data_df = pd.concat([global_roi_data_df, pd.DataFrame([new_data_row])], ignore_index=True)
            else:
                print("WARNING: No valid data to append to the DataFrame.")

            return global_roi_avgs_df
        
    @render.download(filename = "roi_means.xlsx")
    def download_ROI_means():
        output = io.BytesIO()
        global_roi_avgs_df.to_excel(output, index=False)
        output.seek(0)
        return output

    overlay_points_reactive = reactive.value([])

    @render_widget
    def plot_overlay():
        _ = input.clear_points()  # ensures reactivity
        global overlay_img
        asp_ratio = calc_asp_ratio()
        if input.use_cor_mats() == True:
            mats = ycf_cor_mats
        else:
            mats = global_mats 
        mat_ = mats[input.overlay_map()]
        mat = copy.deepcopy(mat_)
        mat[np.isnan(mat)]=0
        mat[np.isinf(mat)]=0
        x_extent = np.linspace(0, input.pixel_size()*mat.shape[1]*asp_ratio, mat.shape[1])
        y_extent = np.linspace(0, input.pixel_size()*mat.shape[0], mat.shape[0])
        vmin_ = np.nanpercentile(mat, 1)
        vmax_ = np.nanpercentile(mat,99)
        mat_nan = copy.deepcopy(mat_)
        mat_nan[mat_nan<=0]=np.nan
        mat_log_nan = np.log10(mat_nan)
        mat_log = copy.deepcopy(mat_log_nan)

        print(f"min of mat_log: {np.nanmin(mat_log_nan)}")
        if np.isnan(mat_log_nan).all():
            mat_log = np.full_like(mat_log_nan, 0.0001)
        else:
            mat_log = copy.deepcopy(mat_log_nan)
            mat_log[np.isnan(mat_log)]=np.nanmin(mat_log_nan)
            mat_log[np.isinf(mat_log)]=np.nanmin(mat_log_nan)
        vmin_log = np.nanpercentile(mat_log, 1)
        vmax_log = np.nanpercentile(mat_log, 99)
        c_scale = batlow_plotly
        overlay_img = mat_log
        fig = px.imshow(mat_log, x=x_extent, y=y_extent,
                        range_color=[vmin_log, vmax_log],
                        # color=np.log10(mat.flatten()), # Apply log10 to the color values
                        color_continuous_scale=c_scale,  # Choose a colorscale (e.g., "Viridis", "Inferno", etc.)
                        labels={"color": f"log {input.overlay_map()}"},
                        origin="upper")
        # fig.update_layout(title="Click three points")

        w = go.FigureWidget(fig)

        selected_points = []

        def on_click(trace, points, selector):
            if points.xs and points.ys:
                x = points.xs[0]
                y = points.ys[0]
                selected_points = overlay_points_reactive.get().copy()
                selected_points.append((x, y))
                overlay_points_reactive.set(selected_points)                
                print(f"Selected: {(x, y)}")
                # Optionally, add a marker
                if len(selected_points) == 3:
                    print("Three points selected:", selected_points)
                    # You can now use selected_points for your affine transform

                global overlay_points
                overlay_points = overlay_points_reactive.get().copy()
                # print("Base points:", base_pts)
                # base_y_idxs =  np.array([pt[0] for pt in base_pts])
                # base_y_coords = base_y_idxs*input.pixel_size()
                # base_x_idxs = np.array([pt[1] for pt in base_pts])
                # base_x_coords = base_x_idxs*input.pixel_size()*asp_ratio
                # base_points = [(base_x_coords[i], base_y_coords[i]) for i in range(len(base_pts))]
                colors = ["red", "green", "blue"]
                with w.batch_update():
                    w.add_scatter(x=[x], y=[y], mode='markers', marker=dict(color=colors, size=10))

                # print("Base_x_coords:", base_x_coords)
                # print("Base_y_coords:", base_y_coords)           
                
        
        w.data[0].on_click(on_click)        
        return w
    
    @render.text
    def overlay_text():
        pts = overlay_points_reactive.get()
        if not pts:
            return "No points selected yet."
        else:
            rounded_pts = [(round(x, 2), round(y, 2)) for x, y in overlay_points]
            return f"Selected Points: {rounded_pts}"     

    
    
    imported_points_reactive = reactive.value([])

    @render_widget
    def imported():
        _ = input.clear_points()  # ensures reactivity
        global imported_img_global
        file = input.imported_image()
        if not file:
            imported_img_global = np.full_like(overlay_img, 0.0001)
            return go.FigureWidget()  # Return empty if no file
        
        img_path = file[0]["datapath"]
        img = Image.open(img_path)
        
        img_np = np.array(img)
        imported_img_global = img_np

        fig = px.imshow(img_np)
        # fig.update_layout(title="Click three points on the imported image.")

        w = go.FigureWidget(fig)

        def on_click(trace, points, selector):
            if points.xs and points.ys:
                x = points.xs[0]
                y = points.ys[0]
                selected_points = imported_points_reactive.get().copy()
                selected_points.append((x, y))
                imported_points_reactive.set(selected_points)                
                print(f"Selected: {(x, y)}")
                # Optionally, add a marker
                if len(selected_points) == 3:
                    print("Three points selected:", selected_points)
                    # You can now use selected_points for your affine transform

                global imported_points
                imported_points = imported_points_reactive.get().copy()
                # print("Base points:", base_pts)
                # base_y_idxs =  np.array([pt[0] for pt in base_pts])
                # base_y_coords = base_y_idxs*input.pixel_size()
                # base_x_idxs = np.array([pt[1] for pt in base_pts])
                # base_x_coords = base_x_idxs*input.pixel_size()*asp_ratio
                # base_points = [(base_x_coords[i], base_y_coords[i]) for i in range(len(base_pts))]
                colors = ["red", "green", "blue"]
                with w.batch_update():
                    w.add_scatter(x=[x], y=[y], mode='markers', marker=dict(color=colors, size=10))
                

        # def on_click(trace, points, selector):
        #     if points.point_inds:
        #         # Get the clicked point's coordinates
        #         y, x = np.unravel_index(points.point_inds[0],img_np.shape[:2])
        #         selected_points = imported_points_reactive.get().copy()
        #         selected_points.append((x, y))
        #         imported_points_reactive.set(selected_points)                
        #         print(f"Selected: {(x, y)}")
        #         # Optionally, add a marker
        #         with w.batch_update():
        #             w.add_scatter(x=[x], y=[y], mode='markers', marker=dict(color='red', size=10))
        #         if len(selected_points) == 3:
        #             print("Three points selected:", selected_points)
        #             # You can now use selected_points for your affine transform
        #         global imported_points
        #         imported_points = [item[0] for item in imported_points_reactive.get().copy()]
        #         # print("Base points:", imported_points[0][0])
        
        w.data[0].on_click(on_click)        
        return w
    
    @render.text
    def imported_text():
        pts = imported_points_reactive.get()
        if not pts:
            return "No points selected yet."
        else:
            return f"Selected Points: {imported_points}"
    
    
    global warped_mats
    warped_mats = {}

    @render.text
    @reactive.event(input.perform_overlay)
    def overlay_result_text():
        # if len(overlay_points) != 3 or len(imported_points) != 3:
        #     return "Error: You must choose exaclty three points from both the imported image and the alignment map."
        # else:
        asp_ratio = calc_asp_ratio()
        img_overlay = overlay_img
        img_imported = imported_img_global

        if input.use_cor_mats() == True:
            mats = ycf_cor_mats
        else:
            mats = global_mats 

        elements = list(mats.keys())

        def axis_to_pixel(points, x_extent, y_extent, img_shape):
            x_min, x_max = x_extent[0], x_extent[-1]
            y_min, y_max = y_extent[0], y_extent[-1]
            width = img_shape[1]
            height = img_shape[0]
            pixel_points = []
            for x, y in points:
                col = (x - x_min) / (x_max - x_min) * (width - 1)
                row = (y - y_min) / (y_max - y_min) * (height - 1)
                pixel_points.append([col, row])
            return pixel_points
        
        
        overlay_x_extent = np.linspace(0, input.pixel_size()*img_overlay.shape[1]*asp_ratio, img_overlay.shape[1])
        overlay_y_extent = np.linspace(0, input.pixel_size()*img_overlay.shape[0], img_overlay.shape[0])

        imported_x_extent = np.linspace(0, img_imported.shape[1], img_imported.shape[1])
        imported_y_extent = np.linspace(0, img_imported.shape[0], img_imported.shape[0])

        # Example usage:
        overlay_points_pixel = axis_to_pixel(overlay_points, overlay_x_extent, overlay_y_extent, img_overlay.shape)
        imported_points_pixel = axis_to_pixel(imported_points, imported_x_extent, imported_y_extent, img_imported.shape)

        src_pts = np.float32(overlay_points_pixel)      # overlay image points (physical coordinates)
        dst_pts = np.float32(imported_points_pixel)  # imported image points (physical coordinates)

        M, inliers = cv2.estimateAffine2D(src_pts, dst_pts)
        print("matrix: ", M)

        
        for element in elements:
            warped_mats[element] = cv2.warpAffine(mats[element], M, (img_imported.shape[1], img_imported.shape[0]))
            print(f"{element} warping completed.")

        new_choices = list(warped_mats.keys())
        ui.update_select("overlay_result_element", choices=new_choices)
        return "Alignment completed. Displaying image (this may take a while)..."



    @render_widget
    def overlay_result():        
        element = input.overlay_result_element()
        alpha = input.overlay_alpha()
        if element == "None yet":
            return go.FigureWidget()
            # img_imported_gray = color.rgb2gray(img_imported)
            # fig = px.imshow(img_imported_gray, color_continuous_scale="gray")
            # w = go.FigureWidget(fig)
            # return w
        else:
            img_imported = imported_img_global
            mat_ = warped_mats[element]           
            
            mat_nan = copy.deepcopy(mat_)
            mat_nan[mat_nan<=0]=np.nan
            mat_log_nan = np.log10(mat_nan)
            mat_log = copy.deepcopy(mat_log_nan)

            print(f"min of mat_log: {np.nanmin(mat_log_nan)}")
            if np.isnan(mat_log_nan).all():
                mat_log = np.full_like(mat_log_nan, 0)
            else:                
                mat_log = copy.deepcopy(mat_log_nan)
                floor = np.nanmin(mat_log) - 1
                mat_log[np.isnan(mat_log)]=floor
                mat_log[np.isinf(mat_log)]=floor

            # mask = warped_overlay > 0
            z = copy.deepcopy(mat_log)
            # z[~mask] = 0  # Set masked-out regions to 0
            
            z_max = np.max(z)
            z_min = np.min(z[z > floor])
            z_mid = ((z_max - z_min)/2)+z_min
            # Custom colorscale: 0 is fully transparent, others are colored
            rgb_cscale = [
                [0, 'rgba(0,0,0,0)'],   # 0 value is fully transparent
                [0.001, f'rgba(0,0,255,{alpha})'],
                [0.5, f'rgba(0,255,0,{alpha})'],
                [1.0, f'rgba(255,0,0,{alpha})']]

            # def rgb2gray(rgb):
            #     return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
            
            # img_imported_gray = rgb2gray(img_imported)

            img_imported_gray = color.rgb2gray(img_imported)
            
            if input.overlay_result_cscale() == "Blue-Green-Red":
                cscale = rgb_cscale
            elif input.overlay_result_cscale() == "batlow":
                cscale = batlow_plotly2

            fig = px.imshow(img_imported_gray, color_continuous_scale="gray")
            fig.update_coloraxes(showscale=False)
            fig.add_trace(go.Heatmap(z=z, colorscale=cscale, opacity=alpha,
                                    zmin=np.percentile(z[z>floor], 1), zmax=np.percentile(z[z>floor], 99),
                                    colorbar=dict(title=f"log {input.overlay_result_element()}")))
            w = go.FigureWidget(fig)        
            # fig.update_layout(title="Overlay Result")
            return w
        

    
    @reactive.effect
    @reactive.event(input.clear_points)
    def clear_selected_points():
        overlay_points_reactive.set([])
        imported_points_reactive.set([])
        global overlay_points
        overlay_points = []
        global imported_points
        imported_points = []


    @render_widget
    def plot():
        asp_ratio = calc_asp_ratio()
        selected_minerals = input.masked_map()
        if isinstance(selected_minerals, tuple):
            selected_minerals = list(selected_minerals) 
        if "All" in selected_minerals:
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = global_mats 
        else:
            if len(selected_minerals) == 1:
                if input.use_cor_mats() == True:
                    mats = ycf_cor_masked_mats[selected_minerals[0]]
                else:
                    mats = global_masked_mats[selected_minerals[0]]
            else:
                if input.use_cor_mats() == True:
                    filtered_mats = {mineral: ycf_cor_masked_mats[mineral] for mineral in selected_minerals if mineral in ycf_cor_masked_mats}

                else:
                    filtered_mats = {mineral: global_masked_mats[mineral] for mineral in selected_minerals if mineral in global_masked_mats}

                combined_maps = {}
                elements = list(next(iter(filtered_mats.values())).keys())

                # Combine the maps for each element
                for elem in elements:
                    combined = None
                    for mineral, mat_dict in filtered_mats.items():
                        if combined is None:
                            combined = mat_dict[elem]  # Start with the first matrix
                        else:
                            combined = np.where(np.isnan(combined), mat_dict[elem], combined)  # Replace NaNs
                    combined_maps[elem] = combined

                mats = combined_maps               

        mat_ = mats[input.element()]
        mat = copy.deepcopy(mat_)
        mat[np.isnan(mat)]=0
        mat[np.isinf(mat)]=0
        vmin_ = np.nanpercentile(mat, input.min_max_vals()[0])
        vmax_ = np.nanpercentile(mat, input.min_max_vals()[1])
        x_extent = np.linspace(0, input.pixel_size()*mat.shape[1]*asp_ratio, mat.shape[1])
        y_extent = np.linspace(0, input.pixel_size()*mat.shape[0], mat.shape[0])
        if input.c_map() == "batlow":
            c_scale = batlow_plotly
        else:
            c_scale = input.c_map()
        if input.use_log() == True:
            mat_nan = copy.deepcopy(mat_)
            mat_nan[mat_nan<=0]=np.nan
            mat_log_nan = np.log10(mat_nan)
            mat_log = copy.deepcopy(mat_log_nan)
            print(f"min of mat_log: {np.nanmin(mat_log_nan)}")
            if np.isnan(mat_log_nan).all():
                mat_log = np.full_like(mat_log_nan, 0.0001)
            else:
                mat_log = copy.deepcopy(mat_log_nan)
                mat_log[np.isnan(mat_log)]=np.nanmin(mat_log_nan)
                mat_log[np.isinf(mat_log)]=np.nanmin(mat_log_nan)
            vmin_log = np.nanpercentile(mat_log, input.min_max_vals()[0])
            vmax_log = np.nanpercentile(mat_log, input.min_max_vals()[1])
            fig = px.imshow(mat_log, x=x_extent, y=y_extent,
                            range_color=[vmin_log, vmax_log],
                            # color=np.log10(mat.flatten()), # Apply log10 to the color values
                            color_continuous_scale=c_scale,  # Choose a colorscale (e.g., "Viridis", "Inferno", etc.)
                            labels={"x": "μm", "y": "μm", "color": f"log {input.element()}"},
                            origin="upper")
        else:
            fig = px.imshow(mat, x=x_extent, y=y_extent,
                            range_color=[vmin_, vmax_],
                            color_continuous_scale=c_scale,  # Choose a colorscale (e.g., "Viridis", "Inferno", etc.)
                            labels={"x": "μm", "y": "μm", "color": input.element()},
                            origin="upper")
        # fig.update_yaxes(autorange='reversed')
        w = go.FigureWidget(fig.data, fig.layout)
        w._config = w._config | {"toImageButtonOptions": {'height': 1200, 'width': 1500,}}
        return w


        # fig, ax = plt.subplots()
        # ax.set_facecolor("black")
        # # ax = np.atleast_2d(ax)
        # # plt.rcParams["figure.figsize"] = (16,8)
        # if input.use_log() == True:
        #     im = ax.imshow(mat, norm=colors.SymLogNorm(linthresh=0.001, vmin=vmin_, vmax=vmax_), cmap=input.c_map(),
        #                 extent=[0, np.shape(mat)[1]*input.pixel_size()*asp_ratio, 0, np.shape(mat)[0]*input.pixel_size()], interpolation='none')
        # else:
        #     im = ax.imshow(mat, vmin=vmin_, vmax=vmax_, cmap=input.c_map(),
        #                 extent=[0, np.shape(mat)[1]*input.pixel_size()*asp_ratio, 0, np.shape(mat)[0]*input.pixel_size()], interpolation='none')
        # ax.set_title(input.element())
        # # divider = make_axes_locatable(ax)
        # # cax = divider.append_axes("right", size="5%", pad=0.01)
        # fig.colorbar(im, pad=0.01, fraction=input.colorbar_fract())
        # ax.set_xlabel("μm")
        # ax.set_ylabel("μm")
        # plt.grid(False)
        # return fig

        


    # @render.plot
    # def plot():
    #     asp_ratio = calc_asp_ratio()
    #     selected_minerals = input.masked_map()
    #     if isinstance(selected_minerals, tuple):
    #         selected_minerals = list(selected_minerals) 
    #     if "All" in selected_minerals:
    #         if input.use_cor_mats() == True:
    #             mats = ycf_cor_mats
    #         else:
    #             mats = global_mats 
    #     else:
    #         if len(selected_minerals) == 1:
    #             if input.use_cor_mats() == True:
    #                 mats = ycf_cor_masked_mats[selected_minerals[0]]
    #             else:
    #                 mats = global_masked_mats[selected_minerals[0]]
    #         else:
    #             if input.use_cor_mats() == True:
    #                 filtered_mats = {mineral: ycf_cor_masked_mats[mineral] for mineral in selected_minerals if mineral in ycf_cor_masked_mats}

    #             else:
    #                 filtered_mats = {mineral: global_masked_mats[mineral] for mineral in selected_minerals if mineral in global_masked_mats}

    #             combined_maps = {}
    #             elements = list(next(iter(filtered_mats.values())).keys())

    #             # Combine the maps for each element
    #             for elem in elements:
    #                 combined = None
    #                 for mineral, mat_dict in filtered_mats.items():
    #                     if combined is None:
    #                         combined = mat_dict[elem]  # Start with the first matrix
    #                     else:
    #                         combined = np.where(np.isnan(combined), mat_dict[elem], combined)  # Replace NaNs
    #                 combined_maps[elem] = combined

    #             mats = combined_maps               

    #     mat_ = mats[input.element()]
    #     mat_nan = copy.deepcopy(mat_)
    #     mat_nan[mat_nan<=0]=np.nan
    #     mat = mat_nan
    #     vmin_ = np.nanpercentile(mat, input.min_max_vals()[0])
    #     vmax_ = np.nanpercentile(mat, input.min_max_vals()[1])
    #     fig, ax = plt.subplots()
    #     ax.set_facecolor("black")
    #     # ax = np.atleast_2d(ax)
    #     # plt.rcParams["figure.figsize"] = (16,8)
    #     if input.use_log() == True:
    #         im = ax.imshow(mat, norm=colors.SymLogNorm(linthresh=0.001, vmin=vmin_, vmax=vmax_), cmap=input.c_map(),
    #                    extent=[0, np.shape(mat)[1]*input.pixel_size()*asp_ratio, 0, np.shape(mat)[0]*input.pixel_size()], interpolation='none')
    #     else:
    #         im = ax.imshow(mat, vmin=vmin_, vmax=vmax_, cmap=input.c_map(),
    #                    extent=[0, np.shape(mat)[1]*input.pixel_size()*asp_ratio, 0, np.shape(mat)[0]*input.pixel_size()], interpolation='none')
    #     ax.set_title(input.element())
    #     # divider = make_axes_locatable(ax)
    #     # cax = divider.append_axes("right", size="5%", pad=0.01)
    #     fig.colorbar(im, pad=0.01, fraction=input.colorbar_fract())
    #     ax.set_xlabel("μm")
    #     ax.set_ylabel("μm")
    #     plt.grid(False)
    #     return fig    

    # @render.text    
    # @reactive.event(input.save_fig)
    # def save_figure():
    #     asp_ratio = calc_asp_ratio()
    #     if input.masked_map() == "All":
    #         mats = global_mats 
    #     else:
    #         mats = global_masked_mats[input.masked_map()]
    #     mat_ = mats[input.element()]
    #     mat_nan = copy.deepcopy(mat_)
    #     mat_nan[mat_nan<=0]=np.nan
    #     mat = mat_nan
    #     vmin_ = np.nanpercentile(mat, input.min_max_vals()[0])
    #     vmax_ = np.nanpercentile(mat, input.min_max_vals()[1])
    #     ax = plt.axes()
    #     ax.set_facecolor("black")
    #     # ax = np.atleast_2d(ax)
    #     # plt.rcParams["figure.figsize"] = (16,8)
    #     if input.use_log() == True:
    #         plt.imshow(mat, norm=colors.SymLogNorm(linthresh=0.001, vmin=vmin_, vmax=vmax_), cmap=input.c_map(),
    #                    extent=[0, np.shape(mat)[1]*input.pixel_size()*asp_ratio, 0, np.shape(mat)[0]*input.pixel_size()], interpolation='none')
    #     else:
    #         plt.imshow(mat, vmin=vmin_, vmax=vmax_, cmap=input.c_map(),
    #                    extent=[0, np.shape(mat)[1]*input.pixel_size()*asp_ratio, 0, np.shape(mat)[0]*input.pixel_size()], interpolation='none')
    #     plt.title(input.element())
    #     plt.colorbar(label=input.colorbar_label(),pad=0.01)
    #     plt.xlabel("μm")
    #     plt.ylabel("μm")
    #     plt.grid(False)
    #     plt.savefig("{}/{}.png".format(global_data_path, input.element()), dpi=300)
    #     return "Your {} image has been saved.".format(input.element())
    

    # @render.plot
    # def plot_rgb():
    #     asp_ratio = calc_asp_ratio()
    #     if input.masked_map_red() == "All":
    #         mats_red = ycf_cor_mats if input.use_cor_mats() else global_mats
    #     else:
    #         mats_red = ycf_cor_masked_mats[input.masked_map_red()] if input.use_cor_mats() else global_masked_mats[input.masked_map_red()]
    #     mat_red = mats_red[input.element_red()]

    #     if input.masked_map_green() == "All":
    #         mats_green = ycf_cor_mats if input.use_cor_mats() else global_mats
    #     else:
    #         mats_green = ycf_cor_masked_mats[input.masked_map_green()] if input.use_cor_mats() else global_masked_mats[input.masked_map_green()]
    #     mat_green = mats_green[input.element_green()]

    #     if input.masked_map_blue() == "All":
    #         mats_blue = ycf_cor_mats if input.use_cor_mats() else global_mats
    #     else:
    #         mats_blue = ycf_cor_masked_mats[input.masked_map_blue()] if input.use_cor_mats() else global_masked_mats[input.masked_map_blue()]
    #     mat_blue = mats_blue[input.element_blue()]

    #     # Normalize each channel
    #     vmin_red = np.nanpercentile(mat_red, input.min_max_vals_red()[0])
    #     vmax_red = np.nanpercentile(mat_red, input.min_max_vals_red()[1])
    #     norm_red = colors.Normalize(vmin=vmin_red, vmax=vmax_red)
    #     img_red = (norm_red(mat_red)) 

    #     vmin_green = np.nanpercentile(mat_green, input.min_max_vals_green()[0])
    #     vmax_green = np.nanpercentile(mat_green, input.min_max_vals_green()[1])
    #     norm_green = colors.Normalize(vmin=vmin_green, vmax=vmax_green)
    #     img_green = (norm_green(mat_green)) 

    #     vmin_blue = np.nanpercentile(mat_blue, input.min_max_vals_blue()[0])
    #     vmax_blue = np.nanpercentile(mat_blue, input.min_max_vals_blue()[1])
    #     norm_blue = colors.Normalize(vmin=vmin_blue, vmax=vmax_blue)
    #     img_blue = (norm_blue(mat_blue)) 

    #     # Combine the channels
    #     rgb = np.dstack((img_red, img_green, img_blue))

    #     ax = plt.axes()
    #     ax.set_facecolor("black")
    #     plt.imshow(rgb, extent=[0, np.shape(rgb)[1] * input.pixel_size() * asp_ratio, 0, np.shape(rgb)[0] * input.pixel_size()], interpolation='none')
    #     plt.grid(False)
    #     plt.xlabel("μm")
    #     plt.ylabel("μm")

    #     # Add a legend for the RGB components
    #     legend_elements = [
    #         Patch(facecolor='red', edgecolor='none', label=f"{input.element_red()}_{input.masked_map_red()} ({input.cmap_ch1()})"),
    #         Patch(facecolor='green', edgecolor='none', label=f"{input.element_green()}_{input.masked_map_green()} ({input.cmap_ch2()})"),
    #         Patch(facecolor='blue', edgecolor='none', label=f"{input.element_blue()}_{input.masked_map_blue()} ({input.cmap_ch3()})")
    #     ]
    #     ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.02, 1.0), fontsize=8, frameon=True)
    #     plt.tight_layout()

    @render_widget
    def plot_rgb():
        asp_ratio = calc_asp_ratio()
        
        if input.masked_map_red() == "All":
            if input.use_cor_mats() == True:
                mats_red = ycf_cor_mats
            else:
                mats_red = global_mats
        else:
            if input.use_cor_mats() == True:
                mats_red = ycf_cor_masked_mats[input.masked_map_red()]
            else:
                mats_red = global_masked_mats[input.masked_map_red()]
        mat_red_ = mats_red[input.element_red()]
        mat_red_[np.isnan(mat_red_)]=0
        mat_red = copy.deepcopy(mat_red_)
        vmin_red = np.nanpercentile(mat_red, input.min_max_vals_red()[0])
        vmax_red = np.nanpercentile(mat_red, input.min_max_vals_red()[1])
        mat_red[mat_red<vmin_red]=0
        mat_red[mat_red>=vmax_red]=vmax_red
        mat_red_norm = (mat_red/np.max(mat_red))*255
        
        
        if input.masked_map_green() == "All":
            if input.use_cor_mats() == True:
                mats_green = ycf_cor_mats
            else:
                mats_green = global_mats
        else:
            if input.use_cor_mats() == True:
                mats_green = ycf_cor_masked_mats[input.masked_map_green()]
            else:
                mats_green = global_masked_mats[input.masked_map_green()]
        mat_green_ = mats_green[input.element_green()]
        mat_green_[np.isnan(mat_green_)]=0
        mat_green = copy.deepcopy(mat_green_)
        vmin_green = np.nanpercentile(mat_green, input.min_max_vals_green()[0])
        vmax_green = np.nanpercentile(mat_green, input.min_max_vals_green()[1])
        mat_green[mat_green<vmin_green]=0
        mat_green[mat_green>=vmax_green]=vmax_green
        mat_green_norm = (mat_green/np.max(mat_green))*255
        
        if input.masked_map_blue() == "All":
            if input.use_cor_mats() == True:
                mats_blue = ycf_cor_mats
            else:
                mats_blue = global_mats
        else:
            if input.use_cor_mats() == True:
                mats_blue = ycf_cor_masked_mats[input.masked_map_blue()]
            else:
                mats_blue = global_masked_mats[input.masked_map_blue()]
        mat_blue_ = mats_blue[input.element_blue()]
        mat_blue_[np.isnan(mat_blue_)]=0
        mat_blue = copy.deepcopy(mat_blue_)
        vmin_blue = np.nanpercentile(mat_blue, input.min_max_vals_blue()[0])
        vmax_blue = np.nanpercentile(mat_blue, input.min_max_vals_blue()[1])
        mat_blue[mat_blue<vmin_blue]=0
        mat_blue[mat_blue>=vmax_blue]=vmax_blue
        mat_blue_norm = (mat_blue/np.max(mat_blue))*255
        rgb = np.stack([mat_red_norm, mat_green_norm, mat_blue_norm], axis=-1)
        x_extent = np.linspace(0, input.pixel_size()*rgb.shape[1]*asp_ratio, rgb.shape[1])
        y_extent = np.linspace(0, input.pixel_size()*rgb.shape[0], rgb.shape[0])

        fig = px.imshow(rgb, x=x_extent, y=y_extent, labels={"x": "μm", "y": "μm"})

        w = go.FigureWidget(fig.data, fig.layout)
        return w              

        # img_main = rbg
        # size = 150  # Size of the triangle image
        # img_triangle = np.zeros((size, size, 3), dtype=np.uint8)

        # p_red = np.array([size//2, 0])
        # p_green = np.array([0, size-1])
        # p_blue = np.array([size-1, size-1])

        # for y in range(size):
        #     for x in range(size):
        #         v0 = p_green - p_red
        #         v1 = p_blue - p_red
        #         v2 = np.array([x, y]) - p_red

        #         d00 = np.dot(v0, v0)
        #         d01 = np.dot(v0, v1)
        #         d11 = np.dot(v1, v1)
        #         d20 = np.dot(v2, v0)
        #         d21 = np.dot(v2, v1)

        #         denom = d00 * d11 - d01 * d01
        #         if denom == 0:
        #             continue

        #         v = (d11 * d20 - d01 * d21) / denom
        #         w = (d00 * d21 - d01 * d20) / denom
        #         u = 1 - v - w

        #         if 0 <= u <= 1 and 0 <= v <= 1 and 0 <= w <= 1:
        #             img_triangle[y, x] = (u * 255, v * 255, w * 255)

        # # Step 2: Resize triangle to match img_main height     

        # img_main_h = img_main.shape[0]
        # img_main_w = img_main.shape[1]
        # triangle_resized = np.array(
        #     Image.fromarray(img_triangle.astype(np.uint8)).resize(
        #         (size, img_main.shape[0] * size // img_triangle.shape[0])
        #     )
        # )

        # main_scaled = np.array(
        #     Image.fromarray(img_main.astype(np.uint8)).resize(
        #         (img_main.shape[1] * size // img_main.shape[0], triangle_resized.shape[0])
        #     )
        # )
        # # Step 4: Combine side by side
        # combined = np.concatenate((main_scaled, triangle_resized), axis=1)

        # # Step 5: Show using Plotly
        # fig = px.imshow(combined)
        # fig.update_layout(
        #     title="Image with RGB Triangle Legend",
        #     coloraxis_showscale=False,
        #     xaxis=dict(showticklabels=False),
        #     yaxis=dict(showticklabels=False)
        # )


        # fig = px.imshow(rgb)
        # legend_colors = {
        #     input.element_red(): 'rgb(255,0,0)',
        #     input.element_green(): 'rgb(0,255,0)',
        #     input.element_blue(): 'rgb(0,0,255)'
        # }

        # # Coordinates for the legend boxes
        # x_start = np.shape(mat_red)[1] + 2
        # y_start = 0

        # for i, (label, color) in enumerate(legend_colors.items()):
        #     fig.add_shape(
        #         type="rect",
        #         x0=x_start, x1=x_start + 10,
        #         y0=y_start + i*(0.10*np.shape(mat_red)[0]), y1=y_start + i*(0.10*np.shape(mat_red)[0]) + 10,
        #         fillcolor=color,
        #         line=dict(width=1, color='black')
        #     )
        #     fig.add_annotation(
        #         x=x_start + 12,
        #         y=y_start + i*(0.10*np.shape(mat_red)[0]) + 5,
        #         text=label,
        #         showarrow=False,
        #         font=dict(size=14),
        #         xanchor='left',
        #         yanchor='middle'
        #     )

        # fig.update_layout(plot_bgcolor="white")

        # Adjust axis limits to fit legend
        # fig.update_layout(
        #     width=600,
        #     height=300,
        #     margin=dict(l=20, r=150),
        #     xaxis=dict(range=[-0.5, 6]),
        #     yaxis=dict(scaleanchor="x", range=[1.5, -0.5])  # to match image orientation
        # )

        

    @render_widget
    def rgb_legend():
        size=350
        img = np.zeros((size, size, 3), dtype=np.float32)*255

        # Apexes of the triangle in (x, y)
        p_red = np.array([size // 2, 0], dtype=np.float32)
        p_green = np.array([0, size - 1], dtype=np.float32)
        p_blue = np.array([size - 1, size - 1], dtype=np.float32)

        # Meshgrid of pixel coordinates
        X, Y = np.meshgrid(np.arange(size), np.arange(size))
        P = np.stack((X, Y), axis=-1).astype(np.float32)

        # Triangle edges
        v0 = p_green - p_red
        v1 = p_blue - p_red

        d00 = np.dot(v0, v0)
        d01 = np.dot(v0, v1)
        d11 = np.dot(v1, v1)
        denom = d00 * d11 - d01 * d01

        v2 = P - p_red  # shape (H, W, 2)
        d20 = v2[..., 0] * v0[0] + v2[..., 1] * v0[1]
        d21 = v2[..., 0] * v1[0] + v2[..., 1] * v1[1]

        v = (d11 * d20 - d01 * d21) / denom
        w = (d00 * d21 - d01 * d20) / denom
        u = 1.0 - v - w

        # Mask inside triangle
        mask = (u >= 0) & (v >= 0) & (w >= 0)

        # Assign RGB values
        img[mask, 0] = u[mask] * 255  # R
        img[mask, 1] = v[mask] * 255  # G
        img[mask, 2] = w[mask] * 255  # B

        # Convert to uint8 for display
        img_uint8 = img.astype(np.uint8)

        # Plot
        fig = px.imshow(img_uint8)
        fig.update_layout(
            width=350,
            height=350,
            plot_bgcolor="white",
            margin=dict(l=0, r=0, t=0, b=0),
            coloraxis_showscale=False,
            xaxis=dict(showticklabels=False, showgrid=False),
            yaxis=dict(showticklabels=False, showgrid=False, scaleanchor="x")
        )

        # Add labels
        fig.add_annotation(x=p_red[0], y=p_red[1], text=input.element_red(), showarrow=False,
                        font=dict(size=14, color="red"), yanchor="bottom", xanchor="center")
        fig.add_annotation(x=p_green[0], y=p_green[1], text=input.element_green(), showarrow=False,
                        font=dict(size=14, color="green"), yanchor="bottom", xanchor="right")
        fig.add_annotation(x=p_blue[0], y=p_blue[1], text=input.element_blue(), showarrow=False,
                        font=dict(size=14, color="blue"), yanchor="bottom", xanchor="left")

        return fig






        
        # vmin_red = np.nanpercentile(rgb[:,:,0], input.min_max_vals_red()[0])
        # vmax_red = np.nanpercentile(rgb[:,:,0], input.min_max_vals_red()[1])
        # # img1 = channelnorm(rgb, 0, vmin_red, vmax_red)
        # vmin_green = np.nanpercentile(rgb[:,:,1], input.min_max_vals_green()[0])
        # vmax_green = np.nanpercentile(rgb[:,:,1], input.min_max_vals_green()[1])
        # # img2 = channelnorm(img1, 1, vmin_green, vmax_green)
        # vmin_blue = np.nanpercentile(rgb[:,:,2], input.min_max_vals_blue()[0])
        # vmax_blue = np.nanpercentile(rgb[:,:,2], input.min_max_vals_blue()[1])
        # # img3 = channelnorm(img2, 2, vmin_blue, vmax_blue)


        # ax = plt.axes()
        # ax.set_facecolor("black")
        # plt.imshow(img3, extent=[0, np.shape(img3)[1]*input.pixel_size()*asp_ratio, 0, np.shape(img3)[0]*input.pixel_size()], interpolation='none')
        # plt.grid(False)
        # plt.xlabel("μm")
        # plt.ylabel("μm")
        # # plt.title("Red: {}  Green: {}  Blue: {}".format(input.element_red(), input.element_green(), input.element_blue()))
        # # Add a legend for the RGB components
        # legend_elements = [
        #     Patch(facecolor='red', edgecolor='none', label=f"{input.element_red()}_{input.masked_map_red()}"),
        #     Patch(facecolor='green', edgecolor='none', label=f"{input.element_green()}_{input.masked_map_green()}"),
        #     Patch(facecolor='blue', edgecolor='none', label=f"{input.element_blue()}_{input.masked_map_blue()}")]
        # ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.02, 1.0), fontsize=8, frameon=True)
        # plt.tight_layout()
        

    # @render.plot
    # def plot_rgb():
    #     asp_ratio = calc_asp_ratio()
    #     if input.masked_map_red() == "All":
    #         if input.use_cor_mats() == True:
    #             mats_red = ycf_cor_mats
    #         else:
    #             mats_red = global_mats
    #     else:
    #         if input.use_cor_mats() == True:
    #             mats_red = ycf_cor_masked_mats[input.masked_map_red()]
    #         else:
    #             mats_red = global_masked_mats[input.masked_map_red()]
    #     mat_red = mats_red[input.element_red()]
    #     if input.masked_map_green() == "All":
    #         if input.use_cor_mats() == True:
    #             mats_green = ycf_cor_mats
    #         else:
    #             mats_green = global_mats
    #     else:
    #         if input.use_cor_mats() == True:
    #             mats_green = ycf_cor_masked_mats[input.masked_map_green()]
    #         else:
    #             mats_green = global_masked_mats[input.masked_map_green()]
    #     mat_green = mats_green[input.element_green()]
    #     if input.masked_map_blue() == "All":
    #         if input.use_cor_mats() == True:
    #             mats_blue = ycf_cor_mats
    #         else:
    #             mats_blue = global_mats
    #     else:
    #         if input.use_cor_mats() == True:
    #             mats_blue = ycf_cor_masked_mats[input.masked_map_blue()]
    #         else:
    #             mats_blue = global_masked_mats[input.masked_map_blue()]
    #     mat_blue = mats_blue[input.element_blue()]
    #     rgb = np.dstack((mat_red, mat_green, mat_blue))
    #     vmin_red = np.nanpercentile(rgb[:,:,0], input.min_max_vals_red()[0])
    #     vmax_red = np.nanpercentile(rgb[:,:,0], input.min_max_vals_red()[1])
    #     img1 = channelnorm(rgb, 0, vmin_red, vmax_red)
    #     vmin_green = np.nanpercentile(rgb[:,:,1], input.min_max_vals_green()[0])
    #     vmax_green = np.nanpercentile(rgb[:,:,1], input.min_max_vals_green()[1])
    #     img2 = channelnorm(img1, 1, vmin_green, vmax_green)
    #     vmin_blue = np.nanpercentile(rgb[:,:,2], input.min_max_vals_blue()[0])
    #     vmax_blue = np.nanpercentile(rgb[:,:,2], input.min_max_vals_blue()[1])
    #     img3 = channelnorm(img2, 2, vmin_blue, vmax_blue)
    #     ax = plt.axes()
    #     ax.set_facecolor("black")
    #     plt.imshow(img3, extent=[0, np.shape(img3)[1]*input.pixel_size()*asp_ratio, 0, np.shape(img3)[0]*input.pixel_size()], interpolation='none')
    #     plt.grid(False)
    #     plt.xlabel("μm")
    #     plt.ylabel("μm")
    #     # plt.title("Red: {}  Green: {}  Blue: {}".format(input.element_red(), input.element_green(), input.element_blue()))
    #     # Add a legend for the RGB components
    #     legend_elements = [
    #         Patch(facecolor='red', edgecolor='none', label=f"{input.element_red()}_{input.masked_map_red()}"),
    #         Patch(facecolor='green', edgecolor='none', label=f"{input.element_green()}_{input.masked_map_green()}"),
    #         Patch(facecolor='blue', edgecolor='none', label=f"{input.element_blue()}_{input.masked_map_blue()}")]
    #     ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.02, 1.0), fontsize=8, frameon=True)
    #     plt.tight_layout()

    # @render.text    
    # @reactive.event(input.save_fig_rgb)
    # def save_figure_rgb():
    #     asp_ratio = calc_asp_ratio()
    #     if input.masked_map_red() == "All":
    #         if input.use_cor_mats() == True:
    #             mats_red = ycf_cor_mats
    #         else:
    #             mats_red = global_mats
    #     else:
    #         if input.use_cor_mats() == True:
    #             mats_red = ycf_cor_masked_mats[input.masked_map_red()]
    #         else:
    #             mats_red = global_masked_mats[input.masked_map_red()]
    #     mat_red = mats_red[input.element_red()]
    #     if input.masked_map_green() == "All":
    #         if input.use_cor_mats() == True:
    #             mats_green = ycf_cor_mats
    #         else:
    #             mats_green = global_mats
    #     else:
    #         if input.use_cor_mats() == True:
    #             mats_green = ycf_cor_masked_mats[input.masked_map_green()]
    #         else:
    #             mats_green = global_masked_mats[input.masked_map_green()]
    #     mat_green = mats_green[input.element_green()]
    #     if input.masked_map_blue() == "All":
    #         if input.use_cor_mats() == True:
    #             mats_blue = ycf_cor_mats
    #         else:
    #             mats_blue = global_mats
    #     else:
    #         if input.use_cor_mats() == True:
    #             mats_blue = ycf_cor_masked_mats[input.masked_map_blue()]
    #         else:
    #             mats_blue = global_masked_mats[input.masked_map_blue()]
    #     mat_blue = mats_blue[input.element_blue()]
    #     rgb = np.dstack((mat_red, mat_green, mat_blue))
    #     vmin_red = np.nanpercentile(rgb[:,:,0], input.min_max_vals_red()[0])
    #     vmax_red = np.nanpercentile(rgb[:,:,0], input.min_max_vals_red()[1])
    #     img1 = channelnorm(rgb, 0, vmin_red, vmax_red)
    #     vmin_green = np.nanpercentile(rgb[:,:,1], input.min_max_vals_green()[0])
    #     vmax_green = np.nanpercentile(rgb[:,:,1], input.min_max_vals_green()[1])
    #     img2 = channelnorm(img1, 1, vmin_green, vmax_green)
    #     vmin_blue = np.nanpercentile(rgb[:,:,2], input.min_max_vals_blue()[0])
    #     vmax_blue = np.nanpercentile(rgb[:,:,2], input.min_max_vals_blue()[1])
    #     img3 = channelnorm(img2, 2, vmin_blue, vmax_blue)
    #     ax = plt.axes()
    #     ax.set_facecolor("black")
    #     plt.imshow(img3, extent=[0, np.shape(img3)[1]*input.pixel_size()*asp_ratio, 0, np.shape(img3)[0]*input.pixel_size()], interpolation='none')
    #     plt.grid(False)
    #     plt.xlabel("μm")
    #     plt.ylabel("μm")
    #     # plt.title("Red: {}  Green: {}  Blue: {}".format(input.element_red(), input.element_green(), input.element_blue()))
    #     # Add a legend for the RGB components
    #     legend_elements = [
    #         Patch(facecolor='red', edgecolor='none', label=f"{input.element_red()}_{input.masked_map_red()}"),
    #         Patch(facecolor='green', edgecolor='none', label=f"{input.element_green()}_{input.masked_map_green()}"),
    #         Patch(facecolor='blue', edgecolor='none', label=f"{input.element_blue()}_{input.masked_map_blue()}")]
    #     ax.legend(handles=legend_elements, loc='upper left',  bbox_to_anchor=(1.02, 1.0), fontsize=8, frameon=True)
    #     plt.tight_layout()
    #     plt.savefig("{}/{}_{}_{}.png".format(global_data_path, input.element_red(), input.element_green(), input.element_blue()), dpi=300)
    #     return "Your {}_{}_{} rgb image has been saved.".format(input.element_red(), input.element_green(), input.element_blue())


    

    @render.text
    def plot_multi():
        return "Select the elements you want to plot and other plot parameters. Then click the 'Display Plot' button, and the multi-element plot will open in a new window."     

    @render.image
    @reactive.event(input.disp_multi_plot)
    def plot_multi_disp():
        asp_ratio = calc_asp_ratio()
        if input.masked_map_multi() == "All":
            if input.use_cor_mats():
                mats = ycf_cor_mats
            else:
                mats = global_mats
        else:
            if input.use_cor_mats():
                mats = ycf_cor_masked_mats[input.masked_map_multi()]
            else:
                mats = global_masked_mats[input.masked_map_multi()]
        elements_2_plot = list(input.elements())
        pixel_size = input.pixel_size()
        plots_per_row = input.plots_per_row()
        fig_size = (input.fig_width(), input.fig_height())
        c_map = input.cmap_multi()
        use_log = input.use_log_multi()
        mats_2_plot = {element: mats[element] for element in elements_2_plot}

        # Calculate the number of rows and columns
        n_rows = math.ceil(len(elements_2_plot) / plots_per_row)
        n_cols = min(len(elements_2_plot), plots_per_row)

        fig, axs = plt.subplots(n_rows, n_cols, figsize=fig_size)
        axs = np.atleast_2d(axs)  # Ensure axs is always a 2D array
        # print(f"Figure size: {fig.get_size_inches()}")
        # print(f"Number of subplots: {len(axs)}")

        # plt.close()

        for idx, elem in enumerate(elements_2_plot):
            i, j = divmod(idx, plots_per_row)
            matrix = mats_2_plot[elem]
            vmin_ = np.nanpercentile(matrix, input.min_val_multi())
            vmax_ = np.nanpercentile(matrix, input.max_val_multi())
            ax = axs[i][j]
            if use_log:
                im = ax.imshow(matrix, cmap=c_map, norm=colors.SymLogNorm(linthresh=0.1, vmin=vmin_, vmax=vmax_),
                            extent=[0, np.shape(matrix)[1] * pixel_size * asp_ratio, 0, np.shape(matrix)[0] * pixel_size],
                            interpolation='none')
            else:
                im = ax.imshow(matrix, cmap=c_map, vmin=vmin_, vmax=vmax_,
                            extent=[0, np.shape(matrix)[1] * pixel_size * asp_ratio, 0, np.shape(matrix)[0] * pixel_size],
                            interpolation='none')
            divider = make_axes_locatable(ax)
            cax = divider.append_axes('right', size='5%', pad=0.01)
            cbar = fig.colorbar(im, cax=cax)
            # cbar.set_label(label='ppm', rotation=90, labelpad=0.1, fontsize=4)
            cbar.ax.tick_params(width=0, labelsize=4, pad=1) 
            ax.set_title(elem, size=4, pad=0.05)
            ax.set_xlabel("μm", size=4, labelpad=0.01)
            ax.set_ylabel("μm", size=4, labelpad=0.01)
            ax.xaxis.set_tick_params(width=0.1, labelsize=4, pad=1)
            ax.yaxis.set_tick_params(width=0.1, labelsize=4, pad=1)
            ax.set_facecolor("black")
            ax.grid(False)
        print(f"Number of subplots: {len(axs)}")

        # Hide unused subplots
        for idx in range(len(elements_2_plot), n_rows * n_cols):
            i, j = divmod(idx, plots_per_row)
            axs[i][j].axis('off')

        plt.tight_layout()
        plt.savefig(f"{global_data_path}_multiplot.png", dpi=300)
        plt.close()

        img: ImgData = {"src": f"{global_data_path}_multiplot.png"}
        return img

        # img = io.imread(f"{global_data_path}_multiplot.png")
        # fig = px.imshow(img)
        # fig.update_layout(showlegend=False, xaxis=dict(visible=False), yaxis=dict(visible=False))
        # w = go.FigureWidget(fig.data, fig.layout)
        # return w

        # fig = go.Figure()
        # fig.add_layout_image(dict(source=f"{global_data_path}_multiplot.png"))
        # fig.show()

        
        # img = plt.imread(f"{global_data_path}_multiplot.png")
        # return img
        # plt.show()
        # return fig
    
    
    
    
    # @render.plot
    # @reactive.event(input.disp_multi_plot)
    # def plot_multi_disp():
    #     asp_ratio = calc_asp_ratio()
    #     if input.masked_map_multi() == "All":
    #         if input.use_cor_mats() == True:
    #             mats = ycf_cor_mats
    #         else:
    #             mats = global_mats
    #     else:
    #         if input.use_cor_mats() == True:
    #             mats = ycf_cor_masked_mats[input.masked_map_multi()]
    #         else:
    #             mats = global_masked_mats[input.masked_map_multi()]
    #     elements_2_plot = list(input.elements())
    #     pixel_size = input.pixel_size()
    #     plots_per_row = input.plots_per_row()
    #     fig_size = (input.fig_width(), input.fig_height())
    #     c_map = input.cmap_multi()
    #     use_log = input.use_log_multi()
    #     mats_2_plot = {}
    #     for element in elements_2_plot:
    #         mats_2_plot[element] = mats[element]
    #     i, j = 0, 0
    #     plt.rc('xtick', labelsize=8)
    #     plt.rc('ytick', labelsize=8)
    #     if len(elements_2_plot) <= plots_per_row:
    #         fig, axs = plt.subplots(1, len(elements_2_plot), figsize=fig_size, squeeze=False)
    #     else:
    #         fig, axs = plt.subplots(math.ceil(len(elements_2_plot) / plots_per_row), plots_per_row, figsize=fig_size)
    #     axs = np.atleast_2d(axs)  # Ensure axs is always a 2D array
    #     for elem in elements_2_plot:
    #         matrix = mats_2_plot[elem]
    #         vmin_ = np.nanpercentile(matrix, input.min_val_multi())
    #         vmax_ = np.nanpercentile(matrix, input.max_val_multi())
    #         if use_log:
    #             im = axs[i][j].imshow(matrix, cmap=c_map, norm=colors.SymLogNorm(linthresh=0.001, vmin=vmin_, vmax=vmax_), extent=[0, np.shape(matrix)[1] * pixel_size * asp_ratio, 0, np.shape(matrix)[0] * pixel_size], interpolation='none')
    #         else:
    #             im = axs[i][j].imshow(matrix, cmap=c_map, vmin=vmin_, vmax=vmax_, extent=[0, np.shape(matrix)[1] * pixel_size * asp_ratio, 0, np.shape(matrix)[0] * pixel_size], interpolation='none')
    #         divider = make_axes_locatable(axs[i][j])
    #         cax = divider.append_axes('right', size='5%', pad=0.01)
    #         axs[i][j].set_facecolor("black")
    #         fig.colorbar(im, cax=cax).set_label(label='ppm', rotation=90, size=8, labelpad=0.01)
    #         axs[i][j].set_title(elem, size="small", pad=0.05)
    #         axs[i][j].set_xlabel("μm", size="small", labelpad=0.01)
    #         axs[i][j].set_ylabel("μm", size="small", labelpad=0.01)
    #         axs[i][j].grid(False)
    #         j += 1
    #         if j % plots_per_row == 0:
    #             i += 1
    #             j = 0
    #     plt.tight_layout()
    #     plt.show()
    #     return fig
        # plt.savefig("{}/multi_map_figure.png".format(global_data_path), dpi=300)
        # img: ImgData = {"src": "{}/multi_map_figure.png".format(global_data_path), "width": "800px"} 
        # return img     


    
    
    
    @render.table
    @reactive.event(input.make_roi_table)
    def roi_table():
        selected_coords, selected_regions, selected_data = get_roi_data()  

        # Convert the selected regions to a DataFrame for display in a table
        if selected_regions:
            new_df = pd.DataFrame(selected_regions)
            new_data_df = pd.DataFrame(selected_data)
            # Define the file path
            file_path = "{}/roi_means.txt".format(global_data_path)
            file_path_data = "{}/roi_data.txt".format(global_data_path)
            if os.path.exists(file_path):
                previous_df = pd.read_csv(file_path, sep="\t")
                comb_df = pd.concat([previous_df, new_df])
                comb_df.to_csv(file_path, sep="\t", index=False)
                previous_data_df = pd.read_csv(file_path_data, sep="\t")
                comb_data_df = pd.concat([previous_data_df, new_data_df])
                comb_data_df.to_csv(file_path_data, sep="\t", index=False)
                return comb_df
            else:
                new_df.to_csv(file_path, sep="\t", index=False)
                new_data_df.to_csv(file_path_data, sep="\t", index=False)
                return new_df

        else:
            return pd.DataFrame({"Message": ["No regions selected"]})

    @render.plot
    @reactive.event(input.plot_rois)
    def plot_roi():
        df = pd.read_csv("{}/roi_means.txt".format(global_data_path), sep="\t")
        if input.masked_map_roi() == "All":
            if input.use_cor_mats() == True:
                mats_roi = ycf_cor_mats
            else:
                mats_roi = global_mats
        else:
            if input.use_cor_mats() == True:
                mats_roi = ycf_cor_masked_mats[input.masked_map_roi()]
            else:
                mats_roi = global_masked_mats[input.masked_map_roi()]
        asp_ratio = calc_asp_ratio()
        pixel_size = input.pixel_size()
        data = mats_roi[input.element_roi()]
        fig, ax = plt.subplots()
        ax.set_facecolor("black")
        vmin_ = np.nanpercentile(data, 1)
        vmax_ = np.nanpercentile(data, 99)
        ax.imshow(data, norm=colors.SymLogNorm(linthresh=0.001, vmin=vmin_, vmax=vmax_), cmap='parula', interpolation='none')
        plt.grid(False)
        plt.title(input.element_roi())
        plt.xticks([])
        plt.yticks([])
        for i in range(len(df)):
            if df["region_type"][i] == "Polygon":
                # Parse the coordinates for the polygon
                coords_rois = ast.literal_eval(df['coords'][i])
                coords_rois = [(coord[1], coord[0]) for coord in coords_rois]
                # Create the polygon
                polygon = plt.Polygon(
                    np.array(coords_rois), edgecolor='red', facecolor='none', lw=1)
                ax.add_patch(polygon)
                # Add text to the polygon
                text_x, text_y = coords_rois[0]
                ax.text(
                    text_x, text_y, f"ROI{i+1}", color='white', fontsize=8, ha='left', va='bottom',
                    bbox=dict(facecolor='black', alpha=0.5, edgecolor='none', pad=1))
            # Parse the coordinates for the rectangle
            elif df["region_type"][i] == "Rectangle":
                coords_rois = ast.literal_eval(df['coords'][i])
                coords_rois = [float(x) for x in coords_rois]
                # Create the rectangle
                rect = plt.Rectangle(
                    (coords_rois[2], coords_rois[0]),
                    (coords_rois[3]) - (coords_rois[2]),
                    (coords_rois[1]) - (coords_rois[0]),
                    edgecolor='red', facecolor='none', lw=1)
                ax.add_patch(rect)
                # Add text to the rectangle
                text_x = coords_rois[2]  # X-coordinate for the text
                text_y = coords_rois[0]  # Y-coordinate for the text
                ax.text(
                    text_x, text_y, f"ROI{i+1}", color='white', fontsize=8, ha='left', va='bottom',
                    bbox=dict(facecolor='black', alpha=0.5, edgecolor='none', pad=1))
        return fig 
    
    @render.plot
    @reactive.event(input.show_roi_means)
    def plot_roi_means():
        df = global_roi_avgs_df
        # df = pd.read_csv("{}/roi_means.txt".format(global_data_path), sep="\t")
        # df = pq.read_pandas("{}/roi_means.parquet".format(global_data_path)).to_pandas()
        plt.errorbar(np.linspace(0, len(df)-1, len(df)), df[input.element_plotly()], yerr=df[f"{input.element_plotly()}_1sd"], 
                     fmt='o', color='blue', markersize=5, capsize=5)
        plt.xlabel("ROI")
        plt.xticks(np.arange(0, len(df), 1))
        plt.grid(False)
        plt.ylabel(f"{input.element_plotly()}")

    @render.text
    @reactive.event(input.roi_to_globals)
    def roi_to_globals_text():
        roi_dict, roi_list = make_roi_dict()
        return f"{roi_list} were added to the global ROI dictionary for use in other processes."

    
    
    
    @render.text
    def line_intro():
        if input.masked_map_line() == "All":
            mats1 = global_mats
        else:
            mats1 = global_masked_mats[input.masked_map_line()]
        mat_names = mats1.keys()
        return "Select the map on which you want to draw the lines above. " \
        "Then click the 'Draw line on map' button. A new window will open with a map. Draw a line on the map " \
        "by clicking at the start of the line, then double clicking at the end of the line, and clicking on the start of the line again. " \
        "Close the window. The line profile will be displayed in the table below. Repeat to add more lines." \
        
    @render.table
    @reactive.event(input.make_line_table)
    def line_table():
        selected_line_coords, selected_line_regions, total_distance = get_line_data()

        if selected_line_regions:
            # Convert the selected regions to a DataFrame for display in a table
            coords = selected_line_coords[0]
            lines_df = pd.DataFrame(selected_line_regions)
            trav_dist = np.linspace(0, total_distance, len(coords))
            lines_df['trav_dist'] = pd.Series([trav_dist.tolist()] * len(lines_df))
            file_path = "{}/line_data.txt".format(global_data_path)
            # Append to the existing Excel file
            if os.path.exists(file_path):
                previous_lines_df = pd.read_csv(file_path, sep="\t")
                comb_lines_df = pd.concat([previous_lines_df, lines_df])
                comb_lines_df.to_csv(file_path, sep="\t", index=False)
                return comb_lines_df
            else:
                lines_df.to_csv(file_path, sep="\t", index=False)
                return lines_df
        else:
            return pd.DataFrame({"Message": ["No line selected"]})




    @render.plot
    @reactive.event(input.plot_line_map)
    def plot_lines():
    # Load the line data
        df = pd.read_csv("{}/line_data.txt".format(global_data_path), sep="\t")
        if input.masked_map_roi() == "All":
            if input.use_cor_mats() == True:
                mats_roi = ycf_cor_mats
            else:
                mats_roi = global_mats
        else:
            if input.use_cor_mats() == True:
                mats_roi = ycf_cor_masked_mats[input.masked_map_line()]
            else:
                mats_roi = global_masked_mats[input.masked_map_line()]
        asp_ratio = calc_asp_ratio()
        pixel_size = input.pixel_size()
        
        data = mats_roi[input.element_line()]
        fig, ax = plt.subplots(1,1)
        ax.set_facecolor("black")
        vmin_ = np.nanpercentile(data, 1)
        vmax_ = np.nanpercentile(data, 99)
        ax.imshow(data, norm=colors.SymLogNorm(linthresh=0.001, vmin=vmin_, vmax=vmax_), cmap='parula', interpolation='none') 
        ax.grid(False)
        ax.set_title(f"{input.element_line()}")
        ax.set_xticks([])
        ax.set_yticks([])

        for i in range(len(df)):
            coords = ast.literal_eval(df['coords'][i])
            line_start = coords[0]
            line_end = coords[-1]
            array = np.array([line_start, line_end]).T
            line_x = array[1]
            line_y = array[0]
            ax.plot(line_x, line_y, color='red', linewidth=2)
            # Add text to the line
            textx = line_start[1]
            texty = line_start[0]
            ax.text(
                textx, texty, f"{i+1}", color='white', fontsize=12, ha='left', va='center',
                bbox=dict(facecolor='black', alpha=0.5, edgecolor='none', pad=1))
        return fig


        
    
    @render.plot
    @reactive.event(input.plot_profiles)
    def plot_profs():
        # Load the line data
        df = pd.read_csv("{}/line_data.txt".format(global_data_path), sep="\t")
        
        if len(df) == 1:
            element_values = ast.literal_eval(df[input.element_line()][0].strip("'"))
            trav_dist = ast.literal_eval(df['trav_dist'][0])
            plt.plot(trav_dist, element_values, color='blue', linewidth=2)
            plt.xlabel("distance (μm)")
            plt.ylabel(f"{input.element_line()}")
            plt.title(f"Line1")
            plt.grid(True)
        
        else:
            fig, axs = plt.subplots(len(df), 1, figsize=(6, 6*len(df)))
            for i in range(len(df)):
                element_values = ast.literal_eval(df[input.element_line()][i].strip("'"))
                trav_dist = ast.literal_eval(df['trav_dist'][i])
                axs[i].plot(trav_dist, element_values, color='blue', linewidth=2)
                axs[i].set_xlabel("distance (μm)")
                axs[i].set_ylabel(f"{input.element_line()}")
                axs[i].set_title(f"Line{i+1}")
                axs[i].grid(True)
            # plt.tight_layout()
            fig.subplots_adjust(hspace=0.5)
            plt.show()
            return fig
        
    @render.text
    @reactive.event(input.lines_to_global)
    def lines_to_globals_text():
        line_dict, line_list = make_lines_dict()
        return f"{line_list} were added to the global Lines dictionary for use in other processes."

        
    @render.plot
    def Pb_Pb_plot():
        mats = global_mats

        age = input.Pb_age()
        mu_var = input.mu()        
        kappa_var = input.kappa()
        cps_206 = mats["CPS 206Pb"]  
        cps_207 = mats["CPS 207Pb"]
        cps_208 = mats["CPS 208Pb"]
        thresh = input.thresh_206cps()

        safe_cps_206 = np.where((cps_206 <= 0) | np.isnan(cps_206) | np.isinf(cps_206), np.nan, cps_206)
        
        # Recalculate r76 each time using the current threshold
        r76 = cps_207 / safe_cps_206
        r76[safe_cps_206 < thresh] = np.nan
        r76[np.isinf(r76)] = np.nan
        # Repeat for r86 if needed
        r86 = cps_208 / safe_cps_206
        r86[safe_cps_206 < thresh] = np.nan
        r86[np.isinf(r86)] = np.nan

        data_x = np.nanmedian(r76)
        data_x_err = 2*np.nanstd(r76)/np.sqrt(np.count_nonzero(np.isnan(r76)))
        data_y = np.nanmedian(r86)
        data_y_err = 2*np.nanstd(r86)/np.sqrt(np.count_nonzero(np.isnan(r86)))

        if input.show_rois_Pb() == True:
            if input.roi_selected_Pb() == "None yet":
                raise ValueError("No ROIs available.")
            roi_data_x = {}
            roi_data_y = {}
            print(input.roi_selected_Pb())
            for roi in input.roi_selected_Pb():
                roi_line = global_roi_avgs_df[global_roi_avgs_df["ROI"] == roi]
                roi_data_x[f"{roi}_mean"] = roi_line["CPS 207Pb"]/roi_line["CPS 206Pb"]
                roi_data_x[f"{roi}_err"] = (np.sqrt((roi_line["CPS 207Pb_1sd"]/roi_line["CPS 207Pb"])**2 + (roi_line["CPS 206Pb_1sd"]/roi_line["CPS 206Pb"])**2)*roi_data_x[f"{roi}_mean"])/np.sqrt(roi_line["N"])
                roi_data_y[f"{roi}_mean"] = roi_line["CPS 208Pb"]/roi_line["CPS 206Pb"]
                roi_data_y[f"{roi}_err"] = (np.sqrt((roi_line["CPS 208Pb_1sd"]/roi_line["CPS 208Pb"])**2 + (roi_line["CPS 206Pb_1sd"]/roi_line["CPS 206Pb"])**2)*roi_data_y[f"{roi}_mean"])/np.sqrt(roi_line["N"])
            # for i in range(len(input.roi_selected_Pb())):
            #     roi_mask = global_roi_dict[input.roi_selected_Pb()[i]]
            #     if "CPS 206Pb" not in roi_mask.keys():
            #         raise ValueError(f"Pb isotope cps data not imported.")
            #     else:

            #         cps_206_roi = roi_mask["CPS 206Pb"]
            #         cps_207_roi = roi_mask["CPS 207Pb"]
            #         cps_208_roi = roi_mask["CPS 208Pb"]
            #         thresh_roi = input.thresh_206cps()

            #         safe_cps_206_roi = np.where((cps_206_roi <= 0) | np.isnan(cps_206_roi) | np.isinf(cps_206_roi), np.nan, cps_206_roi)
            #         r76_roi = cps_207_roi / safe_cps_206_roi
            #         r76_roi[safe_cps_206_roi < thresh_roi] = np.nan
            #         r76_roi[np.isinf(r76_roi)] = np.nan
            #         # Repeat for r86 if needed
            #         r86_roi = cps_208_roi / safe_cps_206_roi
            #         r86_roi[safe_cps_206_roi < thresh_roi] = np.nan
            #         r86_roi[np.isinf(r86_roi)] = np.nan

            #         roi_data_x[f"ROI{i}_data_x"] = r76_roi
            #         roi_data_x[f"ROI{i}_data_x_mean"] = np.nanmean(r76_roi)
            #         # roi_data_x[f"ROI{i}_data_x_err"] = 2*np.nanstd(r76_roi)/np.sqrt(np.count_nonzero(np.isnan(r86_roi)))
            #         roi_data_y[f"ROI{i}_data_y"] = r86_roi
            #         roi_data_y[f"ROI{i}_data_y_mean"] = np.nanmean(r86_roi)
            #         # roi_data_y[f"ROI{i}_data_y_err"] = 2*np.nanstd(r86_roi)/np.sqrt(np.count_nonzero(np.isnan(r86_roi)))
            #         n_valid = np.count_nonzero(~np.isnan(r86_roi))
            #         if n_valid > 0:
            #             roi_data_x[f"ROI{i}_data_x_err"] = 2 * np.nanstd(r76_roi) / np.sqrt(n_valid)
            #             roi_data_y[f"ROI{i}_data_y_err"] = 2 * np.nanstd(r86_roi) / np.sqrt(n_valid)
            #         else:
            #             roi_data_x[f"ROI{i}_data_x_err"] = np.nan
            #             roi_data_y[f"ROI{i}_data_y_err"] = np.nan


        lambda_238 = 0.000155125
        lambda_235 = 0.00098485
        lambda_232 = 0.000049475

        mu_ac = 9.74
        mu_uc = 10.5
        mu_mnt = 9.0
        kappa = 3.82

        stg1_start_6_4 = 9.307
        stg1_start_7_4 = 10.29
        stg1_start_8_4 = 29.487

        stg2_start_6_4 = 11.152
        stg2_start_7_4 = 12.998
        stg2_start_8_4 = 31.230

        t1 = np.arange(3800,4600,100)
        t1_start = np.array([4570])
        t2a = np.arange(0,100, 25)
        t2b = np.arange(100,1000,50)
        t2c = np.arange(1000,3700,100)
        t2 = np.concatenate([t2a, t2b, t2c])
        t2_start = np.array([3700])
        t1_all = np.concatenate([t1, t1_start])
        t2_all = np.concatenate([t2a, t2b, t2c, t2_start])
        t_stg1 = t1_all
        t_stg2 = t2_all
        t = np.concatenate([t_stg1, t_stg2])
        t0_stg1 = np.ones(np.shape(t_stg1))*t1_start
        t0_stg2 = np.ones(np.shape(t_stg2))*t2_start
        t0 = np.concatenate([t0_stg1, t0_stg2])


        def calc_SK_curve(mu, k):        
            r640_stg1 = np.ones(np.shape(t0_stg1))*stg1_start_6_4
            r740_stg1 = np.ones(np.shape(t0_stg1))*stg1_start_7_4
            r840_stg1 = np.ones(np.shape(t0_stg1))*stg1_start_8_4
            r640_stg2 = np.ones(np.shape(t0_stg2))*stg2_start_6_4
            r740_stg2 = np.ones(np.shape(t0_stg2))*stg2_start_7_4
            r840_stg2 = np.ones(np.shape(t0_stg2))*stg2_start_8_4
            r640 = np.concatenate([r640_stg1, r640_stg2])
            r740 = np.concatenate([r740_stg1, r740_stg2])
            r840 = np.concatenate([r840_stg1, r840_stg2])

            mu_stg1 = np.ones(np.shape(t_stg1))*7.192
            mu_stg2 = np.ones(np.shape(t_stg2))*mu
            mu_array = np.concatenate([mu_stg1, mu_stg2])
            mu_35 = mu_array/137.818
            mu_32_stg1 = np.ones(np.shape(t_stg1))*33
            mu_32_stg2 = np.ones(np.shape(t_stg2))*mu*k
            mu_32 = np.concatenate([mu_32_stg1, mu_32_stg2])

            SK_curve_df = pd.DataFrame()
            SK_curve_df["time (Ma)"] = t
            # SK_curve_df["t0"] = t0
            # SK_curve_df["mu"] = mu_array
            # SK_curve_df["mu_35"] = mu_35
            # SK_curve_df["mu_32"] = mu_32
            SK_curve_df["206/204"] = r640 + mu_array*(np.exp(lambda_238*t0)-np.exp(lambda_238*t))
            SK_curve_df["207/204"] = r740 + mu_35*(np.exp(lambda_235*t0)-np.exp(lambda_235*t))
            SK_curve_df["208/204"] = r840 + mu_32*(np.exp(lambda_232*t0)-np.exp(lambda_232*t))
            SK_curve_df["207/206"] = SK_curve_df["207/204"]/SK_curve_df["206/204"]
            SK_curve_df["208/206"] = SK_curve_df["208/204"]/SK_curve_df["206/204"]
            SK_curve_df_sorted = SK_curve_df.sort_values(by="time (Ma)", ascending = False)
            return SK_curve_df_sorted

        SK_curve_ac = calc_SK_curve(mu=mu_ac, k=kappa)
        SK_curve_uc = calc_SK_curve(mu=mu_uc, k=kappa)
        SK_curve_mnt = calc_SK_curve(mu=mu_mnt, k=kappa)
        SK_curve_var = calc_SK_curve(mu=mu_var, k=kappa_var)
        isochron_7_6_3700 = SK_curve_var["207/206"][SK_curve_var["time (Ma)"] == 3700].values[0]
        isochron_8_6_3700 = SK_curve_var["208/206"][SK_curve_var["time (Ma)"] == 3700].values[0]
        isochron_6_4_age = stg2_start_6_4 + mu_var*(np.exp(lambda_238*t2_start)-np.exp(lambda_238*age))
        isochron_7_4_age = stg2_start_7_4 + mu_var/137.818*(np.exp(lambda_235*t2_start)-np.exp(lambda_235*age))
        isochron_8_4_age = stg2_start_8_4 + mu_var*kappa_var*(np.exp(lambda_232*t2_start)-np.exp(lambda_232*age))
        isochron_7_6_age = isochron_7_4_age/isochron_6_4_age
        isochron_8_6_age = isochron_8_4_age/isochron_6_4_age
        isochron_m = (isochron_8_6_3700 - isochron_8_6_age) / (isochron_7_6_3700 - isochron_7_6_age)
        isochron_c = isochron_8_6_age - isochron_7_6_age * isochron_m
        if (data_y - data_y_err) >= 1.8:
            isochron_8_6_pt3 = np.array([1.8])
        else:
            isochron_8_6_pt3 = np.array([(data_y - (3*data_y_err))])
        isochron_7_6_pt3 = (isochron_8_6_pt3 - isochron_c)/isochron_m
        isochron_xs = np.array([np.array([isochron_7_6_3700]), isochron_7_6_age, isochron_7_6_pt3])
        isochron_ys = np.array([np.array([isochron_8_6_3700]), isochron_8_6_age, isochron_8_6_pt3])

        fig,ax = plt.subplots()
        ax.plot(SK_curve_var["207/206"][SK_curve_var["time (Ma)"]<=3700], SK_curve_var["208/206"][SK_curve_var["time (Ma)"]<=3700], color="g", label=f"mu={mu_var}, kappa={kappa_var}")
        if input.show_mnt() == True:
            ax.plot(SK_curve_mnt["207/206"][SK_curve_mnt["time (Ma)"]<=3700], SK_curve_mnt["208/206"][SK_curve_mnt["time (Ma)"]<=3700], ls=":", label="SK75 Mantle", color="gray", lw=1)
        if input.show_ac() == True:
            ax.plot(SK_curve_ac["207/206"][SK_curve_ac["time (Ma)"]<=3700], SK_curve_ac["208/206"][SK_curve_ac["time (Ma)"]<=3700], ls="--", label="SK75 Avg Crust", color="k", lw=1)        
        if input.show_uc() == True:
            ax.plot(SK_curve_uc["207/206"][SK_curve_uc["time (Ma)"]<=3700], SK_curve_uc["208/206"][SK_curve_uc["time (Ma)"]<=3700], ls="-.", label="SK75 Upper Crust", color="gray", lw=1)
        
        
        if input.show_stage_1() == True:
            ax.plot(SK_curve_var["207/206"][SK_curve_var["time (Ma)"]>3700], SK_curve_var["208/206"][SK_curve_var["time (Ma)"]>3700], color="g", label=f"mu={mu_var}, kappa={kappa_var}")
            if input.show_mnt() == True:
                ax.plot(SK_curve_mnt["207/206"][SK_curve_mnt["time (Ma)"]>3700], SK_curve_mnt["208/206"][SK_curve_mnt["time (Ma)"]>3700], ls=":", label="SK75 Mantle", color="gray", lw=1)
            if input.show_uc() == True:
                ax.plot(SK_curve_uc["207/206"][SK_curve_uc["time (Ma)"]>3700], SK_curve_uc["208/206"][SK_curve_uc["time (Ma)"]>3700], ls="-.", label="SK75 Upper Crust", color="gray", lw=1)            
            ax.plot(SK_curve_ac["207/206"][SK_curve_ac["time (Ma)"]>3700], SK_curve_ac["208/206"][SK_curve_ac["time (Ma)"]>3700], ls="--", label="SK75 Avg Crust", color="k", lw=1)
            

        ax.plot(isochron_xs, isochron_ys, label=f"Isochron age = {age} Ma", marker="d", markersize= 10, color="b", ls="--", lw=1, markerfacecolor="none")
        if input.show_map_mean() == True:
            ax.errorbar(x=data_x, y=data_y, xerr=data_x_err, yerr=data_y_err, color="r", label="All Data")
        if input.show_error_ellipse() == True:
            confidence_ellipse(r76, r86, ax, n_std=input.n_std_Pb(), edgecolor='r', lw=2)
        if input.show_all_Pb() == True:
            ax.scatter(x=r76, y=r86, s=2, color="r", alpha=0.5)
        if input.show_rois_Pb() == True:
            for roi in input.roi_selected_Pb():
                eb1 = ax.errorbar(
                        x=roi_data_x[f"{roi}_mean"], y=roi_data_y[f"{roi}_mean"],
                        xerr=roi_data_x[f"{roi}_err"], yerr=roi_data_y[f"{roi}_err"],
                        label=f"{roi}")
                eb1[-1][0].set_linestyle('--')
                eb1[-1][0].set_linewidth(2)
                eb1[-1][1].set_linestyle('--')
                eb1[-1][1].set_linewidth(2)

                # mean_x_key = f"{roi}_data_x_mean"
                # mean_y_key = f"{roi}_data_y_mean"
                # err_x_key = f"{roi}_data_x_err"
                # err_y_key = f"{roi}_data_y_err"
                # data_x_key = f"{roi}_data_x"
                # data_y_key = f"{roi}_data_y"
                # # Only plot if all keys exist and are not nan
                # if (
                #     mean_x_key in roi_data_x and mean_y_key in roi_data_y and
                #     err_x_key in roi_data_x and err_y_key in roi_data_y and
                #     data_x_key in roi_data_x and data_y_key in roi_data_y and
                #     not np.isnan(roi_data_x[mean_x_key]) and not np.isnan(roi_data_y[mean_y_key])
                # ):
                #     ax.errorbar(
                #         x=roi_data_x[mean_x_key], y=roi_data_y[mean_y_key],
                #         xerr=roi_data_x[err_x_key], yerr=roi_data_y[err_y_key],
                #         marker="o", label=f"{roi}"
                #     )
                #     confidence_ellipse(
                #         roi_data_x[data_x_key], roi_data_y[data_y_key], ax, n_std=input.n_std_Pb(), lw=2
                #     )
                # else:
                #     print(f"Skipping {roi}: missing or invalid data.")
        ax.legend()
        if input.autoscale_Pb_plot() == False:
            ax.set_xlim(input.Pb_plot_xlims()[0], input.Pb_plot_xlims()[1])
            ax.set_ylim(input.Pb_plot_ylims()[0], input.Pb_plot_ylims()[1])
        ax.set_xlabel("207Pb/206Pb")
        ax.set_ylabel("208Pb/206Pb")

    

    @render.plot
    @reactive.event(input.make_graphs)
    def mats_graph_plot():
        def create_graph_from_mats(mats):
            # Create a graph
            G = nx.Graph()

            # Add nodes (elements) to the graph
            if input.choose_elems_graph() == True:
                elements_chosen = input.elems_graph()
                elements = []
                node_colors = []
                for e in elements_chosen:
                    if not np.issubdtype(mats[e].dtype, np.number):
                        print(f"Skipping non-numeric element: {e}")
                        continue
                    mean_value = np.nanmean(mats[e])
                    if mean_value >= input.min_conc():
                        elements.append(e)
                        node_colors.append(mean_value)
            else:
                elements_all = list(mats.keys())
                elements = []
                node_colors = []
                for e in elements_all:
                    if not np.issubdtype(mats[e].dtype, np.number):
                        print(f"Skipping non-numeric element: {e}")
                        continue
                    mean_value = np.nanmean(mats[e])
                    if mean_value >= input.min_conc():
                        elements.append(e)
                        node_colors.append(mean_value)

            G.add_nodes_from(elements)

            # Add edges based on correlation between matrices
            mats_2_plot = {}
            for element in elements:
                mats_2_plot[element] = np.nan_to_num(mats[element], nan=0)
            if input.corr_type() == "Pearson":
                correlations = []
                for i, elem1 in enumerate(elements):
                    if not np.issubdtype(mats_2_plot[elem1].dtype, np.number):
                        print(f"Skipping non-numeric element: {elem1}")
                        continue
                    for j, elem2 in enumerate(elements):
                        if i < j:  # Avoid duplicate edges
                            if not np.issubdtype(mats_2_plot[elem2].dtype, np.number):
                                print(f"Skipping non-numeric element: {elem2}")
                                continue
                            # Compute correlation between the two matrices
                            mat1 = mats_2_plot[elem1].flatten()
                            mat2 = mats_2_plot[elem2].flatten()
                            correlation = np.corrcoef(mat1, mat2)[0, 1]
                            correlations.append(correlation)
                            if correlation > input.corr_threshold():  # Adjust the threshold as needed
                                G.add_edge(elem1, elem2, weight=correlation)

            if input.corr_type() == "Spearman":
                correlations = []
                for i, elem1 in enumerate(elements):
                    for j, elem2 in enumerate(elements):
                        if i < j:
                            mat1 = mats_2_plot[elem1].flatten()
                            mat2 = mats_2_plot[elem2].flatten()
                            correlation = stats.spearmanr(mat1, mat2)[0]
                            correlations.append(correlation)
                            if correlation > input.corr_threshold():
                                G.add_edge(elem1, elem2, weight=correlation)

            return G, node_colors

        if input.minerals_graph() == "All":
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = global_mats
        else:
            if input.use_cor_mats() == True:
                mats = ycf_cor_masked_mats[input.minerals_graph()]
            else:
                mats = global_masked_mats[input.minerals_graph()]
        
        G, node_colors = create_graph_from_mats(mats)

        # Normalize node colors for visualization
        norm = colors.LogNorm(vmin=min(node_colors), vmax=max(node_colors))
        cmap = parula_map
        node_colors_mapped = [cmap(norm(value)) for value in node_colors]

        # Get edge weights for visualization
        edges, weights = zip(*nx.get_edge_attributes(G, 'weight').items())

        # Draw the graph
        pos = nx.spring_layout(G)  # Spring layout for better visualization
        fig, ax = plt.subplots(figsize=(30, 24))
        ax.set_facecolor("white")  # Set the background color to white
        fig.patch.set_facecolor("white")  # Set the figure background color to white 
        
        # Draw edges
        nx.draw_networkx_edges(
            G, pos, edge_color="k", width=weights, ax=ax)
        
        # Draw nodes with transparency
        nx.draw_networkx_nodes(
            G, pos, node_color=node_colors_mapped, node_size=500, alpha=0.8, ax=ax)


        # Draw labels with opaque text
        nx.draw_networkx_labels(
            G, pos, font_size=8, font_color="black", ax=ax)

        # Add a colorbar for the node colors
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])
        cbar = plt.colorbar(sm, ax=ax, pad=0.01)
        cbar.set_label("Mean Concentration (ppm)", rotation=90)
        # plt.title("Graph Representation of Mats Dictionary with Node Colors")
        plt.grid(False)
        plt.tight_layout()
        # plt.show()
        return fig
    

    @render.plot
    @reactive.event(input.make_corr_matrix)
    def plot_corr_matrix():
        global global_mats
        if input.minerals_corr_mat() == "All":
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = global_mats
        else:
            if input.minerals_corr_mat() not in global_masked_mats:
                raise ValueError(f"Mineral '{input.minerals_corr_mat()}' not found in masked matrices.")
            if input.use_cor_mats() == True:
                mats = ycf_cor_masked_mats[input.minerals_corr_mat()]
            else:
                mats = global_masked_mats[input.minerals_corr_mat()]

        elements_2_plot = list(input.corr_mat_els())
        mats_2_plot = {}
        for element in elements_2_plot:
            if element not in mats:
                raise ValueError(f"Element '{element}' not found in the selected mineral's masked matrices.")
            mats_2_plot[element] = np.nan_to_num(mats[element], nan=0)
        if elements_2_plot == []:
            raise ValueError("No elements selected for correlation matrix.")
        else:    
            i, j = 0, 0
            # fig_size = (len(elements_2_plot) * 1.5, len(elements_2_plot) * 1.5)
            fig, axs = plt.subplots(1, 1, figsize=(20,20))
            #axs.set_facecolor("black")
            corr_matrix = np.zeros((len(elements_2_plot), len(elements_2_plot)))
            for i, elem1 in enumerate(elements_2_plot):
                for j, elem2 in enumerate(elements_2_plot):
                    if i < j:
                        continue
                    mat1 = mats_2_plot[elem1].flatten()
                    mat2 = mats_2_plot[elem2].flatten()
                    # if input.mineral_corr_mat() != "All":
                    #     mat1 = mat1[mat1 != 0]
                    #     mat2 = mat2[mat2 != 0]
                    #     if mat1.shape != mat2.shape:
                    #         raise ValueError(f"Matrix shapes do not match for elements '{elem1}' and '{elem2}'.")
                        
                    if input.corr_type_matrix() == "Pearson":
                        corr_matrix[i][j] = (np.corrcoef(mat1, mat2)[0, 1])
                    if input.corr_type_matrix() == "Spearman":
                        corr_matrix[i][j] = (stats.spearmanr(mat1, mat2)[0])

            # Mirror the lower triangle to the upper triangle
            corr_matrix = corr_matrix + corr_matrix.T
            if input.cor_log() == True:
                im = axs.imshow(corr_matrix, cmap='seismic', norm=colors.SymLogNorm(linthresh = input.cor_linthresh(), vmin=-1, vmax=1), interpolation='none')
            else:
                im = axs.imshow(corr_matrix, cmap='seismic', interpolation='none')
                im.set_clim(vmin=-1, vmax=1)
            # im = axs.imshow(corr_matrix, cmap='inferno', interpolation='none')
            cbar = plt.colorbar(im, pad=0.01)
            cbar.set_label("Correlation Coefficient (R)", fontsize=12)
            # divider = make_axes_locatable(axs)
            # cax = divider.append_axes("top", size="5%", pad=0.5)  # Adjust size and pad as needed
            # cbar = fig.colorbar(im, cax=cax, orientation="horizontal")
            # cbar.set_label("Correlation Coefficient (R²)", fontsize=12)
            # cax.xaxis.set_ticks_position("top")  # Move ticks to the top
            plt.xticks(np.arange(len(elements_2_plot)), elements_2_plot, fontsize=6, rotation=90, ha='center')
            plt.yticks(np.arange(len(elements_2_plot)), elements_2_plot, fontsize=6)
            # plt.grid(False)
            # plt.show()
            return fig
    
    
    @render.plot
    def plot_hist():
        if input.class_type() == "None":
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = global_mats
        else:
            mats_, _, color_nums, mineral_colors, color_mapping, mineral_colors_mapped = data_loader_3()
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = mats_
        # if input.class_type() == "Compositional Classification":
        #     raise ValueError("No elements selected for Compositional classification.")
        #     # mats, _, mineral_colors, color_mapping, _ = data_loader_2()
        mat_ = mats[input.element_hist()]
        
        # Filter by selected mineral categories
        if "mineral_names" in mats:
            selected_minerals = input.mineral_hist()  # Get selected minerals
            if "All" not in selected_minerals:
                mineral_names = mats["mineral_names"]
                if mineral_names.ndim == 2:
                    # Flatten the mineral_names matrix if it's 2D
                    mineral_names = mineral_names.flatten()
                mineral_mask = np.isin(mineral_names, selected_minerals)
                
                # Assign unique colors to each mineral
                colors_list = ["C0", "indianred", "goldenrod", "darkseagreen", "plum", "palegreen", "blue", "orange", "purple", "red", "green", "yellow", "pink"]  # Use a colormap (e.g., tab10)
                mineral_colors = {mineral: colors_list[i % len(colors_list)] for i, mineral in enumerate(selected_minerals)}
                
                # Plot histogram for each mineral
                fig, ax = plt.subplots()
                x_min = np.nanpercentile(mat_, input.min_max_vals_x()[0])
                x_max = np.nanpercentile(mat_, input.min_max_vals_x()[1])
                for i, mineral in enumerate(selected_minerals):
                    mask = mineral_names == mineral
                    mat_mineral = mat_.flatten()[mask]
                    mat_mineral = mat_mineral[mat_mineral > 0]  # Remove zeros or negative values
                    if input.hist_type() == "KDE":
                        bw_adj_list = [name.strip() for name in input.bw_adj_multi().split(",")]
                        if len(bw_adj_list) == len(selected_minerals):
                            bw_adj = float(bw_adj_list[i])
                        elif len(selected_minerals) == 1:
                            bw_adj = input.bw_adj()
                        else: 
                            bw_adj = input.bw_adj()
                        sns.kdeplot(mat_mineral, ax=ax, bw_adjust=bw_adj, color=color_mapping[mineral], label=mineral, fill=True, alpha=0.5)
                    else:
                        ax.hist(mat_mineral, bins=input.num_bins(), color=color_mapping[mineral], alpha=0.7, label=mineral)
                
                # Add labels, legend, and grid
                plt.xlabel("{}".format(input.element_hist()))
                if input.hist_type() == "KDE":
                    plt.ylabel("Density")
                else:
                    plt.ylabel("Counts")
                plt.xlim((x_min, x_max))
                if input.use_log_hist() == True:
                    plt.xscale('log')
                plt.grid(False)
                plt.legend()
            else:
                mat_nan = copy.deepcopy(mat_)
                mat_nan[mat_nan<=0]=np.nan
                mat = mat_nan
                x_min = np.nanpercentile(mat_, input.min_max_vals_x()[0])
                x_max = np.nanpercentile(mat_, input.min_max_vals_x()[1])
                if input.hist_type() == "KDE":
                    sns.kdeplot(mat.flatten(), color='C0', bw_adjust=input.bw_adj(), fill=True, alpha=0.5)
                else:
                    plt.hist(mat.flatten(), bins=input.num_bins(), color='C0', alpha=0.7)
                plt.xlabel("{}".format(input.element_hist()))
                if input.hist_type() == "KDE":
                    plt.ylabel("Density")
                else:
                    plt.ylabel("Counts")
                plt.xlim((x_min, x_max))
                if input.use_log_hist() == True:
                    plt.xscale('log')
                # plt.title("Histogram of {}".format(input.element_hist()))
                plt.grid(False)

        else:
            mat_nan = copy.deepcopy(mat_)
            mat_nan[mat_nan<=0]=np.nan
            mat = mat_nan
            # vmin_ = np.nanpercentile(mat, input.min_val_hist())
            # vmax_ = np.nanpercentile(mat, input.max_val_hist())
            x_min = np.nanpercentile(mat_, input.min_max_vals_x()[0])
            x_max = np.nanpercentile(mat_, input.min_max_vals_x()[1])
            if input.hist_type() == "KDE":
                sns.kdeplot(mat.flatten(), bw_adjust=input.bw_adj(), color='C0', fill=True, alpha=0.5)
            else:
                plt.hist(mat.flatten(), bins=input.num_bins(), color='C0', alpha=0.7)
            plt.xlabel("{}".format(input.element_hist()))
            if input.hist_type() == "KDE":
                plt.ylabel("Density")
            else:
                plt.ylabel("Counts")
            plt.xlim((x_min, x_max))
            if input.use_log_hist() == True:
                plt.xscale('log')
            # plt.title("Histogram of {}".format(input.element_hist()))
            plt.grid(False)
            # plt.show()

    # @render_widget
    # def plot_bivariate():       

    #     if input.class_type() == "None":
    #         if input.use_cor_mats():
    #             mats = ycf_cor_mats
    #         else:
    #             mats = global_mats
    #     else:
    #         mats_, _, color_nums, mineral_colors, color_mapping, mineral_colors_mapped = data_loader_3()
    #         if input.use_cor_mats():
    #             mats = ycf_cor_mats
    #         else:
    #             mats = mats_

    #     # Ensure the selected elements exist in mats
    #     if input.element_xaxis() not in mats or input.element_yaxis() not in mats:
    #         raise ValueError("Selected elements for the x-axis or y-axis are not available in the data.")

    #     data_x = mats[input.element_xaxis()]
    #     data_y = mats[input.element_yaxis()]

    #     # Filter by selected mineral categories
    #     if "mineral_names" in mats:
    #         selected_minerals = input.mineral_bivariate()
    #         if "All" not in selected_minerals:
    #             mineral_names = mats["mineral_names"]
    #             if mineral_names.ndim == 2:
    #                 mineral_names = mineral_names.flatten()
    #             mineral_mask = np.isin(mineral_names, selected_minerals)
    #             data_x = data_x.flatten()[mineral_mask]
    #             data_y = data_y.flatten()[mineral_mask]

    #     # Calculate percentiles for x and y axes
    #     vmin_x = np.nanpercentile(data_x, input.min_max_vals_xaxis()[0]) * 0.9
    #     vmax_x = np.nanpercentile(data_x, input.min_max_vals_xaxis()[1]) * 1.1
    #     vmin_y = np.nanpercentile(data_y, input.min_max_vals_yaxis()[0]) * 0.9
    #     vmax_y = np.nanpercentile(data_y, input.min_max_vals_yaxis()[1]) * 1.1

    #     # Handle color map if enabled
    #     if input.color_map():
    #         mat_color = mats[input.c_map_bivariate()]
    #         if "mineral_names" in mats and "All" not in selected_minerals:
    #             mat_color = mat_color[mineral_mask]
    #         vmin_color = np.nanpercentile(mat_color, input.min_max_vals_color()[0])
    #         vmax_color = np.nanpercentile(mat_color, input.min_max_vals_color()[1])

    #         fig = go.Figure()
    #         fig.add_trace(go.Scatter(
    #             x=data_x,
    #             y=data_y,
    #             mode='markers',
    #             marker=dict(
    #                 color=mat_color,
    #                 colorscale='Inferno',
    #                 cmin=vmin_color,
    #                 cmax=vmax_color,
    #                 size=8,
    #                 showscale=True,
    #                 colorbar=dict(title=input.c_map_bivariate())
    #             )
    #         ))
    #     elif input.mineral_color():
    #         mineral_colors = np.vectorize(lambda x: color_mapping.get(x, "gray"))(mats["mineral_names"]).flatten()
    #         if "All" not in selected_minerals:
    #             mineral_colors = mineral_colors[mineral_mask]

    #         fig = go.Figure()
    #         fig.add_trace(go.Scatter(
    #             x=data_x,
    #             y=data_y,
    #             mode='markers',
    #             marker=dict(
    #                 color=mineral_colors,
    #                 size=8
    #             )
    #         ))
    #     else:
    #         fig = go.Figure()
    #         fig.add_trace(go.Scatter(
    #             x=data_x,
    #             y=data_y,
    #             mode='markers',
    #             marker=dict(
    #                 size=8
    #             )
    #         ))

    #     # Set axis properties
    #     fig.update_layout(
    #         xaxis=dict(
    #             title=input.element_xaxis(),
    #             type='log' if input.use_log_x_axis() else 'linear',
    #             range=[vmin_x, vmax_x]
    #         ),
    #         yaxis=dict(
    #             title=input.element_yaxis(),
    #             type='log' if input.use_log_y_axis() else 'linear',
    #             range=[vmin_y, vmax_y]
    #         ),
    #         title="Bivariate Plot",
    #         template="plotly_white"
    #     )

    #     return fig
        
    @render.plot  
    def plot_bivariate():
        if input.class_type() == "None":
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = global_mats
        else:
            mats_, _, color_nums, mineral_colors, color_mapping, mineral_colors_mapped = data_loader_3()
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = mats_

        # Ensure the selected elements exist in mats
        if input.element_xaxis() not in mats or input.element_yaxis() not in mats:
            raise ValueError("Selected elements for the x-axis or y-axis are not available in the data.")
        
        if input.use_rois() == True:
            if 'global_roi_dict' not in globals():
                raise ValueError("No ROIs selected. Please select ROIs to plot.")
            else:
                fig, ax = plt.subplots()
                all_data_x = []
                all_data_y = []
                for i in range(len(input.roi_selected())):
                    roi_mask = global_roi_dict[input.roi_selected()[i]]
                    data_x = roi_mask[input.element_xaxis()]
                    data_y = roi_mask[input.element_yaxis()]
                    ax.scatter(data_x, data_y, s=3, label=input.roi_selected()[i])
                    all_data_x.append(data_x.flatten())
                    all_data_y.append(data_y.flatten())
                all_data_x = np.concatenate(all_data_x)
                all_data_y = np.concatenate(all_data_y)
                vmin_x = np.nanpercentile(all_data_x, input.min_max_vals_xaxis()[0]) * 0.9
                vmax_x = np.nanpercentile(all_data_x, input.min_max_vals_xaxis()[1]) * 1.1
                vmin_y = np.nanpercentile(all_data_y, input.min_max_vals_yaxis()[0]) * 0.9
                vmax_y = np.nanpercentile(all_data_y, input.min_max_vals_yaxis()[1]) * 1.1
                ax.set_xlabel("{}".format(input.element_xaxis()))
                ax.set_ylabel("{}".format(input.element_yaxis()))
                ax.set_xlim(vmin_x, vmax_x)
                ax.set_ylim(vmin_y, vmax_y)
                if input.use_log_x_axis():
                    ax.set_xscale('symlog', linthresh=0.1)
                if input.use_log_y_axis():
                    ax.set_yscale('symlog', linthresh=0.1)
                ax.legend()
        
        elif input.use_lines() == True:
            if 'global_line_dict' not in globals():
                raise ValueError("No Lines selected. Please select Lines to plot.")
            else:
                fig, ax = plt.subplots()
                all_data_x = []
                all_data_y = []
                for i in range(len(input.line_selected())):
                    line_mask = global_line_dict[input.line_selected()[i]]
                    data_x = line_mask[input.element_xaxis()]
                    data_y = line_mask[input.element_yaxis()]
                    ax.scatter(data_x, data_y, s=3, label=input.line_selected()[i])
                    all_data_x.append(data_x.flatten())
                    all_data_y.append(data_y.flatten())
                all_data_x = np.concatenate(all_data_x)
                all_data_y = np.concatenate(all_data_y)
                vmin_x = np.nanpercentile(all_data_x, input.min_max_vals_xaxis()[0]) * 0.9
                vmax_x = np.nanpercentile(all_data_x, input.min_max_vals_xaxis()[1]) * 1.1
                vmin_y = np.nanpercentile(all_data_y, input.min_max_vals_yaxis()[0]) * 0.9
                vmax_y = np.nanpercentile(all_data_y, input.min_max_vals_yaxis()[1]) * 1.1
                ax.set_xlabel("{}".format(input.element_xaxis()))
                ax.set_ylabel("{}".format(input.element_yaxis()))
                ax.set_xlim(vmin_x, vmax_x)
                ax.set_ylim(vmin_y, vmax_y)
                if input.use_log_x_axis():
                    ax.set_xscale('symlog', linthresh=0.1)
                if input.use_log_y_axis():
                    ax.set_yscale('symlog', linthresh=0.1)
                ax.legend()

        
        else:
            data_x = mats[input.element_xaxis()]
            data_y = mats[input.element_yaxis()]

            # Ensure data_x and data_y are not empty
            if data_x.size == 0 or data_y.size == 0:
                raise ValueError("The selected data for the x-axis or y-axis is empty.")
            
            # Filter by selected mineral categories
            if "mineral_names" in mats:
                selected_minerals = input.mineral_bivariate()  # Get selected minerals
                if "All" not in selected_minerals:
                    if "mineral_names" not in mats:
                        raise ValueError("'mineral_names' matrix is not available. Ensure it is created in the data loader.")
                    mineral_names = mats["mineral_names"]
                    if mineral_names.ndim == 2:
                        # Flatten the mineral_names matrix if it's 2D
                        mineral_names = mineral_names.flatten()
                    mineral_mask = np.isin(mineral_names, selected_minerals)
                    data_x = data_x.flatten()[mineral_mask]
                    data_y = data_y.flatten()[mineral_mask]

            # Ensure data_x and data_y are still valid after filtering
            if data_x.size == 0 or data_y.size == 0:
                raise ValueError("The filtered data for the x-axis or y-axis is empty.")

            # Calculate percentiles for x and y axes
            vmin_x = np.nanpercentile(data_x, input.min_max_vals_xaxis()[0]) * 0.9
            vmax_x = np.nanpercentile(data_x, input.min_max_vals_xaxis()[1]) * 1.1
            vmin_y = np.nanpercentile(data_y, input.min_max_vals_yaxis()[0]) * 0.9
            vmax_y = np.nanpercentile(data_y, input.min_max_vals_yaxis()[1]) * 1.1

            # Ensure valid percentile ranges
            if vmin_x >= vmax_x or vmin_y >= vmax_y:
                raise ValueError("Invalid percentile ranges for the x-axis or y-axis.")

            # Handle color map if enabled
            if input.color_map():
                if input.c_map_bivariate() not in mats:
                    raise ValueError(f"Element '{input.c_map_bivariate()}' not found in the data.")
                mat_color = mats[input.c_map_bivariate()]
                if "mineral_names" in mats:
                    if "All" not in selected_minerals:
                        mat_color = mat_color[mineral_mask]  # Apply the same mask to mat_color
                    if mat_color.size == 0:
                        raise ValueError("The selected data for the color map is empty.")
                vmin_color = np.nanpercentile(mat_color, input.min_max_vals_color()[0])
                vmax_color = np.nanpercentile(mat_color, input.min_max_vals_color()[1])
                if input.use_log_color():
                    plt.scatter(
                        data_x, data_y, c=mat_color,
                        norm=colors.SymLogNorm(linthresh=0.001, vmin=vmin_color, vmax=vmax_color),
                        cmap='inferno', s=3
                    )
                else:
                    plt.scatter(data_x, data_y, c=mat_color, cmap='inferno', vmin=vmin_color, vmax=vmax_color, s=3)
                plt.colorbar(label=input.c_map_bivariate())
                plt.clim(vmin_color, vmax_color)
            elif input.mineral_color():
                if "mineral_names" not in mats:
                    raise ValueError("'mineral_names' matrix is not available. Ensure it is created in the data loader.")
                mineral_colors = np.vectorize(lambda x: color_mapping.get(x, "gray"))(mats["mineral_names"]).flatten()
                if "All" not in selected_minerals:
                    mineral_colors = mineral_colors[mineral_mask]  # Apply the same mask to mineral_colors
                if mineral_colors.ndim > 1:
                    mineral_colors = mineral_colors.flatten()
                # Filter by selected minerals
                if "All" not in selected_minerals:
                    filtered_color_mapping = {mineral: color_mapping[mineral] for mineral in selected_minerals if mineral in color_mapping}
                else:
                    filtered_color_mapping = color_mapping
                fig, ax = plt.subplots()
                ax.scatter(data_x, data_y, s=3, c=mineral_colors)
                legend_elements = [
                    Patch(facecolor=color, edgecolor='none', label=label)
                    for label, color in filtered_color_mapping.items()
                ]
                ax.legend(handles=legend_elements, fontsize=8, frameon=True)
            else:
                plt.scatter(data_x, data_y, s=3)

            # Apply axes limits
            plt.xlim(vmin_x, vmax_x)
            plt.ylim(vmin_y, vmax_y)

            if input.use_log_x_axis():
                plt.xscale('symlog', linthresh=0.1)
            if input.use_log_y_axis():
                plt.yscale('symlog', linthresh=0.1)

            # Add labels and grid
            plt.grid(False)
            plt.xlabel("{}".format(input.element_xaxis()))
            plt.ylabel("{}".format(input.element_yaxis()))
            # plt.show()
            # return fig

    @render.plot  
    def decon_plot():
        if input.class_type() == "None":
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = global_mats
        else:
            mats_, _, color_nums, mineral_colors, color_mapping, mineral_colors_mapped = data_loader_3()
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else: 
                mats = mats_

        # Ensure the selected elements exist in mats
        if input.decon_xaxis() not in mats or input.decon_yaxis() not in mats:
            raise ValueError("Selected elements for the x-axis or y-axis are not available in the data.")
        
        if input.use_rois_decon() == True:
            if 'global_roi_dict' not in globals():
                raise ValueError("No ROIs selected. Please select ROIs to plot.")
            else:
                fig, ax = plt.subplots()
                all_data_x = []
                all_data_y = []
                for i in range(len(input.roi_selected_decon())):
                    roi_mask = global_roi_dict[input.roi_selected_decon()[i]]
                    data_x = roi_mask[input.decon_xaxis()]
                    data_y = roi_mask[input.decon_yaxis()]
                    ax.scatter(data_x, data_y, s=5, label=input.roi_selected_decon()[i])
                    all_data_x.append(data_x.flatten())
                    all_data_y.append(data_y.flatten())
                all_data_x = np.concatenate(all_data_x)
                all_data_y = np.concatenate(all_data_y)

                model = LinearRegression()
                x = all_data_x.reshape(-1, 1)
                y = all_data_y.reshape(-1, 1)
                valid_mask = ~np.isnan(x).flatten() & ~np.isnan(y).flatten()  # Mask for valid (non-NaN) rows
                x = x[valid_mask].reshape(-1, 1)
                y = y[valid_mask]
                model.fit(x, y)
                slope = model.coef_[0].item()
                intercept = model.intercept_.item()
                r_squared = model.score(x, y) # R² value
                x_pred = np.linspace(np.nanmin(x), input.decon_ideal_val(), 100).reshape(-1, 1)
                y_pred = model.predict(x_pred)
                decon_val = (model.predict(np.array([[input.decon_ideal_val()]]))).item()
                ax.plot(x_pred, y_pred, color='darkred', linestyle="--", linewidth=1, label=f"value = {decon_val:.0f} ppm; R² = {r_squared:.2f}")                
                # ax.text(input.decon_ideal_val(), decon_val * 1.1, f"{decon_val:.0f} ppm", color='black', fontsize=10, ha="center", va="bottom",
                #     bbox=dict(facecolor='white', alpha=1, edgecolor='none', pad=2)) # Reshape input
                # print(f"Deconvolved value = {decon_val:.2f} ppm")

                vmin_x = np.nanpercentile(all_data_x, input.min_max_vals_xaxis_decon()[0]) * 0.9
                vmax_x = np.nanpercentile(all_data_x, input.min_max_vals_xaxis_decon()[1]) * 1.1
                vmin_y = np.nanpercentile(all_data_y, input.min_max_vals_yaxis_decon()[0]) * 0.9
                vmax_y = np.nanpercentile(all_data_y, input.min_max_vals_yaxis_decon()[1]) * 1.1
                ax.set_xlabel("{}".format(input.decon_xaxis()))
                ax.set_ylabel("{}".format(input.decon_yaxis()))
                ax.set_xlim(vmin_x, vmax_x)
                ax.set_ylim(vmin_y, vmax_y)
                if input.use_log_x_axis_decon():
                    ax.set_xscale('symlog', linthresh=0.1)
                if input.use_log_y_axis_decon():
                    ax.set_yscale('symlog', linthresh=0.1)
                ax.legend()
                ax.axvline(input.decon_ideal_val(), color="darkred", linestyle="--", linewidth=1)
        
        elif input.use_lines_decon() == True:
            if 'global_line_dict' not in globals():
                raise ValueError("No Lines selected. Please select Lines to plot.")
            else:
                fig, ax = plt.subplots()
                all_data_x = []
                all_data_y = []
                for i in range(len(input.line_selected_decon())):
                    line_mask = global_line_dict[input.line_selected_decon()[i]]
                    data_x = line_mask[input.decon_xaxis()]
                    data_y = line_mask[input.decon_yaxis()]
                    ax.scatter(data_x, data_y, s=5, label=input.line_selected_decon()[i])
                    all_data_x.append(data_x.flatten())
                    all_data_y.append(data_y.flatten())
                all_data_x = np.concatenate(all_data_x)
                all_data_y = np.concatenate(all_data_y)

                model = LinearRegression()
                x = all_data_x.reshape(-1, 1)
                y = all_data_y.reshape(-1, 1)
                valid_mask = ~np.isnan(x).flatten() & ~np.isnan(y).flatten()  # Mask for valid (non-NaN) rows
                x = x[valid_mask].reshape(-1, 1)
                y = y[valid_mask]
                model.fit(x, y)
                slope = model.coef_[0].item()
                intercept = model.intercept_.item()
                r_squared = model.score(x, y) # R² value
                x_pred = np.linspace(np.nanmin(x), input.decon_ideal_val(), 100).reshape(-1, 1)
                y_pred = model.predict(x_pred)
                decon_val = (model.predict(np.array([[input.decon_ideal_val()]]))).item()
                ax.plot(x_pred, y_pred, color='darkred', linestyle="--", linewidth=1, label=f"value = {decon_val:.0f} ppm; R² = {r_squared:.2f}")                
                # ax.text(input.decon_ideal_val(), decon_val * 1.1, f"{decon_val:.0f} ppm", color='black', fontsize=10, ha="center", va="bottom",
                #     bbox=dict(facecolor='white', alpha=1, edgecolor='none', pad=2)) # Reshape input
                # print(f"Deconvolved value = {decon_val:.2f} ppm")


                vmin_x = np.nanpercentile(all_data_x, input.min_max_vals_xaxis_decon()[0]) * 0.9
                vmax_x = np.nanpercentile(all_data_x, input.min_max_vals_xaxis_decon()[1]) * 1.1
                vmin_y = np.nanpercentile(all_data_y, input.min_max_vals_yaxis_decon()[0]) * 0.9
                vmax_y = np.nanpercentile(all_data_y, input.min_max_vals_yaxis_decon()[1]) * 1.1
                ax.set_xlabel("{}".format(input.decon_xaxis()))
                ax.set_ylabel("{}".format(input.decon_yaxis()))
                ax.set_xlim(vmin_x, vmax_x)
                ax.set_ylim(vmin_y, vmax_y)
                if input.use_log_x_axis_decon():
                    ax.set_xscale('symlog', linthresh=0.1)
                if input.use_log_y_axis_decon():
                    ax.set_yscale('symlog', linthresh=0.1)
                ax.legend()
                ax.axvline(input.decon_ideal_val(), color="darkred", linestyle="--", linewidth=1)

        
        else:
            data_x = mats[input.decon_xaxis()]
            data_y = mats[input.decon_yaxis()]
            fig,ax = plt.subplots()
            ax.scatter(data_x, data_y, s=5, label="Data")


            model = LinearRegression()
            x = data_x.reshape(-1, 1)
            y = data_y.reshape(-1, 1)
            valid_mask = ~np.isnan(x).flatten() & ~np.isnan(y).flatten()  # Mask for valid (non-NaN) rows
            x = x[valid_mask].reshape(-1, 1)
            y = y[valid_mask]
            model.fit(x, y)
            slope = model.coef_[0].item()
            intercept = model.intercept_.item()
            r_squared = model.score(x, y) # R² value
            x_pred = np.linspace(np.nanmin(x), input.decon_ideal_val(), 100).reshape(-1, 1)
            y_pred = model.predict(x_pred)
            decon_val = (model.predict(np.array([[input.decon_ideal_val()]]))).item()
            ax.plot(x_pred, y_pred, color='darkred', linestyle="--", linewidth=1, label=f"value = {decon_val:.0f} ppm; R² = {r_squared:.2f}")                
            # ax.text(input.decon_ideal_val(), decon_val * 1.1, f"{decon_val:.0f} ppm", color='black', fontsize=10, ha="center", va="bottom",
            #     bbox=dict(facecolor='white', alpha=1, edgecolor='none', pad=2)) # Reshape input
            # print(f"Deconvolved value = {decon_val:.2f} ppm")

            # Calculate percentiles for x and y axes
            vmin_x = np.nanpercentile(data_x, input.min_max_vals_xaxis_decon()[0]) * 0.9
            vmax_x = np.nanpercentile(data_x, input.min_max_vals_xaxis_decon()[1]) * 1.1
            vmin_y = np.nanpercentile(data_y, input.min_max_vals_yaxis_decon()[0]) * 0.9
            vmax_y = np.nanpercentile(data_y, input.min_max_vals_yaxis_decon()[1]) * 1.1

            # Ensure valid percentile ranges
            if vmin_x >= vmax_x or vmin_y >= vmax_y:
                raise ValueError("Invalid percentile ranges for the x-axis or y-axis.")
            
            ax.set_xlabel("{}".format(input.decon_xaxis()))
            ax.set_ylabel("{}".format(input.decon_yaxis()))
            ax.set_xlim(vmin_x, vmax_x)
            ax.set_ylim(vmin_y, vmax_y)
            ax.legend()
            ax.axvline(input.decon_ideal_val(), color="darkred", linestyle="--", linewidth=1)
            


   
    @render.plot
    # @reactive.event(input.run_pca)
    def pca_plot():
        if input.class_type() == "None":
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = global_mats
        else:
            mats_, _, _, mineral_colors, color_mapping, _ = data_loader_3()
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = mats_
        selected_elements = input.pca_elements()
        color_element = input.c_map_pca()  # Element for color mapping
        
        # Ensure at least two elements are selected
        if len(selected_elements) < 2:
            raise ValueError("Please select at least two elements for PCA.")
        
        # Extract data for selected elements
        if "mineral_names" in mats:
            selected_minerals = input.mineral_pca()  # Get selected minerals
            if "All" not in selected_minerals:
                if "mineral_names" not in mats:
                    raise ValueError("'mineral_names' matrix is not available. Ensure it is created in the data loader.")
                mineral_names = mats["mineral_names"]
                if mineral_names.ndim > 1:
                    mineral_names = mineral_names.flatten()  # Flatten mineral_names if it's 2D
                mineral_mask = np.isin(mineral_names, selected_minerals)
                # mineral_names = mineral_names[mineral_mask]  # Apply the mask to mineral_names
                # mineral_colors = mineral_colors[mineral_mask]  # Apply the mask to mineral_colors

                # Apply the mask to each array in mats
                mats_ = {
                    k: v.flatten()[mineral_mask].reshape(-1, 1) if v.ndim > 1 else v[mineral_mask]
                    for k, v in mats.items()
                }
        else:
            selected_minerals = ["All"]

        # Prepare data for PCA
        if "All" not in selected_minerals:
            data = np.array([mats_[element].flatten() for element in selected_elements]).T
        else:
            data = np.array([mats[element].flatten() for element in selected_elements]).T
        
        # Handle missing or invalid data
        if np.isnan(data).any():
            print("Data contains NaN values. Cleaning the data...")
            # Replace NaN values with the mean of each column
            imputer = SimpleImputer(strategy="constant", fill_value=0)
            data = imputer.fit_transform(data)
        
        # Standardize the data
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
        
        # Perform PCA
        n_components = int(input.n_components())
        pca = PCA(n_components=n_components)
        pca_result = pca.fit_transform(data_scaled)

        # Calculate loadings
        loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

         # Extract color data
        if color_element not in mats:
            raise ValueError(f"Element '{color_element}' not found in the data.")
        if "All" not in selected_minerals:
            color_data = mats_[color_element].flatten()
        else:
            color_data = mats[color_element].flatten()
        vmin_color = np.nanpercentile(color_data, input.min_max_pca_color()[0])
        vmax_color = np.nanpercentile(color_data, input.min_max_pca_color()[1])
        vmin_x = np.nanpercentile(pca_result[:, 0], input.min_max_pca_xaxis()[0]) * 0.9
        vmax_x = np.nanpercentile(pca_result[:, 0], input.min_max_pca_xaxis()[1]) * 1.1
        vmin_y = np.nanpercentile(pca_result[:, 1], input.min_max_pca_yaxis()[0]) * 0.9
        vmax_y = np.nanpercentile(pca_result[:, 1], input.min_max_pca_yaxis()[1]) * 1.1

        # if "mineral_names" not in mats:
        #     raise ValueError("'mineral_names' matrix is not available. Ensure it is created in the data loader.")

        # # Extract the mineral_names matrix
        # mineral_names = mats["mineral_names"]

        # # Define a color mapping for the categories
        # color_mapping = {
        #     "Unclassified": "C0",
        #     "Magnetite": "C1",
        #     "Silicate": "palegreen",
        #     "Cu-rich phase": "plum"}
        
        # mineral_colors = np.vectorize(color_mapping.get)(mineral_names)
        
        # Plot PCA results
        if input.class_type() == "None":

            if input.pca_color_map() == True:
                fig, ax = plt.subplots()
                if n_components == 2:
                    scatter = ax.scatter(
                        pca_result[:, 0], pca_result[:, 1], c=color_data, cmap='parula',
                        norm=colors.Normalize(vmin=vmin_color, vmax=vmax_color), alpha=1.0, s=6)
                    ax.set_xlabel("PCA Component 1")
                    ax.set_ylabel("PCA Component 2")
                    # ax.set_title("PCA Analysis (2D)")
                    cbar = plt.colorbar(scatter, ax=ax, pad=0.01)
                    cbar.set_label(f"{color_element} (ppm)")
                # elif n_components == 3:
                #     ax = fig.add_subplot(111, projection='3d')
                #     scatter = ax.scatter(
                #         pca_result[:, 0], pca_result[:, 1], pca_result[:, 2], c=color_data, cmap='parula',
                #         norm=colors.Normalize(vmin=vmin_color, vmax=vmax_color), alpha=1.0, s=6
                #     )
                #     ax.set_xlabel("PCA Component 1")
                #     ax.set_ylabel("PCA Component 2")
                #     ax.set_zlabel("PCA Component 3")
                #     # ax.set_title("PCA Analysis (3D)")
                #     cbar = plt.colorbar(scatter, ax=ax, shrink=0.5)
                #     cbar.set_label(f"{color_element} (ppm)")
                else:
                    raise ValueError("Only 2D PCA plots are supported.")
            else:
                fig, ax = plt.subplots()
                if n_components == 2:
                    scatter = ax.scatter(
                        pca_result[:, 0], pca_result[:, 1], alpha=1.0, s=6)
                    ax.set_xlabel("PCA Component 1")
                    ax.set_ylabel("PCA Component 2")
                    # ax.set_title("PCA Analysis (2D)")
                else:
                    raise ValueError("Only 2D PCA plots are supported.")

        else:
            if input.pca_color_map() == True:
                fig, ax = plt.subplots()
                if n_components == 2:
                    scatter = ax.scatter(
                        pca_result[:, 0], pca_result[:, 1], c=color_data, cmap='parula',
                        norm=colors.Normalize(vmin=vmin_color, vmax=vmax_color), alpha=1.0, s=6)
                    ax.set_xlabel("PCA Component 1")
                    ax.set_ylabel("PCA Component 2")
                    # ax.set_title("PCA Analysis (2D)")
                    cbar = plt.colorbar(scatter, ax=ax, pad=0.01)
                    cbar.set_label(f"{color_element} (ppm)")
                # elif n_components == 3:
                #     ax = fig.add_subplot(111, projection='3d')
                #     scatter = ax.scatter(
                #         pca_result[:, 0], pca_result[:, 1], pca_result[:, 2], c=color_data, cmap='parula',
                #         norm=colors.Normalize(vmin=vmin_color, vmax=vmax_color), alpha=1.0, s=6
                #     )
                #     ax.set_xlabel("PCA Component 1")
                #     ax.set_ylabel("PCA Component 2")
                #     ax.set_zlabel("PCA Component 3")
                #     # ax.set_title("PCA Analysis (3D)")
                #     cbar = plt.colorbar(scatter, ax=ax, shrink=0.5)
                #     cbar.set_label(f"{color_element} (ppm)")
                else:
                    raise ValueError("Only 2D PCA plots are supported.")
            if input.pca_color_map() == False:
                fig, ax = plt.subplots()
                if n_components == 2:
                    if "mineral_names" not in mats:
                        raise ValueError("'mineral_names' matrix is not available. Ensure it is created in the data loader.")
                    mineral_colors = np.vectorize(lambda x: color_mapping.get(x, "gray"))(mats["mineral_names"]).flatten()
                    # # mineral_colors = np.vectorize(lambda x: color_mapping.get)(mats["mineral_names"]).flatten()
                    # # mineral_colors = np.vectorize(color_mapping.get)(mats["mineral_names"]).flatten()
                    if "All" not in selected_minerals:
                        mineral_colors = mineral_colors[mineral_mask]  # Apply the same mask to mineral_colors
                    if mineral_colors.ndim > 1:
                        mineral_colors = mineral_colors.flatten()
                    # Filter by selected minerals
                    if "All" not in selected_minerals:
                        filtered_color_mapping = {mineral: color_mapping[mineral] for mineral in selected_minerals if mineral in color_mapping}
                    else:
                        filtered_color_mapping = color_mapping
                    ax.scatter(pca_result[:, 0], pca_result[:, 1], alpha=1.0, s=6, c=mineral_colors)
                    ax.set_xlabel("PCA Component 1")
                    ax.set_ylabel("PCA Component 2")
                    # ax.set_title("PCA Analysis (2D)")
                    legend_elements = [
                        Patch(facecolor=color, edgecolor='none', label=label)
                        for label, color in filtered_color_mapping.items()
                    ]
                    ax.legend(handles=legend_elements, fontsize=8, frameon=True)
                # elif n_components == 3:
                #     ax = fig.add_subplot(111, projection='3d')
                #     ax.scatter(pca_result[:, 0], pca_result[:, 1], pca_result[:, 2], alpha=1.0, s=6, c=mineral_colors.flatten())
                #     ax.set_xlabel("PCA Component 1")
                #     ax.set_ylabel("PCA Component 2")
                #     ax.set_zlabel("PCA Component 3")
                #     # ax.set_title("PCA Analysis (3D)")
                else:
                    raise ValueError("Only 2D PCA plots are supported.")
        
        # Add loadings as arrows
        for i, element in enumerate(selected_elements):
            ax.plot([0, loadings[i, 0]], [0, loadings[i, 1]], color='black', alpha=1.0)
            ax.text(loadings[i, 0] * 1.2, loadings[i, 1] * 1.2, element, color='black', fontsize=10, ha="center", va="center",
                    bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=2))

        plt.xlim(vmin_x, vmax_x)
        plt.ylim(vmin_y, vmax_y)
        if input.use_log_x_axis_pca():
            plt.xscale('symlog', linthresh=input.pca_linthresh_x())
        if input.use_log_y_axis_pca():
            plt.yscale('symlog', linthresh=input.pca_linthresh_y())

        plt.grid(False)
        return fig

    @render.text
    # @reactive.event(input.run_pca)
    def pca_summary():
        # Load data
        if input.class_type() == "None":
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = global_mats
        if input.class_type() == "KMeans Classification" or "Compositional Classification" or "Library Matching":
            mats_, _, _, _, _, _ = data_loader_3()
            if input.use_cor_mats() == True:
                mats = ycf_cor_mats
            else:
                mats = mats_

        selected_elements = input.pca_elements()

        
        # Ensure at least two elements are selected
        if len(selected_elements) < 2:
            return "Please select at least two elements for PCA."
        
        if "mineral_names" in mats:
            selected_minerals = input.mineral_pca()  # Get selected minerals
            if "All" not in selected_minerals:
                if "mineral_names" not in mats:
                    raise ValueError("'mineral_names' matrix is not available. Ensure it is created in the data loader.")
                mineral_names = mats["mineral_names"]
                if mineral_names.ndim > 1:
                    mineral_names = mineral_names.flatten()  # Flatten mineral_names if it's 2D
                mineral_mask = np.isin(mineral_names, selected_minerals)
                # mineral_names = mineral_names[mineral_mask]  # Apply the mask to mineral_names
                # mineral_colors = mineral_colors[mineral_mask]  # Apply the mask to mineral_colors

                # Apply the mask to each array in mats
                mats_ = {
                    k: v.flatten()[mineral_mask].reshape(-1, 1) if v.ndim > 1 else v[mineral_mask]
                    for k, v in mats.items()
                }
        else:
            selected_minerals = ["All"]

        # Prepare data for PCA
        if "All" not in selected_minerals:
            data = np.array([mats_[element].flatten() for element in selected_elements]).T
        else:
            data = np.array([mats[element].flatten() for element in selected_elements]).T

        if np.isnan(data).any():
            # Replace NaN values with 0
            imputer = SimpleImputer(strategy="constant", fill_value=0)
            data = imputer.fit_transform(data)
        
        
        # Standardize the data
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
        
        # Perform PCA
        n_components = int(input.n_components())
        pca = PCA(n_components=n_components)
        pca.fit(data_scaled)
        
        # Return explained variance ratio
        explained_variance = pca.explained_variance_ratio_
        return f"Explained Variance Ratio: {explained_variance}"
    


app = App(app_ui, server)
# run_app(app)