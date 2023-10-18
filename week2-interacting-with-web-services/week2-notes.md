# Interacting with Web Services 

## Web Applications and Services 

A **web application** is an application that you interact with over HTTP. Most of the time when you're using a website on the internet, you're interacting with a web application. So, how does this look behind the scenes? 

Your web browser send an HTTP request to a web server. Then, the web server passes the request along to the web application in charge of deciding what information to show you. The application then generates the website content (in HTML format). The application is also in charge of serving images and any other necessary data so that your browser can render the website on your computer. 

Lot of web applications also have APIs that you can use from your scripts! Web applications that have an API are also known as **web services**. Instead of browsing to a web page to type and click around, you can use your program to send a message known as an **API call** to the web service. The part of the program that listens on the network for API calls is called an API endpoint. 

When you interact with a web service like this, you don't even care what language the other application is using. You interact with it using a specified protocol, and the only important constraint ia that both the service and your program know how to use this protocol. 

<br />

### Data Serialization 

If you have two programs that need to communicate with each other, how do you get that data from one palce to another? 

** What do you send?** When you have a conversation with another person, you don't send thoughts and memories directly between you brains. At least not yet! You first have to convert your thoughts into language, and then transmit that language to another person. They take that language, and convert it back into thoughts. It's the same with programs running in different places, or at different times. 

Taking out a list of lists in memory and writing it to the disk as a **Comma-Separated Value (CSV)** file, is an example of a technique called **data serialization**. Data serialization is the process of taking an in-memory data structure, like a Python object, and turning it into something that can be stored on disk or transmitted across a network. Later, the file can be read, or the network transmission can be received by another program and turned back into an object again. Truning the serialized object back into an in-memory object is called **deserialization**.

Data serialization is extremely useful for communicating with web services. A web service's **API endpoint** takes messages in a specific format, containing specific data. 

Let's start with the contact information in a CSV file. We'll keep just two entries to keep our example's short, but there's no limit to how long these can be. 

```
name,username,phone,department,role
Sabrina Green,sgreen,802-867-5309,IT Infrastructure,System Administrator
Eli Jones,ejones,684-3481127,IT Infrastructure,IT specialist
```

Instead of having a list of lists, we could turn this infomation into a list of dictionaries. In each of these dictionaries, the key will be the name of column, and the value will be corresponding information in each row. It could look something like this below. 

```
people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": "802-867-5309",
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": "684-348-1127",
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]
```
Using a structure like this lets us do interesting things with our information that's much hards to do with CSV files. For example, let's say we want to record more than one phone number for each person. Instead of using a single string for "phone", we could represent that data in another dictionary, like this:

```people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]
```

Now, we can record mulitple phone numbers per person, and give them decriptive names like "office" and "cell". This would be hard to store in a CSV file, because the data is not flat. To help us with that, there's a bunch of different formats that we can use to store our data when the structure isn't flat. 

<br />


### Data Serialization Formats

**JSON (Javascript Object Notation)**. We can use the **json** module in python to convert our people list of dictionaries into JSON format. 

```
import json

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)
```

This code uses the ```json.dump()``` function to serialize the people object into a JSON file. The contents of the file will look something like this:

```
import json

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)
```

**YAML (Yet Another Markup Language)** has a lot in common with JSON. They're both formats that can easily understood by a human when looking at the contents. In this example, we're using the ```yaml.safe_dump()``` method to serialize our object into YAML:

```
import yaml

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)
```
That code will generate a **people.yaml** like that looks like this:

```
- department: IT Infrastructure
  name: Sabrina Green
  phone:
    cell: 802-867-5310
    office: 802-867-5309
  role: Systems Administrator
  username: sgreen
- department: IT Infrastructure
  name: Eli Jones
  phone:
    office: 684-348-1127
  role: IT Specialist
  username: ejones
```

While this doesn't exactly like the JSON example above, both formats list the names of the fields as part of the format, so that both the programs parsing data and the humans looking at it can make sense out of it. This main difference is how these formats are used. JSON is used frequently for transmitting data between web services, while YAML is used the most for storing configuration values. 

<br />

### More About JSON

JSON is **human-readable**, which means it's encoded using printable characters, and formatted in a way that a human can understand. This doesn't necessarily mean that you will understand it when you look at it, but you can. 

Lots of web services send messages back and forth using JSON. 

JSON supports a few **elements** of different data types. These are very basic data types; they represent the most common basic data types supported by any programming language you might use. 

JSON has **strings**, which sre enclosed in quotes. 

```
"Sabrina Green"
```

