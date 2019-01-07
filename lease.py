import xlwings as xw
from mysearch import my_search

DeviceInfoFileList = ['yidianzu.xlsx']
DeviceDic = {}
def get_device_list():
    for d_file in DeviceInfoFileList:
        wb_d = xw.Book(d_file)
        sht_d = wb_d.sheets['Sheet1']
        n = 2
        while True:
            rng = sht_d.range('A' + str(n) + ':H' + str(n))
            value_tmp = rng.value
            print(value_tmp)
            if(value_tmp[0] == None):
                break
            DeviceDic[value_tmp[0]] = value_tmp[1:]
            n += 1
        
            
        

def get_overrall_table(user_sn_file,output_file):
    wb_in = xw.Book(user_sn_file)
    wb_out = xw.Book(output_file)
    sht_in = wb_in.sheets['Sheet1']
    sht_out = wb_out.sheets['Sheet1']
    n = 2
    while True:
        rng_in = sht_in.range('A' + str(n) + ':E' + str(n))
        value_in = rng_in.value
        print(value_in)
        if(value_in[0] == None):
            break
        user_id = str(value_in[0]).partition('.')[0]
        user_info = get_user_info(user_id)
        device_id = value_in[2]
        print(device_id)
        device_info = get_device_info(device_id)
        sht_out.range('A' + str(n)).value = user_info
        sht_out.range('D' + str(n)).value = device_id
        sht_out.range('E' + str(n)).value = device_info
        n += 1
        
def UserInfoProduce(user_sn_file):
    wb = xw.Book(user_sn_file)
    sht1 = wb.sheets['Sheet1']
    sht2 = wb.sheets['Sheet2']
    n = 2
    i = 2
    my_attr = ['sn','displayname']
    while True:
        my_id = ''
        id_number = str(0)
        the_name = sht1.range('A' + str(n)).value
        the_sn = sht1.range('B' + str(n)).value
        if (the_name == None and the_sn == None):
            break
        my_filter = '(displayName=' + str(the_name) + ')'
        result = (my_search(my_filter,my_attr))
        print(the_name,the_sn)
        if (the_name != None):
            my_id = ''
            id_number = 0
            for r in result:
                one_id = r[0].partition(',')[0].partition('=')[2]
                my_id += one_id + ','
                id_number += 1
        sht1.range('C' + str(n)).value = str(id_number)
        sht1.range('D' + str(n)).value = my_id
        n = n+1
        
def get_user_info(user_id):
    the_id = user_id
    my_filter = '(cn=' + str(the_id) + ')'
    my_attr = ['dn','displayName']
    tmp = (my_search(my_filter,my_attr))
    result = []
    result.append(str(the_id))
    result.append(tmp[0][1]['displayName'][0].decode())
    res_list = tmp[0][0].split(',')
    #print(tmp[0][0])
    i = len(res_list) - 4
    info_str = '|'
    while (i > 0):
        info_str += (res_list[i].split('=')[1] + '|')
        #result.append(res_list[i].split('=')[1])
        i -= 1
    result.append(info_str)
    return result

def get_device_info(device_sn):
    try:   
        return_list = DeviceDic[str(device_sn)]
    except:
        return_list = []
    return return_list
    
    
    

    
    
