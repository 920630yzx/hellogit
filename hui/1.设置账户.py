#方法1
config = {
  "base": {                                                    #设置基本信息
    #设置回测开始时间
    "start_date": "2017-01-03",
    #设置回测结束时间
    "end_date": "2017-06-01",
    #设置回测的品种与初始资金额  股票账户就用'stock',期货账户就用'future'
    "accounts": {'stock':1000000, 'future':1000000},
    #设置基准收益
    "benchmark": "000300.XSHG",
    #运行当下策略文件
    "strategy_file_path": os.path.abspath(__file__)
  },
  "extra": {
    #查看最详细的日志，若输入'error'则只看错误,"verbose"则表示查看详细信息
    "log_level": "verbose",
  },
  "mod": {                                                     #设置
    "sys_analyser": {
        #保存report至当下文件
        "report_save_path": '.', 
        #启动策略逐行性能分析
        "enabled": True,
        #打印图形
        "plot": True
     },
    "sys_simulation": {
        "enabled": True, #是否启动sys_simulation
        #设置手续费的倍数,默认是10
        "commission_multiplier": 20,
        #设置滑点
        "slippage": 0.001
    }
  }
}
    
    
    
#方法2    
from rqalpha import run_code

code = """     #输入需要跑的代码

init(context):
    pass

handle_bar(context, bar_dict):
    pass

"""

config = {
  "base": {
    "start_date": "2016-06-01",
    "end_date": "2016-12-01",
    "accounts": {'stock':1000000},
    "benchmark": "000300.XSHG"
  },
  "extra": {
    "log_level": "verbose",
  },
  "mod": {
    "sys_analyser": {
      "enabled": True,
      "plot": True
    }
  }
}




#2_导入api,初始化与执行引擎.
import rqalpha
from rqalpha.api import *

# context作为全局变量做传递,当然context本身也装了一些功能
def init(context):
    context.message = 'hello'
    #用来写开始的时候做什么

def handle_bar(context, bar_dict): #bar_dict是要输的每一更bar
    print (context.message)
    #用来写每次循环要作什么

## config设置
config = {
  "base": {
    "start_date": "2017-04-21",
    "end_date": "2017-05-01",
    "accounts": {'stock':1000000},
    "stock_starting_cash": 1000000,
    "benchmark": "000300.XSHG",
  },
  "extra": {
    "log_level": "error",
  },
  "mod": {
    "sys_analyser": {
      "enabled": False,
      "plot": False
    }
  }
}

# 您可以指定您要传递的参数
rqalpha.run_func(init=init, handle_bar=handle_bar, config=config)


