import streamlit as st
import time 

class Option:
    def __init__(self, name, interest_level, growth_potential, effort_required, category):
        self.name = name
        self.interest_level = interest_level
        self.growth_potential = growth_potential
        self.effort_required = effort_required
        self.category = category

    def calculate_score(self):
        return self.interest_level + self.growth_potential - self.effort_required


class Decision_Engine:
    def __init__(self):
        self.options = []

    def score_ranking(self):
        return sorted(self.options, key=lambda opt: opt.calculate_score(), reverse=True)

    def b_e_s_t__o_p_t_i_o_n(self):
        if not self.options:
            return None
        best_option = max(self.options, key=lambda opt: opt.calculate_score() )
#self.options=[option1Object, option2Object, option3object]
#option1object.name
        return best_option
    
    def delete_option(self,index):
        if 0<= index < len(self.options):
            del self.options[index]

    def clear_all(self):
        self.options.clear()

    def add_options(self,option):
        self.options.append(option)
        


if "engine" not in st.session_state:
    st.session_state.engine = Decision_Engine()
    st.session_state["option_name"] = ""
    st.session_state["option_catrgory"] = ""

engine = st.session_state.engine

#----------------------------------#
#----------------UI----------------#
#----------------------------------#


st.set_page_config(page_title="Personal Decision Engine", page_icon="🧠" ,layout="centered")
st.title("🧠 Personal Decision Engine")
st.write("Compare multiple options and get your best reccomendations")

st.subheader("➕ Add a new option")

with st.form("add_option_form",clear_on_submit = True):
    name = st.text_input("Option Name", key="option_name")
    category = st.text_input("Category (Career / Hobby / Skill / Project)", key="option_category")

    interest = st.slider("Interest level", 0, 10, 0)
    growth = st.slider("Growth Potential", 0, 10, 0)
    effort = st.slider("Effort required", 0, 10, 0)

    submitted = st.form_submit_button("Add Option")

if submitted:
    if name.strip() == "" or category.strip() == "":
        st.error("Name and category cannot be empty")

    else:
        already = True
        for i in engine.options:
            if name.lower() == i.name.lower():
                already = False
        
        if already == False:
            st.error("Option already Exsists")
            already = True
        else:
            option = Option(name.strip(), interest, growth, effort, category)
            engine.add_options(option)
            st.success(f"{name} added successfully!")

st.divider()
st.subheader(" 📋 Saved Options")
if not engine.options:
    st.info("No Options Found")
else:
    for i, option in enumerate(engine.options, start=1):
        st.write(
            f"**No.{i}:** {option.name} ({option.category}) |"
            f"Interest: {option.interest_level} | Growth: {option.growth_potential} | "
            f"Effort: {option.effort_required} | **Score: {option.calculate_score()}**"
            )
        
st.divider()
st.subheader("🗑️ Manage Options")
if engine.options:
    option_names = [f"{i.name}" for i in engine.options]
    selected_option = st.selectbox("Select an option to delete", option_names)
    if st.button("Delte Selected Option"):
        selected_index = option_names.index(selected_option)
        engine.delete_option(selected_index)
        st.error("Option deleted successfully")
        time.sleep(1)
        st.write("delting in (3)")
        time.sleep(1)
        st.write("delting in (2)")
        time.sleep(1)
        st.write("delting in (1)")
        time.sleep(1)
        st.rerun() 

    if st.button("Clear All options"):
        engine.clear_all()
        st.error("All Options Cleared!")
        time.sleep(1)
        st.write("clearing in (3)")
        time.sleep(1)
        st.write("clearing in (2)")
        time.sleep(1)
        st.write("clearing in (1)")
        time.sleep(1)
        st.rerun()

else:
    st.info("No options available to manage")

st.divider()
if st.button("📊 Generate decision report"):
    if not(engine.options):
        st.warning("No Option Found")
    else:
        ranking = engine.score_ranking() #ranking variable holds ranked_options=[option1Object, option2Object]
        best = engine.b_e_s_t__o_p_t_i_o_n()
        st.subheader("🏆 Ranked Recommendations")
        for i,r in enumerate(ranking, start=1): #for loop iteration you get optionObject
            st.write(
                f"𝓝𝓸.{i}: **{r.name}** ({r.category}) → Score: {r.calculate_score()}"
            )
        
        st.info(
            f"💡 Based on your ratings, **{best.name}** is currently your strongest choice."
        )















# options = []
# num = int(input("Enter number of options: "))

# for i in range(1, num + 1):
#     name = input(f"Enter name of option {i}: ")
#     interest = int(input(f"Enter interest level (1-10) for {name}: "))
#     growth = int(input(f"Enter growth potential (1-10) for {name}: "))
#     effort = int(input(f"Enter effort required (1-10) for {name}: "))

#     opt = Option(name, interest, growth, effort)
#     options.append(opt)


# for opt in options:
#     print(opt.name, "Decision Score:", Decision_Engine.decision_score(opt))

# best = Decision_Engine.recommend(options)
# print("Best option is:", best.name)



# option1 = Option("Learn Python", 5, 5, 3)
# option2 = Option("Play Video Games", 4, 2, 1)
# option3 = Option("Start Gym", 3, 4, 4)

# options = [option1, option2, option3]

# print(option1.name, "Decision Score:", Decision_Analyzer.decision_score(option1))
# print(option2.name, "Decision Score:", Decision_Analyzer.decision_score(option2))
# print(option3.name, "Decision Score:", Decision_Analyzer.decision_score(option3))
