---
uid: "402129"
title: Define the Data Model and Set Initial Data
owner: Alexey Kazakov
seealso:
  - linkId: "402971"
---
# Define the Data Model and Set Initial Data

This section explains how to design a business model (database) for an application built with Cross-Platform .NET App UI (XAF) and [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/). 

You will learn how to complete the following tasks:

- Create business classes mapped to database tables
- Define relationships between classes
- Implement dependent properties

To design a business model, build custom classes and inherit your business objects from the `BaseObject` class.

> [!TIP]
> You can use the [PMC](https://learn.microsoft.com/en-us/ef/core/cli/powershell) or [CLI](https://learn.microsoft.com/en-us/ef/core/cli/dotnet) tool to generate the business model from an existing database instead of creating it from scratch in Entity Framework Core. To learn more about this approach in EF Core, refer to the following article: [Reverse Engineering](https://learn.microsoft.com/en-us/ef/core/managing-schemas/scaffolding).

Once you complete the tutorial, your application will look as shown in the image below:

ASP.NET Core Blazor

:   ![ASP.NET Core Blazor Application](~/images/final-app-preview-blazor.png)

Windows Forms

:   ![Windows Forms Application](~/images/final-app-preview-winforms.png)

Proceed to [Create a Solution](xref:404144) to start the tutorial.
