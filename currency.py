#!/usr/bin/env python3

"""currency.py: The Currency Exchange Web Service.

__author__ = "WangKunhao"
__pkuid__  = "1800011715"
__email__  = "1800011715@pku.edu.cn"
"""

def is_number(str):
    #判断字符串能否转化为浮点数
  try:
    # 因为使用float有一个例外是'NaN'
    if str=='NaN':
      return False
    float(str)
    return True
  except ValueError:
    return False
def exchange(currency_from, currency_to, amount_from):#根据汇率将输入的货币的量转化为所求的货币的量
    #向网站上传数据并将网站上的反馈下载下来
    web='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from
    from urllib.request import urlopen

    doc = urlopen(web)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstrs=""
    #将网站上反馈的字符串拆解成列表
    for word in jstr:
        if word=='"':
            jstrs=jstrs+' '
        else:
            jstrs=jstrs+word
    alist=jstrs.split()
    blist=[]
    #判断列表中的数据是否是数字
    for num in alist:
        if is_number(num)==True:
            blist.append(num)  
    return blist[1]

def main():
    #主模块
    currency_from=input()
    currency_to=input()
    amount_from=input()
    print(exchange(currency_from, currency_to, amount_from))


def testA():
    assert('26.63365637256'==exchange(EUR,USD,23))
    assert('8.1726769895361'==exchange(CNY,USD,56))
    assert('190.43110625787'==exchange(EUR,CNY,24))

def testB():
    assert(True==is_number('487'))
    assert(True==is_number('3.76'))
    assert(False==is_number('dhf'))
    assert(False==is_number('".,/'))

def testall():
    testA()
    testB()
    print("All tests passed")

if __name__ == '__main__':
    main()
