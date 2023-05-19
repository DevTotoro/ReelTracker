import requests

class Authentication:
    # attributes
    url = 'http://2.84.243.5:5000'
    token = ''
    
    def login(self,username,password):
        
        # object with credentials
        data = {
            'username': username,
            'password': password
        }
        
        # Send POST request to the login API
        response = requests.post(self.url+'/login', json=data)
        
        # json
        json_data = response.json()

        # Check the response status code and message
        if response.status_code == 200:
            print('Login Successful') 
            self.token = json_data['token']
            return 1
            
        elif response.status_code == 401:
            print('Invalid username or password')
            return 0
            
        else:
            return 0
            
    def register(self,username,password,email):
        # Registration data
        data = {
            'username': username,
            'password': password,
            'email': email
        }
        
        # Send POST request to the registration API
        response = requests.post(self.url+'/register', json=data)

        # Check the response status code and message
        if response.status_code == 201:
            print('Registration successful')
            return 1
        else:
            print('Invalid Username Or Password')
            return 0
        
    def token_authentication(self):
        # Token
        headers = {
            'Authorization': self.token
        }
        
        # Send GET request to the login API
        response = requests.get(self.url+'/token_authentication', headers=headers)

        # Check the response status code and message
        if response.status_code == 200:
            print('Authentication Successful')
            return 1
        elif response.status_code == 401:
            print('Invalid Token')
            return 0
        else:
            return 0