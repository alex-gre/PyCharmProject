import pickle
import matplotlib.pyplot as plt   
ax = pickle.load(open("plot.pickle", "rb"))
plt.show()