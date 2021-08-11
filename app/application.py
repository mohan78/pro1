from datetime import datetime

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from sqlalchemy import Column, Integer, String, DateTime, Text, and_

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Collection(db.Model):
    __tablename__ = 'collections'

    id = Column(Integer, primary_key=True)
    ip_type = Column(String(15))
    source_ipv4 = Column(Text)
    destination_ipv4 = Column(Text)
    octet_delta_count = Column(Integer)
    packet_delta_count = Column(Integer)
    flow_start = Column(DateTime)
    flow_end = Column(DateTime)
    source_transport_port = Column(Integer)
    destination_transport_port = Column(Integer)
    ingress_interface = Column(Integer)
    egress_interface = Column(Integer)
    layer_2_segment_id = Column(Integer)
    protocol_identifier = Column(String)
    flow_end_reason = Column(Integer)
    tcp_control_bits = Column(String)
    ip_class_of_service = Column(Integer)
    maximum_ttl = Column(Integer)
    flow_direction = Column(Integer)
    ingress_interface_attr = Column(Integer)
    egress_interface_attr = Column(Integer)
    vxlan_export_role = Column(Integer)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        start = request.form.get('startDate')
        end = request.form.get('endDate')
        start_date = datetime.strptime(start, '%Y-%m-%d %H:%M')
        end_date = datetime.strptime(end, '%Y-%m-%d %H:%M')
        print(request.form.get('button'))

        button = request.form.get('button')
        if button == 'load':
            rows = db.session.query(Collection).distinct(Collection.source_ipv4, Collection.destination_ipv4)\
                .filter(and_(start_date < Collection.flow_start, Collection.flow_start < end_date)).all()
            return render_template('home.html', start_date=start, end_date=end, rows=rows)

    return render_template('home.html', start_date='', end_date=None, rows=[])


if __name__ == '__main__':
    app.run(debug=Config.DEBUG)