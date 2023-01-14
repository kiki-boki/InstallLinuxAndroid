#APA BANG?
import os,sys,stdiomask,rich,time,random
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
def cler():
	os.system('clear')
def ngetik(s):
	for c in s + '\n' :
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random() * 0.05)
def logo():
	Console(width=70).print(Panel('''         _nnnn_                      
       [bold white] dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | [green]Linux Rules[red]![white] |
       M|[red]@[white]||[red]@) [white]M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL         Ram Minimum 4
     dZP        qKRb   
    dZP          qKKb      Devace Android
   fZP            SMMb
   HZM            MMMM     Suport In Python3.X
   FqM            MMMM
 __| ".        |\dS"qML    https://github.com/kiki-boki
 |    `.       | `' \Zq
_)      \.___.,|     .'    PowerdBy@kiki2022
\____   )MMMMMM|   .'
     `-'       `--'        https://kali.org''',title='[bold][Install Linux In [green]Termux[white]]'))
def anjir():
	cler()
	ngetik('Starting Install .......')
	cler()
	ngetik('Starting Install .......')
	cler()
	ngetik('Starting Install .......')
	cler()
	ngetik('Starting Install .......')
	cler()
	ngetik('Starting Install .......')
	cler()
	ngetik('Starting Install.......')
	time.sleep(2)
def bar():
	cler()
	logo()
	table =Table(title="",width=70)
	table.add_column('NO', justify='center', no_wrap=True)
	table.add_column("MENU", justify='center')
	table.add_row("01","Kali ([green]2,4GB[white])")
	table.add_row("02","Debian ([green]1,3GB[white])")
	table.add_row("03","Ubuntu ([green]1,3GB[white])")
	table.add_row("04","ARCH ([green]800MB[white])")
	table.add_row("05","[yellow]Insall Package[white]")
	console = Console()
	console.print(table)
	uyee=input('input = ')
	if uyee in ['1','01']:
		anjir()
		os.system('apt install wget')
		os.system('wget -O install-nethunter-termux https://offs.ec/2MceZWr')
		os.system('chmod +x install-nethunter-termux')
		Console().print(Panel('Now Runnn [green]./install-nethunter-termux[white]'))
	elif uyee in ['02','2']:
		anjir()
		os.system('apt install wget')
		os.system('apt install proot')
		os.system('wget -q https://raw.githubusercontent.com/sp4rkie/debian-on-termux/master/debian_on_termux_10.sh && sh debian_on_termux_10.sh')
		os.system('chmod +x debian_on_termux_10.sh')
		Console().print(Panel('Now Runn [green]./debian_on_termux_10.sh'))
	elif uyee in ['03','3']:
		anjir()
		os.system('apt install wget')
		os.system('apt install proot')
		os.system('git clone https://github.com/Neo-Oli/termux-ubuntu.git')
		os.system('cd termux-ubuntu')
		os.system('chmod +x ubuntu.sh')
		Console().print(Panel('Now Runnn [green]./ubuntu.sh'))
	elif uyee in ['04','4']:
		anjir()
		os.system('apt install wget')
		os.system('apt install proot')
		os.system('wget https://sdrausty.github.io/TermuxArch/setupTermuxArch.sh')
		os.system('chmod +x setupTermuxArch.sh')
		Console().print(Panel('Noww Runn [green]./setupTermuxArch.sh'))
	elif uyee in ['05','5']:
		ngetik('Waiting...................')
		time.sleep(3)
		os.system('apt update'),os.system('apt upgrade'),os.system('apt install wget'),os.system('apt install proot'),os.system('apt install figlet')
		exit()
	elif uyee in ['']:
		Console(width=100).print(Panel('[red]Input Not Fount!!!!'),justify='center')
if __name__ =='__main__':
	bar()
	#CREATE BY KIKIWIJAYA