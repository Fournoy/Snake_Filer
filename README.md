# Snake_Filer_v1.2

This project was for train myself, and will possibly not work correctly if you use it... 

This program is used to make directory traversal automatically. You can choose the type of file depending on the OS and the name file you want to search.



By downloading and using Snake_Filer, you fully acknowledge and agree to the terms of this disclaimer, and you commit to using the application responsibly and legally.


Information before using it
-----------------------------
How this programm works :
I used the resquets librairy to make the program, it allows me to send a request to the internet page, the request contain an URL and this URL is used to perform the directory traversal or path traversal.
It's important to have the link of an image in the website. It allows us to be in a certain location, for exemple the "var/www/images". The programm use the different path to travel into the folders of the site by sending HTTP request.
When he send an URL, Snake_Filer verify if the response of the request have a <200> HTML code, if the case is True then the directory traversal work (this problem will soon be solved, indeed, some case send a <200> response even if the folder is not find).

Exemple of utilisation (on PortsSwigger)
------------------------------------------
(Soon...)

References :
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
I used lists of different path of PayloadsAllTheThings by swisskyrepo, the lists help me to take multiple paths possibilities. 
