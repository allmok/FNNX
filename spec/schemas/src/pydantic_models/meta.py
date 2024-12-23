from pydantic import BaseModel


class MetaEntry(BaseModel):
    id: str
    producer: str
    producer_version: str
    producer_tags: list[str]
    payload: dict
