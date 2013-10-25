def memo(f):
  cached_results = {}
  def wrapped(*a, **kw):
    cached_result = cached_results.get((a, kw))
    if cached_result is None:
      cached_result = cached_results[(a, kw)] = f(*a, **kw)
    return cached_result
  return wrapped
      
@memo
def knapsack(s, t):
  if sum(s) == t:
    return s
  for si in s:
    res = knapsack(s - {si}, t)
    if res:
      return res
  else:
    return set()


def coins_without(coins, i):
  res = coins[:]
  del res[i]
  return res


def smallest_larger_than(coins, w):
  if not coins:
    return 0
  try:
    return min([smallest_larger_than(coins_without(coins, i), w - coins[i]) + coins[i] for i in range(len(coins))
                if smallest_larger_than(coins_without(coins, i), w - coins[i]) + coins[i] > w] + 
               [smallest_larger_than(coins_without(coins, i), w - coins[i]) for i in range(len(coins))
                if smallest_larger_than(coins_without(coins, i), w - coins[i]) > w])
  except ValueError:
    return 0

print(smallest_larger_than([1, 2, 3, 4, 5], 10))