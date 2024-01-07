# 0x10. Python - Network #0 project:


Description for all the files and directories in this directory
Any file that does't have a description -if there any- is for testing purposes


`0-hbtn_status.py` -> a Python script that fetches https://alx-intranet.hbtn.io/status


`1-hbtn_header.py` -> a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
No check arguments passed to the script (number or type)


`2-post_email.py` -> a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
The email is sent in the email variable
No check arguments passed to the script (number or type)


`3-error_code.py` -> a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
If any urllib.error.HTTPError exception occur it will print:
"Error code: followed by the HTTP status code"


`4-hbtn_status.py` -> a Python script that fetches https://alx-intranet.hbtn.io/status


`5-hbtn_header.py` -> a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header


`6-post_email.py` -> a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
The email is sent in the email variable
No check arguments passed to the script (number or type)


`7-error_code.py` -> same as `3-error_code.py` but uses different package 'requests'


`8-json_api.py` -> a Python script that takes in a letter and sends a POST request to http://36595c7ea186.6ad0eb84.alx-cod.online:5000/search_user with the letter as a parameter.
The letter is sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
	- Display Not a valid JSON if the JSON is invalid
	- Display No result if the JSON is empty
