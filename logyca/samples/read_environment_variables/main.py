from config import settings
import json

print(json.dumps(settings.__dict__,indent=4))

# Output
    # {
    #     "DB_HOST": "psqlt",
    #     "DB_NAME": "test",
    #     "DB_PASS": "es3bv3v3",
    #     "DB_PORT": 5432,
    #     "DB_USER": "postgres",
    #     "DB_SSL": false
    # }
