###### Coin Toss ######
## spin the coin
print("Team A to call...")
call = (input("Heads or Tails??: "))
while call != 'Heads' and  call != 'Tails':
   call = (input("Heads or Tails??: "))
coin = 'Tails'
print("Match Refree to Say, It's  ",coin)
## winning conditions
if coin == call:
    print("Team A have won the toss! What have you decided??")
## losing conditions
else:
    print("Team B have won the toss! What have you decided??")

