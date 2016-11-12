import aifc
import numpy as np
import matplotlib.pyplot as plt

def load_file(fname):
    '''
    reads in aifc files.  Don't ask me about the last line, got it from Dr. Google.
    Essentially just plays with data types
    '''
    aiff = aifc.open(fname, 'rb')
    bits = aiff.readframes(aiff.getnframes())
    aiff.close()
    return np.fromstring(bits, np.short).byteswap()


def plot_spectrogram(frequencies, times, values):
    fig, ax = plt.subplots()
    axis_spectrogram(ax, (frequencies, times, values))
    return fig

def axis_spectrogram(ax, stuff):
    frequencies, times, values = stuff
    extent = [times.min(), times.max(), frequencies.min(), frequencies.max()]
    ax.imshow(values, extent=extent, origin='lower', aspect='auto')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Frequency (Scale)')