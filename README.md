# **eCommerce Platform**

## Overview

This is a full-featured eCommerce platform built with Django, designed to provide a seamless online shopping experience for users. The platform allows users to browse products, add items to a cart, place orders, and manage their profiles. It also includes robust product and inventory management for store administrators.

The project incorporates modern web development practices with a clear separation of concerns following the Model-View-Template (MVT) architecture of Django. Cloudinary is used for hosting product images, and a custom user model extends Django's built-in user functionality to include additional features like profile images and email verification.

## Key Features

- **User Registration & Authentication**: Secure user registration, login, and profile management.
- **Product Catalog**: A dynamic product catalog that supports product images, descriptions, pricing, and inventory.
- **Shopping Cart**: Users can add items to their cart, adjust quantities, and review orders before purchasing.
- **Order Management**: The platform supports the placement of orders and the association of products with user accounts.
- **Image Uploading**: Integrated with Cloudinary for seamless image uploads and management for products.
- **Email Verification**: Sends confirmation emails to users to verify their accounts after registration.
- **Admin Product Management**: Administrators can create, update, and delete products and manage inventory.
- **Responsive Design**: The platform is fully responsive, offering an optimized experience across different devices.

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL or any relational database supported by Django
- **Image Hosting**: Cloudinary for product image management
- **Email**: Django’s email system for sending confirmation emails
- **Security**: Django’s built-in security features such as CSRF protection, session management, and password hashing

## Installation & Setup

### Prerequisites

Ensure you have the following installed on your local development environment:

- Python 3.x
- Django 4.x
- PostgreSQL (or another preferred database)
- Cloudinary account for image hosting

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/malikali001/ecommerce-app.git
