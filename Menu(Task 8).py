import os
import getpass


os.system("espeak-ng 'hello jee'")
os.system("espeak-ng 'i am your voice assistent'")
os.system("espeak-ng 'billu'")

os.system("tput setaf 3")
os.system("espeak-ng 'welcome to my menu'")
print("\t\t\tWelcome to my Menu !!")
os.system("tput setaf 7")
print("\t\t\t-----------------------")


os.system("espeak-ng 'Enter your password'")
password = getpass.getpass("Enter your password") 

if password !="lw":
	os.system("tput setaf 2")
	print("password incorrect...")
	print("try again....")
	exit()
else:
	os.system("espeak-ng 'login successfully'")
	print("login successfully")



#r = input("Where you want to run this menu ?(local/remote) :")
#print(r)

#if r == "remote":
	#ip = input("Enter remote IP : ")	
	#os.system("ssh {}".format(ip))
#else:
	#print("login successfully")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

print("++++++++++++++++++++++++++++++++++MENU LIST++++++++++++++++++++++++++++++++++++")
	
	
print("""\n\t\t\t\tSELECT THE OPTIONS""")
print("\t\t\t\t-----------------------")
	

print("""\n\t\t\t------>Automation of Basic Commands<-------\n
	 
	 1  : Create a username and password
	 2  : Enter your name to pronounce
	 3  : what is the date of today ? 
	 4  : Open the calender of this month
	 5  : Open the firefox
	 6  : Check the process ID
	 7  : Program id you want to kill
	 8  : Information about RAM
	 9  : Information about CPU
	10  : Information about HARD-DISKS
	11  : View the block storage in this system
	12  : Show the ip address
	13  : Check the internet connectivity
	14  : Capture the packects
	15  : Ping another device ip 
	16  : Show all working ports
	17  : List of all the files in the directory
	18  : Make a directory according to your choice 
	19  : Make a file according to your choice 
	20  : Which directory you want to remove ?
	21  : Which file you want to remove
	22  : Which file you want to view ?
	23  : Copy one file to another directory
	24  : Open the task manager
	25  : Clear the cache memory """)



print("""\n\t\t\t----->Automation Python & Ansible<------- 
	26  : Open the PYTHON Interpreter
	27  : Download Ansible """)
	
	

print("""\n\t\t\t------>Automation LVM Partition<-------
	 
	 28  : Display information about filesystem
	 29  : Create a LVM partition
	 30  : Format and mount the LVM partition
	 31  : Extend the size of LVM""")
	#---------------------------------------

print("""\n\t\t\t------>Automation Apache Webserver<-----
	 
	 32  : Configure Webserver
	 33  : Start webserver
	 34  : Show status Webserver
	 35  : Stop Webserver""")

	#------------------------------------------------
print("""\n\t\t\t------>Automation Devops Docker<-------	

	 36  : Start Docker 
	 37  : Show Status Docker
	 38  : Stop Docker
	 39  : List all the docker container
	 40  : List all the docker images
	 41  : Pull Docker Image.
	 42  : Create a Docker Container
	 43  : Show running Docker Container
	 44  : Start runnning Docker Container
	 45  : Stop runnning Docker Container
	 46  : exit
 	 47  : configure docker
	""")

	
	







#######################################################################################
#####################################################################################
os.system("espeak-ng 'do you want to listen menu list ? enter yes or no'")
voicemenu = input("Do you want to listen the menu list ? enter (yes/no) : ") 

