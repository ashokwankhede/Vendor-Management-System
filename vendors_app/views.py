from rest_framework.response import Response
from rest_framework import status
from.serializers import VendorSerializer, PurchaseOrderSerializer
from.models import Vendor, PurchaseOrder
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class VendorCreateListView(APIView):
    """
    Create a new vendor or retrieve a list of existing vendors.
    """
    permission_classes = [IsAuthenticated]
    def post(self, request):
        """
        Create a new vendor with provided data.
        """
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "vendor created!", "vendor": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        Retrieve a list of all existing vendors.
        """
        queryset = Vendor.objects.all()
        serializer = VendorSerializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveUpdateDeleteView(APIView):
    """
    Retrieve, update, or delete a vendor by vendor code.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, vendor_code):
        """
        Retrieve details of a vendor by vendor code.
        """
        try:
            vendor = Vendor.objects.get(vendor_code=vendor_code)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, vendor_code):
        """
        Update details of a vendor by vendor code.
        """
        try:
            vendor = Vendor.objects.get(vendor_code=vendor_code)
            serializer = VendorSerializer(vendor, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "vendor details updated!", "vendor": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': e}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, vendor_code):
        """
        Delete a vendor by vendor code.
        """
        try:
            vendor = Vendor.objects.get(vendor_code=vendor_code)
            vendor.delete()
            return Response({"message": "vendor deleted!"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': e}, status=status.HTTP_404_NOT_FOUND)
        
        
class PurchaseOrderCreateListView(APIView):
    """
    Create a new purchase order or retrieve a list of existing purchase orders.
    """
    permission_classes = [IsAuthenticated]
    def post(self, request):
        """
        Create a new purchase order with provided data.
        """
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "purchase order created!", "purchase order": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        Retrieve a list of all existing purchase orders.
        """
        queryset = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
class PurchaseOrderListUpdateDelete(APIView):
    """
    Retrieve, update, or delete a purchase order by purchase order number.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, po_number):
        try:
            return PurchaseOrder.objects.get(po_number=po_number)
        except Exception as e:
            return Response({'error': e}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, po_number):
        """
        Retrieve details of a purchase order by purchase order number.
        """
        
        order = self.get_object(po_number)
        serializer = PurchaseOrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, po_number):
        """
        Update details of a purchase order by purchase order number.
        """
        order = self.get_object(po_number)
        serializer = PurchaseOrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "purchase order details updated!", "order": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, po_number):
        """
        Delete a purchase order by purchase order number.
        """
        order = self.get_object(po_number)
        order.delete()
        return Response({"message": "purchase order deleted!"}, status=status.HTTP_204_NO_CONTENT)


class VendorPerformanceView(APIView):
    """
    Retrieve performance metrics for a specific vendor by vendor code.
    """

    def get_object(self, vendor_code):
        try:
            return Vendor.objects.get(vendor_code=vendor_code)
        except Exception as e:
            return Response({"error":e},status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, vendor_code):
        """
        Retrieve performance metrics for a specific vendor by vendor code.
        """
        vendor = self.get_object(vendor_code)
        serializer = VendorSerializer(vendor)
        return Response({
            'on_time_delivery_rate': serializer.data['on_time_delivery_rate'],
            'quality_rating_avg': serializer.data['quality_rating_avg'],
            'average_response_time': serializer.data['average_response_time'],
            'fulfillment_rate': serializer.data['fulfillment_rate']
        })


class AcknowledgePurchaseOrderView(APIView):
    """
    Acknowledge a purchase order by updating its acknowledgment date.
    """

    def get_object(self, po_id):
        try:
            return PurchaseOrder.objects.get(po_number=po_id)
        except Exception as e:
            return Response({"error":e},status = status.HTTP_400_BAD_REQUEST)


    def post(self, request, po_id):
        """
        Update acknowledgment date for a purchase order by purchase order ID.
        """
        purchase_order = self.get_object(po_id)
        acknowledgment_date = request.data.get('acknowledgment_date', None)

        if acknowledgment_date is not None:
            purchase_order.acknowledgment_date = acknowledgment_date
            purchase_order.save()

            response_times = PurchaseOrder.objects.filter(
                vendor=purchase_order.vendor, acknowledgment_date__isnull=False).values_list(
                'acknowledgment_date', 'issue_date')
            total_seconds = sum(abs((ack_date - issue_date).total_seconds())
                            for ack_date, issue_date in response_times)
            if response_times:
                average_response_time = total_seconds / len(response_times)
            else:
                average_response_time = 0

            purchase_order.vendor.average_response_time = average_response_time
            purchase_order.vendor.save()

            return Response({'acknowledgment_date': purchase_order.acknowledgment_date}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Acknowledgment date is required.'}, status=status.HTTP_400_BAD_REQUEST)
      
        