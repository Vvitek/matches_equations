from zapalki import *
sign = ['+','-']
digits = '0123456789'
for i in digits:
    for j in digits:
        for k in digits:
            for l in sign:
                solve(i+l+j+'='+k)
                solve(i+'='+j+l+k)