if voicemenu == "yes":

	
	os.system("espeak-ng 'select your desired options'")
	#------------------------------------------
	os.system("espeak-ng 'Automation of Basic Commands'")
	os.system("espeak-ng 'press 1 Create a username and password'")
	os.system("espeak-ng 'press 2 Enter your name to pronounce'")
	os.system("espeak-ng 'press 3 what is the date of today ?'")
	os.system("espeak-ng 'press 4 Open the calender of this month'")

	os.system("espeak-ng 'press 5 Open the firefox'")
	os.system("espeak-ng 'press 6 Check the process ID'")
	os.system("espeak-ng 'press 7 program id you want to kill'")
	os.system("espeak-ng 'press 8 Information about RAM'")
	os.system("espeak-ng 'press 9 Information about CPU'")
	os.system("espeak-ng 'press 10 Information about HARD-DISKS'")
	os.system("espeak-ng 'press 11 View the block storage in this system'")
	os.system("espeak-ng 'press 12 Show the ip address'")
	os.system("espeak-ng 'press 13 Check the internet connectivity'")
	os.system("espeak-ng 'press 14 Capture the packects'")
	os.system("espeak-ng 'press 15 Ping another device ip '")
	os.system("espeak-ng 'press 16 Show all working ports'")
	os.system("espeak-ng 'press 17 List of all the files in the directory'")
	os.system("espeak-ng 'press 18 Make a directory according to your choice '")
	os.system("espeak-ng 'press 19 Make a file according to your choice '")
	os.system("espeak-ng 'press 20 Which directory you want to remove ?'")
	os.system("espeak-ng 'press 21 Which file you want to remove'")
	os.system("espeak-ng 'press 22 Which file you want to view ?'")
	os.system("espeak-ng 'press 23 Copy one file to another directory'")
	os.system("espeak-ng 'press 24 Open the task manager'")
	os.system("espeak-ng 'press 25 Clear the cache memory '")
		
		
	#-----------------------------------------------------------------------

	os.system("espeak-ng 'Automation Python & Ansible'")

	os.system("espeak-ng 'press 26 Create a username and password'")
	os.system("espeak-ng 'press 27 Enter your name to pronounce'")


	#----------------------------------------------------------------------------


	os.system("espeak-ng 'Automation LVM Partition'")

	os.system("espeak-ng 'press 28 Display information about filesystem'")
	os.system("espeak-ng 'press 29 Create a LVM partition'")
	os.system("espeak-ng 'press 30 Format and mount the LVM partition'")
	os.system("espeak-ng 'press 31 Extend the size of LVM '")

	#-----------------------------------------------------------------------------

	os.system("espeak-ng 'Automation Apache Webserver'")
	os.system("espeak-ng 'press 32 Configure Webserver'")
	os.system("espeak-ng 'press 33 Start webserver'")
	os.system("espeak-ng 'press 34 Show status Webserver'")
	os.system("espeak-ng 'press 35 Stop Webserver'")

	#------------------------------------------------------------------------------------

	os.system("espeak-ng 'Automation Devops Docker'")
	os.system("espeak-ng 'press 36 Start Docker '")
	os.system("espeak-ng 'press 37 Show Status Docker'")
	os.system("espeak-ng 'press 38 Stop Docker'")
	os.system("espeak-ng 'press 39 Stop Docker '")
	os.system("espeak-ng 'press 40 Stop Docker'")
	os.system("espeak-ng 'press 41 Pull Docker Image.'")
	os.system("espeak-ng 'press 42 Create a Docker Container'")
	os.system("espeak-ng 'press 43 Show running Docker Container'")
	os.system("espeak-ng 'press 44 Start runnning Docker Container'")
	os.system("espeak-ng 'press 45 Stop runnning Docker Container'")
	os.system("espeak-ng 'press 46 exit '")

else:
	print("you can see menu list")




######################################################################################
#######################################################################################
				
while True:
	os.system("espeak-ng 'enter your choice'")
	
	ch = int(input("Enter your Choice: "))
	print(ch)
	
			

