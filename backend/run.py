from app import create_app, db

app = create_app()

if __name__ == '__main__':
    app_instance = create_app()
    with app_instance.app_context():
     db.create_all()
    app.run(debug=True)
