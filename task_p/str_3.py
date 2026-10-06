stocks = 'В первую минуту торгов стоимость акций ООО «Крутая Компания» составила 100руб. за бумагу'
company_name = stocks.find('«')
end_company_name=stocks.find('составила')
print(stocks[company_name : end_company_name])