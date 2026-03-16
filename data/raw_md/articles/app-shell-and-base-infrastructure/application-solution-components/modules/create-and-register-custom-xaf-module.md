---
uid: "405523"
title: Create and Register a Custom XAF Module
seealso:
  - linkType: HRef
    linkId: https://learn.microsoft.com/en-us/dotnet/core/tutorials/library-with-visual-studio
    altText: 'Tutorial: Create a .NET class library using Visual Studio'
---
# Create and Register a Custom XAF Module

XAF allows you to implement custom modules in your application and to reuse these modules in other XAF applications. 

## Create a Common Cross-Platform XAF Module

An XAF module is a class library that contains a class derived from @DevExpress.ExpressApp.ModuleBase. You can use the [Template Kit](xref:405447) to create an XAF project with a cross-platform module and reuse this module in your application.

1. Use the DevExpress [Template Kit](xref:405447#create-a-new-project) or [CLI template](xref:404967) to create a new solution. Specify the same initial settings (such as framework version and ORM) as in your existing project.  
    The new solution includes several modules: platform-specific application projects (_NewSolutionName.Blazor.Server_ or/and _NewSolutionName.Win_) and a common module (_NewSolutionName.Module_).
1. Copy the _NewSolutionName\NewSolutionName.Module_ folder from the new solution to your solution. 
1. Add the new module project to your solution. Right-click the solution name in the Solution Explorer, select **Add** | **Existing Project…**, and choose _SolutionName\NewSolutionName.Module\NewSolutionName.Module.csproj_.

    ![Add an existing project to an application](~/images/add-existing-project.png)

    The new module will appear in the Solution Explorer.

    ![New module in the solution](~/images/new-solition-module.png)

> [!tip]
> Alternatively, you can define a @DevExpress.ExpressApp.ModuleBase class descendant to convert an existing Class Library into a module. Take the _Module.cs_ file from an existing module as a prototype. Rename this class and set the correct namespace.
> 
> Do not inherit from modules. @DevExpress.ExpressApp.ModuleBase class descendants should be [sealed](https://learn.microsoft.com/en-us/dotnet/articles/csharp/language-reference/keywords/sealed).

## Register a Module in the XAF Application

1. Add a reference to the new module project.
    * Right-click on the **Dependencies** node in the project where you want to add the module (_SolutionName.Blazor.Server_, _SolutionName.Win_, _SolutionName.Module_).
    * Select **Add Project Reference**.

        ![Add a project reference](~/images/add-project-reference.png)

    * In the opened dialog, select your module project and click **OK**.

        ![Reference Manager](~/images/add-project-reference-ref-manager.png)

1. You can register a custom module in the main module project or in platform-specific projects.

   Register a module in the main module project
   :   In the _SolutionName.Module\Module.cs_ file, add the new module to the @DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes list. XAF loads this required module with the main module.

         ```csharp
         public sealed class SolutionNameModule : ModuleBase {
            public SolutionNameModule() {
               // ...
               RequiredModuleTypes.Add(typeof(NewSolutionName.Module.NewSolutionNameModule));
            }
         // ...
         }
         ```
         
         Use this approach when the main module depends on the added custom module. For instance, if you call the `CustomizeTypesInfo` method or if you use the [Model Editor](xref:112582) to configure classes from the custom module.
   Register a module in platform-specific projects
   :   Navigate to the _MyApplication.Blazor.Server\Startup.cs_ (Blazor) or _MyApplication.Win\Startup.cs_ (WinForms) file and call the @DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder`1.Add* method to register the module. 

         # [ASP.NET Core Blazor](#tab/tabid-appbuilder-blazor)
            
         ```csharp{8}
         public class Startup {
            // ...
            public void ConfigureServices(IServiceCollection services) {
                  // ...
                  services.AddXaf(Configuration, builder => {
                     // ...
                     builder.Modules
                        .Add<NewSolutionName.Module.NewSolutionNameModule>();
                     // ...
                  });
                  // ...
            }
            // ...
         }
         ```
            
         # [Windows Forms](#tab/tabid-appbuilder-winforms)

         ```csharp{5}
         public class ApplicationBuilder : IDesignTimeApplicationFactory {
            public static WinApplication BuildApplication(string connectionString) {
                  // ...
                  builder.Modules
                     .Add<NewSolutionName.Module.NewSolutionNameModule>();
                  // ...
            }
            // ...
         }
         ```
         ***
   
> [!note]
> This help topic describes how to add a common cross-platform module to your application. If you need to implement platform-specific logic, for instance, [implement a property editor based on a custom component (Blazor)](xref:402189) or [display a custom data-bound control in an XAF View](xref:404701), use platform-specific application projects — _SolutionName.Blazor.Server_ or _SolutionName.Win_.