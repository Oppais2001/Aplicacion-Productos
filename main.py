import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

listado={'torta clasica(10p)': 14000, 'torta clasica(20p)': 20000, 'torta clasica(30p)': 28000,
         'torta mil hojas(10p)': 16000, 'torta mil hojas(20p)': 25000, 'torta mil hojas(30p)': 30000, 
         'torta de zanahoria(10p)': 17000, 'torta de zanahoria(20p)': 26000, 'torta de zanahoria(30p)': 36000, 
         'torta de nuez(10p)': 16000, 'torta de nuez(20p)': 25000, 'torta de nuez(30p)': 34000, 
         'torta de trufa(10p)': 20000, 'torta de trufa(20p)': 30000, 'torta de trufa(30p)': 40000, 
         'torta de ciruela(10p)': 20000, 'torta de ciruela(20p)': 32000, 'torta de ciruela(30p)': 40000, 
         'torta mixta(10p)': 16000, 'torta mixta(20p)': 25000, 'torta mixta(30p)': 30000,
         'torta selva negra(10p)': 16000, 'torta selva negra(20p)': 25000, 'torta selva negra(30p)': 30000,
         'torta tres leches(10p)': 16000, 'torta mixta(20p)': 24000, 'torta mixta(30p)': 30000,
         'torta merengue(10p)': 15000, 'torta merengue(20p)': 24000, 'torta merengue(30p)': 34000,
         'torta de platano(10p)': 20000, 'torta de platano(20p)': 28000, 'torta de platano(30p)': 36000,
         'kuchen de nuez(24cm)': 8000, 'kuchen de nuez(28cm)': 12000,'kuchen aleman(24cm)': 8000,
         'kuchen aleman(28cm)': 12000,'kuchen de yoghurt griego(24cm)': 8000, 'kuchen de yoghurt giego(28cm)': 12000,
         'pie de limon(24cm)': 10000, 'pie de limon(28cm)': 14000,'queque de platano(con azucar)': 8000,
         'queque de platano(sin azucar)': 9000,'queque de veterraga(con azucar)': 6000,'queque de veterrag(sin azucar)': 7000,
         'queque de zapallo(con azucar)': 8000,'queque de zapallo(sin azucar)': 9000,'queque de zanahoria(con azucar)': 7000,
         'queque de zanahoria(sin azucar)': 8000,'queque de frutos rojos(con azucar)': 7000,
         'queque de frutos rojos(sin azucar)': 8000,'queque marmol(con azucar)': 7000, 'queque marmol(sin azucar)': 8000
}

cantidades={'torta clasica(10p)': 0, 'torta clasica(20p)': 0, 'torta clasica(30p)': 0,'torta mil hojas(10p)': 0,
            'torta mil hojas(20p)': 0, 'torta mil hojas(30p)': 0,'torta de zanahoria(10p)': 0, 'torta de zanahoria(20p)': 0,
            'torta de zanahoria(30p)': 0, 'torta de nuez(10p)': 0, 'torta de nuez(20p)': 0, 'torta de nuez(30p)': 0, 
            'torta de trufa(10p)': 0, 'torta de trufa(20p)': 0, 'torta de trufa(30p)': 0,'torta de ciruela(10p)': 0,
            'torta de ciruela(20p)': 0, 'torta de ciruela(30p)': 0, 'torta mixta(10p)': 0, 'torta mixta(20p)': 0,
            'torta mixta(30p)': 0,'torta selva negra(10p)': 0, 'torta selva negra(20p)': 0, 'torta selva negra(30p)': 0,
            'torta tres leches(10p)': 0, 'torta mixta(20p)': 0, 'torta mixta(30p)': 0,'torta merengue(10p)': 0,
            'torta merengue(20p)': 0, 'torta merengue(30p)': 0,'torta de platano(10p)': 0, 'torta de platano(20p)': 0,
            'torta de platano(30p)': 0,'kuchen de nuez(24cm)': 0, 'kuchen de nuez(28cm)': 0,'kuchen aleman(24cm)': 0,
            'kuchen aleman(28cm)': 0,'kuchen de yoghurt griego(24cm)': 0, 'kuchen de yoghurt giego(28cm)': 0,
            'pie de limon(24cm)': 0, 'pie de limon(28cm)': 0,'queque de platano(con azucar)': 0,'queque de platano(sin azucar)': 0,
            'queque de veterraga(con azucar)': 0,'queque de veterrag(sin azucar)': 0,'queque de zapallo(con azucar)': 0,
            'queque de zapallo(sin azucar)': 0,'queque de zanahoria(con azucar)': 0,'queque de zanahoria(sin azucar)': 0,
            'queque de frutos rojos(con azucar)': 0,'queque de frutos rojos(sin azucar)': 0,'queque marmol(con azucar)': 0,
            'queque marmol(sin azucar)': 0
}


