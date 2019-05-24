# 1 Introduction

## 1.1 This specification defines a big part of the Web platform, in lots of detail

## 1.2 This is HTML5

## 1.3 HTML is the World Wide Web's core markup language

## 1.4 Audience

In particular, familiarity with the basics of DOM is necessary for a complete understanding of some of the more technical parts of this specification.

An understanding of Web IDL, HTTP, XML, Unicode, character encodings, JavaScript, and CSS will also be helpful in places but is not essential.

## 1.5 Scope

This specification is limited to providing a semantic-level markup language and associated semantic-level scripting APIs for authoring accessible pages on the Web ranging from static documents to dynamic applications.

## 1.6 History

For its first five years (1990-1995), HTML went through a number of revisions and experienced a number of extensions, primarily hosted first at CERN, and then at the IETF.

With the creation of the W3C, HTML's development changed venue again. A first abortive attempt at extending HTML in 1995 known as HTML 3.0 then made way to a more pragmatic approach known as HTML 3.2, which was completed in 1997. HTML4 quickly followed later that same year.

In 1998, the W3C membership decided to stop evolving HTML and instead begin work on an XML-based equivalent, called XHTML.

In 2004, Apple, Mozilla, and Opera jointly announced their intent to continue working on the effort under the umbrella of a new venue called the WHATWG.

The WHATWG was based on several core principles, in particular that technologies need to be backwards compatible, that specifications and implementations need to match even if this means changing the specification rather than the implementations, and that specifications need to be detailed enough that implementations can achieve complete interoperability without reverse-engineering each other.

In 2006, the W3C indicated an interest to participate in the development of HTML5 after all, and in 2007 formed a working group chartered to work with the WHATWG on the development of the HTML5 specification. Apple, Mozilla, and Opera allowed the W3C to publish the specification under the W3C copyright, while keeping a version with the less restrictive license on the WHATWG site.

In 2011, however, the groups came to the conclusion that they had different goals: the W3C wanted to publish a "finished" version of "HTML5", while the WHATWG wanted to continue working on a Living Standard for HTML, continuously maintaining the specification rather than freezing it in a state with known problems, and adding new features as needed to evolve the platform.

Since then, the WHATWG has been working on this specification (amongst others), and the W3C has been copying fixes made by the WHATWG into their fork of the document (which also has other changes).

## 1.7 Design notes

### 1.7.1 Serializability of script execution

To avoid exposing Web authors to the complexities of multithreading, the HTML and DOM APIs are designed such that no script can ever detect the simultaneous execution of other scripts.

Even with workers, the intent is that the behavior of implementations can be thought of as completely serializing the execution of all scripts in all browsing contexts.

The exception to this general design principle is the JavaScript `SharedArrayBuffer` class.

Furthermore, due to the JavaScript memory model, there are situations which not only are un-representable via serialized script execution, but also un-representable via serialized statement execution among those scripts.

### 1.7.2 Compliance with other specifications

This specification interacts with and relies on a wide variety of other specifications.

In certain circumstances, unfortunately, conflicting needs have led to this specification violating the requirements of these other specifications. Whenever this has occurred, the transgressions have each been noted as a "willful violation", and the reason for the violation has been noted.

### 1.7.3 Extensibility

HTML has a wide array of extensibility mechanisms that can be used for adding semantics in a safe manner:

- Authors can use the `class` attribute to extend elements, effectively creating their own elements, while using the most applicable existing "real" HTML element, so that browsers and other tools that don't know of the extension can still support it somewhat well. This is the tack used by microformats.
- Authors can include data for inline client-side scripts or server-side site-wide scripts to process using the `data-*=""` attributes. These are guaranteed to never be touched by browsers, and allow scripts to include data on HTML elements that scripts can then look for and process.
- Authors can use the `<meta name="" content="">` mechanism to include page-wide metadata.
- Authors can use the `rel=""` mechanism to annotate links with specific meanings by registering extensions to the predefined set of link types. This is also used by microformats.
- Authors can embed raw data using the `<script type="">` mechanism with a custom type, for further handling by inline or server-side scripts.
- Authors can create plugins and invoke them using the `embed` element. This is how Flash works.
- Authors can extend APIs using the JavaScript prototyping mechanism. This is widely used by script libraries, for instance.
- Authors can use the microdata feature (the `itemscope=""` and `itemprop=""` attributes) to embed nested name-value pairs of data to be shared with other applications and sites.

