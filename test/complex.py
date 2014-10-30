#!/usr/bin/env python

TEST = "complex"
execfile("head.inc")

#######################################################

tproc.set("title", "Hello template world.")
tproc.set("blurb", 1)

users = [
    { "name" : "Joe User", "age" : 18, "city" : "London", 
      "Skills" : [
        { "skill" : "computers" },
        { "skill" : "machinery" }        
    ]},
    { "name" : "Peter Nobody", "age" : 35, "city" : "Paris", 
      "Skills" : [
        { "skill" : "tennis" },
        { "skill" : "football" },
        { "skill" : "baseball" },
        { "skill" : "fishing" }
    ]},    
    { "name" : "Jack Newman", "age" : 21, "city" : "Moscow", 
      "Skills" : [
        { "skill" : "guitar" },
        { "skill" : "piano" },
        { "skill" : "flute" }        
    ]}
]

tproc.set("Users", users)

products = [
    { "key" : 12, "name" : "cake",  "selected" : 0 },
    { "key" : 45, "name" : "milk",  "selected" : 1 },
    { "key" : 78, "name" : "pizza", "selected" : 0 },
    { "key" : 32, "name" : "roll",  "selected" : 0 },
    { "key" : 98, "name" : "ham",   "selected" : 0 },
]

tproc.set("Products", products)
tproc.set("Unused_loop", [])

#######################################################

execfile("foot.inc")
