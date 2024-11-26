import pandas as pd
from django.core.management.base import BaseCommand
from clientes.models import Cliente

class Command(BaseCommand):
    help = 'Load data from CSV file into Cliente model'

    def handle(self, *args, **kwargs):
        # Leer el archivo CSV
        df = pd.read_csv('clientes_banco.csv')

        # Limpiar y procesar los datos según sea necesario
        df['Genero'] = df['Genero'].fillna('Desconocido')
        df['Edad'] = df['Edad'].fillna(df['Edad'].median())
        df['Saldo'] = df['Saldo'].fillna(df['Saldo'].median())
        df['Nivel_de_Satisfaccion'] = df['Nivel_de_Satisfaccion'].fillna(3)
        df['Activo'] = df['Activo'].fillna(0).astype(bool)

        for _, row in df.iterrows():
            Cliente.objects.create(
                edad=row['Edad'],
                genero=row['Genero'],
                saldo=row['Saldo'],
                activo=row['Activo'],
                nivel_de_satisfaccion=row['Nivel_de_Satisfaccion']
            )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully from clientes_banco.csv'))
