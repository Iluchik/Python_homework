select product_name, unit_price from products p 
where unit_price in (select min(unit_price) from products p where category_id = 1);