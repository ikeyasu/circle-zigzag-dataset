import os
import numpy as np
import sys
from PIL import Image
import PIL.ImageOps
import random
import pandas as pd

number_train_images = 6000; # Number of train images in each category
number_test_images = 2000; # Number of train images in each category
npy_dir = './raw/'
train_dir = './train/'
test_dir = './test/'
npy_files = [f for f in sorted(os.listdir(npy_dir)) if os.path.isfile(os.path.join(npy_dir, f))]
print(npy_files)

categories = []

for x in npy_files:
	category_split = x.split('.')
	category = category_split[0].title()
	categories.append(category)
	
print(categories)

if not os.path.exists(test_dir):
	os.makedirs(test_dir)
for y in categories:
	if not os.path.exists(os.path.join(train_dir, y)):
		os.makedirs(os.path.join(train_dir, y))

index_cat = 0		
test_labeled_images = []
for z in npy_files:
	print('Processing file', z)
	images = np.load(os.path.join(npy_dir, z))
	print('Saving in', categories[index_cat])
	for a in range(0, number_train_images, 1):
		print('Processing Image', a+1)
		file_name = '%s.jpg' % (a+1)
		file_path = os.path.join(train_dir, categories[index_cat], file_name)
		img = images[a].reshape(28,28)
		f_img = Image.fromarray(img)
		inverted_image = PIL.ImageOps.invert(f_img)
		inverted_image.save(file_path, 'JPEG')
	for a in range(number_train_images, number_train_images + number_test_images, 1):
		print('Processing Test Image', a + 1)
		img = images[a].reshape(28,28)
		f_img = Image.fromarray(img)
		inverted_image = PIL.ImageOps.invert(f_img)
		test_labeled_images += [(inverted_image, index_cat)]
	index_cat = index_cat + 1

random.shuffle(test_labeled_images)
test_index = 0
answers = []
for i, item in enumerate(test_labeled_images):
	file_name = '%s.jpg' % (i+1)
	file_path = os.path.join(test_dir, file_name)
	img, label = item
	img.save(file_path, 'JPEG')
	answers += [(i + 1, label)]

df = pd.DataFrame(answers, columns=("id", "label"))
df.to_csv("answers.csv", index=False)
