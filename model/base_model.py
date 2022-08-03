#!/usr/bin/python3
# 
import uuid
from daytime import datetime 

class BaseModel:
    def __init__(self, id, created_at, updated_at):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime();
        self.updated_at =datetime.datetime()
        
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
      
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
       
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = self.created_at.isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict