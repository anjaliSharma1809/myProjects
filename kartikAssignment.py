import requests
import sys

def helpMessage():
    print("Please enter the right arguments")
    print("Try python kartikAssignment.py help")

try:
    city=  sys.argv[1]
    if(sys.argv[1]=="help"):
        print("Enter the city name and number of hours in arguments")
        print("Example: python kartikAssignment.py Frankfurt 2")
    
    elif(len(sys.argv)!=3):
        helpMessage()

    else:
        hours = sys.argv[2]    
        try:
            table_data=[['Date','Time','Weather','Temperature '+"\u00b0"+"C",'Wind Speed (m/sec)']]
            if(int(hours)<48):
                
                api_key = 'b5771197a2ff4d9cb8e5f4edf369d326'
                api_url ="https://api.weatherbit.io/v2.0/forecast/hourly?city="+city+"&key="+api_key+"&hours=" + hours

                response = requests.get(api_url)
                jsonResponse = response.json()

                for i in range(int(hours)):
                    table_data.append([jsonResponse['data'][i]['timestamp_local'].split('T')[0],jsonResponse['data'][i]['timestamp_local'].split('T')[1],
                        jsonResponse['data'][i]['weather']['description'],
                    jsonResponse['data'][i]['temp'],jsonResponse['data'][i]['wind_spd']])
                
                print("\n","*"*30,  "Forecast Data","*"*30 ,"\n\n")
                print("City Name :",city, "\nNumber of future Hours Forecasted :", hours,"\n\n\n")                           
                for row in table_data:
                    print("{:>10} {:>10} {:>20} {:>20} {:>20}".format(*row))
            else:
                print("Please Enter Less than 48 Hours")   
        except:
            print("\n\nError : Please enter right credentials")
except:
    helpMessage()
    



    
