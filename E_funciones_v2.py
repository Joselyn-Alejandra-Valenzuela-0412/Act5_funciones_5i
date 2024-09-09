print("funciones creadas por el usuario")
#las funciones 
def Mi_lista():
    amigos=["Homero","paty","Lety"]
    print("--lista--")
    print(amigos)
    for nava in amigos:
        print(nava)
def Mi_tupla():
    amigos=("Homero","paty","Lety")
    print("--tupla--")
    print(amigos)
    for nava in amigos:
        print(nava)
        #conjunto funcion
def Mi_conjunto():
    amigos={"Homero","paty","Lety"}
    print("--conjunto--")
    print(amigos)
    for nava in amigos:
        print(nava)
        # diccionario funcion
def Mi_diccionario():
    amigos={"amigo1": "Homero",
            "amiga2": "paty",
            "amiga3": "Lety"
            }
    print("--diccionario--")
    print(amigos)
    print("--amigos nava--")
    for nava in amigos:
        print(amigos[nava])
        # llama a funciones
Mi_lista()
Mi_tupla()
Mi_conjunto()
Mi_diccionario()
