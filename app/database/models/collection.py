from sqlalchemy import Column, Integer, String, DateTime, Text

from app.extensions import db


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
