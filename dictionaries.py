import urllib.request

def access(url):
    ''' Reads the source code of a web page
    Returns the source code as a string
    '''
    page = urllib.request.urlopen(url) # access the web page
    global source_code
    source_code = page.read() # read the page as bytes
    source_code = str(source_code) # convert to string
    return source_code

print("Your Weather Report")
print()
print("Current observations are available for:")
print("- New York")
print("- Miami")
print("- Nashville")
print("- Los Angeles")
print()
city_xml={"New York":"https://w1.weather.gov/xml/current_obs/display.php?stid=KJRB",
            "Miami":"https://w1.weather.gov/xml/current_obs/KMIA.xml",
            "Nashville":"https://w1.weather.gov/xml/current_obs/KBNA.xml",
            "Los Angeles":"https://w1.weather.gov/xml/current_obs/display.php?stid=KLAX"}


city_input=input("Enter the city you would like a weather report for: ")

while True:
    if city_input in city_xml:
        print("Accessing weather data...")
        print()
        access(city_xml[city_input])
        print("The current weather has been accessed for",city_input)


        #Dictionary without values
        weather_data={"location":'',
                      "weather":'',
                      "temperature":'',
                      "humidity":'',
                      "wind":'',
                      "observation":''}

        #Extracting location and adding it in the dictionary
        splitdata1=source_code.split("location")
        data1=splitdata1[1]
        location=data1[1:len(data1)-2:]
        weather_data["location"]=location
        

        #Extracting weather and adding it in the dictionary
        splitdata2=source_code.split("weather")
        data2=splitdata2[5]
        weather=data2[1:len(data2)-2:]
        
        weather_data["weather"]=weather.lower()

        
        #Extracting temperature and adding it in the dictionary
        splitdata3=source_code.split("temp_f")
        data3=splitdata3[1]
        temperature_f=data3[1:len(data3)-2:]
        
        weather_data["temperature"]=temperature_f+" degrees F"
        

        #Extracting humidty and adding it in the dictionary
        splitdata4=source_code.split("relative_humidity")
        data4=splitdata4[1]
        humidity=data4[1:len(data4)-2:]+"%"
        
        weather_data["humidity"]=humidity
        
        #Extracting wind info and adding it in the dictionary
        splitdata5a=source_code.split("wind_dir")
        data5a=splitdata5a[1]
        wind_direction=data5a[1:len(data5a)-2:].lower()

        
        splitdata5b=source_code.split("wind_mph")
        data5b=splitdata5b[1]
        wind_mph=data5b[1:len(data5b)-2:]

        splitdata5c=source_code.split("wind_kt")
        data5c=splitdata5c[1]
        wind_kt=data5c[1:len(data5c)-2:]

        weather_data["wind"]=wind_direction+" at "+wind_mph+"MPH ( "+wind_kt+" KT )"

        #Extracting date and time of the observation and adding it in the dictionary
        splitdata6=source_code.split("observation_time")
        data6=splitdata6[1]
        observation=data6[1:len(data6)-2:]

        weather_data["observation"]=observation
        
        """Check dictionary through
        print(weather_data)"""

        #LIST OF INFO AVIALABLE
        print()
        print("Information Available")
        print("-location")
        print("-weather")
        print("-temperature")
        print("-humidity")
        print("-wind")
        print("-observation")
        print()
        
        #PROMPTING THE USER FOR WHAT INFO
        
        user_info=input("What weather information would you like? ")

        while True:
            
            if user_info in weather_data:
                print("The",user_info,"in",city_input,"is",weather_data[user_info])
                print()
                user_info=input('What weather information would you like? Or to end, enter "done". ')
            elif user_info=="done":

                #PART 4- option to print the full weather report to an external text file
                print()
                user_report=input("Would you like to export the full weather report? (yes/no) ")
                if user_report=="yes":
                    file_object=open("weather."+city_input+".txt","w")
                    file_object.write("Weather for "+city_input)
                    file_object.write("\n")
                    file_object.write("\n")
                    alldata=''
                    for key,value in weather_data.items():
                        alldata=alldata+key+": "+value+"\n"
                    file_object.write(alldata)
                    file_object.close()
                    print("The full weather report has been exported.")
                    break
                elif user_report=="no":
                    break
            else:
                print("That data is not available.")
                print()
                user_info=input('What weather information would you like? Or to end, enter "done". ')
                
                
        break


    else:
        print("No data available.",end='')
        city_input=input("Please try another city: ")
        True
         



