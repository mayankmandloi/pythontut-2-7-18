class t1:
    city="Indore"
    def __init__(self):
        self.name="Mayank"

class t2(t1):
    state="M.P."

t= t2()
print(t.state,t.city,t.name)