from pydantic import BaseModel


class PipelineNode(BaseModel):
    op_instance_id: str
    inputs: list[str]
    outputs: list[str]
    extra_dynattrs: dict[str, str]


class PipelineVariant(BaseModel):
    nodes: list[PipelineNode]
