from __future__ import division
import os
import sys
import numpy as np
import nibabel as nib

cases = 'caselist.txt'
binary_file = 'output/binary'
training_data='output/Y_train.npy'

with open(cases) as f:
    case_arr = f.read().splitlines()

x_dim=176
y_dim=208
z_dim=176
total_case = len(case_arr)
count=0

f_handle = open(binary_file, 'wb')
for subjects in case_arr:
	img = nib.load(subjects)
	data = img.get_data().astype(np.float32)
	data = data.reshape(x_dim, y_dim, z_dim)
	data[data>0.0]=1
	data.tofile(f_handle)
	print 'Case ' + str(count) + ' done'
	count = count + 1
f_handle.close()

merge = np.memmap(binary_file, dtype=np.float32, mode='r+', shape=(x_dim*total_case, y_dim, z_dim))
print merge.shape
print type(merge)

np.save(training_data, merge)
	
