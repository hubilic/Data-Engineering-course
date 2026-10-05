select
	coalesce(im.sku, ie.sku) as sku,
	im.count as morning_count,
	ie.count as evening_count
from inventory_morning as im full outer join inventory_evening as ie on im.sku = ie.sku
where im.sku is null or ie.sku is null or im.count <> ie.count;
