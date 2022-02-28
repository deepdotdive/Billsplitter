from random import randint


class BillSplitter:
    def __init__(self):
        self.friends_dict: dict = {}
        self.bill = 0

        self.msg_1 = 'Enter the number of friends joining (including you):\n'
        self.msg_2 = '\nNo one is joining for the party'
        self.msg_3 = '\nEnter the name of every friend (including you), each on a new line:'
        self.msg_4 = '\nEnter the total bill value:\n'
        self.msg_5 = '\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n'

        self.n_o_f = int(input(f'{self.msg_1}'))
        self.count_friend()
        self.final_bill()

    def count_friend(self):
        if self.n_o_f > 0:
            print(self.msg_3)
            self.friends_dict = {input(): 0 for _ in range(self.n_o_f)}
        else:
            print(self.msg_2)
            exit()

    def final_bill(self):
        self.bill = int(input(self.msg_4))

    def bill_split(self, n):
        self.bill = round(self.bill / (self.n_o_f - n), 2)
        self.friends_dict.update((_, self.bill) for _ in self.friends_dict)

    def lucky_person(self):

        if input(self.msg_5) == 'Yes':
            self.bill_split(1)

            ran_dom = randint(0, len(self.friends_dict))
            pick_dict = list(self.friends_dict)[ran_dom - 1]
            self.friends_dict[pick_dict] = 0

            return f'\n{pick_dict} is the lucky one!'

        else:
            self.bill_split(0)
            return '\nNo one is going to be lucky\n'


if __name__ == '__main__':
    app = BillSplitter()
    print(app.lucky_person())
    print(app.friends_dict)
