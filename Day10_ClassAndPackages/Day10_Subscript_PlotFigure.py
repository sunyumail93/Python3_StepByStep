#!/usr/bin/env python3
"""
Day10_Subscript_PlotFigure.py
Plot heatmap using seaborn
"""

import seaborn as sns
import matplotlib.pyplot as plt

def PlotHeatmap(DataFrame, OutputName):
	sns_plot = sns.clustermap(DataFrame[["Mean_WT","Mean_KD"]])
	plt.savefig(OutputName)
	plt.show()
