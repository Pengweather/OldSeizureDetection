import gen_filt as gf
import Measurement as mm
import pandas as pd
import numpy as np

data = mm.Measurement("Study_005_channel1.txt")
data.downsample(2)
x = gf.filt_data(data.seizureData)
windowLength = np.floor(data.Fs * 1)
energy = pd.rolling_mean(x**2, windowLength.astype(int) - 1)

print(len(x))


