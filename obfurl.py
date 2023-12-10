import random,string,requests,os,getpass
def obfuscate(url,times=100):C=b'776597651006510165326598651216532656665108659765110651076532';B=times;A=url;return A.split(chr(47))[0]+chr(47)*2+''.join([''.join([random.choice([chr(A)for A in range(97,123)]+[chr(A)for A in range(48,58)])for A in range(B)])+'.'+''.join([random.choice([chr(A)for A in range(97,123)]+[chr(A)for A in range(48,58)]+['.com','discord','bit.ly','api','webhook','download','.exe','telegram','org'])for A in range(B)])+'@'for A in range(3)])+A.lower().replace(chr(119)*3+chr(ord(''.join([chr(int(A))for A in C.decode().replace(str(65),chr(32)).split()])[::-1][11])-ord(str(6))),'').replace(A.split(chr(47))[0]+chr(47)*2,'',1)+chr(35)+''.join([random.choice([chr(A)for A in range(33,127)]+[A.lower().replace(chr(119)*3+chr(ord(''.join([chr(int(A))for A in C.decode().replace(str(65),chr(32)).split()])[::-1][11])-ord(str(6))),'').replace(A.split(chr(47))[0]+chr(47)*2,'',1).split('/')[0]]*5+['discord.com/api/webhooks/'+''.join([random.choice(string.digits)for A in range(18)])+'/'+''.join([random.choice(string.ascii_letters)for A in range(68)])for A in range(15)])for B in range(B)])
def clear():os.system('clear'if os.name!='nt'else'cls')
def credit():print('\x1b[31;1mh\x1b[32;1mt\x1b[33;1mt\x1b[34;1mp\x1b[35;1ms\x1b[36;1m:\x1b[32;1m/\x1b[33;1m/\x1b[34;1mg\x1b[35;1mi\x1b[36;1mt\x1b[32;1mh\x1b[33;1mu\x1b[34;1mb\x1b[35;1m.\x1b[36;1mc\x1b[32;1mo\x1b[33;1mm\x1b[34;1m/\x1b[35;1mE\x1b[36;1mr\x1b[32;1mr\x1b[33;1m0\x1b[34;1mr\x1b[35;1m-\x1b[36;1mI\x1b[32;1mC\x1b[33;1mA\x1b[34;1m/\x1b[35;1mU\x1b[35;1mR\x1b[36;1mL\x1b[32;1m-\x1b[33;1mO\x1b[34;1mb\x1b[35;1mf\x1b[36;1mu\x1b[32;1ms\x1b[33;1mc\x1b[34;1ma\x1b[35;1mt\x1b[36;1mo\x1b[32;1mr\x1b[33;1m/\x1b[0m\n\n')
clear()
os.system('title Priv8 URL Obfuscator'if os.name=='nt'else'')
credit()
while True:
	URL=input('\x1b[33;1mEnter URL: \x1b[0m')
	try:r=requests.get(URL);clear();break
	except Exception:print('\x1b[31;1mUnable to reach URL!\x1b[0m\n')
credit()
print('\x1b[33;1mProcessing...\x1b[0m')
with open(f"obf.txt",'w')as file:file.write(obfuscate(URL))
clear()
credit()
print(f'[32;1m\aSaved URL in "[34;1m{os.path.dirname(__file__)+"/obf.txt"}[32;1m"![0m\n')
if os.name=='nt':os.system(f"notepad.exe {os.path.dirname(__file__)}"+' "/obf.txt"')
getpass.getpass('\x1b[37;1m(Press enter to exit)\x1b[0m')