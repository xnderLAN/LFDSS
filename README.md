from src import create_app, db
app = create_app()
app.app_context().push()
db.create_all(app=create_app())
exit()