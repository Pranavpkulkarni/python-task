from sqlalchemy import Column, BigInteger, String, Enum, Integer, TIMESTAMP
from app.database import Base

class Product(Base):
    __tablename__ = "Product"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum("finished", "semi-finished", "raw"), nullable=False)
    description = Column(String(250))
    product_image = Column(String(255))
    sku = Column(String(100), nullable=False)
    unit_of_measure = Column(Enum("mtr", "mm", "ltr", "ml", "cm", "mg", "gm", "unit", "pack"), nullable=False)
    lead_time = Column(Integer)
    created_date = Column(TIMESTAMP)
    updated_date = Column(TIMESTAMP)
