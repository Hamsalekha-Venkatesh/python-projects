from website import create_app

app = create_app()

# only if we run this file, not just import the file we run the application.
if __name__ == '__main__':
    app.run(debug=True)
