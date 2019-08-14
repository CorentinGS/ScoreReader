import cv2
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np
import PIL.Image


def onselect(eclick, erelease):
	if eclick.ydata > erelease.ydata:
		eclick.ydata, erelease.ydata = erelease.ydata, eclick.ydata
	if eclick.xdata > erelease.xdata:
		eclick.xdata, erelease.xdata = erelease.xdata, eclick.xdata
	ax.set_ylim(erelease.ydata, eclick.ydata)
	ax.set_xlim(eclick.xdata, erelease.xdata)
	fig.canvas.draw()
	plt.savefig("new.png", dpi=1200)


fig = plt.figure(dpi=1200)
ax = fig.add_subplot(111)
filename = "temp/SheetReader.png"
im = PIL.Image.open(filename)
arr = np.asarray(im)
plt_image = plt.imshow(arr)
plt.axis('off')

rs = widgets.RectangleSelector(
	ax, onselect, drawtype='box',
	rectprops=dict(facecolor='red', edgecolor='black', alpha=0.5, fill=True))
plt.show()
