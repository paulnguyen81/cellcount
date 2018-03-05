### Run Length Encoding (RLE)
### Te encode and decode masks for the kaggle competition
### https://www.kaggle.com/paulorzp/fast-run-length-encode
### https://www.kaggle.com/paulorzp/run-length-encode-and-decode

import numpy as np

def rle_encode (img):
    #takes an image numpy array with 1 - mask, 0 - background
    #converts to RLE

    bytes = np.where(img.flatten()==255)[0]
    runs = []
    prev = -2
    for b in bytes:
        if (b>prev+1): runs.extend((b+1, 0))
        runs[-1] += 1
        prev = b
    
    return ' '.join([str(i) for i in runs])


def rle_decode(mask_rle, shape):
    s = mask_rle.split()
    starts, lengths = [np.asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
    starts -= 1
    ends = starts + lengths
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape)