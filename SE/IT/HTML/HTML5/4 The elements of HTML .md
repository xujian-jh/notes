# 4 The elements of HTML

## 4.1 The document element

### 4.1.1 The html element

- Authors are encouraged to specify a lang attribute on the root html element, giving the document's language.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <title>Swapping Songs</title>
</head>

<body>
  <h1>Swapping Songs</h1>
  <p>Tonight I swapped some of the songs I wrote with some friends, who gave me some of the songs they wrote. I love sharing my music.</p>
</body>

</html>
```

4.2 Document metadata

4.2.1 The head element

4.2.2 The title element

4.2.3 The base element

4.2.4 The link element

4.2.4.1 Processing the media attribute

4.2.4.2 Processing the type attribute

4.2.4.3 Fetching and processing a resource from a link element

4.2.4.4 Processing `Link` headers

4.2.4.5 Providing users with a means to follow hyperlinks created using the link element

4.2.5 The meta element

4.2.5.1 Standard metadata names

4.2.5.2 Other metadata names

4.2.5.3 Pragma directives

4.2.5.4 Specifying the document's character encoding

4.2.6 The style element

4.2.7 Interactions of styling and scripting

4.3 Sections

4.3.1 The body element

4.3.2 The article element

4.3.3 The section element

4.3.4 The nav element

4.3.5 The aside element

4.3.6 The h1, h2, h3, h4, h5, and h6 elements

4.3.7 The hgroup element

4.3.8 The header element

4.3.9 The footer element

4.3.10 The address element

4.3.11 Headings and sections

4.3.11.1 Creating an outline

4.3.11.2 Sample outlines

4.3.11.3 Exposing outlines to users

4.3.12 Usage summary

4.3.12.1 Article or section?

4.4 Grouping content

4.4.1 The p element

4.4.2 The hr element

4.4.3 The pre element

4.4.4 The blockquote element

4.4.5 The ol element

4.4.6 The ul element

4.4.7 The menu element

4.4.8 The li element

4.4.9 The dl element

4.4.10 The dt element

4.4.11 The dd element

4.4.12 The figure element

4.4.13 The figcaption element

4.4.14 The main element

4.4.15 The div element

4.5 Text-level semantics

4.5.1 The a element

4.5.2 The em element

4.5.3 The strong element

4.5.4 The small element

4.5.5 The s element

4.5.6 The cite element

4.5.7 The q element

4.5.8 The dfn element

4.5.9 The abbr element

4.5.10 The ruby element

4.5.11 The rt element

4.5.12 The rp element

4.5.13 The data element

4.5.14 The time element

4.5.15 The code element

4.5.16 The var element

4.5.17 The samp element

4.5.18 The kbd element

4.5.19 The sub and sup elements

4.5.20 The i element

4.5.21 The b element

4.5.22 The u element

4.5.23 The mark element

4.5.24 The bdi element

4.5.25 The bdo element

4.5.26 The span element

4.5.27 The br element

4.5.28 The wbr element

4.5.29 Usage summary

4.6 Links

4.6.1 Introduction

4.6.2 Links created by a and area elements

4.6.3 API for a and area elements

4.6.4 Following hyperlinks

4.6.5 Downloading resources

4.6.5.1 Hyperlink auditing

4.6.6 Link types

4.6.6.1 Link type "alternate"

4.6.6.2 Link type "author"

4.6.6.3 Link type "bookmark"

4.6.6.4 Link type "canonical"

4.6.6.5 Link type "dns-prefetch"

4.6.6.6 Link type "external"

4.6.6.7 Link type "help"

4.6.6.8 Link type "icon"

4.6.6.9 Link type "license"

4.6.6.10 Link type "modulepreload"

4.6.6.11 Link type "nofollow"

4.6.6.12 Link type "noopener"

4.6.6.13 Link type "noreferrer"

4.6.6.14 Link type "opener"

4.6.6.15 Link type "pingback"

4.6.6.16 Link type "preconnect"

4.6.6.17 Link type "prefetch"

4.6.6.18 Link type "preload"

4.6.6.19 Link type "prerender"

4.6.6.20 Link type "search"

4.6.6.21 Link type "stylesheet"

4.6.6.22 Link type "tag"

4.6.6.23 Sequential link types

4.6.6.23.1 Link type "next"

4.6.6.23.2 Link type "prev"

4.6.6.24 Other link types

4.7 Edits

4.7.1 The ins element

4.7.2 The del element

4.7.3 Attributes common to ins and del elements

4.7.4 Edits and paragraphs

4.7.5 Edits and lists

4.7.6 Edits and tables

4.8 Embedded content

4.8.1 The picture element

4.8.2 The source element

4.8.3 The img element

4.8.4 Images

4.8.4.1 Introduction

4.8.4.1.1 Adaptive images

4.8.4.2 Attributes common to source, img, and link elements

4.8.4.2.1 Srcset attributes

4.8.4.2.2 Sizes attributes

4.8.4.3 Processing model

4.8.4.3.1 When to obtain images

4.8.4.3.2 Reacting to DOM mutations

4.8.4.3.3 The list of available images

4.8.4.3.4 Decoding images

4.8.4.3.5 Updating the image data

4.8.4.3.6 Selecting an image source

4.8.4.3.7 Updating the source set

4.8.4.3.8 Parsing a srcset attribute

4.8.4.3.9 Parsing a sizes attribute

4.8.4.3.10 Normalizing the source densities

4.8.4.3.11 Reacting to environment changes

4.8.4.4 Requirements for providing text to act as an alternative for images

4.8.4.4.1 General guidelines

4.8.4.4.2 A link or button containing nothing but the image

4.8.4.4.3 A phrase or paragraph with an alternative graphical representation: charts, diagrams, graphs, maps, 
illustrations

4.8.4.4.4 A short phrase or label with an alternative graphical representation: icons, logos

4.8.4.4.5 Text that has been rendered to a graphic for typographical effect

4.8.4.4.6 A graphical representation of some of the surrounding text

4.8.4.4.7 Ancillary images

4.8.4.4.8 A purely decorative image that doesn't add any information

4.8.4.4.9 A group of images that form a single larger picture with no links

4.8.4.4.10 A group of images that form a single larger picture with links

4.8.4.4.11 A key part of the content

4.8.4.4.12 An image not intended for the user

4.8.4.4.13 An image in an e-mail or private document intended for a specific person who is known to be able to view 
images

4.8.4.4.14 Guidance for markup generators

4.8.4.4.15 Guidance for conformance checkers

4.8.5 The iframe element

4.8.6 The embed element

4.8.7 The object element

4.8.8 The param element

4.8.9 The video element

4.8.10 The audio element

4.8.11 The track element

4.8.12 Media elements

4.8.12.1 Error codes

4.8.12.2 Location of the media resource

4.8.12.3 MIME types

4.8.12.4 Network states

4.8.12.5 Loading the media resource

4.8.12.6 Offsets into the media resource

4.8.12.7 Ready states

4.8.12.8 Playing the media resource

4.8.12.9 Seeking

4.8.12.10 Media resources with multiple media tracks

4.8.12.10.1 AudioTrackList and VideoTrackList objects

4.8.12.10.2 Selecting specific audio and video tracks declaratively

4.8.12.11 Timed text tracks

4.8.12.11.1 Text track model

4.8.12.11.2 Sourcing in-band text tracks

4.8.12.11.3 Sourcing out-of-band text tracks

4.8.12.11.4 Guidelines for exposing cues in various formats as text track cues

4.8.12.11.5 Text track API

4.8.12.11.6 Event handlers for objects of the text track APIs

4.8.12.11.7 Best practices for metadata text tracks

4.8.12.12 Identifying a track kind through a URL

4.8.12.13 User interface

4.8.12.14 Time ranges

4.8.12.15 The TrackEvent interface

4.8.12.16 Events summary

4.8.12.17 Security and privacy considerations

4.8.12.18 Best practices for authors using media elements

4.8.12.19 Best practices for implementers of media elements

4.8.13 The map element

4.8.14 The area element

4.8.15 Image maps

4.8.15.1 Authoring

4.8.15.2 Processing model

4.8.16 MathML

4.8.17 SVG

4.8.18 Dimension attributes

4.9 Tabular data

4.9.1 The table element

4.9.1.1 Techniques for describing tables

4.9.1.2 Techniques for table design

4.9.2 The caption element

4.9.3 The colgroup element

4.9.4 The col element

4.9.5 The tbody element

4.9.6 The thead element

4.9.7 The tfoot element

4.9.8 The tr element

4.9.9 The td element

4.9.10 The th element

4.9.11 Attributes common to td and th elements

4.9.12 Processing model

4.9.12.1 Forming a table

4.9.12.2 Forming relationships between data cells and header cells

4.9.13 Examples

4.10 Forms

4.10.1 Introduction

4.10.1.1 Writing a form's user interface

4.10.1.2 Implementing the server-side processing for a form

4.10.1.3 Configuring a form to communicate with a server

4.10.1.4 Client-side form validation

4.10.1.5 Enabling client-side automatic filling of form controls

4.10.1.6 Improving the user experience on mobile devices

4.10.1.7 The difference between the field type, the autofill field name, and the input modality

4.10.1.8 Date, time, and number formats

4.10.2 Categories

4.10.3 The form element

4.10.4 The label element

4.10.5 The input element

4.10.5.1 States of the type attribute

4.10.5.1.1 Hidden state (type=hidden)

4.10.5.1.2 Text (type=text) state and Search state (type=search)

4.10.5.1.3 Telephone state (type=tel)

4.10.5.1.4 URL state (type=url)

4.10.5.1.5 E-mail state (type=email)

4.10.5.1.6 Password state (type=password)

4.10.5.1.7 Date state (type=date)

4.10.5.1.8 Month state (type=month)

4.10.5.1.9 Week state (type=week)

4.10.5.1.10 Time state (type=time)

4.10.5.1.11 Local Date and Time state (type=datetime-local)

4.10.5.1.12 Number state (type=number)

4.10.5.1.13 Range state (type=range)

4.10.5.1.14 Color state (type=color)

4.10.5.1.15 Checkbox state (type=checkbox)

4.10.5.1.16 Radio Button state (type=radio)

4.10.5.1.17 File Upload state (type=file)

4.10.5.1.18 Submit Button state (type=submit)

4.10.5.1.19 Image Button state (type=image)

4.10.5.1.20 Reset Button state (type=reset)

4.10.5.1.21 Button state (type=button)

4.10.5.2 Implementation notes regarding localization of form controls

4.10.5.3 Common input element attributes

4.10.5.3.1 The maxlength and minlength attributes

4.10.5.3.2 The size attribute

4.10.5.3.3 The readonly attribute

4.10.5.3.4 The required attribute

4.10.5.3.5 The multiple attribute

4.10.5.3.6 The pattern attribute

4.10.5.3.7 The min and max attributes

4.10.5.3.8 The step attribute

4.10.5.3.9 The list attribute

4.10.5.3.10 The placeholder attribute

4.10.5.4 Common input element APIs

4.10.5.5 Common event behaviors

4.10.6 The button element

4.10.7 The select element

4.10.8 The datalist element

4.10.9 The optgroup element

4.10.10 The option element

4.10.11 The textarea element

4.10.12 The output element

4.10.13 The progress element

4.10.14 The meter element

4.10.15 The fieldset element

4.10.16 The legend element

4.10.17 Form control infrastructure

4.10.17.1 A form control's value

4.10.17.2 Mutability

4.10.17.3 Association of controls and forms

4.10.18 Attributes common to form controls

4.10.18.1 Naming form controls: the name attribute

4.10.18.2 Submitting element directionality: the dirname attribute

4.10.18.3 Limiting user input length: the maxlength attribute

4.10.18.4 Setting minimum input length requirements: the minlength attribute

4.10.18.5 Enabling and disabling form controls: the disabled attribute

4.10.18.6 Form submission

4.10.18.6.1 Autofocusing a form control: the autofocus attribute

4.10.18.7 Autofill

4.10.18.7.1 Autofilling form controls: the autocomplete attribute

4.10.18.7.2 Processing model

4.10.19 APIs for the text control selections

4.10.20 Constraints

4.10.20.1 Definitions

4.10.20.2 Constraint validation

4.10.20.3 The constraint validation API

4.10.20.4 Security

4.10.21 Form submission

4.10.21.1 Introduction

4.10.21.2 Implicit submission

4.10.21.3 Form submission algorithm
4.10.21.4 Constructing the entry list

4.10.21.5 Selecting a form submission encoding

4.10.21.6 URL-encoded form data

4.10.21.7 Multipart form data

4.10.21.8 Plain text form data

4.10.21.9 The FormDataEvent interface

4.10.22 Resetting a form

4.11 Interactive elements

4.11.1 The details element

4.11.2 The summary element

4.11.3 Commands

4.11.3.1 Facets

4.11.3.2 Using the a element to define a command

4.11.3.3 Using the button element to define a command

4.11.3.4 Using the input element to define a command

4.11.3.5 Using the option element to define a command

4.11.3.6 Using the accesskey attribute on a legend element to define a command

4.11.3.7 Using the accesskey attribute to define a command on other elements

4.11.4 The dialog element

4.12 Scripting

4.12.1 The script element

4.12.1.1 Processing model

4.12.1.2 Scripting languages

4.12.1.3 Restrictions for contents of script elements

4.12.1.4 Inline documentation for external scripts

4.12.1.5 Interaction of script elements and XSLT

4.12.2 The noscript element

4.12.3 The template element
4.12.3.1 Interaction of template elements with XSLT and XPath

4.12.4 The slot element

4.12.5 The canvas element
4.12.5.1 The 2D rendering context

4.12.5.1.1 Implementation notes

4.12.5.1.2 The canvas state
4.12.5.1.3 Line styles

4.12.5.1.4 Text styles

4.12.5.1.5 Building paths

4.12.5.1.6 Path2D objects

4.12.5.1.7 Transformations

4.12.5.1.8 Image sources for 2D rendering contexts

4.12.5.1.9 Fill and stroke styles

4.12.5.1.10 Drawing rectangles to the bitmap

4.12.5.1.11 Drawing text to the bitmap

4.12.5.1.12 Drawing paths to the canvas

4.12.5.1.13 Drawing focus rings and scrolling paths into view

4.12.5.1.14 Drawing images

4.12.5.1.15 Pixel manipulation

4.12.5.1.16 Compositing

4.12.5.1.17 Image smoothing

4.12.5.1.18 Shadows

4.12.5.1.19 Filters

4.12.5.1.20 Working with externally-defined SVG filters

4.12.5.1.21 Drawing model

4.12.5.1.22 Best practices

4.12.5.1.23 Examples

4.12.5.2 The ImageBitmap rendering context

4.12.5.2.1 Introduction

4.12.5.2.2 The ImageBitmapRenderingContext interface

4.12.5.3 The OffscreenCanvas interface

4.12.5.3.1 The offscreen 2D rendering context

4.12.5.4 Color spaces and color correction

4.12.5.5 Serializing bitmaps to a file

4.12.5.6 Security with canvas elements

4.13 Custom elements

4.13.1 Introduction

4.13.1.1 Creating an autonomous custom element

4.13.1.2 Creating a form-associated custom element

4.13.1.3 Creating a customized built-in element

4.13.1.4 Drawbacks of autonomous custom elements

4.13.1.5 Upgrading elements after their creation

4.13.2 Requirements for custom element constructors and reactions

4.13.3 Core concepts

4.13.4 The CustomElementRegistry interface

4.13.5 Upgrades

4.13.6 Custom element reactions

4.13.7 The ElementInternals interface

4.14 Common idioms without dedicated elements

4.14.1 Bread crumb navigation

4.14.2 Tag clouds

4.14.3 Conversations

4.14.4 Footnotes

4.15 Disabled elements

4.16 Matching HTML elements using selectors and CSS

4.16.1 Case-sensitivity of the CSS 'attr()' function

4.16.2 Case-sensitivity of selectors

4.16.3 Pseudo-classes