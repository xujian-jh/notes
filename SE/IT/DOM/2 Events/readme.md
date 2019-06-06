# 2 Events

## 2.1 Introduction to "DOM Events"

- Throughout the web platform events are dispatched to objects to signal an occurrence, such as network activity or user interaction.
- add event listeners to observe events by calling `addEventListener()`
  - Event listeners can be removed by utilizing the `removeEventListener()` method, passing the same arguments.
- Events are objects too and implement the Event interface (or a derived interface).

```js
// add an appropriate event listener
obj.addEventListener("cat", function(e) { process(e.detail) })

// create and dispatch the event
var event = new CustomEvent("cat", {"detail":{"hazcheeseburger":true}})
obj.dispatchEvent(event)
```

## 2.2 Interface Event

```js
event = new Event(type [, eventInitDict])
// Returns a new event whose type attribute value is set to type. The eventInitDict argument allows for setting the bubbles and cancelable attributes via object members of the same name.
event . type
// Returns the type of event, e.g. "click", "hashchange", or "submit".
event . target
// Returns the object to which event is dispatched (its target).
event . currentTarget
// Returns the object whose event listener’s callback is currently being invoked.
event . composedPath()
// Returns the invocation target objects of event’s path (objects on which listeners will be invoked), except for any nodes in shadow trees of which the shadow root’s mode is "closed" that are not reachable from event’s currentTarget.
event . eventPhase
// Returns the event’s phase, which is one of NONE, CAPTURING_PHASE, AT_TARGET, and BUBBLING_PHASE.
event . stopPropagation()
// When dispatched in a tree, invoking this method prevents event from reaching any objects other than the current object.
event . stopImmediatePropagation()
// Invoking this method prevents event from reaching any registered event listeners after the current one finishes running and, when dispatched in a tree, also prevents event from reaching any other objects.
event . bubbles
// Returns true or false depending on how event was initialized. True if event goes through its target’s ancestors in reverse tree order, and false otherwise.
event . cancelable
// Returns true or false depending on how event was initialized. Its return value does not always carry meaning, but true can indicate that part of the operation during which event was dispatched, can be canceled by invoking the preventDefault() method.
event . preventDefault()
// If invoked when the cancelable attribute value is true, and while executing a listener for the event with passive set to false, signals to the operation that caused event to be dispatched that it needs to be canceled.
event . defaultPrevented
// Returns true if preventDefault() was invoked successfully to indicate cancelation, and false otherwise.
event . composed
// Returns true or false depending on how event was initialized. True if event invokes listeners past a ShadowRoot node that is the root of its target, and false otherwise.
event . isTrusted
// Returns true if event was dispatched by the user agent, and false otherwise.
event . timeStamp
// Returns the event’s timestamp as the number of milliseconds measured relative to the time origin.
```

## 2.3 Legacy extensions to the Window interface

- This attribute is not available in workers or worklets, and is inaccurate for events dispatched in shadow trees.
  - Web developers are strongly encouraged to instead rely on the Event object passed to event listeners, as that will result in more portable code.

## 2.4 Interface CustomEvent

- Events using the CustomEvent interface can be used to carry custom data.

```js
event = new CustomEvent(type [, eventInitDict])
// Works analogously to the constructor for Event except that the eventInitDict argument now allows for setting the detail attribute too.
event . detail
// Returns any custom data event was created with. Typically used for synthetic events.
```

## 2.5 [Constructing events](https://dom.spec.whatwg.org/#constructing-events)

## 2.6 Defining event interfaces

## 2.7 Interface EventTarget

## 2.8 Observing event listeners

## 2.9 Dispatching events

## 2.10 Firing events

## 2.11 Action versus occurrence
