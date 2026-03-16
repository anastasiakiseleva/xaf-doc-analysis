---
uid: "402148"
title: Performance Optimization
owner: Alexey Kazakov
---
# Performance Optimization

In modern database-connected client and server applications, multiple aspects can affect performance, such as:

* Client computers or web browsers
* Web server types, their geographic locations, software, and hardware (such as Azure compute units)
* Database server engines along with their physical location and maintenance
* Network communication and latency between system components
* Custom application code and third-party libraries
* Use-case scenarios (database record count, number of concurrent users, etc.)

Performance issues may occur both in XAF applications and non-XAF applications built from scratch. It is impossible to accurately determine the cause of performance issues and provide effective help without collecting quantitative data, for example, the number of SQL queries and their duration in database tables, execution time of .NET or JavaScript methods in problematic scenarios, network latency, or hardware specifications.

The best way to determine the underlying cause of performance issues is to profile application components with specialized performance profilers or loggers. Once you profile your application components and analyze the profiling logs, you will know exactly what contributes to performance delays and will be able to take further actions towards a solution.

If your XAF application has performance issues, we strongly recommend that you troubleshoot it as described in the steps below before you contact our Support Team. Without this profiling, the support team cannot help you resolve your issues properly.

- Step 1: [Database Performance](xref:402149)
- Step 2: [ORM Performance](xref:402151)
- Step 3: [Application Code Performance](xref:402150)

> [!NOTE]
> 
> The DevExpress Support Team cannot profile full-scale projects or databases. If you or your team need assistance with such tasks, contact [consultant companies that have expertise in XAF app development and performance profiling](https://www.devexpress.com/products/net/application_framework/#consulting).

## DevExpress API Performance

If your profiling results indicate a possible performance issue in DevExpress API, please contact our Support Team and include the following diagnostic information:

- All the diagnostic information from [SQL queries](xref:402149#profile-sql-queries) and [application code](xref:402150#profile-net-and-javascript-code) articles.
- Assets that will help our Support Team reproduce the issue locally in a typical development environment with only Microsoft SQL Server and Visual Studio installed. Please include a small debuggable sample project, database backups or demo data generation code, and any other supporting information.
- A list of solutions you tried from the [Data Request and ORM Performance](xref:402151) and [Application Performance - Troubleshooting](xref:402150#troubleshooting) articles and their results.


## Performance in Additional Modules

Refer to the following topics to resolve performance issues in [additional modules](xref:118046):

- [Security - How to reduce the number of permission requests and improve overall performance](https://supportcenter.devexpress.com/ticket/details/t381322/security-how-to-reduce-the-number-of-permission-requests-and-improve-overall-performance)

## Video

In this video, we talk about the best ways to access and manage data in XAF and how to build high-performance applications. 

> [!video https://www.youtube.com/embed/RUyXX2pJcjM]

## High Load Scenarios, Load Testing, and Scalability

- [Deploy and scale an XAF Blazor Server app: use Azure Kubernetes Service to serve hundreds of users](https://github.com/DevExpress/XAF-Blazor-Kubernetes-example)
- [XAF Blazor load testing on Linux and MySql using Puppeteer and GitHub Actions](https://github.com/DevExpress/xaf-blazor-app-load-testing-example)
- [How to integrate XAF functional testing with Continuous Integration systems like Azure DevOps](https://supportcenter.devexpress.com/ticket/details/t844058/easytest-how-to-integrate-xaf-functional-testing-with-continuous-integration-systems)
- [XAF ASP.NET Core Blazor UI deployment, scalability and load testing considerations](https://supportcenter.devexpress.com/ticket/details/s36497/xaf-asp-net-webforms-blazor-ui-deployment-scalability-and-load-testing-considerations)
- [XAF Blazor load test with 100 clients (Video by Joche Ojeda)](https://www.youtube.com/watch?v=rPm41VEAM2Q)
