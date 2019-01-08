from newsapp import app, db
from newsapp.util import update_db

if __name__ == '__main__':
    update_db()
    app.run(debug=True, use_reloader=False)
