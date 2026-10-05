select
	c.id,
	c.name,
	o.placed_at,
	o.id as order_id
from customers as c left join orders as o on c.id = o.customer_id
and o.placed_at between c.signed_up_at and c.signed_up_at + interval '30 days';
