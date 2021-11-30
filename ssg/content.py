import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data = {"content": content}
    
    @property
    def body(self):
        return self.data["content"]

    @body.setter
    def body(self, value):
        self.data["type"] = value

    @property
    def type(self):
        return self.data["type"] if self.data.__contains__("type") else None
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __iter__(self):
        return self.data.__iter__
    
    def __len__(self):
        return self.data.__len__
    
    def __repr__(self):
        data = {}
        return str(data)