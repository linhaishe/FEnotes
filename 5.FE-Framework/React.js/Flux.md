# Flux

## what is flux

1. a pattern
2. Centralized dispatcher
3. unidirectional data flows

## Two way binding vs unidirectional

Bebefits:

Clear,teastable,scalable,predictable

![Xnip2020-05-09_11-49-23](/Users/chenruo/Desktop/Xnip2020-05-09_11-49-23.jpg)

## flux 3 parts

![Xnip2020-05-09_11-54-15](/Users/chenruo/Desktop/Xnip2020-05-09_11-54-15.jpg)

### actions

1. encapsulate events

2. triggered by user interactions and server

3. passed to dispatcher

4. action payload has type and data

   **only the type property is required**

```js
{
type:"USER_SAVED"
data:{
firstName:"Cory",
lastName:"House"
}
}
```

### dispatcher

1. Central hub,the dispatcher is an singleton

是一个单例模式，因此每个程序只有一个dispatcher.

2. Hold list of callbacks
3. broadcast payloads to registered callbacks
4. sends actions to stores

stores register with the dispatcher so that they can be notified when data changes.

## sotre

1. hold app state, logic,data retrieval
2. not a model - contains models
3. one or many sotres in your app
4. registers callbacks with dispatcher(store get updated)
5. uses node's Eventemitter

Remember,the flux dispatcher keeps track of all the stores that wuold like to be notified when a specific action occurs in your app.

when stores update,they emit a change evtnt so react gets the new data

**the structure of a store**

every store has these commom traits (aka interface)

1. Extend eventemitter
2. addChangeListener and removeChangeListener
3. emitChange

![Xnip2020-05-09_12-20-36](/Users/chenruo/Desktop/Xnip2020-05-09_12-20-36.jpg)

## controller views(components)

1. top level component
2. interacts with stores
3. holds data instate
4. sends data to children as props
5. Avoid nesting controller views

![Xnip2020-05-09_17-23-47](/Users/chenruo/Desktop/Xnip2020-05-09_17-23-47.jpg)



1. Action: user clicked "save user button"...

2. Send action payload:payload sent to dispatcher
3. Dispatcher: checks for registered callbacks
4. send action payload: sends payload to all registered callbacks
5. store: receives payload
6. updates storage and fires change event:store updates and emits change event
7. React:receives change event and re-renders

![Xnip2020-05-09_17-29-44](/Users/chenruo/Desktop/Xnip2020-05-09_17-29-44.jpg)

## flux api

![Xnip2020-05-09_17-31-52](/Users/chenruo/Desktop/Xnip2020-05-09_17-31-52.jpg)

waitFor 是一种按特定顺序运行回调的方法。如果同时在flux中注册了多个回调，那么你可能希望以某种顺序调用它们。此api允许你指定在继续执行当前回调之前应完成的回调。

This API allows you to specify the callbacks that should be completed before continuing execution of the current callback. The registered callback that you'd like to wait for is specified by passing the dispatch token of the callback that you'd like to wait for to the waitFor function.

该API允许您指定在继续执行当前回调之前应完成的回调。 您想要等待的已注册回调是通过将您要等待的回调的调度令牌传递给waitFor函数来指定的。

isDispatching() 是一个布尔值，当dispatcher is buzy dispatching things.其值为true.

![Xnip2020-05-09_17-49-32](/Users/chenruo/Desktop/Xnip2020-05-09_17-49-32.jpg)

















