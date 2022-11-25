from datetime import datetime
from typing import Any, Generic, Optional, Type, TypeVar
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)  # type: ignore
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, *, model: Type[ModelType]):
        self.model = model

    def get(self, *, id: int, db: Session) -> Optional[ModelType]:
        return db.query(self.model)\
            .filter(self.model.id == id)\
            .filter(self.model.deleted_at == None)\
            .first()

    def get_multi(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
        db: Session
    ) -> list[ModelType]:
        return db.query(self.model)\
            .filter(self.model.deleted_at == None)\
            .offset(skip)\
            .limit(limit)\
            .all()

    def create(self, *, model: CreateSchemaType, db: Session) -> ModelType:
        model_data = jsonable_encoder(model)
        db_model = self.model(**model_data)
        db.add(db_model)
        db.commit()
        db.refresh(db_model)
        return db_model

    def update(
        self,
        *,
        db_model: ModelType,
        model: UpdateSchemaType | dict[str, Any],
        db: Session
    ) -> ModelType:
        db_model_data = jsonable_encoder(db_model)
        if isinstance(model, dict):
            update_data = model
        else:
            update_data = model.dict(exclude_unset=True)
        for field in db_model_data:
            if field in update_data:
                setattr(db_model, field, update_data[field])
        db_model.updated_at = datetime.now()
        db.add(db_model)
        db.commit()
        db.refresh(db_model)
        return db_model

    def remove(self, *, id: int, db: Session) -> Optional[ModelType]:
        model = self.get(id=id, db=db)
        if model is None:
            return model
        model.deleted_at = datetime.now()
        db.add(model)
        db.commit()
        db.refresh(model)
        return model
