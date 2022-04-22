from datetime import datetime


class DataGenerator:
    def prepare_good_email(self):
        base_part = "test"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")

        return f"{base_part}{random_part}@{domain}"

    def prepare_bad_email(self):
        base_part = "test"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")

        return f"{base_part}{random_part}{domain}"


data_generator = DataGenerator()
