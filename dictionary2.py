dictionary = {}

dictionary['name']="ram"
dictionary['age']=18
dictionary['subject']=['math','science','nepali']
dictionary['education'] = {
'school':{
    'name': 'xavier school',
    'address' : 'kalopul,kathmandu'
},
'High school':{'name':'dav college',
               'address': 'jawlakhel,lailtpur'},
'bachelor level':{
    'name':'xavier college',
    'address':'boudha,kathmandu'
    }
} 
print(dictionary)

#for i in dictionary.keys():
#print(i)

#for i in dictionary['subject']:
    #print(i)

#for i in dictionary['education']:
 #   print(i)    

for i ,j in dictionary['education']['school'].items():
    print(i,"=",j)

#dictionary = {keys:{nestkey:{subnestedkey:value}}}
    
print(dictionary['education']['school']['name'])

