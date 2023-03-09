from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Person, Car, Rent
from .serializers import CarSerializer, PersonSerializer, RentSerializer


class APICar(APIView):

    def get(self, req):
        try:
            car_id = req.query_params.get("car_id")
            post = Car.objects.get(pk=car_id)
            cs = CarSerializer(post)
            return Response(cs.data)
        except Exception as e:
            return Response(f"Error {e}")

    def post(self, req):
        try:
            ps = CarSerializer(data=req.data)
            if ps.is_valid():
                ps.save()
                return Response("Car Created")
            else:
                return Response({"Error": ps.errors})
        except Exception as e:
            return Response(f"Error {e}")

    def put(self, req):
        try:
            car_id = req.query_params.get("car_id")
            car_instance = Car.objects.get(pk=car_id)
            ps = CarSerializer(data=req.data, instance=car_instance)
            if ps.is_valid():
                ps.save()
                return Response("Object Updated")
            else:
                return Response({"Error": ps.errors})
        except Exception as e:
            return Response(f"Error {e}")

    def delete(self, req):
        try:
            car_id = req.query_params.get("car_id")
            car_instance = Car.objects.get(pk=car_id)
            car_instance.delete()
            return Response("Object deleted")
        except Exception as e:
            return Response(f"Error {e}")


