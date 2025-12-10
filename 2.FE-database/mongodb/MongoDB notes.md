MongoDB notes

Intro: 

<mark>CRUD methods </mark>: create, read (aka retrieve), update, and delete

<mark>Mongo</mark> stores all associated data within one record, instead of storing it across many preset tables as in a SQL database. (not a non-relational databases?)

- Scalability: by default, non-relational databases are split (or "shared") across many systems instead of only one. This makes it easier to improve performance at a lower cost.
- Flexibility: new datasets and properties can be added to a document without the need to make a new table for that data.
- Replication: copies of the database run in parallel so if one goes down, one of the copies becomes the new primary data source.
- Mongo's use of JSON as its document storage structure

<mark>Mongoose.js</mark> is an npm module for Node.js that allows you to write objects for Mongo as you would in JavaScript. This can make it easier to construct documents for storage in Mongo.

注册流程就略过了，官网有详细步骤。

```js
//app.js

require('dotenv').config()
const mongoose = require('mongoose');
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true }); 

```

```js
//.env

MONGO_URI='mongodb+srv://heather:lcx9670@cluster0.ssnas.mongodb.net/Cluster0?retryWrites=true&w=majority'
```

First of all we need a <mark>Schema</mark>. Each schema maps to a MongoDB collection. It defines the shape of the documents within that collection. Schemas are building block for Models. They can be nested to create complex models, but in this case we’ll keep things simple. A <mark>model </mark>allows you to create<mark> instances</mark> of your objects, <mark>called documents</mark>.

The `done()` function is a callback that tells us that we can proceed after completing an asynchronous operation such as inserting, searching, updating or deleting. It’s following the Node convention and should be called as `done(null, data)` on success, or `done(err)` on error. 

Repl.it is a real server, and in real servers the interactions with the db happen in handler functions. These function are executed when some event happens (e.g. someone hits an endpoint on your API). 

[source link](https://www.freecodecamp.org/learn/apis-and-microservices/mongodb-and-mongoose/create-a-model)

```js
/* Example */
//这里我没太清楚为什么要用function，不过应该是我对FUNCTION 的理解问题。

var someFunc = function(done) {
  //... do something (risky) ...
  if(error) return done(error);
  done(null, result);
};
```

```js
require('dotenv').config()
const mongoose = require('mongoose');
const Schema= mongoose.Schema;

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true }); 

//create a model
const personSchema = new Schema({
    name:  String, 
    age : Number,
    favoriteFoods : [String]
  });

//create an instance that called document
const Person = mongoose.model('Person', personSchema);

var createAndSavePerson = function(done) {
  var janeFonda = new Person(
    {
      name: "Jane Fonda", 
      age: 84, 
      favoriteFoods: ["vodka", "air"]
    });

  janeFonda.save(function(err, data) {
    if (err) return console.error(err);
    done(null, data)
  });
};


var arrayOfPeople = [
  {name: "Frankie", age: 74, favoriteFoods: ["Del Taco"]},
  {name: "Sol", age: 76, favoriteFoods: ["roast chicken"]},
  {name: "Robert", age: 78, favoriteFoods: ["wine"]}
];

var createManyPeople = function(arrayOfPeople, done) {
  Person.create(arrayOfPeople, function (err, people) {
    if (err) return console.log(err);
    done(null, people);
  });
};

var findPeopleByName = function(personName, done) {
  Person.find({name: personName}, function (err, personFound) {
    if (err) return console.log(err);
    done(null, personFound);
  });
};

var findOneByFood = function(food, done) {
 Person.findOne({favoriteFoods: foodName},function (err, foodFound) {
  if (err) return console.log(err);
    done(null,foodFound);
}); 
};

var findOneByFood = function(foodName,done){
  Person.findOne({favoriteFoods:foodName},function(err,foodFound){
    if(err) return console.log(err);
    done(null,foodFound);
  });
};

var findOneByFood = function(food, done) {
  Person.findOne({favoriteFoods: food}, function (err, data) {
    if (err) return console.log(err);
    done(null, data);
  });
};

var findEditThenSave = function(personId, done) {
  var foodToAdd = 'hamburger';
	Person.findById(personId,function(err,person){
    if(err) return console.log(err);
    person.favoriteFoods.push(foodToAdd);
    person.save((err, updatedPerson) => {
    if(err) return console.log(err);
    done(null,updatedPerson);
     });
  });
};
```

```js
var findAndUpdate = function(personName, done) {
  var ageToSet = 20;
  Person.findByIdAndUpdate({name:personName},{ age: ageToSet },{new: true},function (err, updatedDoc) {
  if (err) return console.log(err);
  done(null, updatedDoc);
});
};
//call back 的问题，callback需再理解
```

```js
const findAndUpdate = (personName, done) => {
  const ageToSet = 20;

  Person.findOneAndUpdate({name: personName}, {age: ageToSet}, {new: true}, (err, updatedDoc) => {
    if(err) return console.log(err);
    done(null, updatedDoc);
  })
};

//You should return the updated document. To do that you need to pass the options document { new: true } as the 3rd argument to findOneAndUpdate(). By default these methods return the unmodified object.
```

```js
//pass
var removeById = function(personId, done) {
  Person.findByIdAndRemove(
    personId,
    (err, removedDoc) => {
      if(err) return console.log(err);
      done(null, removedDoc);
    }
  ); 
};
```

```js
//error
var removeById = function(personId, done) {
  Preson.findByIdAndRemove(
  personId,
  function (err, data) {
    if (err) return console.log(err);
    done(null, data);
  };
  );
};
```

```js
var removeManyPeople = function(done) {
  var nameToRemove = "Mary";
  Person.remove(
    {name:nameToRemove},
    (err, data) => {
      if(err) return console.log(err);
      done(null, data);
    }
  ); 
};
```

```js
//pass
var queryChain = function(done) {
  var foodToSearch = "burrito";
  Person.find({favoriteFoods:foodToSearch}).sort({ name: 1 }).limit(2).select('-age').exec((err,data) =>{   
   
    err ? done(err): done(null, data);
    
  })
  
};
```

```js
//pass
var queryChain = function(done) {
  var foodToSearch = "burrito";
  Person.find({ favoriteFoods: foodToSearch })
  .sort({ name: 1 })
  .limit(2)
  .select('-age')
  .exec(function(error, people) {
      done(null,people);
  });
};
```





