class AccessError(Exception): pass

class Privater:
    def __init__(self, private_data, public=None):
        object.__setattr__(self, "private", private_data)
        object.__setattr__(self, "public", public)
        object.__setattr__(self, "key", id(self))
        object.__setattr__(self, "key_geted", False)
        
    def __getattribute__(self, attr, key=float("inf")):
        if (attr not in ["key"] and attr != "__dict__"):
            if (attr != "private"):
                return object.__getattribute__(self, attr)
            else:
                if (key == object.__getattribute__(self, "key")):
                    return object.__getattribute__(self, "private")
                else:
                    raise AccessError("Access denied")
        else:
            raise AccessError("Access denied")
    def get(self, attr, key):
        self.__getattribute__(attr, key)
    def __setattr__(self, attr, val):
        if (attr not in ["private", "key", "key_geted"] and attr != "__dict__"):
            if (attr == "public"):
                object.__setattr__(self, attr, val)
            else:
                raise AccessError("Access denied")
        else:
            raise AccessError("Access denied")
    def get_key(self):
        if (not self.key_geted):
            return object.__getattribute__(self, "key")
        object.__setattr__(self, "key_geted", True)
    
