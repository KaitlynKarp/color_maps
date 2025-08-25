import colormaps
import scipy
import matplotlib.pyplot as plt

colormaps.get_valid_cmaps()

colormap1=colormaps.cmaps('cmapkk1') #define a single color map

plt.imshow(scipy.stats.norm.rvs(size=(10,10)), cmap=colormap1)
plt.colorbar()
plt.show()

colormaps.register('cmapkk1') #register a color map to be used with matplotlib functions
plt.imshow(scipy.stats.norm.rvs(size=(10,10)), cmap='cmapkk1')
plt.colorbar()
plt.show()

colormaps.register(['cmapkk1', 'cmapkk2']) #register multiple colormaps
colormaps.register() #register all color maps