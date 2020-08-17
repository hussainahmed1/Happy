#!/usr/bin/python
# coding=utf-8
#Original Written By Tech Qaiser 
# Source : Python2"
# donot recode it.

#Import module
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 Happy.py')

#Browser Setting
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exit():
	print "[!] Exit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def hamza(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
##### LOGO #####
banner = """
\033[1;97m╭━━━╮
\033[1;97m┃╭━╮┃
\033[1;97m┃┃╱┃┣━━┳┳━━┳━━┳━╮
\033[1;97m┃┃╱┃┃╭╮┣┫━━┫┃━┫╭╯
\033[1;97m┃╰━╯┃╭╮┃┣━━┃┃━┫┃
\033[1;97m╰━━╮┣╯╰┻┻━━┻━━┻╯
\033[1;97m╱╱╱╰╯

\033[1;97m-----------------------------------------------

\033[1;97mCoder   :\033[1;97mTech Qaiser
\033[1;97mGithub  :\033[1;97mhttps://github.com/TechQaiser
\033[1;97mFacebook:\033[1;97mQaiser Abbas
\033[1;97mYoutube :\033[1;97mTech Qaiser
\033[1;97mNote :\033[1;97mThis Is only For Educational Purpose
\033[1;97mNew Update :\033[1;97m Identity Problem Fixed 100% If You Login With Acces Token

\033[1;97m-----------------------------------------------"""
# titik #
def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r[✔]\033[1;92mLogging In "+o),;sys.stdout.flush();time.sleep(1)

back = 0
id = []

def tlogin():
	os.system('clear')
	print banner
	username = raw_input("[🔐].\033[1;97mTOOL USERNAME: ")
	if username =="Qaiser":
	    os.system('clear')
	    print banner
	    print "[✓] .\033[1;92mTOOL USERNAME: "+username+ " (correct)"
	else:
	    print "[!] Invalid Username."
	    time.sleep(1)
	    tlogin()
	    
	passw = raw_input("[🔐] .\033[1;97mTOOL PASSWORD: ")
	if passw =="Happy":
	    os.system('clear')
	    print banner
	    print "[🔑] \033[1;97mTOOL USERNAME: " +username+ " (correct)"
	    print "[🔑] \033[1;97mTOOL PASSWORD: " +passw+ "  (correct)"
	    time.sleep(2)
	else:
	    print "[!] Invalid Password."
	    time.sleep(1)
	    tlogin()
	try:
		toket = open('login.txt','r')
		os.system('python2 .Happy2.py')
	except (KeyError,IOError):
		methodlogin()
	else:
		print "\033[1;91m[!] \033[1;91mInvalid Password"
		time.sleep(1)
		tlogin()

##### Login Method #####


def methodlogin():
	os.system('clear')
	print banner
	print "[-->1<--] \033[1;97mLogin With Email / Password"
	print "[-->2<--] \033[1;97mLogin Using Fb Token."
	print "[-->3<--] Get Free Acces Token"
	print "[-->4<--] \033[1;97mExit."
	print ('      ')
	hos = raw_input("\n\033[1;96mChoose Option >>  ")
	if hos =="":
		print"\033[1;91m[!] \033[1;95mWrong Input"
		exit()
	elif hos =="1":
		login()
	elif hos =="2":
		os.system('clear')
		print banner
		hosp = raw_input("Paste Any Token Here For Login: ")
		tik()
		hopa = open('login.txt','w')
		hopa.write(hosp)
		hopa.close()
		print "\n\[✓]\033[1;92mLogged In Successfully."
		time.sleep(1)
		os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
		os.system('python2 .Happy2.py')
	elif hos =="3":
		print banner
		
"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"


	elif hos =="0":
		exit()
	else:
		print"[!]\033[1;91mWrong Input"
		exit()
def login():
	os.system("clear")
	try:
		tb=open('login.txt', 'r')
		os.system("python2 .Happy2.py")
	except (KeyError,IOError):
		os.system("clear")
		print (banner)
		hamza('\033[1;97mLogin Your Facebook Account')
		hamza('\033[1;97mNote : Donot Use Your Personal Account Bcoz Of Identity')
		hamza('\033[1;97m Please Sir Use a New Facebook Account To Login Safely')
		print'-------------------------------------'
		iid=raw_input('\033[1;97mNumber/Email = ')
		id=iid.replace(" ","")
		pwd=raw_input('\033[1;97m Password = ')
		tik()
		data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		z=json.load(data)
		if 'access_token' in z:
		    st = open("login.txt", "w")
		    st.write(z["access_token"])
		    st.close()
		    print "\n[✓]\033[1;97mLogged In Successfully."
		    time.sleep(1)
		    os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
		    os.system("clear")
		    os.system("python2 .Happy2.py")
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print ('\033[1;91m User Must Verify Account Before Login.')
		        time.sleep(3)
		        login()
		    else:
		        print ('\033[1;91mEmail / Password Is Wrong ')
		        time.sleep(1)
		        login()
if __name__=='__main__':
    tlogin()
