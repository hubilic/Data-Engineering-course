select
	sum(o.amount) as total_amount,
	o.status,
	c.country
from orders as o join customers as c on o.customer_id = c.id
group by rollup(c.country, o.status) order by c.country nulls last, o.status nulls last;
