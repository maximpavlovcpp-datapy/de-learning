stocks = 'В первую минуту торгов стоимость акций ООО «Крутая Компания» составила 100руб. за бумагу'

start_index = stocks.find('«') + 1  
end_index=stocks.find('»')

company_name = stocks[start_index:end_index]

company_name_upper = company_name.upper()

stocks = stocks.replace(company_name, company_name_upper)

print(stocks)