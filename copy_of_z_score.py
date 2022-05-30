# -*- coding: utf-8 -*-
"""Copy of Z-Score

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13z6IrJLbVq8ymxTJjYJxbxNcBnTa7Irm
"""

import numpy as np
import pandas as pd
import scipy.stats as stats

"""Now first import library numpy or pandas and use scipy.stats library for z-score, scipy is also a module"""

data = np.array([5,6,6,18,15,15,19,22,17,20])

"""Here we create an array of mvalues"""

stats.zscore(data)