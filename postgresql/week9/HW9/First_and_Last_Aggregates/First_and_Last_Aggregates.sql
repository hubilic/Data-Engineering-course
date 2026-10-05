select
	c.id as customer_id,
	c.name,
	min(o.placed_at) as first_order,
	max(o.placed_at) as last_order,
	(
		array_agg(
			o.amount order by o.placed_at asc, o.id asc
			)
	)[1] as first_amount,
	(
		array_agg(
			o.amount order by o.placed_at desc, o.id desc
			)
	)[1] as last_amount
from orders as o join customers as c on o.customer_id = c.id group by c.id;
