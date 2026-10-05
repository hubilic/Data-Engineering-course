select
	c.id,
	c.name,
	sum(case when o.status = 'paid' then 1 else 0 end) as paid_count,
	sum(case when o.status = 'pending' then 1 else 0 end) as pending_count,
	sum(case when o.status = 'cancelled' then 1 else 0 end) as cancelled_count
from customers as c
left join orders as o on c.id = o.customer_id
group by c.id, c.name
order by c.id;
