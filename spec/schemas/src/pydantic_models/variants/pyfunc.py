from pydantic import BaseModel
from typing import Any


class PyFuncVariant(BaseModel):

    pyfunc_classname: str
    extra_values: dict[str, Any] | None = None
