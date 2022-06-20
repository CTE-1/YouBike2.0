import requests

web='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
data=requests.get(web)
data=data.json()
#print(data)

print("\nYoubike 2.0 及時資訊")

str=''
while str != 'Q':
  str=input("\n0:目前有車的站, 1:查詢車站空位, 2:查詢車站Youbike剩餘數量 (按Q離開)")
  
  if str=="0":
    print("\n您要查詢的是目前有車的車站...")
    temp=input("0:查詢地區, 1:不查詢地區")
    if temp=="1":
      for i in data:
        if i['sbi']!=0:
          print("-------------------------------------")
          print("站名 : "+i['sna'])
          print("地區 : "+i['sarea'])
          print("剩餘數量 : ",i['sbi'])
    else:
      area=input("請輸入地區(Ex:松山區)")
      flag=0
      for i in data:
        if i['sbi']!=0 and i['sarea']==area:
          print("-------------------------------------")
          print("站名 : "+i['sna'])
          print("地區 : "+i['sarea'])
          print("剩餘數量 : ",i['sbi'])
          flag=1
      if flag==0:
        print("沒有此區")
  
  if str=="1":
    print("\n您要查詢的是車站空位...")
    temp=input("請輸入站名(Ex:YouBike2.0_濱江果菜市場)")
    flag=0
    for i in data:
        if i['sna']==temp:
          print("-------------------------------------")
          print("站名 : "+i['sna'])
          print("地區 : "+i['sarea'])
          print("空位數量 : ",i['tot']-i['sbi'])
          flag=1
    if flag==0:
      print("沒有此站")
      
  if str=="2":
    print("\n您要查詢的是車站Youbike剩餘數量...")
    temp=input("請輸入站名(Ex:YouBike2.0_濱江果菜市場)")
    flag=0
    for i in data:
        if i['sna']==temp:
          print("-------------------------------------")
          print("站名 : "+i['sna'])
          print("地區 : "+i['sarea'])
          print("剩餘數量 : ",i['sbi'])
          flag=1
    if flag==0:
      print("沒有此站")
  