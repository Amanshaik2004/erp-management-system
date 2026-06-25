from pydantic import BaseModel


class DashboardResponse(BaseModel):

    employees: int

    departments: int

    attendance: int

    leave_requests: int

    products: int

    tickets: int