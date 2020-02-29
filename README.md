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

---
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

```python
class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

class Login(BasePage):
    # LOCATORS
    username_box = "//input[@id='username']"
    password_box = "//input[@id='password']"
```
----

### Basic Logging Tutorial
Logging is a means of tracking events that happen when some software runs. The software’s developer adds logging calls to their code to indicate that certain events have occurred. An event is described by a descriptive message which can optionally contain variable data (i.e. data that is potentially different for each occurrence of the event). Events also have an importance which the developer ascribes to the event; the importance can also be called the level or severity.

#### When to use logging
Logging provides a set of convenience functions for simple logging usage. These are debug(), info(), warning(), error() and critical(). To determine when to use logging, see the table below, which states, for each of a set of common tasks, the best tool to use for it.


| LEVEL   |      WHEN IT IS USED      |
|----------|:-------------|
| DEBUG |Detailed information, typically of interest only when diagnosing problems. |
| INFO |Confirmation that things are working as expected. |
| WARNING |An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.|
| ERROR | Due to a more serious problem, the software has not been able to perform some function.|
| CRITICAL | A serious error, indicating that the program itself may be unable to continue running. |

#### Logging to a file
A very common situation is that of recording logging events in a file, so let’s look at that next. Be sure to try the following in a newly-started Python interpreter, and don’t just continue from the session described above:

```python
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
```

And now if we open the file and look at what we have, we should find the log messages:
```python
DEBUG:root:This message should go to the log file
INFO:root:So should this
WARNING:root:And this, too
```
This example also shows how you can set the logging level which acts as the threshold for tracking. In this case, because we set the threshold to DEBUG, all of the messages were printed.

Find more about the logging [here.](https://docs.python.org/3.8/howto/logging.html#logging-basic-tutorial)

----
#### Runners

You can generate html reports with `pytest-html` and share your test reports or configure it in Jenkins reports.

To install pytest-html:

```
pip install pytest-html
```
Find more about pytest-html [here.](https://github.com/davehunt/pytest-html)

Create a `regression.bat` file under `runners` directory

```bat
cd ..
pytest -v -s -m tagname --html=./reports/htmlreport.html
pause
```
----
### Reading and Writing YAML to a File in Python


YAML stands for Yet Another Markup Language. In recent years it has become very popular for its use in storing data in a serialized manner for configuration files. Since YAML essentially is a data format, the YAML library is quite brief, as the only functionality required of it is the ability to parse YAML formatted files.

#### Installation

The easiest way to install the YAML library in Python is via the pip package manager.

```
$ pip install pyyaml
```
#### Reading YAML Files in Python

The contents of the first file are as follows:

    # fruits.yaml file

    apples: 20
    mangoes: 2
    bananas: 3
    grapes: 100
    pineapples: 1
The contents of the second file are as follows:

    # categories.yaml file

    sports:

    - soccer
    - football
    - basketball
    - cricket
    - hockey
    - table tennis

    countries:

    - Pakistan
    - USA
    - India
    - China
    - Germany
    - France
    - Spain

You can see that the fruits.yaml and categories.yaml files contain different types of data. The former contains information only about one entity, i.e. fruits, while the latter contains information about sports and countries.

Let's now try to read the data from the two files that we created using a Python script. The load() method from the yaml module can be used to read YAML files. Look at the following script:

    # process_yaml.py file

    import yaml

    with open(r'E:\data\fruits.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        fruits_list = yaml.load(file, Loader=yaml.FullLoader)

        print(fruits_list)
Output:

    { 'apples': 20, 'mangoes': 2, 'bananas': 3, 'grapes': 100, 'pineapples': 1 }

In the script above we specified yaml.FullLoader as the value for the Loader parameter which loads the full YAML language, avoiding the arbitrary code execution. Instead of using the load function and then passing yaml.FullLoader as the value for the Loader parameter, you can also use the full_load() function, as we will see in the next example.

Let's now try and read the second YAML file in a similar manner using a Python script:

    # read_categories.py file

    import yaml

    with open(r'E:\data\categories.yaml') as file:
        documents = yaml.full_load(file)

        for item, doc in documents.items():
            print(item, ":", doc)

Since there are 2 documents in the categories.yaml file, we ran a loop to read both of them.

Output:

    sports : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']
    countries : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']

As you can see from the last two examples, the library automatically handles the conversion of YAML formatted data to Python dictionaries and lists.

#### Writing YAML Files in Python
Now that we have learned how to convert a YAML file into a Python dictionary, let's try to do things the other way around i.e. serialize a Python dictionary and store it into a YAML formatted file. For this purpose, let's use the same dictionary that we got as an output from our last program.

    import yaml

    dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
    {'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

    with open(r'E:\data\store_file.yaml', 'w') as file:
        documents = yaml.dump(dict_file, file)

The dump() method takes the Python dictionary as the first, and a File object as the second parameter.

Once the above code executes, a file named store_file.yaml will be created in your current working directory.

    # store_file.yaml file contents:

    - sports:

    - soccer
    - football
    - basketball
    - cricket
    - hockey
    - table tennis
    - countries:

    - Pakistan
    - USA
    - India
    - China
    - Germany
    - France
    - Spain

Another useful functionality that the YAML library offers for the dump() method is the sort_keys parameter. To show what it does, let's apply it on our first file, i.e. fruits.yaml:

    import yaml

    with open(r'E:\data\fruits.yaml') as file:
        doc = yaml.load(file, Loader=yaml.FullLoader)

        sort_file = yaml.dump(doc, sort_keys=True)
        print(sort_file)

Output:

    apples: 20
    bananas: 3
    grapes: 100
    mangoes: 2
    pineapples: 1

You can see in the output that the fruits have been sorted in the alphabetical order.

#### Conclusion
In this brief tutorial, we learned how to install Python's YAML library (pyyaml) to manipulate YAML formatted files. We covered loading the contents of a YAML file into our Python program as dictionaries, as well as serializing Python dictionaries in to YAML files and storing their keys. The library is quite brief and only offers basic functionalities.

Find out more about YAML [here.](https://yaml.org/)

----

### References:
- [Page Object Model (POM), Design Pattern - php example](https://medium.com/tech-tajawal/page-object-model-pom-design-pattern-f9588630800b)
- [Page Object Model (POM) & Page Factory - Java example](https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.ht)
- [Selenium's Page Object Pattern: The Key to Maintainable Tests- Python example](https://justin.abrah.ms/python/selenium-page-object-pattern--the-key-to-maintainable-tests.html)
- [Previous Project with 2019-spring class](https://github.com/2019-spring/pytest-bdd-web)
