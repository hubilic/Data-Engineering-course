select
	o.placed_at,
	SUM(o.amount) as daily_revenue,
	SUM(SUM(o.amount)) over (order by o.placed_at) as running_total
from orders as o where o.status = 'paid'
group by o.placed_at order by o.placed_at;
