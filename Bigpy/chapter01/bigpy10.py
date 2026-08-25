import matplotlib.pyplot as plt


temperatures = [3.3,34.5,14.2,-10]
x=list(range(4))
x_labels = ['Spring','Summer','Fall','Winter']

# bar 차트
plt.title("Bar Chart")
plt.bar(x, temperatures)
plt.xticks(x, x_labels)
plt.yticks(sorted(temperatures))
plt.xlabel("seasons")
plt.ylabel("temperatures")
plt.show()