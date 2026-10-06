print('=== Система мониторинга безопасности v1.0 ===')
print('Загрузка модулей...')
print('Проверка соединения с базой данных...')
print('Cистема готова к работе.')
server_name="prod-db-01"
server_ip="192.168.1.100"
server_port=5432
is_active=True
cpu_load=45.5
print(type(server_name))
print(type(server_ip))
print(type(server_port))
print(type(is_active))
print(type(cpu_load))
api_key="sk_test_abc123xyz"
print(len(api_key))
print('your login: ')
login=input()
print('your password: ')
password=input()
N=len(password)
print(f"user {login} succersfull authorized. Length of password: {N} symbols")
#3.2
print('введите первое число: ')
first_n=input()
f_n=float(first_n)
print('введите второе число: ')
second_n=input()
s_n=float(second_n)
class calc_Opetation:
    def sum(self, a,b):
        return a+b
    def mul(self, a,b):
        return a*b
    def div(self, a,b):
        return a/b
print("какую операцию хотите применить( + , * , / )?")
op=input()
obj=calc_Opetation()
if op=='+' :
    result=obj.sum(f_n, s_n)
    print(f'{result}')
elif op=='*':
    result=obj.mul(f_n, s_n)
    print(f'{result}')
elif op=='/': 
    result=obj.div(f_n, s_n)
    print(f'{result}')
else: print('Неизвестная операция')
