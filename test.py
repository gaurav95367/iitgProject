from selenium import webdriver
from enchant.checker import SpellChecker

print 'Testing :Magnetic Field Behaviour in Single Coil Experiment'
spellCorrect =True		#assuming initially no spelling mistakes
total_mis_spells=0
chkr = SpellChecker("en_US")
#adding some ignore words in dictionary...
chkr.ignore_always('Lenz');chkr.ignore_always('lenz')
chkr.ignore_always('GUWAHATI');chkr.ignore_always('guwahati')
chkr.ignore_always('Shakshat');chkr.ignore_always('shakshat')
chkr.ignore_always('MCB')
chkr.ignore_always('IIT');chkr.ignore_always('iit')
chkr.ignore_always('Behaviour');chkr.ignore_always('behaviour')
chkr.ignore_always('CSE');chkr.ignore_always('cse');
driver=webdriver.Firefox()

driver.get('http://vem-iitg.vlabs.ac.in/Magnetic_Field_Behaviour_in_single_coil.html')
print 'On Introduction Page : '
content =driver.find_element_by_xpath('/html/body')  #content now contains content of introduction
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
x =driver.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/ul/li[2]/a/h6')
x.click()
print 'On Theory Page : '
content =driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]')  #content now contains content of theory
mis_spells=0
chkr.set_text(content.text)
for err in chkr:
        print '         mis-spelled word',mis_spells+1,':',err.word
        mis_spells+=1
print '         REPORT : TOTAL',mis_spells,' MIS-SPELLS FOUND.'
if mis_spells>0:
        spellCorrect = False
total_mis_spells =total_mis_spells + mis_spells
x =driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/p[7]/a/b')
x.click()
if(driver.current_url == 'http://vem-iitg.vlabs.ac.in/images/link1.jpg'):
	print 'Link: working'
else:
	print 'Link :not working'
driver.back()

#now going to procedure page...
x =driver.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/ul/li[3]/a/h6')
x.click()
print 'On Procedure Page : '
driver.get('file:///C:/Users/Gaurav/Desktop/1.html')
content =driver.find_element_by_xpath('/html/body/div/div[3]')  #content now contains content of procedure








driver.close()
if spellCorrect == True :
        print 'RESULT : PASSED, 0 spell mistakes Found!'
else:
        print 'RESULT : FAILED, TOTAL ',total_mis_spells,' FOUND'
		
		
		
