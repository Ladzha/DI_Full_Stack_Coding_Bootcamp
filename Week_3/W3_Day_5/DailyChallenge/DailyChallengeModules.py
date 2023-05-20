def time_to_response(site):
    import requests
    import time
    time_before = time.time()
    # print(time_before)
    response=requests.get(site)
    # print(response)
    time_after = time.time()
    # print(time_after)
    duration=time_after-time_before 
    string = f'It takes {duration} second to get response from {site}'
    print(string)

time_to_response('https://www.google.com/')
time_to_response('https://www.ynet.co.il/home/0,7340,L-8,00.html')
time_to_response('https://www.imdb.com/')