It also has **numbers**, which are not. 

```
1002
```
JSON  has **objects**, which a key-value pair structures like Python Dictionaries. 

```
{
  "name": "Sabrina Green",
  "username": "sgreen",
  "uid": 1002
}
```

And a key-value pair can coantin another object as a value. 

```
{
  "name": "Sabrina Green",
  "username": "sgreen",
  "uid": 1002,
  "phone": {
    "office": "802-867-5309",
    "cell": "802-867-5310"
  }
}
```

JSON has **arrays**, which are equivalent to Python lists. Arrays can contain strings, numbers, objects or other arrays. 

```
[
  "apple",
  "banana",
  12345,
  67890,
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  }
]
```

JSON elements are always **comma-delimited**. 

The json library will help us turn Python objects into JSON, and turn JSON strings into Python objects! The dump() method serializes basic Python objects, writing them to a file. Like in this example:

```
import json

people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

with open('people.json', 'w') as people_json:
    json.dump(people, people_json)
```

That gives us a file with a single line that looks like this:  

```
[{"name": "Sabrina Green", "username": "sgreen", "phone": {"office": "802-867-5309", "cell": "802-867-5310"}, "department": "IT Infrastructure", "role": "Systems Administrator"}, {"name": "Eli Jones", "username": "ejones", "phone": {"office": "684-348-1127"}, "department": "IT Infrastructure", "role": "IT Specialist"}]
```

JSON doesn't need to contain multiple lines, but it sure can be hard to read the result if it's formatted this way! Let's use the **indent** parameter for ```json.dump()``` to make it a bit easier to read.  

```
with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)
```

The resulting file should look like this:  

```
[
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]
```

Another option is to use the ```dumps()``` method, which also serializes Python objects, but returns a string instead of writing directly to a file.  

```
>>> import json
>>> 
>>> people = [
...   {
...     "name": "Sabrina Green",
...     "username": "sgreen",
...     "phone": {
...       "office": "802-867-5309",
...       "cell": "802-867-5310"
...     },
...     "department": "IT Infrastructure",
...     "role": "Systems Administrator"
...   },
...   {
...     "name": "Eli Jones",
...     "username": "ejones",
...     "phone": {
...       "office": "684-348-1127"
...     },
...     "department": "IT Infrastructure",
...     "role": "IT Specialist"
...   }
... ]
>>> people_json = json.dumps(people)
>>> print(people_json)
[{"name": "Sabrina Green", "username": "sgreen", "phone": {"office": "802-867-5309", "cell": "802-867-5310"}, "department": "IT Infrastructure", "role": "Systems Administrator"}, {"name": "Eli Jones", "username": "ejones", "phone": {"office": "684-348-1127"}, "department": "IT Infrastructure", "role": "IT Specialist"}]
```

The ```load()``` method does the inverse of the ```dump()``` method. It deserializes JSON from a file into basic Python objects. The ```loads()``` method also deserializes JSON into basic Python objects, but parses a string instead of a file.  

```
>>> import json
>>> with open('people.json', 'r') as people_json:
...     people = json.load(people_json)
... 
>>> print(people)
[{'name': 'Sabrina Green', 'username': 'sgreen', 'phone': {'office': '802-867-5309', 'cell': '802-867-5310'}, 'department': 'IT Infrastructure', 'role': 'Systems Administrator'}, {'name': 'Eli Jones', 'username': 'ejones', 'phone': {'office': '684-348-1127'}, 'department': 'IT Infrastructure', 'role': 'IT Specialist'}, {'name': 'Melody Daniels', 'username': 'mdaniels', 'phone': {'cell': '846-687-7436'}, 'department': 'User Experience Research', 'role': 'Programmer'}, {'name': 'Charlie Rivera', 'username': 'riverac', 'phone': {'office': '698-746-3357'}, 'department': 'Development', 'role': 'Web Developer'}]
```
<br />

## Python Requests
### The Python Requests Library

** HTTP (HyperText Transfer Protocol) is the protocol of the world-wide web. When you visit a webpage with your web browser, the browser is making a series of **HTTP requests** to web servers somewhere out on the Internet. Those servers will answer with HTTP responses. This is also how we're going to send and receive messages with web applications from our code. 

