import requests
url = 'http://photon.bits-goa.ac.in/lms/login/index.php'
values = {'username': '31120150591',
          'password': '@Mayank26'}

r = requests.post(url, data=values)
print (r.content)


