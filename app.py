import streamlit as st
import requests

def get_response(input_data, endpoint_url):
    response = requests.post(endpoint_url, json={'data': input_data})
    return response.json()

def create_ui():
    st.title('Call Any API')
    endpoint_url = st.text_input('Endpoint', 'https://***')
    input_data = st.text_area('Input Data', '***')
    if st.button('Call'):
        # Call the endpoint
        st.write('Response:', get_response(input_data, endpoint_url))

if __name__ == "__main__":
    create_ui()
