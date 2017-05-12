fin = open ("map2.map",'r')
fout = open("mapaParsirana.txt",'w')

for line in fin:
    map=line

for i in range (0,1360):
    fout.write("{ 0, 0, 0x03A0, 0 },\n")





for i in range (0,1360):
        fout.write("{ 0, 0, 0x03A0, 0 },\n")


mapa = list(map)

while not len(mapa)==0:
    
    for i in range(0,27):
        fout.write("{ 0, 0, 0x03A0, 0 },\n")
    for i in range(0,26):
        #logika za mapa[i]
        
        if mapa[0]=='4':
                fout.write("{ 1, 0, 0x03B0, 0 },\n")
        elif mapa[0]=='1':
                fout.write("{ 1, 0, 0x03E0, 0 },\n")
        elif mapa[0]=='5':
               fout.write("{ 2, 0, 0x03C0, 0 },\n")
        elif mapa[0]=='2':
                fout.write("{ 0, 0, 0x0420, 0 },\n")
        elif mapa[0]=='3':
                fout.write("{ 0, 0, 0x03D0, 0 },\n")
        else:
                fout.write("{ 0, 0, 0x0400, 0 },\n")
        del mapa[0]

    for i in range(0,27):
        #if i==26:
         #   fout.write("{ 0, 0, 0x03A0, 0 }")
        #else:
            fout.write("{ 0, 0, 0x03A0, 0 },\n")




fout.close()
fin.close()