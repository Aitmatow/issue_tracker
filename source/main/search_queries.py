from django.utils import timezone

from webapp.models import *

# Задачи, закрытые за последний месяц.
import datetime
Issue.objects.filter(status = '3', create_date__lte =timezone.now() - datetime.timedelta(days=30))


# Типы задач, встречающиеся в указанном проекте.
Issue.objects.filter(project = '1').values('tip_id')

# Проекты, в которых присутствует задача с указанным словом в описании.
Issue.objects.filter(description__icontains = 'и').values('project_id')

# Проекты, в которых все задачи закрыты.
