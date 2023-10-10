sklad = [
  {"title":"1N4148","počet": 250}, #0
  {"title":"BAV21","počet": 54}, #1
  {"title":"KC147","počet": 147}, #2
  {"title":"2N7002","počet": 97}, #3
  {"title":"BC547C","počet": 10}, #4
]

kod = input("jaký je kod součástky")

if kod == sklad[0]["title"]:
    počet = int(input("jaký počet součástek by jste chtěli ?"))
    if počet > sklad[0]["počet"]:
        print(f"součastek je pouze {sklad[0]['počet']} ")
    elif počet <= sklad[0]["počet"]:
        print(f"součastek je dostatek")
        sklad[0]['počet'] = sklad[0]['počet'] - počet
        print(f"součastek je niní{sklad[0]['počet']}")

elif kod == sklad[1]["title"]:
    počet = int(input("jaký počet součástek by jste chtěli ?"))
    if počet > sklad[1]["počet"]:
        print(f"součastek je pouze {sklad[1]['počet']} ")
    elif počet <= sklad[1]["počet"]:
        print(f"součastek je dostatek")
        sklad[1]['počet'] = sklad[1]['počet'] - počet
        print(f"součastek je niní{sklad[1]['počet']}")

elif kod == sklad[2]["title"]:
    počet = int(input("jaký počet součástek by jste chtěli ?"))
    if počet > sklad[2]["počet"]:
        print(f"součastek je pouze {sklad[2]['počet']} ")
    elif počet <= sklad[2]["počet"]:
        print(f"součastek je dostatek")
        sklad[2]['počet'] = sklad[2]['počet'] - počet
        print(f"součastek je niní{sklad[2]['počet']}")

elif kod == sklad[3]["title"]:
    počet = int(input("jaký počet součástek by jste chtěli ?"))
    if počet > sklad[3]["počet"]:
        print(f"součastek je pouze {sklad[3]['počet']} ")
    elif počet <= sklad[3]["počet"]:
        print(f"součastek je dostatek")
        sklad[3]['počet'] = sklad[3]['počet'] - počet
        print(f"součastek je niní{sklad[3]['počet']}")

elif kod == sklad[4]["title"]:
    počet = int(input("jaký počet součástek by jste chtěli ?"))
    if počet > sklad[4]["počet"]:
        print(f"součastek je pouze {sklad[4]['počet']} ")
    elif počet <= sklad[4]["počet"]:
        print(f"součastek je dostatek")
        sklad[4]['počet'] = sklad[4]['počet'] - počet
        print(f"součastek je niní{sklad[4]['počet']}")
else:
    print(f"{kod} není na skladě")