from fastapi import FastAPI
from fastapi import Depends

from routers.auth_router import router as auth_router
from services.security_service import get_current_user
from routers.department_router import router as department_router
from routers.designation_router import router as designation_router
from routers.employee_router import router as employee_router


app = FastAPI(
    title="ERP Management System"
)

app.include_router(auth_router)
app.include_router(department_router)
app.include_router(designation_router)
app.include_router(employee_router)

@app.get("/profile")
def profile(
    current_user = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role.role_name
    }

