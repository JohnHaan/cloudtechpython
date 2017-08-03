import mod2

result = mod2.sum(3, 4)
print(result)


python

import sys
sys.path.append("/projects/cloudtechpython/20170710/Class_B/ianlee")
import mod2
print(mod2.PI)

reload(mod2)
# 이미 불렀던 모듈에 변경 사항이 생겼을 때
# 안됨
# from imp import reload

