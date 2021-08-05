from datetime import datetime

from flask import Flask, render_template, request

from sqlalchemy import func, distinct, tuple_, and_

from app.database.models import Collection
from app.extensions import db, migrate
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app, db)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        start = request.form.get('startDate')
        end = request.form.get('endDate')
        start_date = datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.strptime(end, '%Y-%m-%d')
        print(request.form.get('button'))

        button = request.form.get('button')
        if button == 'load':
            rows = db.session.query(Collection).distinct(Collection.source_ipv4, Collection.destination_ipv4)\
                .filter(and_(start_date < Collection.flow_start, Collection.flow_start < end_date)).all()
            return render_template('home.html', start_date=start, end_date=end, rows=rows)

    return render_template('home.html', start_date='', end_date=None, rows=[])


if __name__ == '__main__':
    app.run(debug=Config.DEBUG)