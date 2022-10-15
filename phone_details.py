from phonenumbers import carrier,geocoder,timezone
import phonenumbers

num = input("Enter a number with +__ :")
phone = phonenumbers.parse(num)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)