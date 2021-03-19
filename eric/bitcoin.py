import cryptocompare

bitcoin = str(cryptocompare.get_price("BTC"))

bitcoin = bitcoin.replace("{'BTC': {'EUR': ", "")
bitcoin = bitcoin.replace("}}", "")

print (bitcoin)