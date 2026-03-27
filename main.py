class Option:
    def __init__(self, name, interest_level, growth_potential, effort_required):
        self.name = name
        self.interest_level = interest_level
        self.growth_potential = growth_potential
        self.effort_required = effort_required


class Decision_Analyzer:

    @staticmethod
    def decision_score(option):
        score = option.interest_level + option.growth_potential - option.effort_required
        return score

    @staticmethod
    def recommend(options):
        best_option = max(options, key=lambda opt: opt.interest_level + opt.growth_potential - opt.effort_required)
        return best_option

options = []
num = int(input("Enter number of options: "))

for i in range(1, num + 1):
    name = input(f"Enter name of option {i}: ")
    interest = int(input(f"Enter interest level (1-10) for {name}: "))
    growth = int(input(f"Enter growth potential (1-10) for {name}: "))
    effort = int(input(f"Enter effort required (1-10) for {name}: "))

    opt = Option(name, interest, growth, effort)
    options.append(opt)

for opt in options:
    print(opt.name, "Decision Score:", Decision_Analyzer.decision_score(opt))

best = Decision_Analyzer.recommend(options)
print("Best option is:", best.name)

# option1 = Option("Learn Python", 5, 5, 3)
# option2 = Option("Play Video Games", 4, 2, 1)
# option3 = Option("Start Gym", 3, 4, 4)

# options = [option1, option2, option3]

# print(option1.name, "Decision Score:", Decision_Analyzer.decision_score(option1))
# print(option2.name, "Decision Score:", Decision_Analyzer.decision_score(option2))
# print(option3.name, "Decision Score:", Decision_Analyzer.decision_score(option3))
