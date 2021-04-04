### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  
  JavaScript is less proun to throwing an error usioaly it returns undefined  
  Python  is throwing errors much more and helping you avoid mistaces
  in for loops we dont have direct acces to index in Python


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  * 'c' in Object.keys(obj) ? obj.c : 'not in obj'
  * 'c' in dict
- What is a unit test?
  * unittest test multiple funcions of an app with multiple outcomes
- What is an integration test?
  * integration tests test if all functions work together 
  
- What is the role of web application framework, like Flask?

  * the row of flask is to speed up development provide easy to use tools

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  * i would youse query params for operations like searching for something in my database
  * and rout parameter to ceap track of what page i am in if there are multiple pages

- How do you collect data from a URL placeholder parameter using Flask?
  * i wil send the placeholder to the function of that rout and use it
- How do you collect data from the query string using Flask?
  * i wil use request.args
- How do you collect data from the body of the request using Flask?
  * request.get
- What is a cookie and what kinds of things are they commonly used for?
  * cookie are very small peace of data send back and fourth betwean user and server
  * cookies are used to keep track ofserten data like items in a cart
- What is the session object in Flask?
  * session is a dictionary like object that ceaps track of data in flask

- What does Flask's `jsonify()` do?
  * it turs data in to json 
