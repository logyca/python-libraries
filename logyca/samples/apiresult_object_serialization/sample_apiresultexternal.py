from logyca import APIResultDTOExternal, ValidationError
import json
import uuid

aPIResultDTOExternal=APIResultDTOExternal()

aPIResultDTOExternal.validationErrors=[
    ValidationError(detailError="sample1",transactionId="xxx1"),
    ValidationError(detailError="sample2",transactionId="xxx2"),
]

aPIResultDTOExternal.traceAbilityId=uuid.uuid4()
print(f"non-serializable object: {aPIResultDTOExternal.__dict__}")
print(f"serializable object: {json.dumps(aPIResultDTOExternal.to_dict(),indent=4)}")