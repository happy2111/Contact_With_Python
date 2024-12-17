data = [
  {
    "name" : "Tursun",
    "phone" : "+998934445566",
    "email" : "hello@gmail.com",
    "address" : "Tashkent",
  },
  {
    "name" : "Ketmon",
    "phone" : "+998953332211",
    "email" : "ketmon@gmail.com",
    "address" : "Andijon",
  },
]
# вывод
# print(data[0]["name"])
# print(data[1]["name"])

# добавить 
new = {
  "name" : "Teshavoy",
  "phone" : "+998971234567",
  "email" : "tesha@gmail.com",
  "address" : "Navoiy",
}

data.append(new)
# print(data)


# удалить 

# del data[2]
# print(data)


# изменить 

# data[2]["phone"] = "+11234567890"
# print(data)


# искать 
# def search(data, item):
#   print(f"Founding '{item}' ...")
#   for i in range(len(data)):
#     for j in data[i].values():
#       if j.lower() == item.lower():
#         print(f"Founded: {j}")
#       else:
#         print("Not found")
        
      

# item = input("Search: ")
# result = search(data, item)
# print(result)



# Search by name 
# print(data[1]["name"])
# def SearchByName(data, item):
#   for i in range(len(data)):
#     # print(i, "hello")
#     for k in item:
#       print(k)
#     for j in data[i]["name"]:
#       print(j)
#       if j == k:
#         print(f"Founded {data[i]}")


# item = input("Search:  ")
# print(SearchByName(data, item))



# EmailChecker
# def EmailChecker(email):
#   for i in email:
#     if i == "@":
#       return True
#   return False


# print(EmailChecker("hello@gmail.com"))
# print(EmailChecker("helloqweqweq"))




# isDegit 
# print(len("+998934474009"))
# def PhoneChcker(n):
#   status = True
#   if len(n) > 6 and n[0] == "+":
#     for i in range(1, len(n)):
#       if not (n[i] >= '0' and n[i] <= '9'):
#         status = False
#         break
#     return status
#   return False 


# print(PhoneChcker("+998934474009"))
# print(PhoneChcker("+9876543123"))
# print(PhoneChcker("+aaa"))
# print(PhoneChcker("asxdcfvgbhnjm"))
