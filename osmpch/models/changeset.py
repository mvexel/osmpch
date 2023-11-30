from sqlalchemy import JSON, Boolean, Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# <osm version="0.6" generator="CGImap 0.8.10 (2967745 spike-06.openstreetmap.org)" copyright="OpenStreetMap and contributors" attribution="http://www.openstreetmap.org/copyright" license="http://opendatacommons.org/licenses/odbl/1-0/">
# <changeset id="144609804" created_at="2023-11-30T03:03:09Z" closed_at="2023-11-30T03:03:10Z" open="false" user="mvexel" uid="8909" min_lat="37.7809030" min_lon="-86.8872370" max_lat="37.8120684" max_lon="-86.8279860" comments_count="0" changes_count="42">
# <tag k="changesets_count" v="22259"/>
# <tag k="comment" v="cleanup"/>
# <tag k="created_by" v="iD 2.27.3"/>
# <tag k="host" v="https://www.openstreetmap.org/edit"/>
# <tag k="imagery_used" v="Bing Maps Aerial"/>
# <tag k="locale" v="en-US"/>
# </changeset>
# </osm>


class Changeset(Base):
    __tablename__ = "changesets"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    closed_at = Column(DateTime)
    open = Column(Boolean)
    user = Column(String)
    uid = Column(Integer)
    min_lat = Column(Float)
    min_lon = Column(Float)
    max_lat = Column(Float)
    max_lon = Column(Float)
    comments_count = Column(Integer)
    changes_count = Column(Integer)
    tags = Column(JSON)
