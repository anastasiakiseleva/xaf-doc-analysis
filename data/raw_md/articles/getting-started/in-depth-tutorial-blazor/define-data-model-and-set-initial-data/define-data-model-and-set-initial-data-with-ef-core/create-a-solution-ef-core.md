---
uid: '404144'
title: 'Create a Solution'
sealso:
  - linkId: "112569"
---
# Create a Solution

This lesson explains how to use the [DevExpress Template Kit](xref:405447) to create a Cross-Platform .NET App UI (XAF) application for ASP.NET Core Blazor and Windows Forms, including authentication features.

## Step-by-Step Instructions

1. From Visual Studio's main menu, select **File** | **New** | **Project…** to invoke the **Create a new project** dialog.

   ![Create a new XAF project](~/images/spm-create-new-project-devexpress.png)

2. Select **DevExpress v<:xx.x:> Template Kit** and click **Next**.
   
   ![Select Template Kit, DevExpress](~/images/template-kit/template-kit-create-a-new-project.png)

3. Specify the project's name (**MySolution**) and location and click **Create**.

   ![Specify Solution name, DevExpress](~/images/template-kit/template-kit-configure-your-new-project-mysolution.png)

4. In the invoked Template Kit window, select **XAF** and specify the following solution settings:

   * In the **Platforms** section, select **Web (ASP.NET Core Blazor)** and **Desktop (Windows Forms)** options. 
   * In the **Security Options** section, deselect the **Standard** option. In this tutorial, we implement user authentication at a later stage.
   * In the **Additional Modules** section, select the **Validation** module.
   
   Leave the rest of the options in their default state and click **Create Project**.
    
   ![Customize created project, DevExpress](~/images/template-kit/template-kit-xaf-platforms.png)

## Solution Structure

The solution contains the following projects: 

MySolution.Module
:   A [module](xref:118046) project that contains platform-independent code. Use this project to define the business logic that applies to all target platforms.
MySolution.Blazor.Server
:   An ASP.NET Core Blazor application that generates a user interface based on the business logic you define in _MySolution.Module_.
MySolution.Win
:   A WinForms application that generates a user interface based on the business logic you define in _MySolution.Module_.

   ![|Solution Explorer view|](~/images/btutorial_bmd_lesson1_2.png)

Refer to the [](xref:118045) topic for information on the XAF solution structure.

## Database Connection

The DevExpress Template Kit allows you to create XAF applications that target [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/)(_the default choice_) or [XPO](xref:1998) ORM tool. For additional information on how to choose an ORM that suits your needs, refer to the following topic: <xref:404186>.

When you create a new application, the application wizard attempts to find an installed Microsoft SQL Server instance (LocalDB or Express) and sets the connection string accordingly. You can also connect to a different database system as described in the following topic: [Specify EF Core Database Provider in XAF Application](xref:404290).

## First Run

You can now run the application. Click **Start Debugging** or press F5.

The ASP.NET Core Blazor project is set as the startup project. To run the Windows Forms application, right-click the **MySolution.Win** project in the Solution Explorer and select the **Set as Startup Project** item from the context menu.

The following images show the resulting ASP.NET Core Blazor and Windows Forms applications.

ASP.NET Core Blazor

:   ![|ASP.NET Core Blazor application first run|](~/images/tutorial-app-first-run-blazor-devexpress.png)

Windows Forms

:   ![Windows Forms application first run](~/images/tutorial-app-first-run-winforms-devexpress.png)

## Next Lesson

[](xref:402981)
