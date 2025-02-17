# Question 1
# Why doesn’t np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float)
# create a two-dimensional (2D) array? Write it the correct way

# The above code doesn't create a 2D array because of the way the tuples are passed to the np.array() function.
# When you pass multiple arguments to a function, they are treated as separate arguments, not as a single argument.
# So, in this case, you're passing four separate arguments to the np.array() function: three tuples and a dtype argument.
# To create a 2D array, you need to pass a single argument to the np.array() function.

# Here is the correct way:

import numpy as np

x = np.array(((1, 0, 0), (0, 1, 0), (0, 0, 1)), dtype=float)
print("Question 1: \n")
print(f"Correct array: \n{x}\n")


# Question 2
# What is the difference between a = np.array([0, 0, 0]) and a = np.array([[0, 0, 0]])?

a = np.array([0, 0, 0])
print("\nQuestion 2: \n")
print(f"a. Array: {a}")
print(f"Array shape: {a.shape}")
print(f"Array dimentions: {a.ndim}\n")

# Shape attribute is (3,), which indicates that there are three elements in the array in one row
# ndim attribute is 1, which indicates that the array is one-dimensional (1D)

b = np.array([[0, 0, 0]])
print(f"b. Array: {b}")
print(f"Array shape: {b.shape}")
print(f"Array dimentions: {b.ndim}\n")

# Shape attribute is (1, 3), which indicates there are two dimensions: one row (with one element) and three columns.
# ndim attribute is 2, which indicates that the array is 2D


# Question 3
# A 3 by 4 by 4 array is created with arr = np.linspace(1, 48, 48).reshape(3, 4, 4). Index or slice this array to obtain the following:

arr = np.linspace(1, 48, 48).reshape(3, 4, 4)
print("\nQuestion 3 (answer checks): \n")
print(arr)

# There are multiple ways to obtain the specified values:
# a. 20.0
# Using indexing
answer = arr[1, 0, 3]                                      # Selects [second matrix, first row, fourth column]
print(f"a. {answer}")
# Or flatten the array to 1D and then access with new index number (starting at index 0)
answer = arr.flatten()[19]
print(f"a. {answer}")

# b. [ 9. 10. 11. 12.]
answer = arr[0, 2]                                         # Selects [first matrix, third row]
print(f"\nb. {answer}")

# c. [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]
answer = arr[2]                                            # Selects [third matrix]
print(f"\nc. {answer}")

# d. [[5. 6.], [21. 22.] [37. 38.]]
answer = arr[:, 1, 0:2]                                    # Selects [all matrices, second row, first two columns]
print(f"\nd. {answer}")

# e. [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
answer = arr[2, :, -1:-3:-1]                               # Selects [third matrix, all rows, last two columns in reverse]
print(f"\ne. {answer}")

# f. [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]
answer = arr[:, :, 0][:, ::-1]
# [:, :, 0] means select [all matrices, all rows, first column]
# [:, ::-1] means select [all rows, (start at last column end, end at last column, move backwards by 1)] 
print(f"\nf. {answer}")           

# g. [[1. 4.] [45. 48.]]
indices = [0, 3, 44, 47]                                   # Indices of desired values of flattened array
answer = arr.flatten()[indices].reshape(2, 2)              # Flatten array and reshape it to include desired indices
print(f"\ng. {answer}")

# h. [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]
answer = np.array([arr[1, 2], arr[1, 3], arr[2, 0], arr[2, 1]])
print(f"\nh. {answer}")