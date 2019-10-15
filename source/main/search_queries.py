from django.utils import timezone

from webapp.models import *

# Задачи, закрытые за последний месяц.
import datetime
from django.utils import timezone

Issue.objects.filter(status__name = 'Выполнена', create_date__lte =timezone.now() - datetime.timedelta(days=30))


# Типы задач, встречающиеся в указанном проекте.
Issue.objects.filter(project__name = 'Машинное обучение').values('tip__name')

# Проекты, в которых присутствует задача с указанным словом в описании.
Issue.objects.filter(description__icontains = 'и').values('project__name')

# Проекты, в которых все задачи закрыты.
Issue.objects.filter(status__name = 'Выполнена').values('project__name')
