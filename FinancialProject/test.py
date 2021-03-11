import pymongo
# from home import Ui_Home
import dns

server = "mongodb+srv://iBobby:1234@cluster0.1npcu.mongodb.net/<dbname>?retryWrites=true&w=majority"
mylist = []


def mydata():
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database("StockDividend")
        where = {}
        cursor = db.sample_stock.find(where)
        for i in cursor:
            # data = [{'stock_name':i['stock_name'],'current_price':i['current_price'],'dividend':i['dividend']}]
            mylist.append([i['stock_name'], i['current_price'], i['dividend']])
            # print(i)
        # print(mylist)
    stock = "AI"
    # dividend = []
    # stock_price = []
    #
    # for i in mylist:
    #     #print(i)
    #     if i[0] == "AI":
    #         sum = (i[2]*100)/i[1]

    # ---------------------------------คิดอัตราดอกเบี้ย--------------------------
    dividend_list = []
    sum = 0
    month = 12
    total_year = 3
    disposit = 1000
    disposit_month = 1000
    total_disposit = disposit * (12 / 12) * (6 / 100)  # 60
    num = 12
    collect = 0
    dividend_all = 0
    for i in range(total_year,0,-1):
        if num > 0:
            for n in range(month, 0, -1):
                sum += (disposit_month) * (num / 12) * (6 / 100)
                num = num - 1
        total = sum + collect + total_disposit
        collect = (disposit_month * month)*0.06
        month = month + 12
        dividend_all += total
        #dividend_list.append(dividend_all)
        print(total)
    #print(dividend_list)

    #print(sum)
    #print(total)

def calc2():
    dividend = []
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database("StockDividend")

        where = {'stock_name':{'$eq': "AI"}}
        cursor = db.sample_stock.find(where)
        for i in cursor:
            dividend.append(i['dividend'])
            print(i)
    print(dividend[0])

def test3():
    user_list = []
    email_list = []
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database("StockDividend")
        where = {}
        cursor = db.credentials.find(where)
        for i in cursor:
            user_list.append(i['username'])
            email_list.append(i['email'])

    username = "test"
    if username in user_list:
        print("true")
    else:
        print("false")

def Calc():
        sum = 0
        month = 12
        total_year = 2
        disposit = 1000
        disposit_month = 1000
        #dividend = self.get_divident(name) #9.0
        #dv = dividend[0]
        total_disposit = disposit * (12 / 12) * (6 / 100)  # 60
        num = 12
        collect = 0
        dividend_all = 0
        devident_list = []
        for i in range(total_year, 0, -1):
            if num > 0:
                for n in range(month, 0, -1):
                    sum += (disposit_month) * (num / 12) * (6 / 100)
                    num = num - 1
            total = sum + collect + total_disposit
            collect = (disposit_month * month) * (6 / 100)
            month = month + 12
            dividend_all += total
            devident_list.append(total)
            print(dividend_all)
        return devident_list

if __name__ == '__main__':
    dvd = Calc()
    print(dvd)
    for i in dvd:
         print(i)
