def maxProfit(self, prices):
    min_price = float('inf')
    result = 0
    for ele in prices:
        if min_price > ele:
            min_price = ele
        else:
            result = max(result, ele - min_price)
    return result
