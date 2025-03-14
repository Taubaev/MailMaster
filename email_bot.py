from import_emails import import_email_list_from_csv
from get_email_body import get_email_body_from_db
from send_email import send_email
from save_reply import save_reply_to_json

def main():
    print("Запуск программы...")
    
    # Импортируем список e-mail
    email_list = import_email_list_from_csv("emails.csv")
    print(f"Количество email-ов: {len(email_list)}")  # Отображаем количество email-ов

    if not email_list:
        print("Не удалось загрузить email-адреса из CSV.")
    
    # Получаем шаблон письма из базы данных
    email_body = get_email_body_from_db(1)  # допустим, используем шаблон с ID 1
    if not email_body:
        print("Не удалось получить тело письма из базы данных.")
    
    subject = "Тема письма"
    
    # Данные для SMTP сервера
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "mirastaubaev1@gmail.com"  # Вставьте сюда ваш e-mail
    smtp_password = "qefl wzsb drhg iqjx"  # Вставьте сюда ваш пароль приложения

    # Отправка писем
    for email in email_list:
        print(f"Отправка письма на {email}...")
        success = send_email(smtp_user, email, subject, email_body, smtp_server, smtp_port, smtp_user, smtp_password)
        if success:
            print(f"Письмо отправлено на {email}")
        else:
            print(f"Не удалось отправить письмо на {email}")
    
    # Пример сохранения ответа
    reply = "Ответ пользователя"
    save_reply_to_json(reply, "replies.json")
    print("Программа завершена.")

if __name__ == "__main__":
    main()
