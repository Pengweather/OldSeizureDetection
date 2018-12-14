import gen_filt as gf
import Measurement as mm
import Feature as fe
import pandas as pd
import numpy as np

def calculateFeatureValue(Feature, cutoffFreqStart, cutoffFreqEnd):
	x = gf.filt_data(Feature.Measurement.seizureData, cutoffFreqStart, cutoffFreqEnd, MeasObj.Fs, 10)
	energy = pd.rolling_mean(x**2, Feature.WindowLength.astype(int) - 1)
	return energy

MeasObj = mm.Measurement('Study_005_channel1.txt')
MeasObj.downsample(2)
FeatObj = fe.Feature(MeasObj)
calculateFeatureValue(FeatObj, 4, 8)
