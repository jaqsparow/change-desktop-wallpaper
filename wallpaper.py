"""
Author: Javed Shaikh
Purpose: A CLI APP to change desktop wallpaper every minute or so
Usage: wallpaper.py -t <time to change wallpaper in minutes>

Example: To change wallpaper every 2 minutes :
C:\Users\jaqsp>wallpaper.py -t 2
"""
import requests,argparse,time
import ctypes,win32con,os,random

def get_wallpaper():
    #Set your api key here
    #Get your api key at https://www.pexels.com/api/new/
    payload = {'Authorization': '<Your API KEY FOR PEXELS>'}

    #Random number
    num = random.randint(1,99)
    #Search query
    query = 'flower'
    #URL for PEXELS
    url = 'https://api.pexels.com/v1/search?per_page=1&page=' + str(num) + '&query=' + query
    #Make request to pexels to get the photo response object
    res = requests.get(url, headers=payload)

    #Get the url of the image from the response
    if res.status_code == 200:
        img_url = res.json().get('photos')[0]['src']['original']
        #Make request to get the image
        img = requests.get(img_url)
        #Write and save the imgae locally with name temp.jpg
        with open('temp.jpg', 'wb') as f:
            f.write(img.content)
    else:
        print('error in making http request')
def set_wallpaper():
    get_wallpaper()
    path = os.getcwd()+'\\temp.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", help="Enter time in minutes")

    args = parser.parse_args()
    minute = int(args.time)
    while(True):
        time.sleep(minute*60)
        set_wallpaper()
