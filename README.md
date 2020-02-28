# Page Objects and Data-driven Testing

This chapter introduces two important design patterns that are useful in creating
scalable and maintainable test automation framework designs. We will explore
how to use the data-driven approach to create data-driven Selenium tests using
Python libraries.
In the second part of this chapter, you will learn about using the page object pattern
to create highly maintainable and robust tests by separating locators and other
low-level calls from the test cases into a layer of abstraction, which resembles the
functionality of the application similar to what the user experiences within the
browser window.

In this chapter, you will learn:
- What data-driven testing is
- How to use the Data-driven testing (ddt) library along with the unittest
library to create data-driven tests
- How to read data from external sources for data-driven testing
- What the page object pattern is and how it helps in creating a maintainable
test suite
- How to implement the page object pattern for the sample application


## Page Object Model (POM)

![POM_Image](/screenshots/pom_image.png)

### What is POM?

Page Object Model is a design pattern which has become popular in test automation for enhancing test maintenance and reducing code duplication. A page object is an object-oriented class that serves as an interface to a page of your AUT.

The tests then use the methods of this page object class whenever they need to interact with the UI of that page, the benefit is that if the UI changes for the page, the tests themselves don’t need to be changed, only the code within the page object needs to change.

Subsequently all changes to support that new UI are located in one place.

### Why we need POM?
Increasing automation test coverage can result in unmaintainable project structure, if locators are not managed in right way. This can happen due to duplication of code or mainly due to duplicated usage of locators.

For Example, in home page of web application we have menu bar which leads to different modules with different features.

Many automation test cases would be clicking through these menu buttons to execute specific tests. Imagine that the UI is changed/revamped and menu buttons are relocated to different position in home page, this will result automation tests to fail. Automated test cases will fail as scripts will not be able to find particular element-locators to perform action.

Now, QA Engineer need to walk through whole code to update locators where necessary. Updating element-locators in duplicated code will consume a lot of time to only adjust locators, while this time can be consumed to increase test coverage. We can save this time by using Page Object Model in our test automation framework.

### Advantages of Page Object Model:

1. According to Page Object Model, we should keep our tests and element locators separately, this will keep code clean and easy to understand and maintain.
2. The Page Object approach makes test automation framework programmer friendly, more durable and comprehensive.
3. Another important advantage is our Page Object Repository is Independent of Automation Tests. Keeping separate repository for page objects helps us to use this repository for different purposes with different frameworks like, we are able to integrate this repository with other tools like JUnit/NUnit/PhpUnit as well as with TestNG/Cucumber/etc.
4. Test cases become short and optimized as we are able to reuse page object methods in the POM classes.
5. Any change in UI can easily be implemented, updated and maintained into the Page Objects and Classes.

### The page objects pattern
Until now, we were writing Selenium WebDriver tests directly into Python classes using pytest. We were specifying locators and test case steps into these classes. This code is good to start; however, as we progress on, adding more and more tests
to our tests suite, it will become difficult to maintain. This will make tests brittle.

Developing maintainable and reusable test code is important for sustainable test
automation and the test code should be treated as production code and similar
standards and patterns should to be applied while developing the test code.

To overcome these problems, we can use various design patterns and principles such
as Don't Repeat Yourself (DRY), and code refactoring techniques while creating the
tests. If you're a developer, you might already be using these techniques.

The page object pattern is one of the highly used patterns among the Selenium user
community to structure the tests, making them separate from low-level actions, and
providing a high-level abstraction. You can compare the page object pattern to the
facade pattern, which enables creating a simplified interface for complex code.

The page object pattern offers creating an object representing each web page
from the application under test. We can define classes for each page, modeling all
attributes and actions for that page. This creates a layer of separation between the
test code and technical implementation of pages and application functionality that
we will be testing, by hiding the locators, low-level methods dealing with elements,
and business functionality. Instead, the page objects will provide a high-level API for
tests to deal with the page functionality.

Tests should use these page objects at a high level, where any change in attributes
or actions in the underlying page should not break the test. Using the page object
pattern provides the following benefits:
- Creating a high-level abstraction that helps minimize changes when the
underlying page is modified by developers. So, you will change only the
page object and the calling tests will be unaffected.
- Creating reusable code that can be shared across multiple test cases.
- Tests are more readable, flexible, and maintainable.

Let's start refactoring the test that we created in the earlier chapter and implement
the page objects that provide a high-level abstraction for the application that we
are testing. In this example, we will create the following structure for the selected
pages in the sample application. We will start implementing a base page object,
which will be used by all other pages as a template. The base object will also provide
regions that are blocks of functionality available for all other pages; for example, the
search feature is available on all pages of the application. We will create a search
region object that will be available for all the pages inherited from the base page. We
will implement a class for the home page, which represents the home page of the
application; search results page, which shows the list of products matching with the
search criteria; and a product page, which provides attributes and actions related to
a product. We will create a structure as shown in the following diagram:

![pom_implementation](/screenshots/pom_basepage.png)

### References:
- [Page Object Model (POM), Design Pattern - php example](https://medium.com/tech-tajawal/page-object-model-pom-design-pattern-f9588630800b)
- [Page Object Model (POM) & Page Factory - Java example](https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.ht)
- [Selenium's Page Object Pattern: The Key to Maintainable Tests- Python example](https://justin.abrah.ms/python/selenium-page-object-pattern--the-key-to-maintainable-tests.html)
- [Previous Project with 2019-spring class](https://github.com/2019-spring/pytest-bdd-web)
