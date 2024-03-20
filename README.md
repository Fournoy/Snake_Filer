# Snake_Filer
This program is used to make directory traversal automatically. You can choose the type of file depending on the OS and the name file you want to search.


Disclaimer: Any illicit use of this program is strictly prohibited. 
It is important to emphasize that users of Snake_Filer are solely responsible for their actions when using this program. I disclaim any liability for abusive or illicit use of the application by third parties. Users are required to comply with the laws and regulations in their jurisdiction when using Snake_Filer.

By downloading and using Snake_Filer, you fully acknowledge and agree to the terms of this disclaimer, and you commit to using the application responsibly and legally.


Information before using it
-----------------------------
How this programm works :
I used the resquets librairy to make the program, it allows me to send a request to the internet page, the request contain an URL and this URL is used to perform the directory traversal or path traversal.
It's important to have the link of an image in the website. It allows us to be in a certain location, for exemple the "var/www/images". The programm use the different path to travel into the folders of the site by sending URL.
When he send a URL, Snake_Filer verify if the URL have a <200> HTML code, if the case iis True then the directory traversal work. 


Future update
------
More paths possibilites and maybe another kind of test will be implemented.

References :
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
I used lists of different path of PayloadsAllTheThings by swisskyrepo, the lists help me to take multiple paths possibilities. 
