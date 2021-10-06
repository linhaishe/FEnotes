```react
import React from "react";

import ReactDOM from "react-dom";



const Course = ({ courses }) => {

  return (

​    <>

​      <Header course={courses} />

​      {/* <Content course={courses} />

​      <Total course={courses} /> */}

​    </>

  );

};



const Header = ({ courses }) => {

  console.log({ courses });

  return (

​    <>

​      {courses &&

​        courses.map((el) => (

          <div key={el.id}>

​            <h1>{el.name}</h1>

​            <Part parts={el.parts} />

​          </div>

​        ))}

​    </>

  );

};



const Total = ({ parts }) => {

  console.log({ parts });

  const exercisesCount = parts && parts.map((count) => count.exercises);

  // const reducer = (acc, cur) => acc + cur;

  // const sum = exercisesCount.reduce(reducer)



  var sum = exercisesCount.reduce((acc, cur) => acc + cur, 0);



  return <p>Number of exercises {sum}</p>;

};



const Part = ({ part }) => {

  return (

    <p>

​      {part.name} {part.exercises}

​    </p>

  );

};



const Content = ({ parts }) => {

  const partName = parts && parts.map((name) => parts.name);



  return (

    <div>

​      <Part part={partName} />

​    </div>

  );

};



const App = () => {

  const courses = [

​    {

​      name: "Half Stack application development",

​      id: 1,

​      parts: [

​        {

​          name: "Fundamentals of React",

​          exercises: 10,

​          id: 1,

​        },

​        {

​          name: "Using props to pass data",

​          exercises: 7,

​          id: 2,

​        },

​        {

​          name: "State of a component",

​          exercises: 14,

​          id: 3,

​        },

​        {

​          name: "Redux",

​          exercises: 11,

​          id: 4,

​        },

​      ],

​    },

​    {

​      name: "Node.js",

​      id: 2,

​      parts: [

​        {

​          name: "Routing",

​          exercises: 3,

​          id: 1,

​        },

​        {

​          name: "Middlewares",

​          exercises: 7,

​          id: 2,

​        },

​      ],

​    },

  ];

  return <Course courses={courses} />;

};



ReactDOM.render(<App />, document.getElementById("root"));
```

