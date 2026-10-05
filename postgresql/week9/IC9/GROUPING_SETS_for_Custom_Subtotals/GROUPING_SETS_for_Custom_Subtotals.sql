select
	to_char(o.placed_at, 'YYYY') as year,
	c.country,
	sum(o.amount) as revenue
from orders as o join customers as c on o.customer_id = c.id
where o.status = 'paid'
group by grouping sets (
	(to_char(o.placed_at, 'YYYY'), c.country),
	(to_char(o.placed_at, 'YYYY')),
	()
)
order by year nulls last, c.country nulls last;
