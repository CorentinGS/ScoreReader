import cv2
import matplotlib.pyplot as plt

from pdf2image import convert_from_path


def to_png(path, name):
	images = convert_from_path(f"{path}/{name}.pdf")
	images[0].save("temp/{}.png".format(name))


def main():
	path = "images"
	name = "SheetReader"
	to_png(path, name)
	img = cv2.imread("temp/{}.png".format(name), 0)
	histr = cv2.calcHist([img], [0], None, [256], [0, 256])
	plt.plot(histr)
	plt.show()


if __name__ == "__main__":
	main()
