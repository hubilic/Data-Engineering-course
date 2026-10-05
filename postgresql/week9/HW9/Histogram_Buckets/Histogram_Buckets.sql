select
case
	when o.amount >= 0 and o.amount < 50 then '0-50'
	when o.amount >= 50 and o.amount < 100 then '50-100'
	when o.amount >= 100 and o.amount < 500 then '100-500'
	when o.amount >= 500 and o.amount < 1000 then '500-1000'
	when o.amount >= 1000 then '1000+'
end as bucket, count (*) as total_orders from orders as o
where o.amount is not null group by bucket order by min(o.amount);
