import aifc
import numpy as np

def load_file(fname):
    '''
    reads in aifc files.  Don't ask me about the last line, got it from Dr. Google.
    Essentially just plays with data types
    '''
    aiff = aifc.open(fname, 'rb')
    bits = aiff.readframes(aiff.getnframes())
    aiff.close()
    return np.fromstring(bits, np.short).byteswap()
