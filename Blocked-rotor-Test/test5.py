import sys
import time
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

print 'Testing :Blocked-Rotor Test'
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
	
driver.close()

print '	Final Report : '	
		
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
		