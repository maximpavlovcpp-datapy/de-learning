transacrtions=[100, -50, 200, -1500, 300, -100, -2000, 500]
inital_balance=1000
balance=inital_balance
success_count=0
for amount in transacrtions:
     if amount<0 and abs(amount)>balance:
          print(f"Транзакция {amount} отклонена:недостаточно средств")
          continue
     balance+=amount
     success_count+=1 
     if balance==0:
          print(f"Баланс онбнулен, остановка")
          break
print(f"Итоговый баланс: {balance}")
print(f"Успешных транзакций: {success_count}")
     
