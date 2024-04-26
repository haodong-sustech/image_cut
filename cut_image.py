import imageio. v2 as io
import numpy as np
from math import floor
import tifffile as tiff

image_data = io.volread('Stack.tif')
image_rows = np.size(image_data, 1)
image_cols = np.size(image_data, 2)

cut_rows = floor(image_rows/10)
cut_cols = floor(image_cols/10)

image_data_cut =image_data[:, cut_rows:-cut_rows, cut_cols:-cut_cols]

print(image_data_cut.shape)

cut_name = 'Stack_cut.tif'
tiff.imwrite(cut_name, np.array(image_data_cut), bigtiff=True)

