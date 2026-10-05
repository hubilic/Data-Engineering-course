select
	o.placed_at,
	sum(o.amount) as sum_daily
from orders as o
where o.status = 'paid'
group by o.placed_at having SUM(o.amount)> 100;
