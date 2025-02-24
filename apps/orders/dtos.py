from dataclasses import dataclass
from decimal import Decimal

@dataclass
class SalesReportDTO:
    restaurant_id: int
    restaurant_name: str
    total_sales: int
    total_amount: Decimal
