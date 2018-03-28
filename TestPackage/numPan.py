import matplotlib.pyplot as plt

# 121 > 1行2列第1个
fig1 = plt.subplot(231)
plt.title("123")
plt.pie([1, 2, 3])
# 122 > 1行2列第2个
fig2 = plt.subplot(232)
plt.title("213")
plt.pie([10, 5, 5])

plt.show()