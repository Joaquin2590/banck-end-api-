def index(request):
    form =forms.EmpleadoForm()
    #cuando envía el formulario el boton guardar
    if request.method=='POST':
        form=forms.EmpleadoForm(request.POST)
        if form.is_valid():
            print("Formulario OK")
            print("Nombre: ",form.cleaned_data['nombre'])
            print("Email: ",form.cleaned_data['email'])
            print("Telefono: ",form.cleaned_data['Telefono'])
            form.save()
            return listar_empleados(request)
    data={'form':form}
    return render(request,'modelApp/index.html',data)

