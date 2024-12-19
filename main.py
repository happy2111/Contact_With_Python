data = [
  {
    "name" : "Tursun",
    "phone" : "+998934445576",
    "email" : "hello@gmail.com",
    "address" : "Tashkent",
  },
  {
    "name" : "Abdumannop",
    "phone" : "+998953332251",
    "email" : "ketmon@gmail.com",
    "address" : "Andijon",
  },
  {
    "name" : "Toshmurod",
    "phone" : "+9989344869",
    "email" : "tosh@gmail.com",
    "address" : "Qashqa daryo",
  },
  {
    "name" : "Abdumali",
    "phone" : "+9989344888",
    "email" : "tosh@gmail.com",
    "address" : "Qashqa daryo",
  },
  {
    "name" : "Begzod",
    "phone" : "+9989344809",
    "email" : "tosh@gmail.com",
    "address" : "Qashqa daryo",
  },
 
]


def Menyu():
  print("   ***Menyu")
  print("\
        1. Yangi kontakt qo'shish.\n\
        2. Kontaktni yangilash.\n\
        3. Kontaktni o'chirish.\n\
        4. Kontaktni qidirish.\n\
        5. Barcha kontaktlarni ko'rsatish.\n\
        6. Chiqish\n\
        ")


def NameChecker(data, input):
    for i in range(len(data)):
      if data[i]["name"] == input:
        return True
    return False



def PhoneChecker(n):
  status = True
  if len(n) > 6 and n[0] == "+":
    for i in range(1, len(n)):
      if not (n[i] >= '0' and n[i] <= '9'):
        status = False
        break
    return status
  return False 


def EmailChecker(email):
  for i in email:
    if i == "@" and len(email) > 3:
      return True
  return False


def addNewContact(data):
  print("\n\
           ➡ Yandi Kontact qo'shish\n\
        ")
  
  while True:
    name = input("____________ism: ")
    if NameChecker(data, name):
      print("🔺 Siz kiritgan isimlik kontakt mavjut")
    else:
      break

    


  while True:
    phone = input("Telefont raqami: ")
    if PhoneChecker(phone):
      break
    else:
      print("🔺 Telefont raqam 7 tada ko'p bolishi shart, '+' belgisi qatnashishi shart va sonlardan tashkil topgan bo'lishi shart")

  address = input("_________Manzil: ")

  while True:
    email = input("__Email manzili: ")
    if EmailChecker(email):
      break
    else:
      print("🔺 Email da '@' qatnashishi shart va 4 tada belgidan kam bo'lmasligi kerak")


  new_data = {
    "name" : name,
    "phone" : phone,
    "email" : email,
    "address" : address,
  }

  data.append(new_data)
  print("✔ Kontaktga Qo'shildi")


def ChangeContact(data):
  
  print("\n\
          ➡ Kontaktni yangilash\n\
      ")
  summ = 1
  choice = ''
  for i in range(len(data)):
    summ += 1
    name = data[i]["name"]
    print(f"{i + 1}. {name}")
  choice = input(f"\nSiz kimni o'zgartirmoqchisiz (1-{summ - 1}): ")
  while True:
    for j in range(len(data)):
      j_name = data[j]["name"]
      print(j_name)
      if data[int(choice) - 1]["name"] == j_name:
        print("\n1.___________Name: ", data[int(choice) - 1]['name'])
        print("2._Telefont raqam: ", data[int(choice) - 1]['phone'])
        print("3.__________Email: ", data[int(choice) - 1]['email'])
        print("4._________Manzil: ", data[int(choice) - 1]['address'])
        print("5. Chiqish")
        break

    ch_choice = input("\nNimani o'zgartirmoqchisiz (1-5): ")
    
    if ch_choice == "1":
      new_name = input("Yangi ism kiriting: ")
      print(data[int(choice) - 1]["name"])
      data[int(choice) - 1]["name"] = new_name

    if ch_choice == "2":
      while True:
        new_phone = input("Yangi telefon raqam kiriting: ")
        if PhoneChecker(new_phone):
          data[int(choice) - 1]["phone"] = new_phone
          break
        else:
          print("🔺 Telefont raqam 7 tada ko'p bolishi shart, '+' belgisi qatnashishi shart va sonlardan tashkil topgan bo'lishi shart")
    
    if ch_choice == "3":
      while True:
        new_email = input("Yangi email manzil kiriting: ")
        if EmailChecker(new_email):
          data[int(choice) - 1]["email"] = new_email
          break
        else:
          print("🔺 Email da '@' qatnashishi shart va 4 tada belgidan kam bo'lmasligi kerak")
   
    if ch_choice == "4":
      new_address = input("Yangi email manzil kiriting: ")
      data[int(choice) - 1]["address"] = new_address

    if ch_choice >= "6":
      print("🔺 Siz kiritkan bo'lim mavjut emas")

    if ch_choice == "5":
      break


  print("\n✔ O'zgarishlar muvaffaqiyatli saqlandi.\n")
  return


