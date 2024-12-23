from pydantic import BaseModel, ConfigDict


class Empty(BaseModel):
    ...

    model_config = ConfigDict(extra="forbid")
