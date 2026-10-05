with orders_stats as (
	select
		o.customer_id,
		avg(o.amount) as mean_amount,
		stddev(o.amount) as stddev_amount
	from orders as o group by o.customer_id
)
select
	o.id as order_id,
	o.customer_id,
	o.amount,
	os.mean_amount,
	os.stddev_amount
from orders as o join orders_stats as os on os.customer_id = o.customer_id
where o.amount > os.mean_amount +2 * os.stddev_amount;
