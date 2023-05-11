import Datasets
X,Y = Datasets.load_linear_example()
import Regression
model = Regression.LinearRegression()
#print(model.fit(X,Y))
#print(model.theta)
#print(model.predict(X))
#print(model.score(X,Y))