def calcular(producto,cantidad,lista,cantidad1):
    cantidad=int(cantidad)
    v=producto
    precio=0
    if v in listado:
        print(f"El producto {v} está presente en el diccionario")
        precio=listado[v]
    if v in cantidad1:
        cantidad1[v]+=cantidad
    valor=int(precio*cantidad)
    lista.append(valor)
    return lista,cantidad1

def sumaProductos(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma

class MyApp(App):
    def build(self):
        screen_width = Window.width
        screen_height = Window.height
        desired_ratio = 16/9
        target_width = screen_width
        target_height = screen_width * desired_ratio        
        Window.size = (target_width, target_height)
        # Crear un layout principal
        layout = BoxLayout(orientation='vertical',spacing=10, padding=10)
        exception_layout = BoxLayout(orientation='horizontal')
        #variables
        self.Total=[]
        self.cantidad=cantidades.copy()
        self.listado=listado
        # Crear una etiqueta
        self.label = Label(text="Ingresar producto:", font_size=100 ,height=120, size_hint=(1, None))
        self.label1 = Label(text="Ingresar cantidad:", font_size=100 ,height=120,size_hint=(1, None))
        self.label2 = Label(text="",font_size=60, size_hint=(1,None), height=80)
        self.label3 = Label(text="",font_size=60, size_hint=(1,None), height=80)
        self.label4 = Label(text="",font_size=45, size_hint=(1,None), height=1000)
        # Crear un TextInput
        self.text_input = TextInput(multiline=False,font_size=80,height=110, size_hint=(1,None))
        self.text_input1 = TextInput(multiline=False,font_size=80,height=110, size_hint=(1,None))
        # Crear un botón
        button1 = Button(text='ACEPTAR',font_size=100, size_hint=(1,None),width=100,height=100,background_color=("red"))
        button1.bind(on_press=self.read_text)
        # Crear un botón
        button2 = Button(text='REINICIAR',font_size=100, size_hint=(1,None),width=100,height=100,background_color=("green"))
        button2.bind(on_press=self.read_text1)

        # Agregar la etiqueta, el TextInput y el botón al layout
        layout.add_widget(self.label)
        layout.add_widget(self.text_input)
        layout.add_widget(self.label1)
        layout.add_widget(self.text_input1)
        layout.add_widget(self.label2)
        layout.add_widget(self.label3)
        exception_layout.add_widget(button1)
        exception_layout.add_widget(button2)
        layout.add_widget(exception_layout)
        layout.add_widget(self.label4)

        return layout

    def read_text(self, instance):
        Producto=""
        Cantidad=0
        try:
            Producto = self.text_input.text
        except Exception as e:
            self.label3.text ="Error debe ingresar un producto valido"
        try:
            Cantidad = int(self.text_input1.text)
        except Exception as e:
            self.label2.text ="Error debe ingresar un numero valido"
        if (Producto==""):
            self.label3.text ="Error debe ingresar un producto valido"
        elif (Producto not in (listado)):
            self.label3.text ="Error debe ingresar un producto valido"
        elif Cantidad<=0:
            self.label2.text ="Error debe ingresar un numero valido"
        else:
            self.Total,self.cantidad==calcular(Producto,Cantidad,self.Total,self.cantidad)
            Suma=sumaProductos(self.Total)
            SumaProducto=int(self.cantidad[Producto])*int(listado[Producto])
            #print(self.Total)
            #print(self.cantidad[Producto])
            self.label2.text = f"Es(son) {self.cantidad[Producto]} {Producto} por:"
            self.label3.text = f"{SumaProducto} de un total de {Suma}!"
    def read_text1(self, instance):
        self.Total=[]
        self.cantidad=cantidades.copy()
        self.label2.text =""
        self.label3.text =""
        

if __name__ == '__main__':
    MyApp().run()


