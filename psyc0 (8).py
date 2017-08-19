#!/usr/bin/python 
# coding=utf-8
import untangle

from urlparse import urlparse
import urllib
import urllib2
import httplib
#
import cookielib
import re
import re , urllib2 , os , requests , random ,urllib3 , sys ,urllib
import requests as xsec
from time import sleep
from threading import Thread
import socket
from ftplib import FTP
from random import choice
import re , urllib2 , os , requests , random ,urllib3 , sys ,urllib
from platform import system
from random import choice
import time
import socket
from multiprocessing.dummy import Pool as ThreadPool 
import re , urllib2 , os , requests , random ,urllib3 , sys ,urllib
from platform import system
from random import choice
import time
import socket
from multiprocessing.dummy import Pool as ThreadPool 
#import urlparse
from bs4 import BeautifulSoup
##################################################################################################################
sites = []
u_sites = []
wordPress_site = []
u_0 = []
gu_sites = []
joomlasite = []
jolist= []
wplist = []
joomla_site = []
Joomlist= []
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def unescape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    # this has to be last:
    s = s.replace("&amp;", "&")
    parsed = urlparse(s)
    s = parsed.scheme+'://'+parsed.netloc+'/'
    return s

header = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)','msnbot/1.0 (+http://search.msn.com/msnbot.htm)','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)','Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)','Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)','Microsoft Internet Explorer/4.0b1 (Windows 95)','Opera/8.00 (Windows NT 5.1; U; en)','amaya/9.51 libwww/5.4.0','Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)','Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)','Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#~~~~~~~~~~~~
W  = "\33[0m";
R  = "\33[31m";
G  = "\33[32m";
O  = "\33[33m";
B  = "\33[34m";
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    CYAN = '\033[96m'
class colors():
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    
#####################################################################
def looper (ary,fonx):
    
  try:
     for xitem in ary :
        #print xitem
        fonx(xitem)
        #print " Donne!"
  except:
    print  "filed"
  pass
    

###############################################################################################################################################################################################################
#####################################################################

def joomla_version (url):
#XML = 'examples/planet_python.xml'     # can read a file too
  XML = url+'language/en-GB/en-GB.xml'
 
  o = untangle.parse(XML)
  for item in o.metafile:
      #title = item.title.cdata
      link = item.version.cdata
      if link:
        #print title
          version_j =link
  return version_j



###################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#####################################################################
def unique_file(input_filename, output_filename):
  z = []
  
  
  
  with open(input_filename,'r') as fileIn, open(output_filename,'a') as fileOut:
      for line in fileIn:
          for word in line.split():
              if word not in z:
                 z.append(word)
                 fileOut.write(word+'\n')
  #f = open('list_total.txt', 'w').close()
 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#####################################################################         
def deleteContent(pfile):
    fn=pfile.name 
    pfile.close()
    return open(fn,'w')
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#####################################################################

def save_it (lit,file_e):
  thefile = open(file_e, 'w')
  for shell_foundxx in lit:
    print>>thefile, unescape(shell_foundxx)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def save_resultat () :
  
  if len(sites) > 0 :
      #printer(listaf)
      #sites = unique(sites)
      with open("ip_valable.txt", "a") as f:
           #f.write("\n")
           f.write( ip+"\n")
           #f.write("\n")
      save_it(sites,"list_total.txt")
      
  else:
      exit(0)
###############################################################################################################################################################################################################

def printer (final) :
  global u_sites
  index=0
  print "\t\t"
  while index < len(final):
      #base_url =final[index].split("//")[-1].split("/")[0]
      #base_url = base_url.replace("www.", "")
      print "\t[ "+R+str(index+1)+W+" ]",
      #print G+final[index]+W
      #host2 = final[index].split('/')[2]
      #host2 = host2.replace("www.", "")

      
      print G+final[index]+W
      u_sites.append(final[index])
      index=index+1
  print "\t\t"
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

####################################################################
#~~~~~~~~~~~~~
def grab(site):
    try :
        sites.append(site)
        site1 = site.replace("http://","")
        site2 = site1.replace("www.","")
        site3 = site2.replace("/","")
        site4 = site3.replace("","")
        site5,dach = site4.split(".")
        if len(users) < 50 :
            users.append(site5)
    except :
        pass
#~~~~~~~~~~~~~

#####################################################################
###################################################################
def clearScr() :
	"""
	clear the screen in case of GNU/Linux or 
	windows 
	"""
	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]
####################################################################
ip=sys.argv[1]

#########################################################################################################################################################################################################################################################################################################################################################
def extractserver2(ip):
    global sites
    try:
        page = 1
        while page <= 500:
                bing = "http://www.bing.com/search?q=ip%3A"+ip+"+&count=50&first="+str(page)
                openbing  = urllib2.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
                sitess = findwebs
                #listaf = unique(listaf)
                for i in sitess:
                    i=unescape(i)
                    sites.append(i)
                    grab(i)
                    	
                #print bcolors.WARNING + "|-> grabbed  " + str(len(sites)) + " sites"				
                page = page + 21
    except :
	    pass
