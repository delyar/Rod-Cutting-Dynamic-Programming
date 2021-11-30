import sys

def parse_input(file_name):
    f = open(file_name, "r")
    vals = [int(val) for val in f.readline().strip().split()]
    f.close()
    return vals
    
def maximum_total_retail_value(arr):
    n = len(arr)
    table = [0 for x in range(n+1)]
    table[0] = 0
 
    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n+1):
        max_profit = -99999
        for j in range(i):
             max_profit = max(max_profit, arr[j] + table[i-j-1])
        table[i] = max_profit
 
    return table[n]
    
log_vals = parse_input("q1-test-vals.txt")
print(log_vals) #[4, 8, 3, 8, 9] --> L=5

print(maximum_total_retail_value(log_vals))
