---
uid: "404707"
title: ASP.NET Core Blazor Server and Web API Service Configuration Files
---
# ASP.NET Core Blazor Server and Web API Service Configuration Files

The [Template Kit](xref:405447) generates _appsettings.json_ and _appsettings.Development.json_ configuration files for ASP.NET Core-based projects. For production, you should also manually add an _appsettings.Production.json_ file to your ASP.NET Core project. For more information, see [Use multiple environments in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments).

The default `JsonConfigurationProvider` loads configuration information in the following order:

1. _appsettings.json_

2. _appsettings.{Environment}.json_. For example, the _appsettings.Production.json_ and _appsettings.Development.json_ files. Values from the _appsettings.{Environment}.json_ file override keys in _appsettings.json_. For example:

    * In development mode, _appsettings.Development.json_ configuration options override similar values from `appsettings.json`.
    * In production mode, _appsettings.Production.json_ configuration options override similar values from `appsettings.json`.
