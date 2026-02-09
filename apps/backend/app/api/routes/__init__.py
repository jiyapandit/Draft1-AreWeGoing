from .health import router as health_router
from .groups import router as groups_router

all_routers = [health_router, groups_router]
