class EmailServiceFake:
    @staticmethod
    def send(to, subject, body):
        print(f"Fake email sent to {to} with subject {subject} and body {body}")
