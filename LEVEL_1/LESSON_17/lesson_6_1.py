#1.Дано два кортежа, напишите функцию которая соединит их в один dict:
#   Input:
#coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
#code = ('BTC', 'ETH', 'XRP', 'LTC')
#   Output:
#{'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}

coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

#print(dict(zip(coin, code))) # ВАРИАНТ 1


def new_dict(*args):
    new_dict = {}
    for i in code:
        new_idx = code.index(i)
        i2 = coin[new_idx]
        new_dict[i2] = i
    return new_dict

print(new_dict())   # ВАРИАНТ 2