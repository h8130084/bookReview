# Data Centric Development Milestone Project - Book Review website

The website was designed to allow users to write a book review and / or search for books that have been reviewed by other users.
The site also allows users to write comments about the review and upvote the book. Users can also upvote so people can see quickly how popular the book is.
The website offers a search bar to search for reviewed books.
The website then generates the results in an easy to list and gives users the name of the book which is also a link to more details of the book.
The site also allows users to edit the book details to help allow users to edit any inaccurate information about the book.

The overall aim is to have an easy to navigate website that was designed desktop first to enable users to find a book and review it.

# UX

The UX has been designed for desktop first to make it easy for all users to navigate and access the content they want.

I have provided a number of user stories below: 

* As a user who wants to find a book I want to be able to search for it

* As a user who wants to know more about a book before I buy it I want to be able to find details of the book

* As a user who wants to make a decison about a book I want to be able to see what other people think about the book and if other users agree with the review

* As a user who wants to buy a book I want to be able to click a link that takes me to a page to buy the book

* As a user who is not sure of the next book to read I want to be able to look though a list of books for inspiration

* As a user who likes to share my opinon I want to be able to add my own review of the books I have read

* As a user who likes to read I want to know details of the book such as the author

* As a user who wants to start reading I want to find a book that someone has read and has left a review

* As a user who likes to read I want to be able to commment on reviews to share my opionon

* As a desktop user I want to be able to navigate the website easily so I and find the information I want with ease

* As a mobile user I want to be able to navigate the website easily so I and find the information I want with ease

* I have also included some mock-ups for the initial planning phase of the website


# Features

The navigation bar allows users to navigate back to the Home page quickly without needing to use the back button. 
The navigation bar also has a search bar to allow users to search from any page for a book they want to find.
The navigation bar allows users to add a new book the site at any time.
This feature is clear and users should be able to navigate around the site with ease. 

The site has forms to allow users to Create, Edit and Delete book reviews.

pre populated with data-----

buy book from amazon

The site has a comments feature that allowes users to write a comment about the review and then displays it on the relevant review page.
There is also a button for upvotes so users can quickly glance at how popular the review has been.

The footer provides a brief description around the purpose of the website and give a link as a potential idea for future partners. ---- social media links


# Technologies used

* used HTML5 and CSS3 Python and JQuery/ Javascript

* used Flask, Mongo DB, Jinja Templating

* Materialize - https://materializecss.com/
used Materialize for the grid and the the styling

* cdnjs - "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
used this to apply the styling from Materialize

* Google fonts - https://fonts.google.com 
used google fonts to apply fonts to the text within the website

# Testing

I completed much of my testing as I built the website up.

Before I started the code work I set up a new app on heroic and made a new collection on Mongo DB with fields that I had pre planned 
with the information I felt would be relevant for a book review website. 

I initially started with the base.html page that had the bare bones of a layout to include a header a footer and a main section 
that had some colour just to differentiate and ensure my styling was correct.

I then started making the rest of the website including the add a book, edit a book delete a book. Generally the code worked and testing was 
completed throughout by using the inspector tool to assess whether the site was responsive. As I used Materilaize I did not have 
many issues with the responsiveness of the website. 

My first real challenge was when it came to implementing the comments section. Though trial and error I got the code to save the comments to 
the database. However I had a problem where I couldn’t link the comment to the specific review.  After some further research I managed to get 
this working however this  did take some time and a number of trial and error attempts. I was caught between changing my current code and trying 
to write new code. Eventually I added a hidden input that would match the ObjectID of the books collection. 

After this I was then met with another challenge of trying to load the book with its specific comments. The code at the time was generating 
all comments for every book on every book. Again this required further research I was unsure how to progress as I was attempting to use an 
if statements in the Jinja templating. I was not able to get it to work as When I was using the IF statement it just wouldn’t load any comments. 
After further investigation I managed to amend my app.py file in order to allow the code to find the comment which had the correct book ID. 
This was probably the most time consuming part of the project. Again this was done though trial and error. 

The next issue I had was when editing a book review, it would auto populate with the phrase “New Text” , this was down to some unnecessary JQuery 
that had the phrase in it. After removing this I found it wasn’t displaying correctly. I used the inspector and found that the code was finding the 
correct information but just not displaying it. Further research showed that the value in a text area was not generating it compared to a 
value in an input tag. Therefore I removed the value tag and put the {{book.Review}} in between the opening and closing tags.

As I have worked though the project my ideas of how I wanted the users to interact with the website have changed from the original plan. 
I want users to be able to writer their own review for a book, which means multiples of the same book must be allowed. This was on the basis 
that if users commented on the book the comment may get missed by other users and I felt this was the most user friendly way to do this. 

The CSS across the whole site has been amended a few occasions. Generally Materialize has allowed me to style the site and CSS has
been used as a secondary styling agent. The CSS was useful for trial and error of assessing how the website looked across multiple devices. 
After feedback on my previous project, I have decided to limit the colour scheme on the website rather than a host of colours. 
I did change the colour of the Delete button to red to give users a clear indicator this is what he button was for.

Finally testing the website I have included an IF statement in jinja templating to hide a button to but the book 
if the user has not provided a link to the website. As this was a redundant link if there was not end destination.

There is still one issue that I feel is not overly user-friendly. If the link provided by the user is not a valid link the web. 
In the future I would  look to amend this with Javascript/ JQuery to add an If statement that would check if http/ https was at the start of 
the link, if it wasn’t it would add it , if it was it wouldn’t.

# Deployment

The deployment was completed through Github with regular commits.

I used heroku to create an app. I had to change my app.py file in order to deploy to heroku. I changed the debug mode to False.
I had to update the requirements file in order to help deploy to heroku as Flask_pymongo was missing. 
Created a Procfile to tell heroku I am running a python webapp. I had to link my herkou with my github. Once linked up I had to 
ensure my PORT and IP and Config Vars  all had hte relevant information in. Finally I restarted the dynos. 



# Credits and media

* I have used mongo DB documentatin to help implement the functionality of the website
* I used w3school website and stack overflow for assistance with moving footer to the bottom of the page
* I used w3school website for code on the social media links
* I used Materialize for the grid and the styling of the page including the nav bar
* I used google fonts to style the font on the page
* I used mockflow to make a wireframe for the initial planning and idea phase

# Acknowledgement

The inspiration for this project came from the the task manager mini project and other book review websites.











