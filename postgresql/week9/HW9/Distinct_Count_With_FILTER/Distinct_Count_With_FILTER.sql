select
	b.id as book_id,
	b.title,
	count(distinct o.id) as total_orders,
	count(distinct o.customer_id) as distinct_customers,
	count(distinct o.customer_id) filter (where o.status = 'paid') as distinct_paying_customers
from books as b
join order_items oi on oi.book_id = b.id
join orders as o on o.id = oi.order_id group by b.id;
