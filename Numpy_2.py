### numpy의 기본사용법 
import numpy as np

array1 = np.array(
    [1   ,2   ,3]
)
array2 = np.array(
    [4   ,5   ,6]
)


# - numpy 배열 합치기(가로 기준으로)

array3 = np.concatenate(
    [
        array1 , array2
    ]
)

print(
    array3.shape
    ) # 데이터의 크기  , 몇개가 담겨있는가 를 먼저 출력
print(array3)

# - numpy 배열 형태 바꾸기
array4 = np.array(
    [1,  2, 3, 4]
)
# array4를 reshape를 사용하여 2*2 배열로 만들어보자 
array5 = array4.reshape(
    (2,2)
)  
print(array5)

# 세로축을 기준으로 배열 합하기
array6 = np.arange(4).reshape(
    1,4
)
print(array6)
array7 = np.arange(8).reshape(
    2,4
) 
print(array7)

array8 = np.concatenate(
    [
        array6,array7
    ]  , axis=0  # array6의 데이터 값이 array7의 1번째 열 다음으로 추가된다.
)
print(array8)

