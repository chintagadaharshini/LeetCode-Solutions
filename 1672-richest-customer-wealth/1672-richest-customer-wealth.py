class Solution(object):
    def maximumWealth(self, accounts):
        maximum = 0

        for customer in accounts:
            total = 0

            for money in customer:
                total += money

            if total > maximum:
                maximum = total

        return maximum
        