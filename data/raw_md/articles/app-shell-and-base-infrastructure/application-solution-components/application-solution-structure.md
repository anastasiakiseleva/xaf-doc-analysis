---
uid: "118045"
title: Application Solution Structure
seealso:
- linkId: "404144"
---
# Application Solution Structure

An XAF solution can include multiple projects for various platforms, such as ASP.NET Core Blazor, WinForms, and Web API applications. All projects can share the same business model, logic, and controllers if they use the same modules. If you require only one application type, you can exclude the others from your solution. The [Template Kit](xref:405447) allows you to select which platforms to include in a new application.

![Solution Modules](~/images/app-solution-components.png)

## Blazor Application Project _(SolutionName.Blazor.Server)_

Contains code specific to your application's ASP.NET Core Blazor version.

_How to add the project to a new solution:_ In the [Template Kit](xref:405447), select the **Web (ASP.NET Core Blazor)** option in the **Platforms** section, or leave both checkboxes (**Web (ASP.NET Core Blazor)** and **Desktop (Windows Forms)**) unchecked.

## End-to-End/Functional Test Project _(SolutionName.E2E.Tests)_

Contains a predefined configuration for [end-to-end (functional) tests](xref:113211). In this project, you can write C# functional tests for your XAF applications.

_How to add the project to a new solution:_ Select the **End-to-End / Functional Tests** option in the **Platforms** section of the [Template Kit](xref:405447).

## Middle Tier Project _(SolutionName.MiddleTier)_

Contains a predefined configuration for the Middle Tier Server, which is an ASP.NET Core service that acts as an intermediary between the client application and the database server. This server filters secured data, and clients cannot access the database server directly. Refer to the following help topics for additional information about the Middle Tier Server:

* [Security Tiers](xref:404691#security-tiers)
* <xref:404389>
* <xref:113439>

_How to add the project to a new solution:_ Select the **Middle Tier Security** option in the **Security Options** section of the [Template Kit](xref:405447).

## Main Module Project _(SolutionName.Module)_

Use this project to implement UI-independent application elements. For instance, you can define a business model and implement UI-independent controllers. Your projects can use the same business model and share controllers from this project.

_How to add the project to a new solution:_ The [Template Kit](xref:405447) always adds this project to a solution.

## Web API Application Project _(SolutionName.WebApi)_

Contains Web API settings. Refer to the following help topic for additional information on how to add a Web API service to your application: <xref:403394>.

_How to add the project to a new solution:_ Select the **Standalone (Separate Projects)** option in the **Blazor / Web API Service Options** section of the [Template Kit](xref:405447).

## WinForms Application Project _(SolutionName.Win)_

Contains code specific to your application's WinForms version.

_How to add the project to a new solution:_ Select the **Desktop (Windows Forms)** option in the **Platforms** section of the [Template Kit](xref:405447).

![Enable Solution Projects in Template Kit](~/images/template-kit/template-kit-solution-structure.png)