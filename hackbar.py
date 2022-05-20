from tkinter import *
import webview
import requests


url='https://akr3ch.github.io/cs/'

def get():
	entry_value = entry.get().lower()
	if 'bypass file upload filter' in entry_value or 'bypass file upload' in entry_value:
		answer_value = requests.get(url+'bypass-file-upload').text
	elif 'bypass 401' in entry_value or 'bypass 403' in entry_value or '401 bypass' in entry_value or '403 bypass' in entry_value or '401/403 bypass' in entry_value or '403/401 bypass' in entry_value:
		answer_value = requests.get(url+'403-bypass').text
	elif 'password reset' in entry_value or 'password' in entry_value and 'reset' in entry_value:
		answer_value = test_pass_reset
	elif 'php filter' in entry_value:
		answer_value = requests.get(url+'php-filter').text
	elif 'keyboard' in entry_value:
		answer_value = requests.get(url+'keyboard').text
	elif 'curl' in entry_value:
		answer_value = requests.get(url+'curl').text
	elif 'ssti' in entry_value:
		answer_value = requests.get(url+'ssti').text
	elif 'xss' in entry_value and 'payloads' in entry_value:
		answer_value = requests.get(url+'xss').text
	elif 'xss' in entry_value and 'polyglot' in entry_value:
		answer_value = requests.get(url+'xss-polyglot').text
	elif 'xss' in entry_value and 'lfi' in entry_value:
		answer_value = requests.get(url+'xss-to-lfi').text
	elif 'xss' and 'dork' in entry_value:
		answer_value = requests.get(url+'xss-dorks').text
	elif 'subdomain' in entry_value:
		answer_value = requests.get(url+'subdomain-enum').text
	elif 'api' and 'endpoint' in entry_value:
		answer_value = requests.get(url+'api-endpoint-bypass').text
	elif 'open' and 'redirect' in entry_value:
		answer_value = requests.get(url+'open-redirect').text
	elif 'hydra' in entry_value:
		answer_value = requests.get(url+'hydra').text
	elif 'xxe' and 'protocol' in entry_value:
		answer_value = requests.get(url+'xxe-protocols').text
	elif 'xxe' in entry_value:
		answer_value = requests.get(url+'xxe').text
	elif 'ssrf' in entry_value or 'server side request forgery' in entry_value:
		answer_value = requests.get(url+'ssrf').text
	elif 'csrf' in entry_value:
		answer_value = requests.get(url+'csrf').text
	elif 'lfi' in entry_value:
		answer_value = requests.get(url+'lfi').text
	elif 'mysql' in entry_value:
		answer_value = requests.get(url+'mysql').text
	elif 'nosql' in entry_value:
		answer_value = requests.get(url+'nosqli').text
	elif 'read command output into cookie' in entry_value:
		answer_value = requests.get(url+'read-cmd-out-into-cookie').text
	elif 'python' in entry_value and 'rce' in entry_value:
		answer_value = requests.get(url+'py-rce').text
	elif 'mssql' in entry_value:
		answer_value = requests.get(url+'dump-mssql').text
	elif 'html smuggling' in entry_value:
		answer_value = requests.get(url+'html-smuggling').text
	elif entry_value == 'x':
		answer_value = requests.get(url+'x').text
	elif 'reverse shell' in entry_value:
		answer_value = requests.get(url+'reverse-shells').text
	elif 'php' in entry_value and 'shell' in entry_value:
		answer_value = requests.get(url+'php-rev-shell').text
	elif 'php eval' in entry_value or 'eval' in entry_value:
		answer_value = requests.get(url+'php-eval-code').text
	elif 'sql' in entry_value and 'rce' in entry_value:
		answer_value = requests.get(url+'sqli-to-rce').text
	elif 'sql' in entry_value:
		answer_value = requests.get(url+'sqli').text
	elif 'sqlmap' in entry_value and 'websocket' in entry_value:
		answer_value = requests.get(url+'sqlmap-websocket').text


	answer.delete(1.0, END)
	try:
		answer.insert(INSERT, answer_value)
	except(NameError):
		answer.insert(INSERT, '                           		 		  	    					      			𝟎_𝟎 𝐒𝐨𝐫𝐫𝐲, 𝐢𝐧𝐩𝐮𝐭 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝 𝟎_𝟎')
root = Tk()

topframe = Frame(root)

entry =  Entry(topframe,width=100,borderwidth=2,bg='grey',fg='black')
entry.pack(side=LEFT)

topframe.pack(side = TOP)
buttomframe = Frame(root)

button = Button(topframe, text="search", command=get)
button.pack()

scroll = Scrollbar(buttomframe)
scroll.pack(side=RIGHT,fill=Y)
answer = Text(buttomframe, width=240, height=60, yscrollcommand=scroll.set)
scroll.config(command=answer.yview)
# banner
answer.insert(INSERT, '''\n\n\n\n\n\n\n\n\n

\t\t\t\t\t\t\t\t██   █  █▀ █▄▄▄▄ ▄███▄   ▄█▄     ▄  █       ▄ ▄   ██      ▄▄▄▄▄        ▄  █ ▄███▄   █▄▄▄▄ ▄███▄   
\t\t\t\t\t\t\t\t█ █  █▄█   █  ▄▀ █▀   ▀  █▀ ▀▄  █   █      █   █  █ █    █     ▀▄     █   █ █▀   ▀  █  ▄▀ █▀   ▀  
\t\t\t\t\t\t\t\t█▄▄█ █▀▄   █▀▀▌  ██▄▄    █   ▀  ██▀▀█     █ ▄   █ █▄▄█ ▄  ▀▀▀▀▄       ██▀▀█ ██▄▄    █▀▀▌  ██▄▄    
\t\t\t\t\t\t\t\t█  █ █  █  █  █  █▄   ▄▀ █▄  ▄▀ █   █     █  █  █ █  █  ▀▄▄▄▄▀        █   █ █▄   ▄▀ █  █  █▄   ▄▀ 
\t\t\t\t\t\t\t\t   █   █     █   ▀███▀   ▀███▀     █       █ █ █     █                   █  ▀███▀     █   ▀███▀   
\t\t\t\t\t\t\t\t  █   ▀     ▀                     ▀         ▀ ▀     █                   ▀            ▀            
\t\t\t\t\t\t\t\t ▀                                                 ▀
	''')
answer.pack()

buttomframe.pack()

def update():
	answer.insert(INSERT,'No update available')


def about():
	webview.create_window('akrech', 'https://akr3ch.github.io')
	webview.start()


# create a menu
menubar = Menu(root)
# create a sub-menu
menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu=menu)
menu.add_command(label="Update",command=update)
menu.add_command(label="About", command=about)
menu.add_command(label="Exit", command=root.quit)


root.config(menu=menubar)
root.title("💀𝗵𝗮𝗰𝗸𝗶𝘁💀")

root.mainloop()