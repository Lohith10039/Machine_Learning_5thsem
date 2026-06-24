import numpy as np

A = np.array([10, 20, 30, 40, 50])
B = np.array([5, 10, 15, 20, 25])

addition_result = A + B 
subtraction_result = A - B  
multiplication_result = A * B 
division_result = A / B  
sum_A = np.sum(A)
print("1. Addition of A and B:        ", addition_result)
print("2. Subtraction of B from A:    ", subtraction_result)
print("3. Element-wise multiplication:", multiplication_result)
print("4. Element-wise division:      ", division_result)
print("5. Sum of all elements in A:   ", sum_A)