## 1.8 HTML vs XML syntax

## 1.9 Structure of this specification

### 1.9.1 How to read this specification

First, it should be read cover-to-cover, multiple times.

Then, it should be read backwards at least once.

Then it should be read by picking random sections from the contents list and following all the cross-references.

### 1.9.2 Typographic conventions

## 1.10 Privacy concerns

### 1.10.1 Cross-site communication

## 1.11 A quick introduction to HTML

```html
<!DOCTYPE html>
<html lang="en">
 <head>
  <title>Sample page</title>
 </head>
 <body>
  <h1>Sample page</h1>
  <p>This is a <a href="demo.html">simple</a> sample.</p>
  <!-- this is a comment -->
 </body>
</html>
```

A DOM (Document Object Model) tree is an in-memory representation of a document.

DOM trees contain several kinds of nodes, in particular a DocumentType node, Element nodes, Text nodes, Comment nodes, and in some cases ProcessingInstruction nodes.

```ps
├── DOCTYPE: html
└── html lang="en"
    ├── head
    │    ├── #text：⏎␣␣
    │    ├── title
    │    │    └── #text: Sample page
    │    └── #text: ⏎␣
    ├── #text: ⏎␣
    └── body
         ├── #text: ⏎␣␣
         ├── h1
         │    └── #text: Sample page
         ├── #text: ⏎␣␣
         ├── p
         │    ├── #text: This is a
         │    ├── a href="demo.html"
         │    │    └── #text: simple
         │    └── #text: sample.
         ├── #text: ⏎␣␣
         ├── #comment: this is a comment
         └── #text: ⏎␣⏎
```

- The source contains a number of spaces (represented here by "␣") and line breaks ("⏎") that all end up as Text nodes in the DOM.
- However, for historical reasons not all of the spaces and line breaks in the original markup appear in the DOM.
  - all the whitespace before head start tag ends up being dropped silently
  - all the whitespace after the body end tag ends up placed at the end of the body.

This DOM tree can be manipulated from scripts in the page. Scripts (typically in JavaScript) are small programs that can be embedded using the script element or using event handler content attributes.

```js
<form name="main">
 Result: <output name="result"></output>
 <script>
  document.forms.main.elements.result.value = 'Hello World';
 </script>
</form>
```

Each element in the DOM tree is represented by an object, and these objects have APIs so that they can be manipulated.

```js
var a = document.links[0]; // obtain the first link in the document
a.href = 'sample.html'; // change the destination URL of the link
a.protocol = 'https'; // change just the scheme part of the URL
a.setAttribute('href', 'https://example.com/'); // change the content attribute directly
```

HTML documents represent a media-independent description of interactive content. To influence exactly how such rendering takes place, authors can use a styling language such as CSS.

```html
<!DOCTYPE html>
<html lang="en">
 <head>
  <title>Sample styled page</title>
  <style>
   body { background: navy; color: yellow; }
  </style>
 </head>
 <body>
  <h1>Sample styled page</h1>
  <p>This page is just a demo.</p>
 </body>
</html>
```

### 1.11.1 Writing secure applications with HTML

The security model of the Web is based on the concept of "origins", and correspondingly many of the potential attacks on the Web involve cross-origin actions.

#### Not validating user input

#### Cross-site scripting (XSS)

#### SQL injection

#### Cross-site request forgery (CSRF)

#### Clickjacking

### 1.11.2 Common pitfalls to avoid when using the scripting APIs

### 1.11.3 How to catch mistakes when writing HTML: validators and conformance checkers

## 1.12 Conformance requirements for authors

### 1.12.1 Presentational markup

### 1.12.2 Syntax errors

### 1.12.3 Restrictions on content models and on attribute values

## 1.13 Suggested reading