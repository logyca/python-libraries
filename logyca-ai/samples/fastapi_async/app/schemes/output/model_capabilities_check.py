from logyca_ai import ModelCapabilities

class ModelCapabilitiesCheck:
    def __init__(self, model:str, version:str, model_capabilities:ModelCapabilities) -> None:
        self.model = model
        self.version = version
        self.model_capabilities = model_capabilities
    def to_dict(self)->dict:
        tmp = self.__dict__
        tmp["model_capabilities"] = tmp["model_capabilities"].to_dict()
        return tmp
