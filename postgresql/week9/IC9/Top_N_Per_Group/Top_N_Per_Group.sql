select distinct on (c.country)
	c.country,
	c.name,
	SUM(o.amount) as lifetime_value
from customers as c join orders as o on c.id = o.customer_id
where o.status = 'paid'
group by c.country, c."name", c.id
order by c.country, lifetime_value desc;
