# 2 Common infrastructure

## 2.1 Terminology

- This specification refers to both HTML and XML attributes and IDL attributes, often in the same context.
- Similarly, the term "properties" is used for both JavaScript object properties and CSS properties.

### 2.1.1 Parallelism

- To run steps in parallel means those steps are to be run, one after another, at the same time as other logic in the standard (e.g., at the same time as the event loop).
- By contrast, an operation that is to run immediately must interrupt the currently running task, run itself, and then resume the previously running task.

### 2.1.2 Resources

- The specification uses the term supported when referring to whether a user agent has an implementation capable of decoding the semantics of an external resource.

### 2.1.3 XML compatibility

- The term "HTML elements" refers to any element in the HTML namespace ("<https://www.w3.org/1999/xhtml>"), and all attributes defined or mentioned in this specification have no namespace.

### 2.1.4 DOM trees

- A content attribute is said to change value only if its new value is different than its previous value; setting an attribute to a value it already has does not change it.

### 2.1.5 Scripting

### 2.1.6 Plugins

### 2.1.7 Character encodings

### 2.1.8 Conformance classes

### 2.1.9 Dependencies

### 2.1.10 Extensibility

### 2.1.11 Interactions with XPath and XSLT

## 2.2 Case-sensitivity and string comparison

## 2.3 Policy-controlled features

2 Common infrastructure
