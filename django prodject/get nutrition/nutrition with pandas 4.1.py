'''

2023.05.11.14.14.53.660
nutrition with pandas 4.py
    added 
    food_list = []
    food_list.append('apple')
    food_list.append('broccoli')
    food_list.append('chicken')
            name = nutrient['nutrientName']
            value = nutrient['value']
            unit = nutrient['unitName']

replaced
    for result in data['foods'][:20]:
    for
    for result in data['foods']:



'''

import pandas as pd
import requests

api_key = 'wkFMcAoVtbSF0H6WcGcC2gpscOmLKsvWFcF2Kxg2'
food_list = 'Apples'

# food_list.append('Apples')
# food_list.append('Bananas')
# food_list.append('Oranges')


# request = urllib.request.Request('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=Dui2EkKe7wOzTVZOVTVCENxQBchaEqfZmuIneUEA')
# request.add_header('content-type', 'application/json')
# request.data = b'{"query": "banana", "dataType": ["Foundation"]}'
try:

    url = f'htps://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}&query={food_list}'
    print(url)
    response = requests.get(url)

    if response.status_code == 200: #means that the request was successful
        data = response.json()
        food_nutrients = []
        for result in data['foods']:
            nutrients = result['foodNutrients']
            for nutrient in nutrients:
                name = nutrient['nutrientName']
                value = nutrient['value']
                unit = nutrient['unitName']
                food_nutrients.append([name, value, unit])
        df = pd.DataFrame(food_nutrients, columns=['Nutrient Name', 'Value', 'Unit'])
        df.to_csv('banana_nutrition.csv', index=False)
        print('Data saved to banana_nutrition.csv')
    else:
        # print('Error retrieving data')
        print(response.status_code)
    pass

except Exception as e:
    # Print the error message with the error code
    print(f'Error code: {str(e)}\nError message: {e}')
