#### numpy 배열 초기화 방법 
import numpy as np

# 먼저 0부터 3까지의 배열 만들어 보기
array1 = np.arange(4) # <- 0부터 3까지의 수를 array1 변수에 지정해줌

print(array1)

# 4*4크기의 dtype이 실수형인 // data를 만들고 그 값이 모두 0인 배열 만들어 보기
array2 = np.zeros(
    (4,4)  , dtype=float
)
print(array2)

# 5*5크기의 dtype이 실수형인 // data를 만들고 그 값이 모두 1인 배열 만들어 보기
array3 = np.ones(
    (5,5)  , dtype=float
)
print(array3)

# 0부터 9까지의 랜덤의 수를 초기화 된 배열로 만들기 크기는 3*3
array4 = np.random.randint(
    0,10   , (
        3,3
    )
)
print(array4)

# 평균이 0이고 , 표준 편차가 1인 표준 정규를 띄는 배열 만들어보기 크기는 3*3
array5 = np.random.normal(
    0,1  , (3,3)
)
print(array5)
