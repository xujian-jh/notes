# [DOM] (Document Object Model)

## Abstract

- DOM defines a platform-neutral model for events, aborting activities, and node trees.

## Table of Contents

- 1 Infrastructure
  - 1.1 Trees
  - 1.2 Ordered sets
  - 1.3 Selectors
  - 1.4 Namespaces
- 2 Events
  - 2.1 Introduction to "DOM Events"
  - 2.2 Interface Event
  - 2.3 Legacy extensions to the Window interface
  - 2.4 Interface CustomEvent
  - 2.5 Constructing events
  - 2.6 Defining event interfaces
  - 2.7 Interface EventTarget
  - 2.8 Observing event listeners
  - 2.9 Dispatching events
  - 2.10 Firing events
  - 2.11 Action versus occurrence
- 3 Aborting ongoing activities
  - 3.1 Interface AbortController
  - 3.2 Interface AbortSignal
  - 3.3 Using AbortController and AbortSignal objects in APIs
- 4 Nodes
  - 4.1 Introduction to "The DOM"
  - 4.2 Node tree
    - 4.2.1 Document tree
    - 4.2.2 Shadow tree
      - 4.2.2.1 Slots
      - 4.2.2.2 Slotables
      - 4.2.2.3 Finding slots and slotables
      - 4.2.2.4 Assigning slotables and slots
      - 4.2.2.5 Signaling slot change
    - 4.2.3 Mutation algorithms
    - 4.2.4 Mixin NonElementParentNode
    - 4.2.5 Mixin DocumentOrShadowRoot
    - 4.2.6 Mixin ParentNode
    - 4.2.7 Mixin NonDocumentTypeChildNode
    - 4.2.8 Mixin ChildNode
    - 4.2.9 Mixin Slotable
    - 4.2.10 Old-style collections: NodeList and HTMLCollection
      - 4.2.10.1 Interface NodeList
      - 4.2.10.2 Interface HTMLCollection
  - 4.3 Mutation observers
    - 4.3.1 Interface MutationObserver
    - 4.3.2 Queuing a mutation record
    - 4.3.3 Interface MutationRecord
    - 4.3.4 Garbage collection
  - 4.4 Interface Node
  - 4.5 Interface Document
    - 4.5.1 Interface DOMImplementation
  - 4.6 Interface DocumentType
  - 4.7 Interface DocumentFragment
  - 4.8 Interface ShadowRoot
  - 4.9 Interface Element
    - 4.9.1 Interface NamedNodeMap
    - 4.9.2 Interface Attr
  - 4.10 Interface CharacterData
  - 4.11 Interface Text
  - 4.12 Interface CDATASection
  - 4.13 Interface ProcessingInstruction
  - 4.14 Interface Comment
- 5 Ranges
  - 5.1 Introduction to "DOM Ranges"
  - 5.2 Boundary points
  - 5.3 Interface AbstractRange
  - 5.4 Interface StaticRange
  - 5.5 Interface Range
- 6 Traversal
  - 6.1 Interface NodeIterator
  - 6.2 Interface TreeWalker
  - 6.3 Interface NodeFilter
- 7 Sets
  - 7.1 Interface DOMTokenList
- 8 Historical
  - 8.1 DOM Events
  - 8.2 DOM Core
  - 8.3 DOM Ranges
  - 8.4 DOM Traversal

---

[DOM]:https://dom.spec.whatwg.org/
