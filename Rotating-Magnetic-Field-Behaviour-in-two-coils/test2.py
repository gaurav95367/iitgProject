import sys
from enchant.checker import SpellChecker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting some initial variables...
result =[0,0,0,0,0,0,0,0,0,0]				#list to store result of test	-1=no test yet 0=fail 1=pass
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

print ''
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
	
driver.close()

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
		
		
		
