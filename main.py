import os.path
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import cv2
import matplotlib.pyplot as plt
from pdf2image import convert_from_path


def to_png(file, name):
	images = convert_from_path(file, dpi=500)
	images[0].save("temp/{}.png".format(name), quality=100)


def main():
	Tk().withdraw()
	filename = askopenfilename()
	path, file_extension = os.path.splitext(filename)

	name = "SheetReader"
	if file_extension == ".pdf":
		to_png(filename, name)
		img = cv2.imread("temp/{}.png".format(name), 0)
	elif file_extension == '.png':
		img = cv2.imread(filename, 0)
	else:
		return
	histr = cv2.calcHist([img], [0], None, [256], [0, 256])
	plt.plot(histr)
	plt.show()

if __name__ == "__main__":
	main()
