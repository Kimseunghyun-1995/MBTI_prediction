from mbti_categories import *
import numpy
import matplotlib.pyplot as plt


class UserDB:

    Users = []

    # UserDB에 새로운 유저를 추가
    def add_user(self, user):
        self.Users.append(user)

    # name 을 가진 유저를 UserDB 에서 찾음
    def find_user(self, name):
        for user in self.Users:
            if user.name == name:
                return user
        return -1

    def print_all_users_mbti(self):
        for user in self.Users:
            print(user.get_user_mbti_string())

    def display_main_user_chart(self):
        argmax = numpy.argmax([user.compare_count for user in self.Users])
        self.Users[argmax].display_chart()
        plt.show()
