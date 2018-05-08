#1_order_shares买入一只股票的一定股份数
import rqalpha
from rqalpha.api import *

def init(context):
    context.s1 = '000001.XSHE'

def handle_bar(context, bar_dict):
    cur_position = context.portfolio.positions[context.s1].quantity #计算现在的仓位有多少
    shares = context.portfolio.cash/bar_dict[context.s1].close #现在持有的现金/现在股票的价格(收盘价),算出现在能够下多少单
    if cur_position==0: #如果这支股票没有持仓,就要shares来下单
        order_shares(context.s1, shares)
        
        
        
#2_order_target_percent买入两只股票的一定百分比      
def init(context):
    context.s1 = '000001.XSHE'
    context.s2 = '600036.XSHG'

def handle_bar(context, bar_dict):
    if context.s1 not in context.portfolio.positions:
        order_target_percent(context.s1, 0.5) #0.5表示下50%的总资金量
    if context.s2 not in context.portfolio.positions:
        order_target_percent(context.s2, 0.5)     
        
        

#3_sell_open卖空一手股指期货与buy_close买多平仓
#连续两天MA下跌卖出一手股指期货，连续两天MA上涨买入平仓。      
def init(context):
    context.future = get_future_contracts("IF")[0] #拿到期货合约名称

def handle_bar(context, bar_dict):
    prices = history_bars(context.future, 12, '1d', 'close') #拿到历史数据
    ma = talib.EMA(prices, 10) #通过历史数据计算10日均线
    sell_qty = context.portfolio.positions[future].sell_quantity #计算持仓情况
    if ma[-1] < ma[-2] and ma[-2] < ma[-3] and sell_qty == 0: #若满足这个条件,则sell_open卖空一手股指期货； sell_qty == 0表示无头寸
        sell_open(context.future, 1)

    if ma[-1] > ma[-2] and ma[-2]>ma[-3] and sell_qty > 0: #若满足这个条件,则sell_openbuy_close买多平仓；  sell_qty > 0表示有头寸
        buy_close(context.future, 1)      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        