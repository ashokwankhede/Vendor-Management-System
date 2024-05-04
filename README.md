# Vendor-Management-System
# Django REST API Setup

This repository contains a Django project with a RESTful API using Django REST Framework.

## Prerequisites

- Python (version 3.9+ recommended)
- Django
- Django REST Framework

# Setup Instructions

## Create a Virtual Environment:
- python -m venv env_name

## Install Dependencies:
- pip install django
- pip install djangorestframework

## Run the server by executing following command:
- python manage.py runserver

## Superuser Creation and Token Generation
To create a superuser and generate a token, execute the following commands:
- python manage.py createsuperuser
After creating the superuser, make a POST request to the following endpoint:
- http://localhost:8000/api/generate-token/
Include the username and password of the superuser in the request body to generate a token.

## Accessing Django Admin Panel with Superuser Credentials:
To access the Django admin panel navigate to the following endpoint:
- http://127.0.0.1:8000/admin/
in your web browser. Log in using the credentials of the superuser you created earlier.
This will grant you access to the admin interface, allowing you to manage the database with administrative privileges.

###### API Testing ########

## Vendor:
# To create a new vendor, make a POST request to the following endpoint.
Endpoint:
- http://localhost:8000/api/vendors/
Request Body:
- {
  "name": "vendor name",
  "contact_details": "Phone/Email",
  "address": "address",
  "vendor_code": "vendor_code"
  }
Headers:
Authorization: Token your_obtained_token.

# To retrieve a list of vendors, you can make a GET request to the following endpoint:
Endpoint:
- http://localhost:8000/api/vendors/
Headers:
Authorization: Token your_obtained_token.

This request will return a JSON object containing a list of vendors along with their details. You can use this endpoint to fetch the list of vendors in your application.

# To retrieve details about a specific vendor, you can make a GET request to the following endpoint:

Endpoint:
- http://localhost:8000/api/vendors/{vendor_code}/
Headers:
Authorization: Token your_obtained_token.

This request will return a JSON object containing details about the vendor with the specified vendor code.

# To update details of a specific vendor, you can make a PUT request to the following endpoint:
Endpoint:
- http://localhost:8000/api/vendors/ABC123/
Replace `ABC123` with the vendor code of the vendor you want to update.
 
- Request Body:
  {
    "name": "Updated Vendor Name",
    "contact_details": "Updated Phone/Email",
    "address": "Updated Address",
    "vendor_code": "ABC123"
  }
Headers:
Authorization: Token your_obtained_token.

This request will update the details of the vendor with the specified vendor code with the provided information in the request body.

# To delete a specific vendor, you can make a DELETE request to the following endpoint:
Endpoint:
- http://localhost:8000/api/vendors/{vendor_code}/
Headers:
Authorization: Token your_obtained_token.
This request will delete the vendor with the specified vendor code from the database.

## Purchase Order
# To create a purchase order via API, you can utilize the following HTTP POST request:
Endpoint:
- http://127.0.0.1:8000/api/purchase_orders/

Headers:
Authorization: Token your_obtained_token

Body:
{
  "po_number": "01",
  "vendor": "01",
  "order_date": "2023-01-01",
  "delivery_date": "2023-01-10",
  "items": [
    {
      "item_name": "20"
      }
  ],
  "quality_rating": 4.5,
  "issue_date": "2023-01-01",
  "status": "Pending",
  "acknowledgment_date": "2023-01-02"
}
Add vendor code which should be present in the DB.
This request will create a new purchase order with the provided details.

# To retrieve all purchase orders via API, you can use the following HTTP GET request:

Endpoint:
- http://127.0.0.1:8000/api/purchase_orders/
- 
Headers:
Authorization: Token your_obtained_token
This request will fetch all existing purchase orders from the server.

# To retrieve a specific purchase order via API, you can use the following HTTP GET request:

Endpoint:
- http://127.0.0.1:8000/api/purchase_orders/{po_id}/

Headers:
Authorization: Token your_obtained_token
This request will fetch the details of the purchase order with the specified ID from the server.

# To update a specific purchase order via API, you can use the following HTTP PUT request:

Endpoint:
- http://127.0.0.1:8000/api/purchase_orders/{po_id}/

Headers:
Authorization: Token your_obtained_token

Body:
{
  "po_number": "updated_po_number",
  "vendor": "updated_vendor",
  "order_date": "2023-01-01",
  "delivery_date": "2023-01-10",
  "items": [
    {
      "item_name": "updated_item_name"
    }
  ],
  "quality_rating": 4.5,
  "issue_date": "2023-01-01",
  "status": "Updated",
  "acknowledgment_date": "2023-01-02"
}

This request will update the details of the purchase order with the specified ID on the server.

# To delete a specific purchase order via API, you can use the following HTTP DELETE request:

Endpoint:
- http://127.0.0.1:8000/api/purchase_orders/{po_id}/

Headers:
Authorization: Token your_obtained_token
This request will delete the purchase order with the specified ID from the server.

## Retrieve a vendor's performance metrics:

Endpoint:
- GET http://127.0.0.1:8000/api/vendors/{vendor_id}/performance/

Headers:
Authorization: Token your_obtained_token

Description:
This endpoint retrieves the performance metrics of a vendor with the specified vendor_id. The performance metrics include:

1. On-time Delivery Rate: This is calculated each time a purchase order (PO) status changes to "completed". It represents the average of the number of POs delivered before the delivery_date and the total number of POs delivered.

2. Quality Rating Average: This is calculated after every PO completion and represents the average of all ratings given to that specific vendor.

3. Average Response Time: This is calculated each time a PO is acknowledged by the vendor. It is the time difference between the issue_date and acknowledgment_date for each PO, and then the average of these times for all POs of the vendor.

4. Fulfillment Rate: This is calculated when a PO status is set to "completed". It represents the average of the number of successfully fulfilled POs (status = "completed" without issues) divided by the total number of POs issued to the vendor.

## To acknowledge a purchase order with the given `po_id` and trigger the recalculation of the `average_response_time`, you can use the following methods:

Endpoint:
- PUT http://127.0.0.1:8000/api/vendors/{vendor_id}/performance/

Headers:
Authorization: Token your_obtained_token
### API Endpoint Description:
This endpoint is utilized to acknowledge the purchase order identified by the `po_id` and subsequently trigger the recalculation of the `average_response_time`.
   

