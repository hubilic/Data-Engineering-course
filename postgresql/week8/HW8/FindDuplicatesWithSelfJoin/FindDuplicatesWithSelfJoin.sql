SELECT
    c.id,
    c.email,
    c.country,
    c2.id as duplicate_id
from customers as c
join customers c2 on lower(c.email) = lower(c2.email)
and c.country = c2.country
and c.id < c2.id;
