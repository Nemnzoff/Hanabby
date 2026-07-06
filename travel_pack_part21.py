# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: TravelPack
class Reminder:
    def __init__(self, task, date):
        self.task = task
        self.date = date

    @staticmethod
    def add_reminder(task, date_str):
        reminder = Reminder(task, datetime.strptime(date_str, '%Y-%m-%d'))
        print(f'Напоминание добавлено: "{reminder.task}" на {reminder.date.strftime("%d.%m")}')
        return reminder

    @staticmethod
    def list_reminders():
        print('Список напоминаний:')
        if Reminder.reminders == []:
            print('  Нет напоминаний.')
            return
        for r in Reminder.reminders:
            print(f'  - {r.task} ({r.date.strftime("%d.%m")})')

    @staticmethod
    def remove_reminder(task):
        to_remove = [r for r in Reminder.reminders if r.task == task]
        for r in to_remove:
            Reminder.reminders.remove(r)
        print(f'Напоминание "{task}" удалено.')

Reminder.reminders = []
