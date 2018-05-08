#history_bars
#数据获取代码 上证股票:.XSHG  深证股票：.XSHE
#当前可交易股指期货： get_future_contracts("IF")[0]

import rqalpha
from rqalpha.api import *

def init(context):
    context.sh_stock = '600036.XSHG' #这里若需要同时获取两只股票该如何写呢？
    context.sz_stock = '000001.XSHE'
    context.future = get_future_contracts("IC")[0] #("IF")[0]表示沪深300当前交易的主力合约,("IF")[1]表示次主力,
    #这个一般是按上一日成交量排序的;同理("IC")[0]表示上证50股指期货主力合约

# bar_dirt可读取bar信息
def handle_bar(context, bar_dict):
    # history_bars用来读取历史数据
    sh_stock = history_bars(context.sh_stock, 1, '1d') #1表示过去1天,'1d'表示日线数据
    print ('sh_stock:', sh_stock)
    print (bar_dict[context.sh_stock].last) #这里是打印最新的价格
    sz_stock = history_bars(context.sz_stock, 1, '1d')
    print ('sz_stock:', sz_stock)
    future = history_bars(context.future, 1, '1d')
    print ('future:', future)

config = {
  "base": {
    "start_date": "2018-05-03",
    "end_date": "2018-05-03",
    "accounts": {'stock':1000000, 'future':1000000},
    "benchmark": "000300.XSHG"
  },
  "extra": {
    "log_level": "error",
  },
  "mod": {
    "sys_analyser": {
      "enabled": True,
      "plot": True
    }
  }
}

rqalpha.run_func(init=init, handle_bar=handle_bar, config=config)






