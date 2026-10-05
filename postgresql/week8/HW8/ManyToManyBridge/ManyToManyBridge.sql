select
	a.id,
	a.title,
	count(art.article_id) as tag_count
from articles as a
join article_tags as art on a.id = art.article_id
group by a.id, a.title
having count(art.tag_id) > 3;

select
	t.id,
	t.name,
	count(art.article_id) as article_count
from tags as t
join article_tags as art on t.id = art.tag_id
group by t.id, t.name
having count(art.tag_id) > 5;


select
	a.id,
	a.title,
	string_agg(t.name, ', ' order by t.name) as tags
from articles as a
join article_tags as art on a.id = art.article_id
join tags as t on t.id = art.tag_id
group by a.title, a.id;
