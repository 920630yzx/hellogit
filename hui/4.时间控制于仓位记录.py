'''
#1_不隔周策略
scheduler.run_weekly(buy, tradingday=1, time_rule=market_open(minute=10)) #buy表示方法,写在最前面;tradingday=1表示周一
scheduler.run_weekly(close, tradingday=-1, time_rule=market_close(minute=10))

#不隔夜策略   区别于不隔周策略就不用写tradingday了
scheduler.run_daily(buy, time_rule=market_open(minute=10))
scheduler.run_daily(close, time_rule=market_close(minutue=10))
'''

#时间控制(具体不隔周的例子)：
import rqalpha
from rqalpha.api import *

def init(context):
    context.s1 = '000001.XSHE'
    scheduler.run_weekly(buy, tradingday=1, time_rule=market_open(minute=10))  #这里以日线数据进行回测,所以time_rule没发挥作用;#buy表示方法,写在最前面;tradingday=1表示周一
    #time_rule=market_open(minute=10)表示开盘后的10分钟,time_rule=market_close(minute=10)表示收盘前的10分钟,但这里不起作用?
    scheduler.run_weekly(close, tradingday=-1, time_rule=market_close(minute=10))

def handle_bar(context, bar_dict):
    pass

def buy(context, bar_dict): #满仓买入
    cur_position = context.portfolio.positions[context.s1].quantity
    if cur_position==0:
        order_target_percent(context.s1, 1)
        print('buy:', context.now)

def close(context, bar_dict): #满仓卖出
    cur_position = context.portfolio.positions[context.s1].quantity
    if cur_position>0:
        order_target_value(context.s1, 0)
        print('close:', context.now)

config = {
  "base": {
    "start_date": "2017-10-20",
    "end_date": "2017-11-21",
    "accounts": {'stock':1000000},
    "benchmark": "000001.XSHE"
  },
  "extra": {
    "log_level": "error",
  },
#   "mod": {
#     "sys_analyser": {
#       "enabled": True,
#       "plot": True
#     }
#   }
}

rqalpha.run_func(init=init, handle_bar=handle_bar, config=config)



#仓位记录
import rqalpha
from rqalpha.api import *
# import os

def init(context):
    context.s1 = '000001.XSHE'
    context.s2 = '600036.XSHG'

def handle_bar(context, bar_dict):
    record(context, bar_dict)
    if context.s1 not in context.portfolio.positions:
        order_target_percent(context.s1, 0.5)  #以50%的仓位买入
    if context.s2 not in context.portfolio.positions:
        order_target_percent(context.s2, 0.2)  #以20%的仓位买入

#记录当前已占用的资金
def record(context, bar_dict):
    pos_s1 = context.portfolio.positions[context.s1].quantity #股票context.s1的持有量
    pos_s2 = context.portfolio.positions[context.s2].quantity #股票context.s2的持有量
    price_s1 = context.portfolio.positions[context.s1].avg_price #乘以股票平均持有成本,得到总资产
    price_s2 = context.portfolio.positions[context.s2].avg_price #乘以股票平均持有成本,得到总资产
    capital = pos_s1*price_s1+pos_s2*price_s2 #得到总持仓资金
    plot("capital", capital) #画出图形


config = {
  "base": {
    "start_date": "2015-06-01",
    "end_date": "2017-12-30",
    "accounts": {'stock':1000000},
    "benchmark": "000300.XSHG",
#     "strategy_file_path": os.path.abspath(__file__)
  },
  "extra": {
    "log_level": "error",
  },
  "mod": {
    "sys_analyser": {
#       "report_save_path": '.',
      "enabled": True,
      "plot": True
    }
  }
}
rqalpha.run_func(init=init, handle_bar=handle_bar, config=config)



