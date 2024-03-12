from django.shortcuts import render, redirect


from models.Cliente import Cliente


def crear_usuario(nombre, email, direccion, telefono):
    cliente = Cliente.objects.create_user(
        nombre=nombre, email=email, direccion=direccion, telefono=telefono)
    cliente.save()

    return cliente
