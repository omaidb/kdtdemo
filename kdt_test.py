import openpyxl

# 打开excel
from base_kdt import KeyWord

excel = openpyxl.load_workbook('test.xlsx')
# 获取所有的sheets
sheets = excel.sheetnames
# 遍历所有的sheet
for sheet in sheets:
    wb = excel[sheet]  # 打开遍历到的sheet
    for values in wb.values:
        parans = {}
        action = values[1]
        parans['ele_type'] = values[2]
        parans['index'] = values[3]
        parans['txt'] = values[4]
        # 结合文件来进行判断
        if type(values[0]) is int:
            print(values)
            if values[1] == 'browser':
                kw = KeyWord(parans['txt'])
            else:
                getattr(kw, action)(**parans)
        else:
            pass
