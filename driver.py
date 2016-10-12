from __future__ import print_function # for keeping consistency with the python 3 print function
import numpy as np # standard array processing library
import matplotlib.pyplot as plt # standard data visualization library
from scipy.signal import spectrogram # for, ya know, spectrograms
import gzip # for unpacking zip files
import os # library for os operations
import sys
sys.dont_write_bytecode = True # keeps from writing extra pyc files when we load local files
import utils # utils file from next door


# relative paths to the data. The r is there because backslashes are dicks
h1_dir = r".\sample_data\small_data_sample\right_whale"
h0_dir = r".\sample_data\small_data_sample\no_right_whale"

# couple quick lambda functions to attach filenames to their path
h1_map = lambda fname: os.path.join(h1_dir, fname)
h0_map = lambda fname: os.path.join(h0_dir, fname)

# map those path making functions above onto the lists of path names from os.listdir
h1_files = map(h1_map, os.listdir(h1_dir))
h0_files = map(h0_map, os.listdir(h0_dir))

# now load in our files
print("Loading files")
h1s = map(utils.load_file, h1_files)
h0s = map(utils.load_file, h0_files)
print("Loaded %i files" % (len(h1s) + len(h0s)))

# do a lil bit of data viz
fig = plt.figure(figsize=(8, 11))
for i, (h1, h0) in enumerate(zip(h1s, h0s)):
    for j, h in enumerate([h1, h0]):
        ax = fig.add_subplot(5, 2, 2*i+j+1)
        ax.plot(np.linspace(0, 2, h.shape[0]), h, color="#5379f3", alpha=0.6)
        ax.set_title(['Whale', 'No Whale'][j])
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
fig.tight_layout()

# let's measure some basic features and see how these points look plotted against each other
features = {'mean': np.mean, 'variance': np.var}
feature_names = features.keys()

colors = ["#3d99f0", "#f03d3d"]
area = np.pi*(12**2)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
for label, h, color in zip(['Whales', 'No Whales'], [h1s, h0s], colors):
    x, y = [map(features[name], h) for name in feature_names]
    ax.scatter(x, y, s=area, c=color, label=label, alpha=0.6)
    ax.set_xlabel(feature_names[0])
    ax.set_ylabel(feature_names[1])
ax.legend()
