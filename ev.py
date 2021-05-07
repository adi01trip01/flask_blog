import os

os.environ['API_USER'] = 'SuperUser'
os.environ['API_PASSWORD'] = 'CIAArea51'

a = os.getenv('API_USER')
b = os.environ.get('API_PASSWORD')
print(a, b)
