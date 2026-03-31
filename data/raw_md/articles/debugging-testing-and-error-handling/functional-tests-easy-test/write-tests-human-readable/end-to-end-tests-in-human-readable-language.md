---
uid: "403965"
title: 'End-to-End Tests in Human Readable Language'
seealso:
- linkType: HRef
  linkId: 'https://supportcenter.devexpress.com/ticket/details/t844058/easytest-how-to-integrate-xaf-functional-testing-with-continuous-integration-systems'
  altText: EasyTest - How to integrate XAF functional testing with Continuous Integration systems like Azure DevOps
- linkType: HRef
  linkId: 'https://supportcenter.devexpress.com/ticket/details/t752621/easytest-syntax-highlighting-collapsible-regions-and-code-snippets-in-functional-test'
  altText: EasyTest - Syntax highlighting, collapsible regions, and code snippets in functional test files (*.ets, *.inc) opened with Notepad++ and Visual Studio Code
---
# End-to-End Tests in Human Readable Language

This topic describes the basics of using EasyTest, and the components it comprises. For step-by-step instructions on how to test your XAF applications, refer to the [Test an Action](xref:113218) topic.

## Add EasyTest to Your Project

Refer to the following articles for information on how to integrate EasyTest functional tests to your XAF projects:

- [Integrate EasyTest into XAF WinForms Applications](xref:403492)
- [Integrate EasyTest into XAF Blazor UI Applications](xref:403393)
- [EasyTest Configuration](xref:113209)

## Create a Test

### Write Tests in Human-Readable Language

Add a new text file to your project, change the file extension to `*.ets`, and enter a test script in it. Refer to the following topic for a list of available script commands: [EasyTest Script Reference](xref:113208).

The following code snippet demonstrates a sample test added to a newly created XAF application

# [sample.ets](#tab/tabid-ets)
    
```ETS
#DropDB DBName 
#Application BlazorAppName 
#Application WinAppName 
    
*FillForm 
    User Name = Admin 
    
*Action Log In 
    
*Action Navigation(Student) 
    
*CheckTable  
    RowCount = 0 
    
*Action New 
    
*FillForm 
    First Name = John 
    Last Name = Smith 
    
*Action Save 
    
*CheckFieldValues 
    Full Name = John Smith 
    
*Action Navigation(Student) 
    
*CheckTable  
    RowCount = 1 
    Columns = First Name, Last Name 
    Row = John, Smith 
```
***

## Run a Test

With EasyTest, you can test your applications from Visual Studio or integrate functional testing in your CI/CD environment.

For information on how to run tests refer to the following topic: [Run Tests](xref:113210).


## EasyTest Components

When you create a new **XAF** solution, the *FunctionalTests* folder is added to the module project.

![EasyTest_FunctionalTests](~/images/easytest_functionaltests116378.png)

This folder contains the [EasyTest configuration file](xref:113209) and the *Sample.ets* sample test script file. You can use the sample test script to get a general idea of the script syntax. 

EasyTest requires that the *Config.xml* configuration file is present in the folder containing a test script to be able to perform the test script. This file serves as a central storage for the configuration information required by test scripts. The configuration file created by default contains application definitions for the solution's application project. You can create test scripts in any folder. However, since the *FunctionalTests* folder contains the automatically generated configuration file, it is recommended that you store test scripts here. For more information about the configuration file, refer to the [EasyTest Configuration](xref:113209) topic.

New solutions are created with a separate EasyTest connection string defined in application projects' configuration files. This connection string is named **EasyTestConnectionString**. While testing, the applications use the database specified by this connection string.


## EasyTest Limitations

* Administrative privileges may be required to run EasyTest scripts. If a script fails to run, try to start **Visual Studio** as an administrator.