#####################################################################################

	





	if (ch==1):
		os.system("espeak-ng 'Create a username'")
		username = input("Create a user name you want :  ")
		os.system("useradd {}".format(username))
		os.system("espeak-ng 'Create a password'")
		password = input("Create a user name you want :  ")
		os.system("passwd {}".format(password))
		

	elif (ch==2):
		os.system("espeak-ng 'Enter your good name to pronounce'")
		pronounce = input("Enter your good name to pronounce :")
		os.system("espeak-ng '{}'".format(pronounce))

	
	elif (ch==3):
		os.system("espeak-ng 'date of today is '")
		print("DATE of today is..")
		os.system("date")
		
	elif (ch==4):
		os.system("espeak-ng 'open the calender of this month'")
		print("CALENDER of the month")
		os.system("cal")

	elif (ch==5):
		os.system("espeak-ng 'open the firefox'")
		print("open the firefox")
		os.system("firefox")

	elif (ch==6):
		os.system("espeak-ng 'enter the program for which you want to check the process id'")
		processid = input("enter the program for which you want to check the process id : ")
		os.system("ps aux | grep -i {}".format(processid))


	elif (ch==7):

		os.system("espeak-ng 'enter the program id you want to kill : '")
		killid = input("enter the program id you want to kill : ")
		os.system("kill '{}'".format(killid))

	elif (ch==8):
		os.system("espeak-ng 'Information about RAM'")
		print("Information about RAM")
		os.system("free -m")
	elif (ch==9):
		os.system("espeak-ng 'Information about CPU'")
		print("Information about CPU")
		os.system("lscpu")
	
	elif (ch==10):
		os.system("espeak-ng 'Information about hard disks'")
		print("Information about HARD-DISKS")
		os.system("fdisk -l")
	
	
	

	elif(ch==11):
		os.system("espeak-ng 'view the block storage in this system'")
		print("view the block storage in this system")
		os.system("lsblk")



	elif(ch==12):
		os.system("espeak-ng 'show the ip address'")
		print("show the IP address")
		os.system("ifconfig")

	elif(ch==13):
		os.system("espeak-ng 'check the internet connectivity'")
		print("Check the internet connectivity")
		os.system("ping google.com")


	elif(ch==14):
		os.system("espeak-ng 'capture the packects'")
		print("capture the packects")
		os.system("tcpdump")
	
	elif(ch==15):
		os.system("espeak-ng 'enter the ip of that device you want to ping with'")
		anotherip = input("ping another device ip : ")
		os.system("ping '{}'".format(anotherip))




	elif(ch==16):
		os.system("espeak-ng 'show all working ports'")
		print("show all working ports ")
		os.system("netstat -tnlp")
	


	elif(ch==17):
		os.system("espeak-ng 'list of all the files in the directory'")
		print("list of all the files in the directory")
		os.system("ls")
	


	elif(ch==18):
		os.system("espeak-ng 'make a directory according to your choice'")
		directory = input("make a directory according to your choice : ")
		os.system("mkdir /{}".format(directory))
	
	elif(ch==19):
		os.system("espeak-ng 'make a file according to your choice'")
		createfile = input("make a file according to your choice : ")
		os.system("gedit '{}'".format(createfile))

	elif(ch==20):
		os.system("espeak-ng 'which directory you want to remove'")
		removedirectory = input("which directory you want to remove : ")
		os.system("rm rf /'{}'".format(removedirectory))

	elif(ch==21):
		os.system("espeak-ng 'which file you want to remove'")
		removefile = input("which file you want to remove : ")
		os.system("rm rf '{}'".format(removefile))

	elif(ch==22):
		os.system("espeak-ng 'which file you want to view'")
		viewfile = input("which file you want to view : ")
		os.system("cat '{}'".format(viewfile))

	elif(ch==23):
		os.system("espeak-ng 'enter the name of source file you want to copy'")
		sourcefile = input(" enter the name of source file you want to copy : ")
		os.system("espeak-ng 'enter the name of destination file'")
		destinationfile = input(" enter the name of destination file : ")
		os.system("cp {} {}".format(sourcefile,destinationfile))

	elif(ch==24):
		os.system("espeak-ng 'open the task manager'")
		print("open the task manager")
		os.system("top")

	elif(ch==25):
		os.system("espeak-ng 'clear the cache memory'")
		print(" clear the cache memory ")
		os.system("echo 3 > /proc/sys/vm/drop_caches")
		os.system("free -m")

########################################################################################

    #python and ansible
  
	elif(ch==26):
		os.system("espeak-ng 'open the python interpreter'")
		os.system("python3")
	
	elif(ch==27):
		os.system("espeak-ng 'Downloading the ansible'")
		print("Downloading the ansible ")
	#	os.system("python3")
		os.system("pip3 install ansible")
		


#######################################################################################
	
 #LVM	

	
	elif (ch==28):
		os.system("espeak-ng 'Display information about filesystem'")
		print("Display information about filesystem")
		os.system("df -h")
		

	elif (ch==29):
		os.system("espeak-ng 'create a LVM Partition'")
		print("create a LVM Partition..")
		os.system("tput setaf 3")
		os.system("espeak-ng 'Display the information about the hardisks  '")
		print("Display the information about the hardisks..")
		os.system("fdisk -l")
		print("\n\n")
		os.system("tput setaf 3")
		os.system("espeak-ng 'Gve the name of the device you want'")
		device = input("Give the name of the device you want : ")
		os.system("fdisk -l {}".format(device))
		print("\n\n")
		os.system("espeak-ng 'create a physical volume'")
		os.system("pvcreate {}".format(device))
		print("\n\n")
		os.system("espeak-ng 'display the physical volume'")
		os.system("pvdisplay {}".format(device))
		print("\n\n")
		os.system("espeak-ng 'enter the volume group name'")
		aa = input("ENTER VOLUME GROUP NAME : ")
		os.system("espeak-ng 'create a volume group'")
		os.system("vgcreate {} {}".format(aa,device))
		os.system("espeak-ng 'display the volume group'")
		os.system("vgdisplay {}".format(aa))
		print("\n\n")		
		os.system("espeak-ng 'enter logical group name'")
		bb = input("ENTER LOGICAL GROUP NAME : ")
		os.system("espeak-ng 'enter the size of logical volume in GB'")
		lvsize = input("Enter the size of logical volume in GB : ")
		os.system("lvcreate --size {} --name {} {}".format(lvsize,bb,aa))


	elif (ch==30):
		
		os.system("espeak-ng 'enter the volume group name'")
		aa = input("ENTER VOLUME GROUP NAME")
		os.system("espeak-ng 'enter the logical group name'")
		bb = input("ENTER LOGICAL GROUP NAME")
		os.system("espeak-ng 'display volume group name'")
		os.system("vgdisplay {}".format(aa))
		os.system("espeak-ng 'formatting the LVM partition'")	
		print("Format the LVM Partition")
		os.system("mkfs.ext4 /dev/{}/{}".format(aa,bb))
		print("\n\n")
		os.system("espeak-ng 'mount the LVM partition'")
		print("Mount the LVM Partition")
		os.system("espeak-ng 'enter the foldername for mount'")
		foldername = input("enter the foldername for mount : ")
		os.system("mkdir /{}".format(foldername))
		os.system("mount /dev/{}/{}  /{}".format(aa,bb,foldername))
		os.system("espeak-ng 'successfully mounted'")
		print("successfully mounted")

	elif(ch==31):
		
		os.system("espeak-ng 'enter the volume group name'")
		aa = input("ENTER VOLUME GROUP NAME")
		os.system("espeak-ng 'enter the logical group name'")
		bb = input("ENTER LOGICAL GROUP NAME")
		os.system("espeak-ng 'How much you want to extend the size of LVM Partition'")
		c = input("How much you want to extend the size of LVM Partition : ")
		os.system("lvextend --size +{}  /dev/{}/{}".format(c,aa,bb))
		os.system("espeak-ng 'volume has been extended'")
		print("\n\nvolume has been extended")
		os.system("resize2fs /dev/{}/{}".format(aa,bb))
		print("\n\n")
		os.system("espeak-ng 'information about the LVM Partiton'")
		print("information about the LVM Partiton")
		os.system("df -h")
