select
	o.id as order_id,
	o.customer_id,
	o.placed_at,
	previous.id as previous_order_id,
	previous.placed_at as previous_order_date
from orders as o
left join lateral (
	select o2.id, o2.placed_at
	from orders as o2
	where o2.customer_id = o.customer_id
	  and o2.placed_at < o.placed_at
	order by o2.placed_at desc
	limit 1
) as previous on true
order by o.customer_id, o.placed_at;
