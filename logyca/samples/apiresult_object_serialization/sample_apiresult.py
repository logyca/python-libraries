from logyca import APIResultDTO
import json

aPIResultDTO=APIResultDTO()

print(f"non-serializable object: {aPIResultDTO.__dict__}")
print(f"serializable object: {json.dumps(aPIResultDTO.to_dict(),indent=4)}")