########################################################################################



        #WEBSERVER

	elif (ch==32):
		os.system("espeak-ng 'Configure Webserver'")
		print("Configure Webserver")
		os.system("yum install httpd -y")
	

	elif (ch==33):
		os.system("espeak-ng 'start webserver'")
		print("Start Webserver")
		os.system("systemctl start httpd")
		os.system("systemctl enable httpd")
	elif (ch==34):
		os.system("espeak-ng 'Show the Status of Webserver'")
		print("Show Status of Webserver")
		os.system("systemctl status httpd")
	
	elif (ch==35):
		os.system("espeak-ng 'Stop Webserver'")
		print("Stop Webserver")
		os.system("systemctl stop httpd")


#######################################################################################		



	#DOCKER	
	
	elif (ch==36):
		os.system("espeak-ng 'start docker'")
		print("Start Docker..")
		os.system("systemctl start docker")
	elif (ch==37):
		os.system("espeak-ng 'show the status of docker'")
		print("Show Status of Docker..")
		os.system("systemctl status docker")
	
	elif (ch==38):
		os.system("espeak-ng 'stop docker'")
		print("Stop Docker..")
		os.system("systemctl stop docker")
		
	elif (ch==39):
		os.system("espeak-ng ' list all the docker containers'")
		print("List all docker containers..")
		os.system("docker ps -a")

	elif (ch==40):
		os.system("espeak-ng 'List all docker images'")
		print("List all docker images..")
		os.system("docker images")
	
	elif (ch==41):
		os.system("espeak-ng 'pull docker images'")
		print("Pull docker image..")
		os.system("espeak-ng 'which docker image you want to pull'")
		image = input("which docker image you want to pull ? ")
		os.system("docker pull {}".format(image))

	elif (ch==42):
		os.system("espeak-ng 'Give the name of docker container you want to launch '")
		print("Create a Docker container")
		container = input("Give the name of docker container you want to launch ? ") 
		os.system("espeak-ng 'which docker image you want to attach'")
		availableimage = input("which docker image you want to attach ? ")
		
		os.system("docker run -it --name {} {}".format(container,availableimage))
	

	elif (ch==43):
		os.system("espeak-ng 'Show running Docker Container'")
		print("Show running Docker Container")
		os.system("docker ps")
	elif (ch==44):
		os.system("espeak-ng 'Start running Docker Container'")
		print("Start runnning Docker Container")
		startcontainer = input("which conatiner you want to start : ")
		os.system("docker start {}".format(startcontainer))
	elif (ch==45):
		os.system("espeak-ng 'Stop running Docker Container'")
		print("Stop runnning Docker Container")
		stopcontainer = input("which conatiner you want to stop : ")
		os.system("docker stop {}".format(stopcontainer))
		
####################################################################################

    


	elif (ch==46):
		os.system("espeak-ng 'tata bye bye'")
		print("not supported")
		os.system("exit")	

	elif (ch==47):
		os.system("espeak-ng 'configure docker'")
		print("configure docker")
		os.system("yum install docker-ce --nobest")
	
	

########################################################################################
		

	else:
		print("not supported")
		os.system("exit")	
	
	
	



########################################################################################


