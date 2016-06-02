import sys
from enchant.checker import SpellChecker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting some initial variables...
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
wait = WebDriverWait(driver, 10)		# seeting wait time for firefox to be 10 seconds


def find(xpath):						# a function to find web-elements 
	try:
		element = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
		return element
	except:
		print 'element with xpath =',xpath,'not found'
		sys.exit()

print 'Testing :Magnetic Field Behaviour in Single Coil Experiment'
driver.get('http://vem-iitg.vlabs.ac.in/Magnetic_Field_Behaviour_in_single_coil.html')
print 'On Introduction Page : '
content =find('/html/body')  #content now contains content of introduction
chkr.set_text(content.text)
mis_spells=0
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        spellCorrect = False
total_mis_spells =total_mis_spells + mis_spells

#now going to theory page...
x =find('/html/body/div/div[3]/div/div[1]/ul/li[2]/a/h6')
x.click()
print 'On Theory Page : '
content =find('/html/body/div/div[3]/div/div[2]')  #content now contains content of theory
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        spellCorrect = False
total_mis_spells =total_mis_spells + mis_spells
x =find('/html/body/div/div[3]/div/div[2]/p[7]/a/b')
x.click()
if(driver.current_url == 'http://vem-iitg.vlabs.ac.in/images/link1.jpg'):
	print '	Link: working'
else:
	print '	Link :not working'
driver.back()

#now going to procedure page...
x =find('/html/body/div/div[3]/div/div[1]/ul/li[3]/a/h6')
x.click()
print 'On Procedure Page : '
content = find('/html/body')
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        spellCorrect = False
total_mis_spells =total_mis_spells + mis_spells
x = find('/html/body/div/div[3]/div/div[2]/p[14]/a')
x.click()
if(driver.current_url == 'https://www.youtube.com/watch?v=WArVrQHXLCc'):
	print '	Link 1: working'
else:
	print '	Link 1:not working'
driver.back()
x = find('/html/body/div/div[3]/div/div[2]/p[15]/a')
x.click()
if(driver.current_url == 'https://www.youtube.com/watch?v=V7kVdELtX5M'):
	print '	Link 2: working'
else:
	print '	Link 2:not working'
driver.back()

#now going to simuator of experiment 1
x = find('/html/body/div/div[3]/div/div[1]/ul/li[4]/a/h6')
x.click()
print 'On Simulator of Exp 1 : '
driver.implicitly_wait(20)		#wait for 20s to load simulator 1
if(driver.current_url == 'http://vem-iitg.vlabs.ac.in/Magnetic_Field_Behaviour_in_single_coil(experiment1).html'):
	print '	simulator for Exp 1: working'
else:
	print '	simulator for Exp 1:not working-',driver.current_url

#now going to simuator of experiment 1
x = find('/html/body/div/div[3]/div/div[1]/ul/li[5]/a/h6')
x.click()
print 'On Simulator of Exp 2 : '
driver.implicitly_wait(20)		#wait for 15s to load simulator 1
if(driver.current_url == 'http://vem-iitg.vlabs.ac.in/Magnetic_Field_Behaviour_in_single_coil(experiment2).html'):
	print '	simulator for Exp 2: working'
else:
	print '	simulator for Exp 2:not working-',driver.current_url

#now going to quiz page
x = find('/html/body/div/div[3]/div/div[1]/ul/li[6]/a/h6')
x.click()
content = find('/html/body')
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        spellCorrect = False
total_mis_spells =total_mis_spells + mis_spells
x= find('/html/body/div/div[3]/div/div/div[2]/form/div/div[2]/input[2]')
x.click()
x= find('/html/body/div/div[3]/div/div/div[2]/form/div/input[3]')	#clicking on submit button
x.click()
x = find('/html/body/div/div[3]/div/div/div[2]/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/tick.gif.jpg':
	print 'correct output for Magnetic_Field_Behaviour_in_Single_Coil_07_quiz_p1.org'
else :
	print 'wrong output for Magnetic_Field_Behaviour_in_Single_Coil_07_quiz_p1.org'
driver.refresh();		#refreshing page
x = find('/html/body/div/div[3]/div/div/div[2]/form/div/div[2]/input[1]')
x.click()
x= find('/html/body/div/div[3]/div/div/div[2]/form/div/input[3]')	#clicking on submit button
x.click()
x = find('/html/body/div/div[3]/div/div/div[2]/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	print 'correct output for Magnetic_Field_Behaviour_in_Single_Coil_07_quiz_p2.org'
else :
	print 'wrong output for Magnetic_Field_Behaviour_in_Single_Coil_07_quiz_p2.org'
driver.refresh();		#refreshing page
x= find('/html/body/div/div[3]/div/div/div[2]/form/div/input[3]')	#clicking on submit button
x.click()
x = find('/html/body/div/div[3]/div/div/div[2]/form/div/div[1]/img')
if x.get_attribute('src') == 'http://vem-iitg.vlabs.ac.in/images/wrong.gif.jpg':
	print 'correct output for Magnetic_Field_Behaviour_in_Single_Coil_07_quiz_p3.org'
else :
	print 'wrong output for Magnetic_Field_Behaviour_in_Single_Coil_07_quiz_p3.org'
	




driver.close()
if spellCorrect == True :
        print 'RESULT : PASSED, 0 spell mistakes Found!'
else:
        print 'RESULT : FAILED, TOTAL ',total_mis_spells,' FOUND'
		
	



