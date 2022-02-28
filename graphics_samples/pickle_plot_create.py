import pickle
import matplotlib.pyplot as plt
ax = plt.plot([101,200,520,600])
pickle.dump(ax, open("plot.pickle", "wb"))