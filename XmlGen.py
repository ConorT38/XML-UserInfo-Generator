import random

fname = ["Michelle","Phyllis","Sally","Stacey","Macey","Marilyn","Claudette","Claudia","Alannah","Anne","Emma","Emily","Orla","Aoife","Katie","Catherine","Yvonne","Simone","June","Carmel","Maureen","Helen","Lisa","Kym","Mary-Kate","Maggie","Miranda","Kelly","Leiha","Jane","Sarah","Michael","Jackson","Bobby","Billy","Shane","Sean","Graham","David","Niall","Seamus","Cathal","Callum","Karl","Carl","Josh","Joe","Joey","Richard","Dick","George","Alan","Abraham","Bryan","Bob","Barry","Will","Liam","Ben","James","Eric","Abdul"]

lastn = ["Thompson","Carroll","Hynes","Kelly","Ryan","Bachin","Murray","Findon","Strutt","Ramone","Austin","O'Keeffe","O'Brien","Mullen","Fanning","Curran","McNamara"]

phonenum = "3538-{0}"

town = ["Enfield","Newtown","Johnstown","Leixlip","Summerhill","Blancardstown","Clifford","Kilcock","Maynooth","Swords","Carragh","Navan","Trim","Mullingar"]

county = ["Meath","Dublin","Cork","Kilkenny","Cavan","Wicklow","Wexford","WestMeath","Louth","Leitrim","Roscommmon","Galway","Mayo","Clare",]

estate = ["Blackwater","Evergreen","New Inn","Glen Abhainn","Glenroyal","Delmere","NewRoad","Road",]

dig = random.randint(1,120)

age = random.randint(18,90)

xmlnum = 0

while xmlnum < 10000:
    
        f =random.randint(0,61) 
        first = fname[f]
        
        l = random.randint(0,15)
        last = lastn[l]

        num = str(random.randint(1000000, 9999999))
        number =phonenum.format(num)

        t = random.randint(0,12)
        c = random.randint(0,13)
        e = random.randint(0,7)

        to = town[t]
        co = county[c]
        es = estate[e]
                           
        

        
        f = open("C:\\Users\\Conor\\Documents\\xml\\"+str(xmlnum)+number+".xml",'w')
        f.write("<root>\n\n   <user>\n   <fname>\n     "+first+"\n  </fname>\n         <lname>\n          "+last+"\n   </lname>\n              <age>\n                "+str(age)+"\n         </age>\n                   <number>\n                      "+number+"\n            </number>\n                         <address>\n                              "+str(dig)+" "+es+", "+to+", Co."+co+"\n                    <address>\n\n   </user>\n\n</root>")
        f.close()
        
        xmlnum = xmlnum+1
        fil= "{0}.xml has been created."
        print fil.format(xmlnum)

        if xmlnum ==10000:
            print "Done."

        


