for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for y in range(1,5):
                if( i != k ) and (i != j) and (i != y) and (j != y) and (j != k) and (y != k):
                    print(i,j,k,y)


