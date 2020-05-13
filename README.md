# SneakGateWay Marketplace #

### Data-Centric Development Milestone Project 3 ###
By: Melville Ng

## Demo ##
Website site link can be found [here](https://mel-buyandsell-marketplace.herokuapp.com/)

## Aim ##
The aim of this project is to build an E-commerce website with Mongodb as it database. 
Through the website, user can list and sell their sneaker. At the same time, people that like sneaker as a 
hobby can buy their sneaker too.  The User will be able to create listing, read the listing, edit the 
listing and delete the listing. 

## UI ##
The intention to make the website modern looking, easy to navigate and comfortable on the eyes. 
Colours of white and grey are chosen to suit the different colourway of the product. 
Different colour of the button is used to make the site look livelier.

## UX ##
The website can store what the user wants to sell to be available to view by another user. 
The website also can create an account to keep track of all your listing. 
The font of the website was taken from google font to make the font more unique instead of the standard font.

Bootstrap breakpoints is responsive for small, medium and large screens for the navigation bar. 
When the screen, reaches medium or small screen the navigation bar will change to be a hamburger icon on the top right corner of the website. 
Drop down menu will appear when u press the hamburger icon which will link you to different pages of the website. 
On large screen device the navigation bar will display all the link at the top.

## ER Diagram ##
ER Diagram can be found [here](https://github.com/melvilleng/bnsmarketplace/blob/master/misc/image.png)

## User Stories ##
* As a user - I want to be able to see all the listing of shoes
* As a user – I want to be able to create an account to store all my listing.
* As a user – I want to be able to sign up for an account.
* As a user – I want to be able to navigate through the different listing
* As a user – I want to be able to log in and log out
* As a user – I want to be able to see all the listing that I listed under my account.
* As a user – I want to be able to create a listing, edit the listing and delete the listing.
* As a user – I want to be able to post picture so that people can see which shoes is that.
* As a user – I want to be able to search for the item name that I want to find.
* As a user – I want to be able to leave a review on the seller.

## Feature ##
* The site can be access by member of the public and logged in user but only logged in user are able to create listing.
* Anyone on the site can view the home page where all the listing will be posted to. 
* On each listing, there a view page button where once click u can view more information of the listing.
* All site visitor has the option to create an account. The information that is required are username, email and password.
* User can sign in through the navbar login where the login page will have to fill in the username and password. 
There also a sign-up button where if the user did not have account on the website they are also to sign up. 
Lastly, the submit button to submit the username and password to be sign in.

* Once signed in, the signed user will be at his/her personal listing page where the banner will display the signed user 
username and all the listing that the user has posted before.

* Once signed in, the user navbar will change to Home, My Listing, Create Listing and Logout. 
From here the user will be able to click on the create listing and the user will be bring to the create listing page. 

* On the create listing page, the user has to fill in the product name, Size, Price, Description , 
paste in an image url for image in to appear in the listing and the date of this post. 

* There a back button where it will bring the user back to the home page and the create listing button to list the 
sneaker the user is listing and will be brought back to the personal listing page. 

* If the user wants to edit anything the user can edit from my listing page when click on the edit button.
 The user will be able to edit any info that the signed in user wants to edit except the date of the listing post. 
 Once the post is edited it will bring the user back to my listing page.

* If the user does not want the post any more or want to take it down. The user can delete it through the delete button.

* On the banner there my review button where once clicked it will bring the signed in user to the signed in user review page 
where the user can see the seller and buyer review,  they can leave a buyer review after they deal finish through email.

* The Logout on navbar can log the signed user out.

* For visitor that is browsing for shoes to buy they can click on the view page to view for more details. 
Once there are happy or want to contact the seller for more information there a contact seller here button. 
It will redirect u to the seller user profile where his username and email will be there for the potential buyer 
to contact the seller through email. From there if the potential buyer wants to see the review of the seller or give the seller a review.
 The potential seller can click on the review me. At the review page, the buyer can give the seller a review or can just look through the 
 seller review by another buyer or seller.

* At the top right-hand corner, there a search feature where user can search by keyword for the sneaker that is listed on the website. For example, if the user type in the keyword ‘Jordan’ only sneakers with the name of Jordan in it will appear.



Future features
* Lets user to be able to upload image from their computer instead of using image url.

* For the review to be added a 1 – 5-star rating.

* Add a chat bot so the seller and buyer can contact each other through the website instead of email.

* Add a undo delete feature where if the user want to retrieve the user listing back.


## Wireframes ##
Wireframes was created to help me to visualise and design a layout for my website. The wireframe can 
be view via this [link](https://github.com/melvilleng/bnsmarketplace/blob/master/misc/Wireframe).

## Technologies Used ##
Below are a list of framework, programming languages and tools used for the website:
* HTML5
* CSS
* Bootstrap 4
* Gitpod  
* Google Fonts 
* Github
* Balsamiq
* Python
* Flask
* Jinjia2
* Mongodb
* Heroku
* Erdplus






### Testing ###
* Home Page:
    When I click on the home,login,sign up and view page button it will redirect me to the individual pages.
    When I click on the create account the create account pop up will appear and after I fill in all the details it will bring me to the login page to login.
    The search feature is working. Tested with typing jordan and only jordan related product listing will be shown.


* Sign up page
    Tested with filling in username, email and password and press the create account button 
    It will bring me to the login page,  I am able to login mean the sign up feature is working.
    The back button will bring me back to the home page

* Login Page
    After typing in the username and password I have register earlier I am able to be redirect to my listing page which only sign in user can view.

    Press on the sign-up button it will redirect me to the sign up page.

    After logging in sign up and sign in on navbar got change to My listing, Creating listing and logout

    When create listing is clicked on, it will be redirect to the create listing page where i fill in the listing title ,size, price, description , upload the image URL and date.
    Once all is fill up will press the create listing page and redirect back to my listing page where the info I just fill in earlier was added on my listing page. 

* My listing page

    My review button will bring to the logged user review page.

    The edit button on the listing will bring me to the edit listing page where I can edit each attribute. Tested one by one and all updated on what I change.

    Tested the delete button and the listing is deleted.

    Test the logout feature and the user was logged out.

* More info product page

    The back button will bring me back to the home page.
    The contact seller will bring me to the posted or seller info page.

* Seller info page
    When I click on the review me button it will bring me to the review page

* Review page
    On the review page when I click on the buyer or seller review button I will direct to their individual review page where I can type the review I give for the buyer or seller and leave the name behind. Once I click on the create reciew button my review will be added on the review page.



* Tested the website on mobile

The website was tested on different web browser and different mobile device. Device and browsers tested on are:

Ipad
Safari
MacBook Air –
Google Chrome
Safari
Window laptop
google chrome
Microsoft Edge
Iphone
Safari
Samsung S10
Google Chrome
Samsung Web Browser




### Bugs ###
Have problem getting the time to stop showing. Manage to hide away the time by only declare I want he date.
For the description I was not able to retain the original text when editing. Fix this issue by change the textarea to input.

### Deployment ###
Heroku was used to be deployed for the website. MongoDB is use for the database.

On Gitpod I will login to Heroku first after that I will git push to Heroku master.
After that I will go to the config vars to put in the Mongo_URI and Secret_Key.


## Credit ##
* Stockx
* Goat
* Stackoverflow
* Special thanks to my [lecturer](https://github.com/kunxin-chor/) for the guidance.



