from flask_restful import Resource
import logging


class Usuarios(Resource):
    
    def get(self):
        try:
            json = {
                "nome": "Teste",
                "Sobrenome": "Outro Teste",
                "Idade": 25
            }
            return json, 200
        except Exception as e:
            return {"Message", f"Erro ao retornar usuário: {e}"}, 400
