Environment
===========

* `1, eclipse`
	:: version: Eclipse Helios SR2 Packages (v 3.6.2) 
	filename: eclipse-jee-helios-SR2-win32-x86_64.zip (Extracting to  E:\Helios3\eclipse)
	first step: 
	add two line to modify eclipse.ini
	-vm
	C:/Java/jdk1.7.0_51_x64/bin/javaw.exe
	
* `2, egit`
	:: org.eclipse.egit-updatesite-1.2.0.201112221803-r-site.zip
	Extracting to the folder E:\Helios3\eclipse\MyPlugins\git\eclipse
	
* `3, pydev`
	:: version: 3.6.0
	filename: PyDev 3.6.0.zip
	Extracting to the folder E:\Helios3\eclipse\MyPlugins\pydev\eclipse
	
* `4, plugins type`
   links 
	:: E:\Helios3\eclipse\links
		git.link (content: path=MyPlugins/git)
		pydev.link (content: path=MyPlugins/pydev)

Version 1.0
===========
add views.py

Execute
=======
Click the right button of project, run django -> Custom command, 
input: runserver 0.0.0.0:8100  

Test URL:
=========
http://127.0.0.1:8100/hello/