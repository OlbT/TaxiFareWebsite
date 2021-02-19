import streamlit as st

'''
# TaxiFareModel front
'''
pickup_datetime = st.text_input('pickup_datetime', '2013-07-06 17:18:00 UTC')
pickup_longitude = st.text_input('pickup_longitude', '-73.950655')
pickup_latitude= st.text_input('pickup_latitude', '40.783282')
dropoff_longitude = st.text_input('dropoff_longitude', '-73.984365')
dropoff_latitude = st.text_input('dropoff_latitude', '40.769802')
passenger_count = st.text_input('passenger_count', '1')
st.write('The current movie title is', pickup_datetime)

import requests

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count,
    "key": "2012-10-06%2012:10:20.0000001"
    }

url = f"http://taxifare.lewagon.ai/predict_fare/"

if st.button('click me'):
    # print is visible in server output, not in the page
    print('button clicked!')
    response = requests.get(url, params=params).json()

    ''' le prix de la course est aproximativement : '''
    response['prediction']    
else:
    st.write('I was not clicked 😞')

response = requests.get(url, params=params).json()

''' le prix de la course est aproximativement : '''
response['prediction']










st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''




'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
