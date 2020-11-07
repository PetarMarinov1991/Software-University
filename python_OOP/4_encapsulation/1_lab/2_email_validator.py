import re


class EmailValidator:
    def __init__(self, min_length: int, valid_mails: [], valid_domains: []):
        self.min_length = min_length
        self.valid_mails = valid_mails
        self.valid_domains = valid_domains

    @staticmethod
    def split_mail(mail):
        delimiters = '@', '.'
        regex = '|'.join(map(re.escape, delimiters))
        username, email, domain = re.split(regex, mail)
        return username, email, domain

    def __validate_name(self, name: str):
        return len(name) >= self.min_length

    def __validate_mail(self, mail: str):
        return mail in self.valid_mails

    def __validate_domain(self, domain: str):
        return domain in self.valid_domains

    def validate(self, email):
        username, email, domain = EmailValidator.split_mail(email)
        return \
            EmailValidator.__validate_name(self, username) and \
            EmailValidator.__validate_mail(self, email) and \
            EmailValidator.__validate_domain(self, domain)