#########################################################################################################################################################################################################################################################################################################################################################
###################################################################
def test(url):
    try:
        #wp_url=url
        iij=joomla_version (url)
        openbing = urllib2.urlopen(url)
        readbing = openbing.read()
        req = requests.get(url)
        if re.findall("Joomla", readbing) or "Joomla" in req.text or urllib2.urlopen(url+"administrator").getcode() == 200:
            try :
                print G+"[!]-> "+B+" Joomla   :  [   "+iij+"   ]   " +O+  url +W
                with open("joomla.txt", "a") as f:
                    f.write(url+"\n")
            except:
                print G+"[!]-> "+B+" Joomla   :  [   unknown   ]   " +O+  url +W
                with open("joomla.txt", "a") as f:
                          f.write(url+"\n")
            #rce(url)
        
        #if re.findall("WordPress", readbing) or "WordPress" in req.text or urllib2.urlopen(url+"wp-login.php").getcode() == 200:
              #print G+"[!]-> "+O+" WordPress : " +  url +W
        #else:
                #print "rass el kos"
                #pass
    except:
        pass
#################################################################
def testwp(url):
    
    try:
        global wordPress_site
        wordPress_site = []
       #Powered by WordPress
        #log3()
        
        agent = random.choice(header)
        
        Wp_admin=(url+'wp-login.php')
        Wp_version=(url)
        request_web_version =urllib2.Request(Wp_version)
        request_web_version.add_header('User-Agent', agent)
        #print Wp_version
        #__response = urllib2.urlopen('http://www.'+url).read()
        #check_version = re.findall('WordPress',__response)
        #print check_version
        #print Wp_admin
        
        
        request_web =urllib2.Request(Wp_admin)
        request_web.add_header('User-Agent', agent)
        
        if urllib2.urlopen(request_web).getcode() == 200 :
          Read_wp = urllib2.urlopen(Wp_admin)
          O_Read_wp = Read_wp.read()
          
          if re.findall("WordPress",O_Read_wp):
            #print "1"
            wordPress_site.append(Wp_admin)
            #u_sites.remove(str(url))
            wplist.append(str(url))
            with open("wordpress.txt", "a") as f:
                f.write(url+"\n")
            
            Read_wp_version = urllib2.urlopen(Wp_version)
            O_Read_wp_version = Read_wp_version.read()
            #if re.findall("js?ver=",O_Read_wp):
            #soup = BeautifulSoup(O_Read_wp_version)
            #metatags = soup.find_all('meta',attrs={'name':'generator'})
            #for tag in metatags:
             #print tag
            try :
                 check_version = re.findall(r'ver=(.*)"',O_Read_wp_version)[0]
                 print G+"[!]-> "+R+"Wordpress :"+W+ '{:{align}{width}}'.format(" [   "+R+check_version+W+"   ]", align='^', width='25')+"  "+O+str(Wp_version)+W 
            
            except:
                print G+"[!]-> "+R+"Wordpress"+W+" :  ["+R+"  Unknown  "+W+"] "+"  "+O+str(Wp_version)+W 
            #print check_version
                  
    except:
        #joomla_test2(url)
        #testjoo(url)
        test(url)
        pass


#####################################################################
#################################################################



#########################################################################################################################################################################################################################################################################################################################################################
def extractserver(ip):
    global sites
    xxxx = []
    try:
        page = 1
        while page <= 500:
                bing = "http://www.bing.com/search?q=ip%3A"+ip+"+&count=50&first="+str(page)
                openbing  = urllib2.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
                sitess = findwebs
                #listaf = unique(listaf)
                for i in range(len(findwebs)):
                    #sites.append(i)
                    allnoclean = findwebs[i]
                    findall1 = re.findall('http[s]?://(.*?)/', allnoclean)
                    for idx, item in enumerate(findall1):
                        if 'www' not in item:
                            findall1[idx] = 'http://www.' + item + '/'
                        else:
                            findall1[idx] = 'http://' + item + '/'
                    xxxx.extend(findall1)
                #print bcolors.WARNING + "|-> grabbed  " + str(len(sites)) + " sites"				
                page = page + 10
        final = unique(xxxx)
        sites.extend(final)
    except :
	    pass


#########################################################################################################################################################################################################################################################################################################################################################
###################################################################



clearScr()

#extractserver(ip)
#sites = unique(sites)
#print bcolors.WARNING + "|-> grabbed  " + str(len(sites)) + " sites"
#print bcolors.WARNING + "|-> grabbed  " + str(len(sites)) + " sites"
#printer (sites)
#del sites  [:]

extractserver2(ip)
sites = unique(sites)
print bcolors.WARNING + "|-> grabbed  " + str(len(sites)) + " sites"

save_resultat ()
unique_file("list_total.txt", "output_filename")
#looper (sites,test)
looper (sites,testwp)