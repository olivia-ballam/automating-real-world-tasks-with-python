# Week 4 Putting it all Together 
## Project Problem Statement 
You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

- Given a bunch of images and descriptions of each of the new products, you’ll:

- Upload the new products to your online store. Images and descriptions should be uploaded separately, using two different web endpoints.

- Send a report back to the supplier, letting them know what you imported.

Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:

- Run a script on your web server to monitor system health.

- Send an email with an alert if the server is ever unhealthy.

## How to Approach the Problem 

**Break the problem down into smaller pieces.** If you’re not sure how to solve a piece of the puzzle, look for an even smaller piece that you can solve. Build up those smaller pieces into a larger solution!

**Make one change at a time.** Write unit tests to make sure that each new part of the solution works the way you think it does. Run you unit tests frequently to make sure that each part of you solution **keeps working** as you maek changes.

**Use version control.** Check each part of your solution into version control as you complete it, so you can always roll back to knowm version of your code if you make a mistake. 

**Review module documentation!** ading the documentation takes time, but as you become more familiar with the APIs provided by these modules, it could save you from writing a bunch of custom code that could have just been a call to a module function! 

## Automate updating catalog information
### Introduction 

You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs). 

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong. 

### What you'll do 

- Write a script that summerizes and processes sales data into different categories
- Generate a PDF using Python
- Automatically send a PDF by email
- Write a script to check the health status of the system