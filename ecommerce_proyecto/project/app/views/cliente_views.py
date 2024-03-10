from django.shortcuts import render, redirect


from models.Cliente import Cliente


def crear_usuario(nombre, email, direccion, telefono):
    cliente = Cliente.objects.create_user(
        nombre=nombre, email=email, direccion=direccion, telefono=telefono)
    cliente.save()

    return cliente


def registro_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        user = Cliente.objects.create_user(nombre, email, direccion, telefono)
        user.save()
        return redirect('/')
    return render(request, 'registro.html')
