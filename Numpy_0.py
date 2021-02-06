# numpy란 ? 
'''
일반적으로 대규모 다차원 배열을 쉽게 처리 할 수 있도록 지원하는 파이썬의 라이브러리
데이터 구조 외에도 수치 계산을 위해 효율적으로 구현된 기능을 제공
'''
# numpy의 차원 
'''
- 1차원 축(행) : axis 0 => Vector
- 2차원 축(행) : axis 1 => Matrix
- 3차원 축(행) : axis 2=> Tensor // 3차원 이상
'''

### numpy의 기본 사용 방법 

# numpy 사용하기  
import numpy as np

# 일반적 python list
list_data = [1 , 2, 3]

array = np.array(list_data) # numpy형식으로 array라는 변수에 list_data를 지정함

# size를 통한 데이터의 개수 확인
print(array.size)
# dtype을 통한 데이터의 타입 확인
print(array.dtype)
# 특정한 index에 접근
print(
    array[2]
    )



