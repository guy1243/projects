country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'
                }

print(country_code.get('India'), "\n")

print(country_code.get('Israel', 'not found'))