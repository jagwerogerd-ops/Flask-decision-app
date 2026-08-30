from flask import Flask, render_template,request

app = Flask(__name__)

# this will act as our database ( A list of python dictionaries)
decisions = [
{
 "title":"Invest in Bitcoin",
 "reason":"Market trend looked strong and many analysts predicted growth",
 "Confidence_level": "3",
 "Outcome": "Price dropped shortly after investment",
 "Lesson": "Avoid investing based only on hype, do deeper research", 
 "CreatedAt": "2026-03-01",
},
{
  "title": "Wake up at 5 AM daily", 
 "reason": "More quiet time for focused work",
 "Confidence_level": "5",
 "Outcome": "Productivity improved in the mornings",
 "Lesson": "Morning routines can significantly increase focus", 
 "CreatedAt": "2026-03-03",
},
{
 "title": "Start a flask teaching project", 
 "reason": "Student learn better by building real applications",
 "Confidence_level": "2",
 "Outcome": "Students engaged more and asked deeper questions",
 "Lesson" : "Hands on projects improve understanding significantly", 
 "CreatedAt":  "2026-03-02",
},

{
 "title": "Buy a second monitor", 
 "reason": "Coding and teaching would be easier with more screen space",
 "Confidence_level": "4",
 "Outcome": "Workflow became faster and more organized", 
 "Lesson": "Small hardware upgrades can greatly improve productivity", 
 "CreatedAT": "2026-03-07",

},
{
"title": "Use Excalidraw for teaching diagrams", 
"reason": "It is simple, visual, and good for explaining systems",
"Confidence_level": "9",
"Outcome": "Workflow became faster and more organized", 
"Lesson": "Small hardware upgrades can greatly improve productivity", 
"CreatedAT": "2026-03-06",
}
]

# structure of a single decision 
decision = {
"ID":"", #integer
"title": "", #text
"reason": "", #text
"confidence_level":"", #interger
"outcome": "", #text
"lesson": "", #text
"created_at": "",#date  
}

#views

# Would be a place to see all decisions
@app.route("/decisions")
def home():

    #logic to retrieve all decisions from the database

   return render_template("home.html", decision=decisions)
   



# Reading a Single decisions
@app.route("/decisions/<int:id>")
def single_decision(id):
    rendered_decision = None
    for decision in decisions: 
        print(decisions[id])
        rendered_decision = decisions[id]

        return render_template("single_decision.html",decision=decision[id])
  

# Ceate a decision
@app.route("/create_decision", methods=["GET","POST"])
def create_decision():
    if request.method =="POST":
        #logic to create a decision 
        decision= {
       "title": request.form["title"],
       "reason":request.form["reason"],
       "confidence_level": request.form["confidence_level"],}
        decisions.append(decision)
        
        print ("We have posted:", decisions)
       
    return render_template("create_decision.html",decisions=decisions)



@app.route("/decisions/update/<int:id>", methods=["GET", "POST"]) 
def update_decision(id):

    decision = ''
    for decision in decisions: 
        print(decisions[id])
      #render_decision = decisions[id]

    return render_template("update_decision.html", decision=decisions[id])
        

    if request.method == "POST":
           title = request.form["title"]
           reason = request.form["reason"]
           confidence_level = request.form["confidence_level"]


    return render_template("update_decision.html", decision=decision)



if __name__ == '__main__':
 app.run(debug=True) 

