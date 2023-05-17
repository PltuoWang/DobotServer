import Port30004 as Pt34

Dobot=Pt34.Dobot30004('192.168.168.1') #Dobot IP
TcpPos=Dobot.realtime('ToolVectorActual')
print(TcpPos)