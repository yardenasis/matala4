import requests
try:
    file=open("dests.txt",encoding = 'utf8')
    city_list = dict()

    for line in file:
        target=line
        base='תל אביב'
        key="AIzaSyD1RlA8EeE-udEFdfGNfEEzDvrTggGNquQ"
        url_geo="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (target,key)
        response1=requests.get(url_geo).json()
        place=response1['results'][0]['geometry']['location']
        lng=place['lng']
        lat=place['lat']
        url_dis='https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=%s&destinations=%s&key=%s' %(base,target,key)
        response=requests.get(url_dis).json()
        distance=response['rows'][0]['elements'][0]['distance']['text']
        duration=response['rows'][0]['elements'][0]['duration']['text']
        tup=(distance,duration,lat,lng)
        city_list[target]=tup
    import json
    printing_the_data=json.dumps(city_list,ensure_ascii=False,indent=4).encode('utf8')
    print(printing_the_data.decode())

    longest_distance= sorted(city_list,key=city_list.get,reverse=True)[:3]
    print(longest_distance)
except:
    print("משהו השתבש ,אנא נסה שנית")