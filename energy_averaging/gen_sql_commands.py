if __name__ == '__main__':
    for i in ['100', '200', '300', '400', '500', '600', '700', '800', '900', '1000',
              '2000', '3000', '4000', '5000', '8000', '10000', '15000', '20000', '25000']:
        print('INSERT INTO power_cons_' + i + ' SELECT * FROM household_power_consumption LIMIT ' + i + ';')
