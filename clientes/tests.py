from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Cliente

class ClienteAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.cliente_data = {
            'edad': 30,
            'genero': 'M',
            'saldo': 5000.0,
            'activo': True,
            'nivel_de_satisfaccion': 4
        }
        self.response = self.client.post(
            reverse('cliente-list'),
            self.cliente_data,
            format="json"
        )

    def test_crear_cliente(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_cliente(self):
        cliente = Cliente.objects.get()
        response = self.client.get(
            reverse('cliente-detail', kwargs={'pk': cliente.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, cliente)

    def test_actualizar_cliente(self):
        cliente = Cliente.objects.get()
        update_data = {
            'edad': 35,
            'genero': 'F',
            'saldo': 6000.0,
            'activo': False,
            'nivel_de_satisfaccion': 5
        }
        response = self.client.put(
            reverse('cliente-detail', kwargs={'pk': cliente.id}),
            update_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_eliminar_cliente(self):
        cliente = Cliente.objects.get()
        response = self.client.delete(
            reverse('cliente-detail', kwargs={'pk': cliente.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
