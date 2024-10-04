# tupla
atributos = ("Nome", "E-mail", "Profissão")

# lista de dicionários
usuarios = [
        {
            atributos[0]: "Fulano de tal",
            atributos[1]: "fulano@email",
            atributos[2]: "Programador"
        },
        {
            atributos[0]: "Cicrano da Silva",
            atributos[1]: "cicrano@email",
            atributos[2]: "Administrador"
        },
        {
            atributos[0]: "Beltrano de Souza",
            atributos[1]: "beltrano@email",
            atributos[2]: "Recepcionista"
        }
    ]

# cadastrar novo usuário
usuario = {}
for atributo in atributos:
        usuario[atributo] = input(f"Informe o valor do campo {atributo}: ")
usuarios.append(usuario)

# Exibir os dados de cada usuário
for usuario in usuarios:
    print("")
    for atributo in atributos:
        print(f"{atributo}: {usuario.get(atributo)}.")
print("")