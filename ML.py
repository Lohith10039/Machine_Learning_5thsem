import numpy as np
arr = np.arange(1, 21)
print("1. Array:",arr)
print("2. Shape:",arr.shape)
print("3. Max:",arr.max(),"Min:", arr.min())
print("4. Mean:",arr.mean(),"Std Dev:",round(arr.std(),4))

matrix = arr.reshape(4, 5)
print("5. Reshaped Matrix:\n", matrix)
print("6. Second row:", matrix[1, :])
print("7. Third column:", matrix[:, 2])
