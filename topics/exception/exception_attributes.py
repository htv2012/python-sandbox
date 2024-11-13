# 
#  exception_attributes.py
#  exception
#  
#  Created by Hai Vu on 2013-09-27.
#  Copyright 2013 Hai Vu. All rights reserved.
# 

try:
    x = 0
    y = 7 / x
except ZeroDivisionError as e:
    print(dir(e))