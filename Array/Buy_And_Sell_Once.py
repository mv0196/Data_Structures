def buy_and_sell_once(arr):
    max_profit=0.0
    min_price=arr[0]
    for price in arr:
        min_price=min(min_price,price)
        compare_profit=price-min_price
        max_profit=max(max_profit,compare_profit)
    return max_profit
print(buy_and_sell_once([310,315,275,295,260,275,290,230,255,250]))
