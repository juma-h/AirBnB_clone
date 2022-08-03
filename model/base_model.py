#!/usr/bin/python3
# 
import uuid
from daytime import datetime 

class BaseModel:
    def __init__(self, id, created_at, updated_at):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime();
        self.updated_at =datetime.datetime();