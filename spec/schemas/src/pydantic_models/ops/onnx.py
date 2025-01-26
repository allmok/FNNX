from pydantic import BaseModel
from typing import Literal
from pydantic_models.op_instances import OpInstance
from pydantic_models.common import Empty


class Opset(BaseModel):
    domain: str
    version: int


class ONNXAttributes(BaseModel):
    opsets: list[Opset]
    requires_ort_extensions: bool
    has_external_data: bool
    onnx_ir_version: int


class ONNX_v1(OpInstance):
    op: Literal["ONNX_v1"]
    attributes: ONNXAttributes
