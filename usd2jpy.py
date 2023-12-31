from currency_converter import CurrencyConverter

# CurrencyConverter を利用した USD-JPY 為替
def get_currencyconverter_rate() :
    return round(CurrencyConverter().convert(1, 'USD', 'JPY'), 2)


# メイン
if __name__ == '__main__':
    print (get_currencyconverter_rate())