The [Python Requests library](https://requests.readthedocs.io/en/latest/) makes it super easy to write programs that send and receive HTTP. Instead of having to understand the HTTP protocol in great detail, you can just make a very simple HTTP connections using Python objects, and then send and receive messages using the methods of those objects. Let's look at an example. 

```
>>> import requests
>>> response = requests.get('https://www.google.com')
```

That was a basic request for a web page, we used the Requests library to make a **HTTP GET** request for a specific **URL (Uniform Resource Locator)**. The URL tells the Requests library the name of the resource **(www.google.com)** and what protocol to use to get the resource **(http://)**. The result we get is an object type [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response).

What did the web server respond with? Lets take a look at the the first 300 characters of the [Response.text](https://requests.readthedocs.io/en/latest/api/#requests.Response.text)

```
>>> print(response.text[:300])
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="de"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="dZfbIAn803LDGXS9
```
Now, it might be hard for you to read the **HTML (HyperText Markup Language)** that was returned in this resonse, but you web browser knows just how to turn that into a familiar-looking web page. 

Even with this simple example, the Requests module has done a whole lot of work for us! We didn't have to write any code to find the web server, make a network connection construct an HTTP message, wait for a response, or decode the response. Not that HTML can't be messy enough on its own, but let's look at the first bytes of the raw message that we received from the server:

```
>>> response = requests.get('https://www.google.com', stream=True)
>>> print(response.raw.read()[:100])
b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x02\xff\xc5Z\xdbz\x9b\xc8\x96\xbe\xcfS`\xf2\xb5-\xc6X\x02$t\xc28\xe3v\xdc\xdd\xee\xce\xa9\xb7\xdd;\xe9\x9d\xce\xf6W@\t\x88\x11`@>D\xd6\x9b\xce\xe5<\xc3\\\xcd\xc5\xfc\xab8\x08\xc9Nz\x1f.&\x8e1U\xb5j\xd5:\xfc\xb5jU\x15\x87;^\xe2\x16\xf7)\x97\x82b\x1e\x1d\x1d\xd2S'
```

What's all that? The response was **compressed** with [gzip](https://www.gzip.org/), so it had to be **decompressed** before we could even read the text of the HTML. One more thing that the Requests library handled for us!

The [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object also contains the exact request that was created for us. We can check out the headers stored in our object to see that the Requests module told the web server that it was okay to compress the content:

```
>>> response.request.headers['Accept-Encoding']
'gzip, deflate'
```

And then the server told us that the content had actually been compressed.

```
>>> response.headers['Content-Encoding']
'gzip'
```
<br />

### Useful Operations for Python Requests

There's a ton of things that we can do with Python Request. 

First, how do we know if a request we made got a successful response? You can check out the value of [Response.ok](https://requests.readthedocs.io/en/latest/api/#requests.Response.ok), which will be **True** if the response was good, and **False** if it wasn't.

```
>>> response.ok
True
```
Now keep this in mind that this will only tell you if the web server says that the response successfully fulfilled the request. The response module can't determine if that data that you got back is the kind of data that you were expecting. You'll need to do your own checking for that!

If the boolean isn't specific enough for your needs, you can get the [HTTP response code](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) that was returned by looking a [Response.status code](https://requests.readthedocs.io/en/latest/api/#requests.Response.ok).

```
>>> response.status_code
200
```

To write maintainable, stable code, you'll always want to check your response to make sure they succeeded before trying to process them further. For example, you could do something like this. 

```
response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))
```

But you don't really need to do that. Requests has us covered here too! We can use the [Response.raise for status()](https://requests.readthedocs.io/en/latest/api/#requests.Response.raise_for_status) method, which will raise an **HTTPError** exception only if the response wasn't successful.

```
response = requests.get(url)
response.raise_for_status()
```
<br />

### HTTP GET and POST Methods

HTTP supports several [HTTP methods](https://datatracker.ietf.org/doc/html/rfc7231#section-4.3), like GET, POST, PUT, and DELETE. 

The [HTTP Get method](https://datatracker.ietf.org/doc/html/rfc7231#section-4.3.1), of course, retrieves or **gets** the resource specified in the URL. By sending a Get request to the webserver, you're asking for the server to GET the resource for you. When you're browsing the web, most of what you're doing us using your web browser to issue a whole bnch of GET requests for the text, images, videosm and so forth that your browser will display. 

A GET request can have **parameters**. Have you ever seen a URL thta look like this? 

```
https://example.com/path/to/api/cat_pictures?search=grey+kitten&max_results=15
```

The question mark separates the URL respource from the resource's parameters. These parameters are one or more key-value pairs, formated as a [query string](https://en.wikipedia.org/wiki/Query_string). In the example above, the **search** parameter is set to "grey+kitten", and the **max results** parameter is set to 15. 

But you don't have to write your own code to create an URL like that one. With ```requests.get()```, you can provide a dictionary of parameters, and the Requests module module will construct the correct URL for you!

```
>>> p = {"search": "grey kitten",
...      "max_results": 15}
>>> response = requests.get("https://example.com/path/to/api", params=p)
>>> response.request.url
'https://example.com/path/to/api?search=grey+kitten&max_results=15'
```
You might notice that using parameters in Requests is yet another form of data serialization. Querey strings are handy when we want to send small bits of information, but as our data becomes more complex, it can get hard to represent it usign query strings. 

An alternative in that case is using the [HTTP POST method](https://datatracker.ietf.org/doc/html/rfc7231#section-4.3.3). This method sends, or **posts**, data to a web service. Whenever you fill a seb form and press a button to submit, you're usign the POST method to send that data back to the web server. This method tends to be used when there's a bunch of data to transmit. 

A POST request can look very similar to a GET request. Instead of setting the params attribute, which gets turned into a querey string and appended to the URL, we use the **data** attribute, which contains the data that will be sent as part of the POST request. 

```
>>> p = {"description": "white kitten",
...      "name": "Snowball",
...      "age_months": 6}
>>> response = requests.post("https://example.com/path/to/api", data=p)
```

Let's check out the generated URL for this request:

```
>>> response.request.url
'https://example.com/path/to/api'
```

See how much simpler the URL is on this POST now? Where did all the parameters go? They're part of the **body** of the HTTP message. We can see them by checking out the **body** attribute.

```
>>> response.request.body
'description=white+kitten&name=Snowball&age_months=6'
```

So, if we need to send and receive data from a web service, we can turn our data into dictionaries and then pass as the **data** attribute of a POST request. 

Today, it's supper common to send and receive data specifically in JSON format, so the Requests module can do the conversion directly for us, using the **json** parameter. 

```>>> response = requests.post("https://example.com/path/to/api", json=p)
>>> response.request.url
'https://example.com/path/to/api'
>>> response.request.body
b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 
```

<br />

## What is Django?

Djano is a **full-stack web framework** written in Python. 

A full-stack web framework handles a bunch of different components that asre typical when creating a web application It contains libraries that help you handle each of the pieces: writing your application's code, storing and retrieving data, receiving web requests, and responding to them. If you need to build an application that has a web frontend using a web framework like Django can save you alot of time and effort, because a lot of challenges are already solved for you. 

Web frameworks are commonly split into three basic components: (1) the application code, where you'll add all of your applications logic; (2) the data storage, where you'll configure what data you want to store and how you're storing it; and (3) the web server, where you'll state which pages are served by which logic. 

Spilting your code like that helps you write more module code, promotes code resue, and allows for flexibility when viewing and accessing data. For example, you could have a simple web page where users of the system can access the information already stored in it, and seperate programmatic interface that can be used by other scripts or applications to transmit data to the system. 

When you're writing a web application, there's a ton of little decisions to make. Relying on a framework like Django is similar to using external libraries for your code. There are a lot of features, which you can use very easily, instead of writing everything from scratch and re-making all of the same mistakes that we all make when writing a web application for the first time. 

Django has a ton of useful components for building websites. Django can be used for serving a company website, including customer reviews. It does this by taking the request for a URL and parsing it using the **urlresolver** module. This is a core module in Django that interprets URL requests and matches them against a list of defined patterns. If a URL matches a pattern, the request is passed to the associated function, called a **view**. This allows you to serve different pages depending on what URL is being requested. You can even build complex logic into the fucntion handling the request to make more dynamic, interactive and exciting pages. 

Django can also handle reading and writing data from a database, letting you store and retrieve data used by your application. In the lab, the database holds the customer reviews for the company. When a user loads the website, the logic will ask the database fir all available customer reviews. These are reteived and formatted into a web page, which is served as a response to the URL request. Django makes it easy to interact with data stored in a database by using an **object-realtional mapper**, or **ORM**. This tool provides an easy mapping between data models defined as Python classes and an underlying database that stores the data in question. 

On top of this, the Django application running in the lab includes an **endpoint** that can be used to add new customer reviews to the database. This endpoint is configured to receive data in JSON format, sent through an HTTP POST request. The data transmitted will then be stored in the database and added to the list of all reviews. The framework even generates an interactive web form, that lets us directly with the endpoint using our browser, which can be really handy for testing and debugging. 

Django is one of many popular web frameworks. Alternative Python-based web frameworks similar to Django include Flask, Bottle, CherryPy, and CubicWeb. There are a host of other frameworks written in other languages too, not just Python.