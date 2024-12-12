select supplier_id, MAX(unit_price) as max_price from products p
group by supplier_id
having supplier_id in (1, 3, 5)
order by supplier_id;