import sys
from enchant.checker import SpellChecker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting some initial variables...
result =[0,0,0,0,0,0,0,0,0,0,0]				#list to store result of test	-1=no test yet 0=fail 1=pass
spellCorrect =True		# assuming initially no spelling mistakes
total_mis_spells=0		# variable to hold total number of mis-spells
chkr = SpellChecker("en_US")
# adding some ignore words in dictionary...
chkr.ignore_always('Lenz');chkr.ignore_always('lenz')
chkr.ignore_always('GUWAHATI');chkr.ignore_always('guwahati')
chkr.ignore_always('Shakshat');chkr.ignore_always('shakshat')
chkr.ignore_always('MCB')
chkr.ignore_always('IIT');chkr.ignore_always('iit')
chkr.ignore_always('Behaviour');chkr.ignore_always('behaviour')
chkr.ignore_always('CSE');chkr.ignore_always('cse');
driver=webdriver.Firefox()			
wait = WebDriverWait(driver, 120)		# seeting wait time for firefox to be 120 seconds

def find(xpath):						# a function to find web-elements 
	try:
		element = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
		return element
	except:
		print 'element with xpath =',xpath,'not found or the your net connection is slow'
		sys.exit()

# Testing : Magnetic Field Behaviour in Single Coil Experiment =>
print '\n'
print 'Testing : Magnetic Field Behaviour in Single Coil Experiment =>'
driver.get('http://vem-iitg.vlabs.ac.in/Magnetic_Field_Behaviour_in_single_coil.html')
#testing introduction page
print 'On Introduction Page : '
x = find('/html/body/div/div[3]/div/div[1]/ul/li[1]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of introduction
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[0]=-1;
else:
		result[0]=1;	
total_mis_spells =total_mis_spells + mis_spells

#tesing theory page
print 'On Theory Page : '
x=find('/html/body/div/div[3]/div/div[1]/ul/li[2]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of theory
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[1]=-1;
else:
		result[1]=1;	
total_mis_spells =total_mis_spells + mis_spells
#now checking links....
sucess=True
x = find('/html/body/div/div[3]/div/div[2]/p[7]/a/b')
x.click()
x = driver.current_url
check ='http://vem-iitg.vlabs.ac.in/images/link1.jpg'
if(driver.current_url != check):
	print '	link with href=',check,'not working properly' 
	sucess=False
else:
	print '	link with href=',check,'working properly'
driver.back()
if sucess == False:
		result[2] = -1
else:
		result[2]=1
		print 	'	All links working properly'	

#now going to procedure page
print('On procedure page')
x = find('/html/body/div/div[3]/div/div[1]/ul/li[3]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of procedure
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[3] = -1
else:
		result[3] = 1
#now checking links
sucess=True
x = find('/html/body/div/div[3]/div/div[2]/p[14]/a')
x.click()
check ='https://www.youtube.com/watch?v=WArVrQHXLCc'
if(driver.current_url != check):
	print '	link with href=',check,'not working properly' 
	sucess=False
else:
	print '	link with href=',check,'working properly' 
driver.back()
x = find('/html/body/div/div[3]/div/div[2]/p[15]/a')
x.click()
check = 'https://www.youtube.com/watch?v=V7kVdELtX5M'
if(driver.current_url != check):
	print '	link with href=',check,'not working properly' 
	sucess=False
else:
	print '	link with href=',check,'working properly' 
driver.back()

if sucess == False:
		result[4] = -1
else:

		result[4]=1
		print 	'	All links working properly'	

		
#now going to simulator 1 
print 'On Simulator of Exp 1  : '
x = find('/html/body/div/div[3]/div/div[1]/ul/li[4]/a/h6')
x.click()
x = driver.current_url
check ='http://vem-iitg.vlabs.ac.in/Magnetic_Field_Behaviour_in_single_coil(experiment1).html'
if(x == check):
	print '	simulator for Exp : working'
	result[5]=1
else:
	print '	simulator for Exp not working'
	result[5]=-1
		
#now going to simulator 2
print 'On Simulator of Exp 2  : '
x = find('/html/body/div/div[3]/div/div[1]/ul/li[5]/a/h6')
x.click()
x = driver.current_url
check ='http://vem-iitg.vlabs.ac.in/Magnetic_Field_Behaviour_in_single_coil(experiment2).html'
if(x == check):
	print '	simulator for Exp : working'
	result[6]=1
else:
	print '	simulator for Exp not working'
	result[6]=-1

	
#now going to quiz page
print 'on quiz page :'
x=find('/html/body/div/div[3]/div/div[1]/ul/li[6]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of quiz
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[7] = -1
else:
		result[7] = 1
x= find('/html/body/div/div[3]/div/div/div[2]/form/div/div[2]/input[2]')
x.click()
x= find('/html/body/div/div[3]/div/div/div[2]/form/div/input[3]')	#clicking on submit button
x.click()
x = find('/html/body/div/div[3]/div/div/div[2]/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/tick.gif.jpg':
	result[8]=1
else :
	result[8]=-1
driver.refresh();		#refreshing page
x = find('/html/body/div/div[3]/div/div/div[2]/form/div/div[2]/input[1]')
x.click()
x= find('/html/body/div/div[3]/div/div/div[2]/form/div/input[3]')	#clicking on submit button
x.click()
x = find('/html/body/div/div[3]/div/div/div[2]/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[9]=1
else :
	result[9]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div/div[3]/div/div/div[2]/form/div/input[3]')	#clicking on submit button
x.click()
x = find('/html/body/div/div[3]/div/div/div[2]/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[10]=1
else :
	result[10]=-1

print 'Final Report : '	
testname = 	'Magnetic_Field_Behaviour_in_Single_Coil_02_Introduction'
if result[0] == 1:
		print testname,'passed'
elif result[0] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Magnetic_Field_Behaviour_in_Single_Coil_03_theory_p1'
if result[1] == 1:
		print testname,'passed'
elif result[1] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Magnetic_Field_Behaviour_in_Single_Coil_04_theory _p2'
if result[2] == 1:
		print testname,'passed'
elif result[2] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Magnetic_Field_Behaviour_in_Single_Coil_05_Procedure_p1'
if result[3] == 1:
		print testname,'passed'
elif result[3] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Magnetic_Field_Behaviour_in_Single_Coil_06_Procedure_p2'
if result[4] == 1:
		print testname,'passed'
elif result[4] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Magnetic_Field_Behaviour_in_Single_Coil_07_Simulator1'
if result[5] == 1:
		print testname,'passed'
elif result[5] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Magnetic_Field_Behaviour_in_Single_Coil_08_Simulator2'
if result[6] == 1:
		print testname,'passed'
elif result[6] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Magnetic_Field_Behaviour_in_Single_Coil_09_quiz_p1'
if result[7] == 1:
		print testname,'passed'
elif result[7] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Magnetic_Field_Behaviour_in_Single_Coil_10_quiz_p2'
if result[8] == 1:
		print testname,'passed'
elif result[8] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Magnetic_Field_Behaviour_in_Single_Coil_11_quiz_p3'
if result[9] == 1:
		print testname,'passed'
elif result[9] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'	
	
testname = 	'Magnetic_Field_Behaviour_in_Single_Coil_12_quiz_p4'
if result[10] == 1:
		print testname,'passed'
elif result[10] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'	


#Testing : Rotating Magnetic Field Behaviour in two coils =>
result =[0,0,0,0,0,0,0,0,0,0,0]				#list to store result of test	-1=no test yet 0=fail 1=pass
spellCorrect =True		# assuming initially no spelling mistakes
total_mis_spells=0		# variable to hold total number of mis-spells

print 'Testing : Rotating Magnetic Field Behaviour in two coils =>'
driver.get('http://vem-iitg.vlabs.ac.in/Rotating%20Magnetic%20Field%20Behaviour%20in%20two%20coils.html')

#testing introduction page
print 'On Introduction Page : '
x = find('/html/body/div/div[3]/div/div[1]/ul/li[1]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of introduction
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[0]=-1;
else:
		result[0]=1;	
total_mis_spells =total_mis_spells + mis_spells

#tesing theory page
print 'On Theory Page : '
x=find('/html/body/div/div[3]/div/div[1]/ul/li[2]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of theory
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[1]=-1;
else:
		result[1]=1;	
total_mis_spells =total_mis_spells + mis_spells
#now chking links....
sucess=True
x = find('/html/body/div/div[3]/div/div[2]/p[4]/a/b')
x.click()
if(driver.current_url != 'http://vem-iitg.vlabs.ac.in/images/wave10.gif'):
	print '	link with href=http://vem-iitg.vlabs.ac.in/images/wave10.gif  not working properly' 
	sucess=False
else:
	print '	link with href=http://vem-iitg.vlabs.ac.in/images/wave10.gif  working properly' 
driver.back()
x = find('/html/body/div/div[3]/div/div[2]/p[5]/a/b')
x.click()
if(driver.current_url != 'http://vem-iitg.vlabs.ac.in/images/wave11.gif'):
		print '	link with href=http://vem-iitg.vlabs.ac.in/images/wave11.gif not working properly' 
		sucess=False
else:
		print '	link with href=http://vem-iitg.vlabs.ac.in/images/wave11.gif   working properly' 
driver.back()
x = find('/html/body/div/div[3]/div/div[2]/p[6]/a/b')
x.click()
if(driver.current_url != 'http://vem-iitg.vlabs.ac.in/images/wave12.gif'):
		print '	link with href=http://vem-iitg.vlabs.ac.in/images/wave12.gif  not working properly' 		
		sucess=False
else:
		print '	link with href=http://vem-iitg.vlabs.ac.in/images/wave12.gif   working properly' 		
driver.back()
x = find('/html/body/div/div[3]/div/div[2]/p[7]/a/b')
x.click()
if(driver.current_url != 'http://vem-iitg.vlabs.ac.in/images/rotating_two_coil_img.gif'):
		print '	link with href=http://vem-iitg.vlabs.ac.in/images/rotating_two_coil_img.gif not working properly' 				
		sucess=False
else:
		print '	link with href=http://vem-iitg.vlabs.ac.in/images/rotating_two_coil_img.gif  working properly' 					
		driver.back()
if sucess == False:
		result[2] = -1
else:

		result[2]=1
		print 	'	All links working properly'	

#now going to procedure page
print('On procedure page')
x = find('/html/body/div/div[3]/div/div[1]/ul/li[3]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of procedure
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[3] = -1
else:
		result[3] = 1
#now checking links
sucess=True
x = find('/html/body/div/div[3]/div/div[2]/p[8]/a')
x.click()
if(driver.current_url != 'https://www.youtube.com/watch?v=bnnKPv28Jvw'):
	print '	link with href=https://www.youtube.com/watch?v=bnnKPv28Jvw  not working properly' 
	sucess=False
else:
	print '	link with href=https://www.youtube.com/watch?v=bnnKPv28Jvw  working properly' 
driver.back()
if sucess == False:
		result[4] = -1
else:

		result[4]=1
		print 	'	All links working properly'	

#now going to simulator page
print 'On Simulator of Exp  : '
x = find('/html/body/div/div[3]/div/div[1]/ul/li[4]/a/h6')
x.click()
x = driver.current_url
if(x == 'http://vem-iitg.vlabs.ac.in/Rotating%20Magnetic%20Field%20Behaviour%20in%20two%20coils(experiments).html'):
	print '	simulator for Exp : working'
	result[5]=1
else:
	print '	simulator for Exp not working-'
	result[5]=-1

#now going to quiz page
print 'on quiz page :'
x=find('/html/body/div/div[3]/div/div[1]/ul/li[5]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of quiz
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[6] = -1
else:
		result[6] = 1
x= find('/html/body/div/div[3]/div/div[2]/form/div/div[2]/input[1]')
x.click()
x= find('/html/body/div/div[3]/div/div[2]/form/input')	#clicking on submit button
x.click()
x = find('/html/body/div/div[3]/div/div[2]/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/tick.gif.jpg':
	result[7]=1
else :
	result[7]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div/div[3]/div/div[2]/form/div/div[2]/input[2]')
x.click()
x= find('/html/body/div/div[3]/div/div[2]/form/input')	#clicking on submit button
x.click()
x = find('/html/body/div/div[3]/div/div[2]/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[8]=1
else :
	result[8]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div/div[3]/div/div[2]/form/input')	#clicking on submit button
x.click()
x = find('/html/body/div/div[3]/div/div[2]/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[9]=1
else :
	result[9]=-1
	

print 'Final Report : '	
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_02_introduction'
if result[0] == 1:
		print testname,'passed'
elif result[0] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_03_theory_p1'
if result[1] == 1:
		print testname,'passed'
elif result[1] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_04_theory_p2'
if result[2] == 1:
		print testname,'passed'
elif result[2] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_05_procedure_p1'
if result[3] == 1:
		print testname,'passed'
elif result[3] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_06_procedure_p2'
if result[4] == 1:
		print testname,'passed'
elif result[4] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_07_simulator'
if result[5] == 1:
		print testname,'passed'
elif result[5] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_08_quiz_p1'
if result[6] == 1:
		print testname,'passed'
elif result[6] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_09_quiz_p2'
if result[7] == 1:
		print testname,'passed'
elif result[7] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_10_quiz_p3'
if result[8] == 1:
		print testname,'passed'
elif result[8] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_11_quiz_p4'
if result[9] == 1:
		print testname,'passed'
elif result[9] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'	

#Testing : Rotating Magnetic Field Behaviour in three coils =>
result =[0,0,0,0,0,0,0,0,0,0,0]				#list to store result of test	-1=no test yet 0=fail 1=pass
spellCorrect =True		# assuming initially no spelling mistakes
total_mis_spells=0		# variable to hold total number of mis-spellsprint ''

print 'Testing : Rotating Magnetic Field Behaviour in three coils =>'
driver.get('http://vem-iitg.vlabs.ac.in/Rotating%20Magnetic%20Field%20Behaviour%20in%20three%20coils.html')

#testing introduction page
print 'On Introduction Page : '
x = find('/html/body/div/div[3]/div/div[1]/ul/li[1]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of introduction
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[0]=-1;
else:
		result[0]=1;	
total_mis_spells =total_mis_spells + mis_spells

#tesing theory page
print 'On Theory Page : '
x=find('/html/body/div/div[3]/div/div[1]/ul/li[2]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of theory
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[1]=-1;
else:
		result[1]=1;	
total_mis_spells =total_mis_spells + mis_spells
#now chking links....
sucess=True
x = find('/html/body/div[1]/div[3]/div/div[2]/p[48]/a[1]/b')
x.click()
x=driver.current_url
if(x != 'http://vem-iitg.vlabs.ac.in/images/wave.gif'):
	print '	link with href=http://vem-iitg.vlabs.ac.in/images/wave.gif  not working properly' 
	sucess=False
else:
	print '	link with href=http://vem-iitg.vlabs.ac.in/images/wave.gif  working properly' 
driver.back()
x = find('/html/body/div[1]/div[3]/div/div[2]/p[48]/a[2]/b')
x.click()
x= driver.current_url
if(x != 'http://vem-iitg.vlabs.ac.in/images/wave2.gif'):
		print '	link with href=http://vem-iitg.vlabs.ac.in/images/wave2.gif not working properly' 
		sucess=False
else:
		print '	link with href=http://vem-iitg.vlabs.ac.in/images/wave2.gif   working properly' 
driver.back()
if sucess == False:
		result[2] = -1
else:

		result[2]=1
		print 	'	All links working properly'	

#now going to procedure page
print('On procedure page')
x = find('/html/body/div/div[3]/div/div[1]/ul/li[3]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of procedure
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[3] = -1
else:
		result[3] = 1
#now checking links
sucess=True
x = find('/html/body/div/div[3]/div/div[2]/p[8]/a')
x.click()
x = driver.current_url
check = 'https://www.youtube.com/watch?v=G0wGc85BTcI'
if(x != check):
	print '	link with href=',check,' not working properly' 
	sucess=False
else:
	print '	link with href=',check,'  working properly' 
driver.back()
if sucess == False:
		result[4] = -1
else:

		result[4]=1
		print 	'	All links working properly'	

#now going to simulator page
print 'On Simulator of Exp  : '
x = find('/html/body/div/div[3]/div/div[1]/ul/li[4]/a/h6')
x.click()
x = driver.current_url
check = 'http://vem-iitg.vlabs.ac.in/Rotating_Magnetic_Field_Behaviour_in_three_coils(experiments).html'
if(x == check):
	print '	simulator for Exp : working'
	result[5]=1
else:
	print '	simulator for Exp not working'
	result[5]=-1

#now going to quiz page
print 'on quiz page :'
x=find('/html/body/div/div[3]/div/div[1]/ul/li[5]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of quiz
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[6] = -1
else:
		result[6] = 1
x= find('/html/body/div[1]/div[3]/div[1]/div[2]/form/div/div[2]/input[1]')
x.click()
x= find('/html/body/div[1]/div[3]/div[1]/div[2]/form/input')	#clicking on submit button
x.click()
x = find('/html/body/div[1]/div[3]/div[1]/div[2]/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/tick.gif.jpg':
	result[7]=1
else :
	result[7]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div[1]/div[3]/div[1]/div[2]/form/div/div[2]/input[2]')
x.click()
x= find('/html/body/div[1]/div[3]/div[1]/div[2]/form/input')	#clicking on submit button
x.click()
x = find('/html/body/div[1]/div[3]/div[1]/div[2]/form/div/div[1]/img[1]')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[8]=1
else :
	result[8]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div[1]/div[3]/div[1]/div[2]/form/input')	#clicking on submit button
x.click()
x = find('/html/body/div[1]/div[3]/div[1]/div[2]/form/div/div[1]/img[1]')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[9]=1
else :
	result[9]=-1
	


print 'Final Report : '	
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_02_introduction'
if result[0] == 1:
		print testname,'passed'
elif result[0] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_03_theory_p1'
if result[1] == 1:
		print testname,'passed'
elif result[1] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_04_theory_p2'
if result[2] == 1:
		print testname,'passed'
elif result[2] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_05_procedure_p1'
if result[3] == 1:
		print testname,'passed'
elif result[3] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_06_procedure_p2'
if result[4] == 1:
		print testname,'passed'
elif result[4] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_07_simulator'
if result[5] == 1:
		print testname,'passed'
elif result[5] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_08_quiz_p1'
if result[6] == 1:
		print testname,'passed'
elif result[6] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_09_quiz_p2'
if result[7] == 1:
		print testname,'passed'
elif result[7] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Rotating_Magnetic_Field_Behaviour_in_two_coils_10_quiz_p3'
if result[8] == 1:
		print testname,'passed'
elif result[8] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Rotating_Magnetic_Field_Behaviour_in_three_coils_11_quiz_p4'
if result[9] == 1:
		print testname,'passed'
elif result[9] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'		
		
		
# Testing : The DC Test for Stator Resistance =>
result =[0,0,0,0,0,0,0,0,0,0,0]				#list to store result of test	-1=no test yet 0=fail 1=pass
spellCorrect =True		# assuming initially no spelling mistakes
total_mis_spells=0		# variable to hold total number of mis-spellsprint ''

print '\n'
print 'Testing : The DC Test for Stator Resistance =>'
driver.get('http://vem-iitg.vlabs.ac.in/Introduction_DC.html')

#testing introduction page
print 'On Introduction Page : '
x = find('/html/body/div/div[4]/ul/li[1]/a')
x.click()
content =find('/html/body')  #content now contains content of introduction
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[0]=-1;
else:
		result[0]=1;	
total_mis_spells =total_mis_spells + mis_spells

#tesing theory page
print 'On Theory Page : '
x=find('/html/body/div/div[4]/ul/li[2]/a')
x.click()
content =find('/html/body')  #content now contains content of theory
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[1]=-1;
else:
		result[1]=1;	
total_mis_spells =total_mis_spells + mis_spells

#now going to procedure page
print('On procedure page')
x = find('/html/body/div/div[4]/ul/li[3]/a')
x.click()
content =find('/html/body')  #content now contains content of procedure
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[2] = -1
else:
		result[2] = 1
#now checking links
sucess=True
x = find('/html/body/div/div[4]/div/h2/a')
x.click()
x = driver.current_url
check = 'https://www.youtube.com/watch?v=RkT6fv4j3RM'
if(x != check):
	print '	link with href=',check,' not working properly' 
	sucess=False
else:
	print '	link with href=',check,'  working properly' 
driver.back()
if sucess == False:
		result[3] = -1
else:

		result[3]=1
		print 	'	All links working properly'	

#now going to simulator page
print 'On Simulator of Exp  : '
x = find('/html/body/div/div[4]/ul/li[4]/a')
x.click()
x = driver.current_url
check = 'http://vem-iitg.vlabs.ac.in/Experiment_DC.html'
if(x == check):
	print '	simulator for Exp : working'
	result[4]=1
else:
	print '	simulator for Exp not working-'
	result[4]=-1
	
#now going to quiz page
print 'on quiz page :'
x=find('/html/body/div/div[4]/ul/li[5]/a')
x.click()
content =find('/html/body')  #content now contains content of quiz
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[5] = -1
else:
		result[5] = 1
x= find('/html/body/div/div[4]/div/form/div/div[2]/input')
x.click()
x= find('/html/body/div/div[4]/div/form/div/div[3]/input[2]')	#clicking on submit button
x.click()
x = find('/html/body/div/div[4]/div/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/tick.gif.jpg':
	result[6]=1
else :
	result[6]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div/div[4]/div/form/div/div[3]/input[1]')
x.click()
x= find('/html/body/div/div[4]/div/form/div/div[3]/input[2]')	#clicking on submit button
x.click()
x = find('/html/body/div/div[4]/div/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[7]=1
else :
	result[7]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div/div[4]/div/form/div/div[3]/input[2]')	#clicking on submit button
x.click()
x = find('/html/body/div/div[4]/div/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[8]=1
else :
	result[8]=-1
	


print 'Final Report : '	
		
testname = 	'The_DC_Test_for_Stator_Resistance_02_introduction'
if result[0] == 1:
		print testname,'passed'
elif result[0] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'The_DC_Test_for_Stator_Resistance_03_theory'
if result[1] == 1:
		print testname,'passed'
elif result[1] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'The_DC_Test_for_Stator_Resistance_04_procedure'
if result[2] == 1:
		print testname,'passed'
elif result[2] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'The_DC_Test_for_Stator_Resistance_05_procedure_p2'
if result[3] == 1:
		print testname,'passed'
elif result[3] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'The_DC_Test_for_Stator_Resistance_06_simulator'
if result[4] == 1:
		print testname,'passed'
elif result[4] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'The_DC_Test_for_Stator_Resistance_07_quiz_p1'
if result[5] == 1:
		print testname,'passed'
elif result[5] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'The_DC_Test_for_Stator_Resistance_08_quiz_p2'
if result[6] == 1:
		print testname,'passed'
elif result[6] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'The_DC_Test_for_Stator_Resistance_09_quiz_p3'
if result[7] == 1:
		print testname,'passed'
elif result[7] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'The_DC_Test_for_Stator_Resistance_10_quiz_p4'
if result[8] == 1:
		print testname,'passed'
elif result[8] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

#Testing : Blocked-Rotor Test =>
result =[0,0,0,0,0,0,0,0,0,0,0]				#list to store result of test	-1=no test yet 0=fail 1=pass
spellCorrect =True		# assuming initially no spelling mistakes
total_mis_spells=0		# variable to hold total number of mis-spellsprint ''

print '\n' 
print 'Testing : Blocked-Rotor Test =>'
driver.get('http://vem-iitg.vlabs.ac.in/Introduction_blockr.html')

#testing introduction page
print 'On Introduction Page : '
x = find('/html/body/div/div[4]/ul/li[1]/a')
x.click()
content =find('/html/body')  #content now contains content of introduction
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[0]=-1;
else:
		result[0]=1;	
total_mis_spells =total_mis_spells + mis_spells

#tesing theory page
print 'On Theory Page : '
x=find('/html/body/div/div[4]/ul/li[2]/a')
x.click()
content =find('/html/body')  #content now contains content of theory
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[1]=-1;
else:
		result[1]=1;	
total_mis_spells =total_mis_spells + mis_spells

#now going to procedure page
print('On procedure page')
x = find('/html/body/div/div[4]/ul/li[3]/a')
x.click()
content =find('/html/body')  #content now contains content of procedure
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[2] = -1
else:
		result[2] = 1
#now checking links
sucess=True
x = find('/html/body/div/div[4]/div/h2/a')
x.click()
x = driver.current_url
check = 'https://www.youtube.com/watch?v=aq-ab3CnEwk'
if(x != check):
	print '	link with href=',check,' not working properly-',x 
	sucess=False
else:
	print '	link with href=',check,'  working properly' 
driver.back()
if sucess == False:
		result[3] = -1
else:

		result[3]=1
		print 	'	All links working properly'	

#now going to simulator page
print 'On Simulator of Exp  : '
x = find('/html/body/div/div[4]/ul/li[4]/a')
x.click()
x = driver.current_url
check = 'http://vem-iitg.vlabs.ac.in/Experiment_blockr.html'
if(x == check):
	print '	simulator for Exp : working'
	result[4]=1
else:
	print '	simulator for Exp not working'
	result[4]=-1
#now cheking links
sucess=True
x = find('/html/body/div/div[4]/div/h1/p[3]/a/i')		#link 1
x.click()
x = driver.current_url
check = 'http://vem-iitg.vlabs.ac.in/images/totalbl.gif'
if(x != check):
	print '	link with href=',check,' not working properly' 
	sucess=False
else:
	print '	link with href=',check,'  working properly' 
driver.back()
x = find('/html/body/div/div[4]/div/h1/p[4]/a/i')		#link 2
x.click()
x = driver.current_url
check = 'http://vem-iitg.vlabs.ac.in/images/statorbl.gif'
if(x != check):
	print '	link with href=',check,' not working properly' 
	sucess=False
else:
	print '	link with href=',check,'  working properly' 
driver.back()
x = find('/html/body/div/div[4]/div/h1/p[5]/a/i')		#link 3
x.click()
x = driver.current_url
check = 'http://vem-iitg.vlabs.ac.in/images/rotorbl.gif'
if(x != check):
	print '	link with href=',check,' not working properly' 
	sucess=False
else:
	print '	link with href=',check,'  working properly' 
driver.back()
x = find('/html/body/div/div[4]/div/h1/p[6]/a/i')		#link 4
x.click()
x = driver.current_url
check = 'http://vem-iitg.vlabs.ac.in/images/eddyctnbl.gif'
if(x != check):
	print '	link with href=',check,' not working properly' 
	sucess=False
else:
	print '	link with href=',check,'  working properly' 
driver.back()
x = find('/html/body/div/div[4]/div/h1/p[7]/a/i')		#link 5
x.click()
x = driver.current_url
check = 'http://vem-iitg.vlabs.ac.in/images/absbbl.gif'
if(x != check):
	print '	link with href=',check,' not working properly' 
	sucess=False
else:
	print '	link with href=',check,'  working properly' 
driver.back()

if sucess == False:
		result[5] = -1
else:

		result[5]=1
		print 	'	All links working properly'	

#now going to solved examples page
print 'on solved examples page :'
x=find('/html/body/div/div[4]/ul/li[5]/a')
x.click()
content =find('/html/body')  #content now contains content of quiz
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[6] = -1
else:
		result[6] = 1		
		
		
	
#now going to quiz page
print 'on quiz page :'
x=find('/html/body/div/div[4]/ul/li[6]/a')
x.click()
content =find('/html/body')  #content now contains content of quiz
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[7] = -1
else:
		result[7] = 1
x= find('/html/body/div/div[4]/div/form/div/div[3]/div[1]/input')
x.click()
x= find('/html/body/div/div[4]/div/form/div/div[3]/div[10]/div[5]/div[5]/input[2]')	#clicking on submit button
x.click()
x = find('/html/body/div/div[4]/div/form/div/div[1]/img[1]')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/tick.gif.jpg':
	result[8]=1
else :
	result[8]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div/div[4]/div/form/div/div[3]/label[1]')
x.click()
x= find('/html/body/div/div[4]/div/form/div/div[3]/div[10]/div[5]/div[5]/input[2]')	#clicking on submit button
x.click()
x = find('/html/body/div/div[4]/div/form/div/div[1]/img[1]')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[9]=1
else :
	result[9]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div/div[4]/div/form/div/div[3]/div[10]/div[5]/div[5]/input[2]')	#clicking on submit button
x.click()
x = find('/html/body/div/div[4]/div/form/div/div[1]/img[1]')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[10]=1
else :
	result[10]=-1
	


print 'Final Report : '	
		
testname = 	'No_Load _Test_02_introduction'
if result[0] == 1:
		print testname,'passed'
elif result[0] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'No_Load _Test_03_theory'
if result[1] == 1:
		print testname,'passed'
elif result[1] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'No_Load _Test_04_procedure_p1'
if result[2] == 1:
		print testname,'passed'
elif result[2] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'No_Load _Test_05_procedure_p2'
if result[3] == 1:
		print testname,'passed'
elif result[3] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'No_Load _Test_06_simulator_p1'
if result[4] == 1:
		print testname,'passed'
elif result[4] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Blocked_Rotor _Test_07_simulator_p2'
if result[5] == 1:
		print testname,'passed'
elif result[5] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Blocked_Rotor _Test_08_solvedExamples'
if result[6] == 1:
		print testname,'passed'
elif result[6] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Blocked_Rotor _Test_09_quiz_p1'
if result[7] == 1:
		print testname,'passed'
elif result[7] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Blocked_Rotor _Test_10_quiz_p2'
if result[8] == 1:
		print testname,'passed'
elif result[8] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Blocked_Rotor _Test_11_quiz_p3'
if result[9] == 1:
		print testname,'passed'
elif result[9] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Blocked_Rotor _Test_12_quiz_p4'
if result[9] == 1:
		print testname,'passed'
elif result[9] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

#Testing : Stator Resistance Starter =>
result =[0,0,0,0,0,0,0,0,0,0,0]				#list to store result of test	-1=no test yet 0=fail 1=pass
spellCorrect =True		# assuming initially no spelling mistakes
total_mis_spells=0		# variable to hold total number of mis-spellsprint ''

print '\n'
print 'Testing : Stator Resistance Starter =>'
driver.get('http://vem-iitg.vlabs.ac.in/Stator%20Resistance%20Starter%28quiz%29.html')

#testing introduction page
print 'On Introduction Page : '
x = find('/html/body/div[1]/div[3]/div/div[1]/ul/li[1]')
x.click()
content =find('/html/body')  #content now contains content of introduction
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[0]=-1;
else:
		result[0]=1;	
total_mis_spells =total_mis_spells + mis_spells

#tesing theory page
print 'On Theory Page : '
x=find('/html/body/div[1]/div[3]/div/div[1]/ul/li[2]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of theory
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[1]=-1;
else:
		result[1]=1;	
total_mis_spells =total_mis_spells + mis_spells

#now going to procedure page
print('On procedure page')
x = find('/html/body/div/div[3]/div/div[1]/ul/li[3]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of procedure
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[2] = -1
else:
		result[2] = 1
#now checking links
sucess=True
x = find('/html/body/div/div[3]/div/div[2]/p[31]/a/span')
x.click()
x = driver.current_url
check = 'https://www.youtube.com/watch?v=x6U9t8LwTBI'
if(x != check):
	print '	link with href=',check,' not working properly' 
	sucess=False
else:
	print '	link with href=',check,'  working properly' 
driver.back()
if sucess == False:
		result[3] = -1
else:

		result[3]=1
		print 	'	All links working properly'	

#now going to simulator page
print 'On Simulator of Exp  : '
x = find('/html/body/div/div[3]/div/div[1]/ul/li[4]/a/h6')
x.click()
x = driver.current_url
check = 'http://vem-iitg.vlabs.ac.in/Stator%20Resistance%20Starter(experiment).html'
if(x == check):
	print '	simulator for Exp : working'
	result[4]=1
else:
	print '	simulator for Exp not working'
	result[4]=-1

#now going to quiz page
print 'on quiz page :'
x=find('/html/body/div[1]/div[3]/div/div[1]/ul/li[5]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of quiz
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[5] = -1
else:
		result[5] = 1
x= find('/html/body/div[1]/div[3]/div/div[2]/div/div[2]/input[2]')
x.click()
x= find('/html/body/div[1]/div[3]/div/div[2]/div/input[3]')	#clicking on submit button
x.click()
x = find('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/img[1]')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/tick.gif.jpg':
	result[6]=1
else :
	result[6]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div[1]/div[3]/div/div[2]/div/div[2]/input[1]')
x.click()
x= find('/html/body/div[1]/div[3]/div/div[2]/div/input[3]')	#clicking on submit button
x.click()
x = find('/html/body/div[1]/div[3]/div/div[2]/div/div[2]/input[2]')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[7]=1
else :
	result[7]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div[1]/div[3]/div/div[2]/div/input[3]')	#clicking on submit button
x.click()
x = find('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[8]=1
else :
	result[8]=-1
	


print 'Final Report : '	
testname = 	'Stator_Resistance_Starter_02_introduction'
if result[0] == 1:
		print testname,'passed'
elif result[0] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Stator_Resistance_Starter_03_theory'
if result[1] == 1:
		print testname,'passed'
elif result[1] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Stator_Resistance_Starter_04_procedure_p1'
if result[2] == 1:
		print testname,'passed'
elif result[2] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Stator_Resistance_Starter_05_procedure_p2'
if result[3] == 1:
		print testname,'passed'
elif result[3] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Stator_Resistance_Starter_06_simulator'
if result[4] == 1:
		print testname,'passed'
elif result[4] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Stator_Resistance_Starter_07_quiz_p1'
if result[5] == 1:
		print testname,'passed'
elif result[5] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Stator_Resistance_Starter_08_quiz_p2'
if result[6] == 1:
		print testname,'passed'
elif result[6] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Stator_Resistance_Starter_09_quiz_p3'
if result[7] == 1:
		print testname,'passed'
elif result[7] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Stator_Resistance_Starter_10_quiz_p4'
if result[8] == 1:
		print testname,'passed'
elif result[8] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
#Testing : Auto Transformer Starting =>		
result =[0,0,0,0,0,0,0,0,0,0,0]				#list to store result of test	-1=no test yet 0=fail 1=pass
spellCorrect =True		# assuming initially no spelling mistakes
total_mis_spells=0		# variable to hold total number of mis-spellsprint ''

print '\n'
print 'Testing : Auto Transformer Starting =>'
driver.get('http://vem-iitg.vlabs.ac.in/Auto%20Transformer%20Starting%28intro%29.html')

#testing introduction page
print 'On Introduction Page : '
x = find('/html/body/div/div[3]/div/div[1]/ul/li[1]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of introduction
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[0]=-1;
else:
		result[0]=1;	
total_mis_spells =total_mis_spells + mis_spells

#tesing theory page
print 'On Theory Page : '
x=find('/html/body/div/div[3]/div/div[1]/ul/li[2]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of theory
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[1]=-1;
else:
		result[1]=1;	
total_mis_spells =total_mis_spells + mis_spells

#now going to procedure page
print('On procedure page')
x = find('/html/body/div/div[3]/div/div[1]/ul/li[3]')
x.click()
content =find('/html/body')  #content now contains content of procedure
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[2] = -1
else:
		result[2] = 1
#now checking links
sucess=True
x = find('/html/body/div/div[3]/div/div[2]/p[25]/a/span')
x.click()
x = driver.current_url
check = 'https://www.youtube.com/watch?v=CwA2Idd5e7s&feature=related'
if(x != check):
	print '	link with href=',check,' not working properly' 
	sucess=False
else:
	print '	link with href=',check,'  working properly' 
driver.back()
if sucess == False:
		result[3] = -1
else:

		result[3]=1
		print 	'	All links working properly'	

#now going to simulator page
print 'On Simulator of Exp  : '
x = find('/html/body/div/div[3]/div/div[1]/ul/li[4]/a/h6')
x.click()
x = driver.current_url
check = 'http://vem-iitg.vlabs.ac.in/Auto%20Transformer%20Starting(experiment).html'
if(x == check):
	print '	simulator for Exp : working'
	result[4]=1
else:
	print '	simulator for Exp not working'
	result[4]=-1

#now going to quiz page
print 'on quiz page :'
x=find('/html/body/div/div[3]/div/div[1]/ul/li[5]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of quiz
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[5] = -1
else:
		result[5] = 1
x= find('/html/body/div[1]/div[3]/div/div[2]/div/input[2]')
x.click()
x= find('/html/body/div[1]/div[3]/div/div[2]/div/input[5]')	#clicking on submit button
x.click()
x = find('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/img[1]')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/tick.gif.jpg':
	result[6]=1
else :
	result[6]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div[1]/div[3]/div/div[2]/div/div[2]/input[1]')
x.click()
x= find('/html/body/div[1]/div[3]/div/div[2]/div/input[5]')	#clicking on submit button
x.click()
x = find('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/img[1]')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[7]=1
else :
	result[7]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div[1]/div[3]/div/div[2]/div/input[5]')	#clicking on submit button
x.click()
x = find('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/img[1]')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[8]=1
else :
	result[8]=-1
	


print 'Final Report : '	
testname = 	'Auto_Transformer_Starting_02_introduction'
if result[0] == 1:
		print testname,'passed'
elif result[0] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Auto_Transformer_Starting_03_theory'
if result[1] == 1:
		print testname,'passed'   
elif result[1] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Auto_Transformer_Starting_04_procedure_p1'
if result[2] == 1:
		print testname,'passed'
elif result[2] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Auto_Transformer_Starting_05_procedure_p2'
if result[3] == 1:
		print testname,'passed'
elif result[3] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Auto_Transformer_Starting_06_simulator'
if result[4] == 1:
		print testname,'passed'
elif result[4] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Auto_Transformer_Starting_07_quiz_p1'
if result[5] == 1:
		print testname,'passed'
elif result[5] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Auto_Transformer_Starting_08_quiz_p2'
if result[6] == 1:
		print testname,'passed'
elif result[6] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Auto_Transformer_Starting_09_quiz_p3'
if result[7] == 1:
		print testname,'passed'
elif result[7] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Auto_Transformer_Starting_10_quiz_p4'
if result[8] == 1:
		print testname,'passed'
elif result[8] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'			

#Testing : Star-Delta Starting => 
result =[0,0,0,0,0,0,0,0,0,0,0]				#list to store result of test	-1=no test yet 0=fail 1=pass
spellCorrect =True		# assuming initially no spelling mistakes
total_mis_spells=0		# variable to hold total number of mis-spellsprint ''

print '\n'
print 'Testing : Star-Delta Starting => '
driver.get('http://vem-iitg.vlabs.ac.in/Star%20Delta%20Starting%28intro%29.html')

#testing introduction page
print 'On Introduction Page : '
x = find('/html/body/div/div[3]/div/div[1]/ul/li[1]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of introduction
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[0]=-1;
else:
		result[0]=1;	
total_mis_spells =total_mis_spells + mis_spells

#tesing theory page
print 'On Theory Page : '
x=find('/html/body/div/div[3]/div/div[1]/ul/li[2]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of theory
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        result[1]=-1;
else:
		result[1]=1;	
total_mis_spells =total_mis_spells + mis_spells

#now going to procedure page
print('On procedure page')
x = find('/html/body/div/div[3]/div/div[1]/ul/li[3]/a/h6')
x.click()
content =find('/html/body')  #content now contains content of procedure
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[2] = -1
else:
		result[2] = 1
#now checking links
sucess=True
x = find('/html/body/div/div[3]/div/div[2]/p[29]/a/span')
x.click()
x = driver.current_url
check = 'https://www.youtube.com/watch?v=bKk9PS8kQTs&feature=related'
if(x != check):
	print '	link with href=',check,' not working properly' 
	sucess=False
else:
	print '	link with href=',check,'  working properly' 
driver.back()
if sucess == False:
		result[3] = -1
else:

		result[3]=1
		print 	'	All links working properly'	

#now going to simulator page
print 'On Simulator of Exp  : '
x = find('/html/body/div/div[3]/div/div[1]/ul/li[4]/a/h6')
x.click()
x = driver.current_url
check = 'http://vem-iitg.vlabs.ac.in/Star%20Delta%20Starting(experiment).html'
if(x == check):
	print '	simulator for Exp : working'
	result[4]=1
else:
	print '	simulator for Exp not working'
	result[4]=-1

#now going to quiz page
print 'on quiz page :'
x=find('/html/body/div/div[3]/div/div[1]/ul/li[5]/a/img')
x.click()
content =find('/html/body')  #content now contains content of quiz
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
		result[5] = -1
else:
		result[5] = 1
x= find('/html/body/div[1]/div[3]/div/div[2]/div/div[2]/input[1]')
x.click()
x= find('/html/body/div[1]/div[3]/div/div[2]/div/input[5]')	#clicking on submit button
x.click()
x = find('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/tick.gif.jpg':
	result[6]=1
else :
	result[6]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div[1]/div[3]/div/div[2]/div/div[2]/input[2]')
x.click()
x= find('/html/body/div[1]/div[3]/div/div[2]/div/input[5]')	#clicking on submit button
x.click()
x = find('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/img[1]')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[7]=1
else :
	result[7]=-1
driver.refresh();		#refreshing page
x= find('/html/body/div[1]/div[3]/div/div[2]/div/input[5]')	#clicking on submit button
x.click()
x = find('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/img[1]')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	result[8]=1
else :
	result[8]=-1
	
driver.close()

print 'Final Report : '	
testname = 	'Star_Delta_Starting_Starting_02_introduction'
if result[0] == 1:
		print testname,'passed'
elif result[0] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Star_Delta_Starting_Starting_03_theory'
if result[1] == 1:
		print testname,'passed'   
elif result[1] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Star_Delta_Starting_Starting_04_procedure_p1'
if result[2] == 1:
		print testname,'passed'
elif result[2] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Star_Delta_Starting_Starting_05_procedure_p2'
if result[3] == 1:
		print testname,'passed'
elif result[3] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'

testname = 	'Star_Delta_Starting_Starting_06_simulator'
if result[4] == 1:
		print testname,'passed'
elif result[4] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Star_Delta_Starting_Starting_07_quiz_p1'
if result[5] == 1:
		print testname,'passed'
elif result[5] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Star_Delta_Starting_Starting_08_quiz_p2'
if result[6] == 1:
		print testname,'passed'
elif result[6] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Star_Delta_Starting_Starting_09_quiz_p3'
if result[7] == 1:
		print testname,'passed'
elif result[7] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
testname = 	'Star_Delta_Starting_Starting_10_quiz_p4'
if result[8] == 1:
		print testname,'passed'
elif result[8] == -1:
		print testname,'failed'
else:
		print testname,'not attempted'
		
		
		
		