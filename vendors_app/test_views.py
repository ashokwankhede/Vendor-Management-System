from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status


class TestSetup(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ashok', password='admin')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()


class VendorViewSetTests(TestSetup):
    def test_create_vendor(self):
        response = self.client.post('/api/vendors/',{
        "name": "XYT Enterprises",
        "contact_details": "987-654-3210",
        "address": "456 Elm St, City, Country",
        "vendor_code": "XYT457",
        "on_time_delivery_rate": 0.78,
        "quality_rating_avg": 4.2,
        "average_response_time": 3.2,
        "fulfillment_rate": 0.91
        })
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_check_purchase_order(self):
        response = self.client.get('/api/purchase_orders/',{
            "po_number": "PO123",
            "vendor": "PQR789",
            "order_date": "2024-04-30T08:00:00",
            "delivery_date": "2024-05-05T08:00:00",
            "delivered_date": "2024-05-010T08:00:00",
            "items": [
                {"item_name": "Item 1", "price": 10.99},
                {"item_name": "Item 2", "price": 20.99}
            ],
            "quantity": 100,
            "status": "Pending",
            "quality_rating": 1.2,
            "issue_date": "2024-04-30T08:00:00",
            "acknowledgment_date": "2024-04-30T08:00:00",
        }
        )
        print(response.content)
        print("check purchase completed")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    
    


