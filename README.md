<h1 align="center"> Ecommerce Photo Store - 🎨 <i>PG's Picsies</i> 📸 </h1>

</br>
<hr>

# Contents
- [Project Setup](#project-setup)
- [Background](#background)
- [Project Overview](#project-schematic)
  - [Workflow](#workflow)
  - [Features](#features)
  - [Database Schema](#database-schema)
- [Tools](#tools)
- [Implementation](#implementation)
- [Topics Covered](#topics-covered)
- [Resources](#resources)
- [Credits](#credits)

</br>
<hr>

# Project Setup
- Please refer to the [Guidebook](GUIDE.md) for steps to setup the development environment and execute the project.


# Background
The aim of the project is to build a functional E-commerce platform without a payment gateway. The tech stack I will be using are mentioned in [Tools](#tools). The project being a skills demonstration for Full-Stack Development will have  browsing functionality and a barter-exchange checkout.

The E-commmerce platform I have chosen to develop will be a Photo Store like ShutterStock, Pexels, FreePik, etc. Images advertised on the platform will be loaned. The website consists of :
- Images theme on the platform is *Nature*
- Art from *Bing Image Creator*
- Photos from *Pexels*
- Users or Customers can be Photographers, Artists or Enthusiasts.

<br>

A fully functional website allows the following functions to be performed :
- Authorize and authenticate Users(Customers) based on their credentials
- Customers can :
  - create their own profiles
  - Browse *Products* and add items to the *Cart*
  - Search *Products* through filters - *Category, Inventory, Artist Profile* 
  - Upload photographs and art to the *Product Inventory* as Payment
- *Real-Time Updates* updates inventory items based on the checked-out items

</br>
<hr>

# Project Overview
- Overview presents a detailed review about the project through the following:
  - Application Workflow,
  - Application Features,
  - Database Schema 

## Workflow
```mermaid
graph TB

subgraph USERS
  A(User)
  B(Authentication)
  C(Authorization)
  J(Verified User)

  A -->|User Logs In| B
  B -->|Authenticated User is verified| C
  C -->|System grants access to Authorized User or Customer| J
end

subgraph PLATFORM
  D(Home)
  E(Search)
  F(Search Results)
  G(Cart)
  H(Inventory)
  K(Customer Profile)
  D <-->|search by keywords| E
  E -->F
  F -->|Customer adds items to Cart| G
  G <-->|Backend Adds/Removes items| H
  D -->|Customer can edit profile| K
  D -->|Customer adds items to Cart| G
end

subgraph REAL-TIME UPDATES
  I(WebSocket-*Not Implemented*)
end

subgraph CHECKOUT
  L(Payment Gateway)
  G -->|Customer Checkout|L
  L-->|Uploaded Image for Payment| H
end

subgraph ORDERS
  M(Order History)
  L -->|<br>Successful payment saves Customer Order & exchanged image|M
end

G <-->|Server-Client instant communication| I
I <-->|Server-Client instant communication| H
J -->|Verified Customer, can add Products to Cart| D
J -->|search by filters-Theme,Category,Artist| E


```


## Features
### User Login/Sign Up
  - Login/Signup includes User Authentication & Authorization
  - System(database and Backend) authenticates and authorizes User based on their credentials
  - Upon successful authentication, Users/Customers can 
    - View or edit their profiles, 
    - Browse or search for products and
    - Proceed to [**Checkout**](#checkout) to barter an image in exchange for the images they would like to own
- **User *login* page**
![Login page](/screenshots/login.png)

- **User *registration* page** ( logo and text remain the same for sign up page as well )
![Sign Up page](/screenshots/signup.png)

### Home 
  - Customers once authenticated will be welcomed with their name
  - Home page consists of :
    - 'Photo' & 'Art of the Day' images,
    - Images related to 'Theme of the Day'
  - If unauthenticated Users access the **Home** page they will be redirected to *Login* upon doing either of the following actions :
    - add image to Cart, Or
    - access [**Checkout**](#checkout)
  - Unauthenticated Users can still :
    - search for images using the Search bar,
    - browse images in 'Products'
<!--
![Text](path/to/image)
-->
- **Non-User *Home* page**
![Non-User Home page](/screenshots/home-nonUser.png)
- **User *Home* page** 
![User Home page](/screenshots/home-user.png)


### Products
  - *Images*
    - 'Photo' & 'Art of the Day' images,
    - Authenticated and Unauthenticated Users can access all images using *Search Filters*
    - Only verified Users/Customers can add items to *Cart* and *Checkout* for payment
  - *Search Filters*
    - Authenticated and Unauthenticated Users can filter images by - *Image Theme, Image Type & Artist*
  - *Cart*
    - After authentication, Customer can :
      - add/remove items 
      - access *Checkout* to purchase added products
  - *Inventory*
    - Only Admin has access
    - All Users/Customers information is accessible
    - All images information is accessible
    - All Carted items & Orders are accessible
    - *Cart* items trigger *Inventory* updates through [*Real-Time Updates*](#real-time-updates)
- **Filter images by Type, Theme and Artist**
![Products page](/screenshots/products.png)


### Checkout
  - Displays all items added to *Cart*
  - Provides options to 'Change Quantity' or 'Remove', default quantity is 1
  - Provides options to 'Continue Shopping' or 'Proceed to Payment'
- **Checkout view of verified Customer**
![Checkout](/screenshots/checkout.png)

### Payment Gateway
  - Final display of all items added to Cart with quantity
  - Provides options to 'Remove'
  - Explains payment procedure
  - Information about payment is to be filled in the form
  - Upon successful payment, redirects to *Home* page with success message
- **Payment view - payment procedure & items summary**
![Payment summary](/screenshots/payment1.png)
- **Payment view - payment information**
![Payment details](/screenshots/payment2.png)
- **Successful Payment view - order & payment confirmation message**
![Payment success message](/screenshots/payment-success.png)


### Real-Time Updates
<span style="color: red;">Not Implemented</span>

  - Real-time updates via WebSockets enable real-time interactions, including updating the cart and inventory.



## Database Schema
- Database (SQLite) is implemented as an in-built version for Django
- Django Models are defined using the framework (`models.py`) for each of the apps defined (`users`, `photostore`)  to emulate tables similar to SQL
- After defining the required models the changes are updated through 'Migrations', which translate the instructions in `models.py` to the database to create/update tables
- Database schema (below) defines the logical flow of data through the application backend
![Database Schema](/design/DATABASE-SCHEMA.png)


</br>
<hr>

# Tools
- **Frontend**
  - Figma (for design)
  - HTML
  - CSS 

- **Database**
  - SQLite

- **Backend**
  - Django (Python)

</br>
<hr>

# Implementation
## **Week 0: Project Design**
- [X] Week 0: Define project directories and files
- [X] Week 0: Use Figma to build ecommerce store design

## **Week 1: Project Setup and HTML/CSS**
- [X] Project Setup: Create a Django project.
- [X] HTML/CSS: Review and strengthen HTML and CSS skills.
- Resources: Online HTML/CSS tutorials, Django documentation.

## **Week 2: Django Fundamentals**
- [X] Django Basics: Learn about Django's project structure, settings, and apps.
- [X] Models: Create Django models for products and categories.
- Resources: Official Django documentation, Django for Beginners book.

## **Week 3: Django Views and Templates**
- [X] Views: Create views to render product listings and detail pages.
- [X] Templates: Build HTML templates for product pages.
- Resources: Django documentation on views and templates.

## **Week 4: User Authentication**
- [X] User Authentication: Implement user registration and login functionality.
- [X] Custom User Model: Create a custom user model with additional fields.
- Resources: Django authentication documentation, Django for Beginners book.

## **Week 8: Real-time Updates (WebSockets)**
<span style="color: red;"> Not Implemented </span>
- [ ] WebSocket Basics: Understand WebSocket communication.
- [ ] Implement Real-Time: Add real-time features like instant cart updates.
- Resources: WebSockets tutorials, Django Channels documentation.

## OPTIONAL
**Week 5: JavaScript Basics**
- [ ] JavaScript Fundamentals: Start learning JavaScript from scratch (Vanilla JS).
- [ ] Interactive Features: Enhance your product pages with basic interactivity.
- Resources: MDN JavaScript guide, JavaScript.info, freeCodeCamp's JavaScript curriculum.

**Week 6: Frontend Interactivity with JavaScript**
- [ ] Dynamic Content: Use JavaScript to load products dynamically.
- [ ] Event Handling: Implement user interactions like adding products to the cart.
- Resources: JavaScript tutorials, interactive coding platforms like CodePen.

**Week 7: Django REST Framework**
- [ ] API Development: Learn to build RESTful APIs with Django REST Framework.
- [ ] API Endpoints: Create API endpoints for product data.
- Resources: Django REST Framework documentation, DRF tutorials.

**Week 9: User Authorization and Permissions**
- [X] Authorization: Implement user roles (e.g., admin, customer).
- [ ] Permission Control: Set up authorization for views and API endpoints.
- Resources: Django authorization documentation.

**Week 10: Database Optimization and Transactions**
- [X] SQL Skills: Deepen your SQL knowledge for database queries.
- [ ] Transactions: Learn about database transactions and ACID properties.
- [ ] Database Optimization: Optimize database queries for performance.
- Resources: SQL tutorials, SQL optimization guides.

**Week 11: Advanced JavaScript**
- [ ] Advanced JavaScript Concepts: Dive deeper into JavaScript, including DOM manipulation.
- [ ] Implement Complex Features: Enhance user experience with advanced JS features.
- Resources: Advanced JavaScript courses, MDN web APIs.

**Week 12: Final Testing and Deployment**
- [ ] Testing: Write unit and integration tests for your application.
- [ ] Deployment: Deploy your Django application to a hosting platform (e.g., Heroku).
- Resources: Django testing documentation, deployment guides.

</br>
<hr>

# Topics Covered
<details>
<summary>
<b>Frontend Development</b>
</summary>

1. **HTML/CSS Fundamentals:**
   - Review and strengthen your HTML and CSS skills.

2. **JavaScript Basics:**
   - Learn JavaScript fundamentals (Vanilla JS).
   - Enhance product pages with basic interactivity.

3. **Frontend Interactivity:**
   - Use JavaScript to load products dynamically.
   - Implement user interactions like adding products to the cart.

4. **Django Templating:**
   - Build HTML templates for product pages using Django's template engine.
   - Serve static files (CSS, JS) in Django.
</details>

<details>
<summary>
<b>Backend Development with Django</b>
</summary>

1. **Django Basics:**
   - Understand Django's project structure, settings, and apps.

2. **User Authentication:**
   - Implement user registration and login functionality.
   - Create a custom user model with additional fields.

3. **Django Views and API Development:**
   - Create views to render product listings and detail pages.
   - Set up authorization for views and API endpoints.

4. **Real-time Updates (WebSockets):**
   - Implement real-time features like instant cart updates.
   
5. **Advanced JavaScript Integration:**
   - Dive deeper into JavaScript for frontend enhancements.
   
6. **Testing and Deployment:**
   - Write unit and integration tests for your application.
   - Deploy your Django application to a hosting platform (e.g., Heroku).
</details>

<details>
<summary>
<b>Database Integration with SQLite</b>
</summary>

1. **Database Design:**
   - Create Django models for products and categories.

2. **Django REST Framework:**
   - Build RESTful APIs with Django REST Framework.
   - Create API endpoints for product data.

3. **Database Optimization and Transactions:**
   - Deepen SQL knowledge for database queries.
   - Learn about database transactions and ([ACID properties](https://www.geeksforgeeks.org/acid-properties-in-dbms/)).
   - Optimize database queries for performance.
</details>

</br>
<hr>

# Resources
- Django
  - [Official Django Documentation](https://docs.djangoproject.com/)
  - [CS50-Web Programming](https://cs50.harvard.edu/web/2020/weeks/3/)
  - [MDN Django Web Framework (Mozilla Developer Network)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

- SQLite
  - [Official SQLite Documentation](https://www.sqlite.org/docs.html)

- [JavaScript - freeCodeCamp](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)


</br>
<hr>

# Credits
- **Planning assistance - ChatGPT (GPT-3.5)**
- **Development assistance - [![built with Codeium](https://codeium.com/badges/main)](https://codeium.com/badges/main)**