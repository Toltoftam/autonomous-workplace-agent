from pydantic import BaseModel


class WorkflowResult(
    BaseModel
):

    workflow_name: str

    status: str

    result: dict
