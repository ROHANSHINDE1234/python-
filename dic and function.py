#dictionary is nothing but key value pairs
d1 = {}
print(type(d1))
d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "Salman":"Roti",
      "Shubham":{"B":"maggie","A":"Rice"}}

print(d2["Harry"])
print(d2["Rohan"])
print((d2["Shubham"]["A"]))
d2["Ankit"]= "Junk food"
d2["Nihal"]= "Pizza"
print(d2)
del d2["Nihal"]

d3 = d2.copy()
del d3["Harry"]

d2.update({"Mohit":"Bhendi"})

print(d2.items())
