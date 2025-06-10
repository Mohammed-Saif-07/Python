# # disctionaries are used to store 
# # data values in key:value pairs

# dict["key"] = "value" to assign or add new
# dict are mutable,unordered(no indexing)
# no duplicate keys in dict(primary key kinda)
info = {
    "key" : "value",
    "name": "Saif",
    "learning": "coding",
    "age": 35,
    "is_adult":True,
    "marks": 94.4,

    "subjects" :["Python","C"],
    "topics": ("dict","set")
}

info["name"] = "Saifyy"
info["surname"] = "ansari"
print(info)
