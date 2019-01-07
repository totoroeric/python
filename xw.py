import xlwings as xw

def say_hi():
    wb = xw.Book.caller()
    sht = wb.sheets[0]
    sht.range('A2').value = 'Hello, world'
    
