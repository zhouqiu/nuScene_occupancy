import multiprocessing
import time
import random
keys = ["q", "w", "e"]

# def mini_fun(i,key):
#     A[key] = i * 2
#
#
# def fun(idx):
#     global A
#     A = {}
#     print("process {}: A = {}".format(idx, A))
#
#     mini_fun(idx,keys[idx])
#     time.sleep(random.randint(1,10))
#     print("process {}: A = {}".format(idx, A))
#
#
#
# for i in range(3):
#
#     m = multiprocessing.Process(target=fun, args=(i, ))
#     m.start()

import numpy as np
#
# a = np.array([])
# print(a.shape)
# a = a.reshape(-1, 2)
# print(a.shape)
# b = np.concatenate((a, np.zeros_like(a[:, 0:1])), axis=-1)
# print(b.shape)
#
# #
# # a = []
# # if a:
# #     print(1)
# # else:
# #     print(2)
#
# a = np.array([1,-1,3,0,-2])
# print (~(a>0))

# points_label = np.array([0,1,2,3,4,-1,-2]).astype(np.uint8)
# print(points_label)
# point_cloud_range = [-51.2, -51.2, -5.0, 51.2, 51.2, 3.0]
# print(point_cloud_range[3:])
# print(point_cloud_range[:3])
# #     max_volume_space = [51.2, 51.2, 3],
# #     min_volume_space = [-51.2, -51.2, -5],
import yaml
import numpy as np

label_mapping = "./project/config/label_mapping/nuscenes-noIgnore.yaml"
with open(label_mapping, 'r') as stream:
    nuscenesyaml = yaml.safe_load(stream)
learning_map = nuscenesyaml['learning_map']
import pdb
pdb.set_trace()
points_label = np.array([1,2,3,0]).reshape((4,1)).astype(np.int8)
labels = np.vectorize(learning_map.__getitem__)(points_label)
print("1")