from fastapi import APIRouter, HTTPException
from app.modules.categorias.service import *
from app.modules.categorias.schemas import CategoriaCreate, CategoriaUpdate, CategoriaRead
from app.modules.categorias.unit_of_work import CategoriaUnitOfWork

router = APIRouter(prefix="/categorias", tags=["categorias"])
def svc(): return CategoriaService(CategoriaUnitOfWork())

@router.get("/", response_model=list[CategoriaRead])
def listar(): return svc().listar()

@router.get("/{id}", response_model=CategoriaRead)
def obtener(id: int):
    try: return svc().obtener(id)
    except CategoriaNoEncontrada: raise HTTPException(404, "No encontrada")

@router.post("/", response_model=CategoriaRead, status_code=201)
def crear(data: CategoriaCreate):
    try: return svc().crear(data)
    except CategoriaDuplicada: raise HTTPException(409, "Nombre duplicado")

@router.put("/{id}", response_model=CategoriaRead)
def actualizar(id: int, data: CategoriaUpdate):
    try: return svc().actualizar(id, data)
    except CategoriaNoEncontrada: raise HTTPException(404, "No encontrada")

@router.delete("/{id}", status_code=204)
def eliminar(id: int):
    try: svc().eliminar(id)
    except CategoriaNoEncontrada: raise HTTPException(404, "No encontrada")