import datetime
from Ex13.database import db

class Empresa(db.Model):
    __tablename__ = 'tb_empresa'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45))
    confiabilidade = db.Column(db.Float())

    def serialize(self):
        return {'id': self.id,
                'nome' : self.nome,
                'confiabilidade' : self.confiabilidade
                }