from admin_web.routes import router as admin_router

# Add admin routes
app.include_router(admin_router, prefix="/admin")