from main_app import create_app, create_db

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
