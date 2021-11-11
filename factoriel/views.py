from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def factoriel(request):
    """Endpoint for factorial"""
    print(request.query_params)
    nb = request.query_params["number"]
    if not nb:
        return Response({"message" : "number needed"}, status=400)
    try:
        number = int(nb)
    except ValueError:
        return Response({"message" : "number has to be an integer"}, status=400)
    fact = 1
    while number > 1:
        fact = fact * number
        number = number - 1
    return Response({"factorial" : fact})