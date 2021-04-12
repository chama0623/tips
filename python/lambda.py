# ラムダ式, 無名関数
# lambda 引数1, 引数2, ... : 式
# x%2が0のとき"even",それ以外のとき"odd"を返す無名関数
get_odd_even = lambda x: 'even' if x % 2 == 0 else 'odd'

print(get_odd_even(3))
# odd

print(get_odd_even(4))
# even