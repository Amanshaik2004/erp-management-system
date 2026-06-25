from fastapi import FastAPI
from fastapi import Depends

from routers.auth_router import router as auth_router
from services.security_service import get_current_user
from routers.department_router import router as department_router
from routers.designation_router import router as designation_router
from routers.employee_router import router as employee_router
from routers.attendance_router import router as attendance_router
from routers.leave_router import router as leave_router
from routers.payroll_router import router as payroll_router
from routers.category_router import router as category_router
from routers.supplier_router import router as supplier_router
from routers.product_router import router as product_router
from routers.inventory_router import router as inventory_router
from routers.customer_router import router as customer_router
from routers.sales_order_router import router as sales_order_router
from routers.sales_order_item_router import router as sales_order_item_router
from routers.invoice_router import router as invoice_router
from routers.dashboard_router import router as dashboard_router
from routers.salary_structure_router import router as salary_structure_router
from routers.payslip_router import router as payslip_router
from routers.project_router import router as project_router
from routers.project_task_router import router as project_task_router
from routers.timesheet_router import router as timesheet_router
from routers.client_router import router as client_router
from routers.lead_router import router as lead_router
from routers.opportunity_router import router as opportunity_router
from routers.ticket_router import router as ticket_router
from routers.notification_router import router as notification_router
from routers.reports_router import router as reports_router


app = FastAPI(
    title="ERP Management System"
)

app.include_router(auth_router)
app.include_router(department_router)
app.include_router(designation_router)
app.include_router(employee_router)
app.include_router(attendance_router)
app.include_router(leave_router)
app.include_router(payroll_router)
app.include_router(category_router)
app.include_router(supplier_router)
app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(customer_router)
app.include_router(sales_order_router)
app.include_router(sales_order_item_router)
app.include_router(invoice_router)
app.include_router(dashboard_router)
app.include_router(salary_structure_router)
app.include_router(payslip_router)
app.include_router(project_router)
app.include_router(project_task_router)
app.include_router(timesheet_router)
app.include_router(client_router)
app.include_router(lead_router)
app.include_router(opportunity_router)
app.include_router(ticket_router)
app.include_router(notification_router)
app.include_router(reports_router)


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

