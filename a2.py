s1 =[2,3,1]
s2 =['b' 'a' 'c']
s3 =list(zip(s1,s2))
print(s3,"\n")

#part2
stock=['reliance' 'infosys' 'tcs']
price=[2175,1127,2750]

new_dict = {stock: prices for stock,
            prices in zip(stock, prices)}
print('\n{}'.format(new_dict))