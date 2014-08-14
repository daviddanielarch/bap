class Type(object):
    pass
    
class BasicType(Type):
    pass
    
class LabelType(Type):
    pass
    
class AddrLabel(LabelType):
    def __init__(self, addr=None):
        self.addr = addr
    
    def __repr__(self):
        return 'addr 0x%x'% self.addr
        
class StrLabel(LabelType):
    def __init__(self, name=None):
        self.name = name
    
    def __repr__(self):
        return 'label {0}'.format(str(self.name))
        
class Register(BasicType):
    def __init__(self, bits=None):
        self.bits = bits
    
    def __repr__(self):
        if self.bits == 1:
            return 'bool'
        else:
            return 'u{0}'.format(str(self.bits))

class TMem(BasicType):
    def __init__(self, index_type=None):
        self.index_type = index_type
    
    def __repr__(self):
        return '?u{0}'.format(str(self.index_type))
