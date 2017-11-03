#Created by: Alireza Teimoori
#Created on: 2 Nov 2017
#Created for: ICS3UR-1
#Lesson: Unit_4-02
#This program taked user's address and shows it 


def postage (adress ,city, postal_code, province, apt = ''):
    # prints out mailing address
    
    if(apt == ''):
        print (adress+' '+ city +' '+ postal_code + ' '+province)
    else:
        print(adress+' '+ city +' '+ postal_code + ' '+province +' '+ apt)
        
user_adress = raw_input("enter your adress: ",)
user_apt = raw_input("enter you apartment number if you want: ",)
user_city = raw_input("enter your city: ",)
user_postal_code = raw_input("enter your postal code: ")
user_province = raw_input("enter your province: ",)
postage(user_adress, user_apt, user_city, user_postal_code, user_province)
