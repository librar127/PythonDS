select 
Amount,
ROW_NUMBER OVER (Order by Amount DESC) row_number
from Orders