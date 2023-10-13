# Manipulating Images 

## Application Programming Interfaces

### Built-In Libaries vs. External Libaries 

The Python Standard Library comes as a part of the Python installation and includes modules for the most common tasks you can do with Python. But there’s a ton of other things you might want to do in your scripts, and not all of them are in the standard library. This is where the external modules come into play. When developers write a Python module that they think others might find useful, they publish it in **PyPI** -- also known as the [**Python Package Index**](https://pypi.org/). We can browse this repository of Python Modules to find the module we need. It includes thousands of projects, which are classified by different categories, like topic, development status, and intended audience. 

In this module, we’re going to be **transforming** and **converting** images. To do that we’ll be using a popular library for image manipulation: the **Python Imaging Library (PIL)**. The original PIL Library hasn’t been updated since 2009 and does not support Python 3. Fortunately, there’s a current fork of PIL called **Pillow**, that properly supports Python 3 and is kept up-to-date. The Pillow library is packaged with the name pillow, but the module name in Python is still **PIL**.

```>>> import PIL
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'PIL'
```