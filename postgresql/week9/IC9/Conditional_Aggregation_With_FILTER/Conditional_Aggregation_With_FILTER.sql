select
	o.customer_id,
	count(*) as total_orders,
	count(*) filter (where o.status = 'paid') as paid_orders,
	count(*) filter (where o.status = 'cancelled') as refunded_orders,
	sum(o.amount) filter (where o.status = 'paid') as paid_revenue
from orders as o
group by o.customer_id;
