from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import * 

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = w3.eth.contract(address=address_contract, abi=abi)
account = ''

def log():
    acc = int(input("Введите номер аккаунта: "))
    return acc

# Функция для создания недвижимости
def create_estate(your_account):
    size = int(input("Введите размер недвижимости: "))
    estate_address = input("Введите адрес недвижимости: ")
    es_type = input("Введите тип недвижимости: ")  # например, 'house' или 'apartment'
    contract.functions.createEstate(size, estate_address, es_type).transact({'from': your_account})

# Функция для создания объявления
def create_ad(your_account):
    price = int(input("Введите цену объявления: "))
    id_estate = int(input("Введите ID недвижимости: "))
    ad_status = input("Введите статус объявления: ")  # например, 'active' или 'inactive'
    contract.functions.createAd(price, id_estate, ad_status).transact({'from': your_account})

# Функция для изменения статуса недвижимости
def change_status_estate(your_account):
    id_estate = int(input("Введите ID недвижимости: "))
    contract.functions.changeStatusEstate(id_estate).transact({'from': your_account})

# Функция для изменения статуса объявления
def change_status_ad(your_account):
    id_ad = int(input("Введите ID объявления: "))
    id_estate = int(input("Введите ID недвижимости: "))
    contract.functions.changeStatusAd(id_ad, id_estate).transact({'from': your_account})

# Функция для вывода средств
def withdraw(your_account):
    value = int(input("Введите сумму для вывода: "))
    contract.functions.withDraw(value).transact({'from': your_account})

# Функция для покупки недвижимости
def buy_estate(your_account):
    id_ad = int(input("Введите ID объявления: "))
    contract.functions.buyEstate(id_ad).transact({'from': your_account})

# Функция для получения баланса
def get_balance(your_account):
    balance = contract.functions.getBalance().call({'from': contract})
    return balance

# Функция для получения списка недвижимости
def get_estates(your_account):
    estates = contract.functions.getEstates().call({'from': your_account})
    return estates

# Функция для получения списка объявлений
def get_ads(your_account):
    ads = contract.functions.getAds().call({'from': your_account})
    return ads

# Функция для пополнения баланса
def pay(your_account):
    value = int(input("Введите сумму для пополнения: "))
    contract.functions.pay().transact({'from': your_account, 'value': value})




def main():
    hello = """
Добро пожаловать в систему!
выберите:
1. Авторизация
2. Выход из аккаунта
3. Выход из программы
"""
    account = ''
    while True:
        if account == '' or account == None:
            choise  = int(input(hello))
            match choise:
                case 1:
                    account = log()
                case 2:
                    account = ''
                    main()
                case 3:
                    exit(0)
                case _:
                    print("Выберите число 1 или 2 \n")
        else:
            hello = """
Выберите:
1. Создать недвижимость
2. Создать объявление
3. Изменить статус недвижимости
4. Изменить статус объявления
5. Купить недвижимость
6. Пополнить баланс контракта
7. Снять деньги
8. Вывести баланс контракта
9. Вывести список недвижимости
10. Вывести список объявлений
11. Выйти
"""
            choise  = int(input(hello))
            match choise:
                case 1:
                    create_estate(account)
                case 2:
                    create_ad(account)
                case 3:
                    change_status_estate(account)
                case 4:
                    change_status_ad(account)
                case 5:
                    buy_estate(account)
                case 6:
                    pay(account)
                case 7:
                    withdraw(account)
                case 8:
                    print(get_balance(account))
                case 9:
                    print(get_estates(account))
                case 10:
                    print(get_ads(account))
                case 11:
                    account = ''
                    main()
                case _:
                    print("Выберите число от 1 до 10 \n")

if __name__ == '__main__':
    main()