import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('test.csv')

x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(x, y)

y_pred = reg.predict(x)

# 데이터 시각화
plt.scatter(x, y, color='blue')
plt.plot(x, y_pred, color = 'green')
plt.title('Score by hours')
plt.xlabel('hours')
plt.ylabel('score')
plt.show()

# 9시간때 점수 예측
print('9시간 공부할 때 예상 점수 : ', reg.predict([[9]]))
reg.coef_		# 기울기 m
reg.intercept_	# y절편 b

# 데이터 세트 분리
from sklearn.linear_model
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# 모델 만들기
from sklearn.linear_model import LinearRegression
reg = LinearRegression()

reg.fit(X_train, y_train)

# 데이터 시각화
plt.scatter(X_train, y_train, color='blue')
plt.plot(X_train, reg.predict(X_train), color = 'green')
plt.title('Score by hours (train data)')
plt.xlabel('hours')
plt.ylabel('score')
plt.show()

# 모델 평가
reg.score(X_test, y_test)		# 테스트 세트 평가
reg.scroe(X_train, y_train)		# 훈련세트 평가

