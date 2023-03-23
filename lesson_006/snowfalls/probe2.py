snowflake = [[0, 998], [1, 951], [3, 598], [6, 526], [8, 120], [9, 572], [10, 647], [11, 1011], [14, 49], [15, 1078], [17, 819], [18, 316], [19, 62]]
finish = [2, 6, 11, 12]
print('snowflake=',snowflake)
print('finish=',finish)
finish.reverse()
print(finish)
count=0
for i in finish:
    # print('i=',i)
    for j in snowflake:
        # print('j=', j)
        # print('j[0]=',j[0])
        if j[0] == i:
            snowflake.remove(j)
print('snowflake_new=', snowflake)
print('count=', count)

