![enter image description here](https://cloudfront-us-east-1.images.arcpublishing.com/infobae/UEZCFF3XMJF3XHZX5YIM5D735E.jpeg)
# Airbnb clone console.

>## Description.
Backend console of the Airbnb clone.

>## Coding style.
The code of this project is written in Python lenguage following the PyCodeStyle.

>## Usage.
This console works both in interactive mode and in non-interactive mode. A prompt is printed notifying that the console is ready to execute commands.

	$./console.py
	(hbnb)

In non-interactive mode a command must be piped.

	$echo "create BaseModel" | ./console.py
	(hbnb) 1fd71f1b-2f83-463a-b2f8-765522b7dac1
	$

>## Commands.
|Commands              |Description                     |
|----------------------|--------------------------------|
|`quit`                |`Leave the console.`            |
|`EOf`                 |`Leave the console.`            |
|`help`                |`A little help to know how to use the command.`|
|`create <class>`      |`Creates a new instance of a given. class with a unique ID and saves it to a JSON file.`|
|`show <class> <id>`   | `Prints the string representation of a class instance.`|
|`destroy <class> <id>`| `Destroy an instance based on the class name and id`|
|`all <class>`         | `Shows us the string representation of all the instances.`|
|`update`              | `Updates the instance of the class with more attributes.` |

>## Authors.

 - Daniel Ortiz (<a href = "https://github.com/Dannyelgeek">Dannyelgeek<a>)
 - Camilo Zapata (<a href = "https://github.com/ZapataCamilo">Milo<a>)

