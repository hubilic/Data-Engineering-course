select
	dm.date as day,
	sum(dm.value) filter (where dm.metric_name = 'visits') as visits,
	sum(dm.value) filter (where dm.metric_name = 'signups') as signups
from daily_metrics as dm group by date;
