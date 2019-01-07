        while the_name !=  None  or the_sn != None:
        print(the_name,the_sn)
        my_filter = '(displayName=' + the_name + ')'
        my_search(my_filter,my_attr)
        n = n+1
        the_name = sht1.range('A' + str(n)).value
        the_sn = sht1.range('B' + str(n)).value

