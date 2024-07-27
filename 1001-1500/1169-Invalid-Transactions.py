class Solution(object):
    def invalidTransactions(self, transactions):
        customerTransactions = defaultdict(list)
        invalidIds = set()
        
        for i, transaction in enumerate(transactions):
            details = transaction.split(',')
            customer, time, amount, city = details
            if int(amount) > 1000:
                invalidIds.add(i)
            for existingTransaction in customerTransactions[customer]:
                if existingTransaction[2] != city and abs(existingTransaction[1] - int(time)) <= 60:
                    invalidIds.add(i)
                    invalidIds.add(existingTransaction[0])
            customerTransactions[customer].append([i, int(time), city])
            
        return [transactions[i] for i in invalidIds]