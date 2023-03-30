[py-image]: https://img.shields.io/badge/python-v3.10.0-blue
[py-url]: https://www.python.org/
[flask-image]: https://img.shields.io/badge/flask-v2.2.2-darkgreen
[flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[ariadne-image]: https://img.shields.io/badge/Ariadne-v0.17.0-magenta
[ariadne-url]: https://ariadnegraphql.org/
[pytest-image]: https://img.shields.io/badge/Pytest-v7.2.0-red
[pytest-url]: https://docs.pytest.org/en/7.2.x/
[post-image]: https://img.shields.io/badge/-POST-yellow


# Api para validar senha
[![python version][py-image]][py-url] [![flask version][flask-image]][flask-url] [![ariadne version][ariadne-image]][ariadne-url] [![pytest version][pytest-image]][pytest-url]

# Instruções para a equipe do Studio SOL 🌞
### Olá pessoal! Espero que gostem da minha versão desse projeto, não o subi no github pois como a instrução dizia para subir no drive, fiz como solicitado.
### Para facilitar os testes criei uma imagem no docker hub com todo o ambiente necessário, que pode ser acessível via:
> - docker pull 1blueevee/verify-password
> - docker run  --name blueevee-api -d -p 5000:5000 1blueevee/verify-password
> - Após isso podem executar requisições `POST` para `http://localhost:5000/graphql` baseado nos parâmetros descritos abaixo:

## Regras possíveis:
> - **minSize:** tem pelo menos x caracteres.
> - **minUppercase:** tem pelo menos x caracteres maiúsculos
> - **minLowercase:** tem pelo menos x caracteres minúsculos
> - **minDigit:** tem pelo menos x dígitos (0-9)
> - **minSpecialChars:** tem pelo menos x caracteres especiais ( Os caracteres especiais são os caracteres da seguinte string: "!@#$%^&*()-+\/{}[]" )
> - **noRepeted:** não tenha nenhum caractere repetido em sequência ( ou seja, "aab" viola esta condição, mas "aba" não)

### ![POST][post-image] */graphql*
### Query para consultar validade da senha
> Verifica se a senha é válida de acordo com as regras passadas  
 ```json
 query { 
     verify(password: "TesteSenhaForte!123&", rules: [
         {rule: minSize, value: 8},
        {rule: minSpecialChars, value: 2},
        {rule: noRepeted, value: 0},
        {rule: minDigit, value: 4}
    ]){
        verify
        noMatch
    }
}
```
> Retorna um boleano com o status da validade e os motivos desse status
```json
{
    "data": {
        "verify": {
            "verify": false,
            "noMatch": ["minDigit"]
        }
    }
}
```
### ![POST][post-image] */graphql*
### Query para consultar os valores possíveis para regras
```json
{
    __type(name: "Rules"){
        enumValues{
            name
        }
    }
}
```