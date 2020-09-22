import matplotlib.pyplot as plt
fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.bar(list(range(10)), list(range(10,20)))
fig.savefig('to.png')   # save the figure to file
plt.close(fig)