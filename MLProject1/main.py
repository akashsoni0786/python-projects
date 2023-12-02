import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

# ['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module']
dibetes  = datasets.load_diabetes()

# print(dibetes.keys())

diabetes_X = dibetes.data

# print(diabetes_X)

diabetes_X_train = diabetes_X[:-20]

diabetes_X_test = diabetes_X[-20:]

diabetes_Y_train = dibetes.target[:-20]

diabetes_Y_test = dibetes.target[-20:]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train,diabetes_Y_train)

diabetes_y_predicted = model.predict(diabetes_X_test)

print("Mean squared error : ",mean_squared_error(diabetes_Y_test,diabetes_y_predicted))

print("Weights :",model.coef_)
print("Intercept : ",model.intercept_)

# plt.scatter(diabetes_X_test,diabetes_Y_test)
#
# # plt.scatter(diabetes_X_train,diabetes_Y_train)
# plt.plot(diabetes_X_test,diabetes_y_predicted)
# plt.show()


