from Ex13.app.history.model import Empresa

def get_all():
    return Empresa.query.all()