def DelContact(data):
  print("\n\
           ➡ Kontaktni o'chirish.\n\
        ")
  print("          0. ⬅ Orqaga")
  counter = 0
  for i in range(len(data)):
    counter += 1
    name = data[i]["name"]
    print(f"          {i + 1}. {name}")
  choice = int(input(f"Kimni ochirmoqchisiz (0-...{counter}): "))
  for i in range(len(data)):
    name = data[i]["name"]
    if data[choice - 1] == data[i]:
      del data[i]
      print(f"✔ '{name}' ochirildi")
      break
  if choice == 0:
    Menyu()
  return


def SearchByName(data):
  while True:
    print(" #. Orqaga ")
    item = input("Ism kiriting: ")
    for i in range(len(data)):
      name = data[i]["name"]
      if item == name:
        print(f"\n\
            {data[i]["name"]}:\n\
                Tel. raqami: {data[i]["phone"]}\n\
                Email manzil: {data[i]["email"]}\n\
                Manzil: {data[i]["address"]}\n\
                  ")
        break
      j = 0
      while j < len(name):
        if j >= len(item):
          break
        if item[j] == name[j]:
          k = 0
          b = False
          while k < len(item):
            if item[k] == name[k]:
              b = True
            else:
              b = False
            k += 1
          if b:
            print(f"\n\
            {data[i]["name"]}:\n\
                Tel. raqami: {data[i]["phone"]}\n\
                Email manzil: {data[i]["email"]}\n\
                Manzil: {data[i]["address"]}\n\
                  ")
          break
        j += 1
    if item == "#":
      SearchContact(data)
      break    


def SearchByLastNumber(data):
  while True:
    item = input("Oxirgi 2ta raqam kiriting: ")
    for i in range(len(data)):
      phone = f"{data[i]["phone"][-2]}{data[i]["phone"][-1]}" 
      if phone == item:
        print(f"\n\
              {data[i]["name"]}:\n\
                  Tel. raqami: {data[i]["phone"]}\n\
                  Email manzil: {data[i]["email"]}\n\
                  Manzil: {data[i]["address"]}\n\
                    ")
    print("\n\
      #. Orqaga.\n\
      ")
    if item == "#":
      SearchByPhone(data)
      break


def SearchByNumberStandart(data):
  while True:
    print(" #. Orqaga ")
    item = input("Raqam kiriting: ")
    for i in range(len(data)):
      phone = data[i]["phone"]
      if item == phone:
        print(f"\n\
            {data[i]["name"]}:\n\
                Tel. raqami: {data[i]["phone"]}\n\
                Email manzil: {data[i]["email"]}\n\
                Manzil: {data[i]["address"]}\n\
                  ")
        break
      if item in phone:
        print(data[i])  
        
    #   j = 0
    #   while j <= len(phone):
    #     if j >= len(item):
    #       break
    #     if item[j] == phone[j]:
    #       k = 0
    #       b = False
    #       while k < len(item):
    #         if item[k] == phone[k]:
    #           b = True
    #         else:
    #           b = False
    #         k += 1
    #       if b:
    #         print(f"\n\
    #         {data[i]["name"]}:\n\
    #             Tel. raqami: {data[i]["phone"]}\n\
    #             Email manzil: {data[i]["email"]}\n\
    #             Manzil: {data[i]["address"]}\n\
    #               ")
    #       break
    #     j += 1
    if item == "#":
      SearchContact(data)
      break


def SearchByPhone(data):
  print("\n\
        #. Orqaga.\n\
        1. Oxirgi ikitta raqam bo'yicha qidirih.\n\
        2. Standart qidirish.\n\
        ")
  choice = input(": ")
  print("")
  if choice == "1":
    SearchByLastNumber(data)
  elif choice == "2":
    SearchByNumberStandart(data)
  elif choice == "#":
    SearchContact(data)
  else:
    Menyu()

  

def SearchContact(data):
  print("\n\
           ➡ Kontaktni qidirish.\n\
        ")
  print("\n\
        0. ➡ Orqaga\n\
        1. Ism bo'yicha qidirish.\n\
        2. Telefon raqam bo'yicha qidirish.\n\
        ")
  choice = int(input("Son kiriting (0-2): "))
  if choice == 0:
    Menyu()
  elif choice == 1:
    SearchByName(data)
  elif choice == 2:
    SearchByPhone(data)
  return 


def AllContacts(data):
  while True:
    for i in range(len(data)):
      name = data[i]["name"]
      phone = data[i]["phone"]
      email = data[i]["email"]
      address = data[i]["address"]
      print(f"\n\
            {name}:\n\
                Tel. raqami: {phone}\n\
                Email manzil: {email}\n\
                Manzil: {address}\n\
                  ")
    print("\n\
      #. Orqaga.")
    choice = input(": ")
    if choice == "#":
      break
    else:
      break
  return 





while True:
  Menyu()
  menyu_choice = int(input("(1-6) son kiriting: "))
  if menyu_choice == 1:
    addNewContact(data)
  elif menyu_choice == 2:
    ChangeContact(data)
  elif menyu_choice == 3:
    DelContact(data)
  elif menyu_choice == 4:
    SearchContact(data)
  elif menyu_choice == 5:
    AllContacts(data)
  elif menyu_choice == 6:
    break
  elif menyu_choice > 6:
    print("🔺 Siz kiritkan bo'lim mavjut emas")

