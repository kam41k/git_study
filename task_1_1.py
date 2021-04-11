duration = 400153

sec = duration % 60
split_duration = f'{sec} сек'
if duration // 60 > 0:
    min = duration // 60 % 60
    split_duration = f'{min} мин {split_duration}'
    if duration // 60 // 60 > 0:
        hours = duration // 60 // 60 % 24
        split_duration = f'{hours} час {split_duration}'
        if duration // 60 // 60 // 24 > 0:
            days = duration // 60 // 60 // 24
            split_duration = f'{days} дн {split_duration}'

print(split_duration)