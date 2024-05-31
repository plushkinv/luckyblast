
#то что ниже обязательно заполнить своими данными
proxy_use = 0 #  0 - не использовать, 1 - использовать ротируемые прокси
proxy_login = 'pluy'
proxy_password = '5lecp'
proxy_address = 'gaom'
proxy_port = '80'
proxy_changeIPlink = "hte3b204"


#то что ниже желательно настроить под себя
minimal_need_balance = 0.0011 # минимальный баланс на кошельке который должен быть чтобы начать с ним работу.
skolko_mintit = [1,2] # выбираете диаазон сколько минтить за один раз


#укажите паузу в работе между кошельками, минимальную и максимальную. 
#При смене каждого кошелька будет выбрано случайное число. Значения указываются в секундах
timeoutMin = 1880 #минимальная 
timeoutMax = 5400 #максимальная
#задержки между операциями в рамках одного кошелька
timeoutTehMin = 30 #минимальная 
timeoutTehMax = 70 #максимальная



#то что ниже можно менять только если понимаешь что делаешь
proxies = { 'all': f'http://{proxy_login}:{proxy_password}@{proxy_address}:{proxy_port}',}
if proxy_use:
    request_kwargs = {"proxies":proxies, "timeout": 120}
else:
    request_kwargs = {"timeout": 120}

slippage = 1    # % 
gas_kef=1.1 #коэфициент допустимого расхода газа на подписание транзакций. можно выставлять от 1.1 до 2

rpc_links = {
    'eth': 'https://rpc.ankr.com/eth',
    'rpc': 'https://blast.blockpi.network/v1/rpc/public',
    'scan': 'https://blastscan.io/tx',
}