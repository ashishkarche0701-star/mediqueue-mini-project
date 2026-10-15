from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3, os
from datetime import datetime
app=Flask(__name__); app.secret_key=os.environ.get("SECRET_KEY","dev-only-change-me")
DB=os.path.join(os.path.dirname(__file__),"mediqueue.db")
class PatientNode:
    def __init__(self,row):
        self.id=row["id"]; self.name=row["name"]; self.age=row["age"]; self.complaint=row["complaint"]; self.priority=row["priority"]; self.status=row["status"]; self.created_at=row["created_at"]; self.next=None
class PatientLinkedList:
    def __init__(self): self.head=None; self.tail=None
    def append(self,node):
        if self.head is None: self.head=self.tail=node
        else: self.tail.next=node; self.tail=node
    def values(self):
        out=[]; cur=self.head
        while cur: out.append(cur); cur=cur.next
        return out
def db():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def init_db():
    with db() as c: c.execute("CREATE TABLE IF NOT EXISTS patients(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,age INTEGER NOT NULL,complaint TEXT NOT NULL,priority TEXT NOT NULL,status TEXT NOT NULL,created_at TEXT NOT NULL)")
def patients():
    linked=PatientLinkedList()
    with db() as c: rows=c.execute("SELECT * FROM patients ORDER BY id").fetchall()
    for r in rows: linked.append(PatientNode(r))
    return linked.values()
init_db()
@app.get("/")
def index():
    allp=patients(); waiting=sorted([p for p in allp if p.status=="Waiting"],key=lambda p:0 if p.priority=="Emergency" else 1)
    return render_template("index.html",patients=allp,waiting=waiting)
@app.post("/patients")
def add():
    name=request.form.get("name","").strip(); complaint=request.form.get("complaint","").strip(); priority=request.form.get("priority","Normal")
    try:
        age=int(request.form.get("age",""))
        if not name or not complaint or not 0<=age<=120 or priority not in ("Emergency","Normal"): raise ValueError()
    except ValueError:
        flash("Enter a name, age from 0 to 120, complaint, and valid priority."); return redirect(url_for("index"))
    with db() as c: c.execute("INSERT INTO patients(name,age,complaint,priority,status,created_at) VALUES(?,?,?,?,?,?)",(name,age,complaint,priority,"Waiting",datetime.now().isoformat(timespec="minutes")))
    flash("Demo patient registered."); return redirect(url_for("index"))
@app.post("/patients/<int:pid>/call")
def call(pid):
    waiting=sorted([p for p in patients() if p.status=="Waiting"],key=lambda p:0 if p.priority=="Emergency" else 1)
    if waiting and waiting[0].id==pid:
        with db() as c: c.execute("UPDATE patients SET status='In Treatment' WHERE id=?",(pid,))
    else: flash("Call the next patient in the emergency-first queue.")
    return redirect(url_for("index"))
@app.post("/patients/<int:pid>/complete")
def complete(pid):
    with db() as c: c.execute("UPDATE patients SET status='Treated' WHERE id=? AND status='In Treatment'",(pid,))
    return redirect(url_for("index"))
@app.get("/health")
def health(): return {"status":"ok","app":"MediQueue"}
if __name__=="__main__": app.run(debug=True)
