select
	c.country,
	o.status,
	round (
		100.0 * count(*)
		/ sum(count(*)) over (partition by c.country), 2) as percentage
from customers as c join orders as o on c.id = o.customer_id group by c.country, o.status;
