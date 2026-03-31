---
uid: "402150"
title: Application Code Performance
seealso: []
---
# Application Code Performance

This article explains how to profile code performance and avoid common performance issues.

## Profile .NET and JavaScript Code

If [SQL profilers](xref:402149) did not reveal any issues and [data model tune-ups](xref:402151) did not help, you can profile your application code (both speed and memory consumption). This is an advanced task: before you begin, review basic concepts in trusted resources, such as Microsoft documentation.

- Method execution time and call count:

    - **.NET**: Refer to the following article: [Profile application performance in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/profiling/beginners-guide-to-performance-profiling). 
    
        Useful tools: SmartBear AQTime, RedGate ANTS Performance Profiler, JetBrains dotTrace.
    - **JavaScript and network**: [Use Developer Tools in your web browser](https://developer.chrome.com/docs/devtools/#performance).

- Memory consumption:

    - Useful tools: SciTech Software .NET Memory Profiler, SmartBear AQTime, RedGate ANTS Memory Profiler, JetBrains dotMemory.
    - [Profile Memory Usage in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/profiling/memory-usage)
    - [About profiling memory leaks](https://dennisgaravsky.blogspot.com/2013/07/about-profiling-memory-leaks.html) 
    - [Troubleshooting Exceptions: System.OutOfMemoryException](https://learn.microsoft.com/en-us/previous-versions/9w766t6y(v=vs.140)).
    - [Memory leak via event handlers (MSDN)](https://learn.microsoft.com/en-us/archive/blogs/abhinaba/memory-leak-via-event-handlers).
    - [Perfmon counters to check memory leak](https://stackoverflow.com/questions/13473761/perfmon-counters-to-check-memory-leak).


The following blog post describes how to use different tools and techniques together: [The Compromise Between Development Time and Performance in Data-Driven ASP.NET MVC](https://www.red-gate.com/simple-talk/development/dotnet-development/the-compromise-between-development-time-and-performance-in-data-driven-asp-net-mvc/).

> [!NOTE]
> 
> The list of commercial profiling tools above is incomplete and is provided for informational purposes only. DevExpress is neither responsible for nor does it endorse any content offered by third-parties.

## Troubleshooting

After you obtain diagnostic information, check the following common causes for performance issues. We recommend that you follow all the advice from this list in your application.

- **The application or an individual View is loaded slowly for the first time (typically with scheduler, dashboards or reports), but subsequent loads are faster.**

    Such delays usually occur because your app loads additional assemblies or compiles MSIL code (for instance, when a View used a control that was not used by other Views). To decrease the application startup time, refer to the following topic: [](xref:400286).
- **The application always starts slowly.**

    **Solution 1:** .NET apps start faster when they are built with the x86 target platform. Usually, x64 apps are generally slower than x86 apps. For more information, see [AnyCPU Exes are usually more trouble than they’re worth](https://learn.microsoft.com/en-us/archive/blogs/rmbyers/anycpu-exes-are-usually-more-trouble-than-theyre-worth).

    **Solution 2:** Optimize how XAF collects types declared within the _YourSolutionName.Module_ and _YourSolutionName.Module.PlatformName_ projects. 
    
    XAF uses the `GetDeclaredExportedTypes`, `GetDeclaredControllerTypes`, and `GetRegularTypes` methods to go through all assembly types and find the declared business objects, DbContext descendants, Controllers, List, Property Editors, and so on. 
    
    Default XAF code uses reflection to collect all the necessary types. To optimize performance, you can override those methods and return lists of predefined types without calling methods of the base class. 
    
    If you override the `GetRegularTypes` method, you do not need to register types already returned by the overridden `GetDeclaredExportedTypes` and `GetDeclaredControllerTypes` methods. Here is an example from the source code of the built-in XAF module:

    # [C#](#tab/tabid-csharp)
    
    ```csharp
    protected override IEnumerable<Type> GetRegularTypes() {
        return new Type[]{typeof(IModelOptionsSchedulerModule),typeof(IModelOptionsScheduler) };
    }
    protected override IEnumerable<Type> GetDeclaredExportedTypes() {
        return Type.EmptyTypes;
    }
    protected override IEnumerable<Type> GetDeclaredControllerTypes() {
        return new Type[] { typeof(SchedulerDetailViewController) };
    }
    ```
    ***

    **Solution 3:** If your application does not use actions declared through the Action attribute, you can instruct XAF not to look for these actions. Set the `DevExpress.ExpressApp.SystemModule.ObjectMethodActionsViewController.Enabled` static property to `false`.

    **Solution 4:** Use the `XafApplication.EnableModelCache` property (v16.1+). If you enable the cache, XAF generates the Application Model content only on first application startup. It then caches the contents to a file to reduce consequent startup times.

    You can also enable parallel loading of business types and tune the model cache. Set the static UseMultithreadedLoading and SkipEmptyNodes properties of the [DevExpress.ExpressApp.ModelCacheManager](xref:DevExpress.ExpressApp.ModelCacheManager) class to `true` before the XafApplication.Setup method is called in the _YourSolutionName.Win/Program.xx_ file (v16.2+). We also added [various startup performance enhancements](https://supportcenter.devexpress.com/ticket/details/t731177/performance-enhancements-in-xaf-v19-1-for-all-supported-platforms) in v19.1+.

- **References to non-existent assemblies or types in the AssemblyName and TypeName columns of the service XPObjectType table. This may happen if you use XPO for data access and have been developing/upgrading your app for a long time.**

    XPO uses this information to try and load an assembly during the XPDictionary initialization. This may result in startup performance degradation. To detect this issue, check your _eXpressAppFramework.log_ file. Look for messages that refer to outdated DevExpress assemblies, such as "Resolve the 'DevExpress.ExpressApp.ViewVariantsModule.v11.1' assembly". You can also review records in XPObjectType using your database engine tools.

    Delete or purge unwanted XPObjectType records, so that XAF does not search for unused types. Note that some invalid records might be tied with corresponding persistent object records if inheritance mapping is used. In such cases, record deletion will lead to foreign key constraint violation.

    You can also update these rows manually or call the `ModuleUpdater.UpdateXPObjectType()` method as shown in the article: [How to: Handle Renamings and Deletions of Business Classes and their Properties](xref:113254).

- **A View is painted slowly, and the application freezes when it is necessary to redraw this View.**

    Check whether any exceptions are thrown when the View is displayed. Even if these exceptions are handled and do not break the application's execution, many exceptions may cause noticeable freezes, especially during debugging. An example of such a situation is when there is a mistake in the column's display format definition. In this case, a `FormatException` will be thrown for each cell. To see these exceptions, enable Common Language Runtime Exceptions and disable the Just My Code option in Visual Studio. See [Manage exceptions with the debugger in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/debugger/managing-exceptions-with-the-debugger) for more details.


- **The application creates many entries in the Output window while debugging or in production, and this slows down its performance.**

    Turn off or lower the detail level of [the eXpressAppFramework and XPO log switches](xref:112575) in the configuration files.

- **A Web application works very slowly while debugging.**

    Disable the [Browser Link feature](https://supportcenter.devexpress.com/ticket/details/t102322/visual-studio-2013-2015-2017-2019-troubleshooting-issues-related-to-browser-link-feature) in Visual Studio.

- **The Excessive Conditional Appearance rule updates due to control value changes.** 

    [How to avoid excessive ConditionalAppearance rule updates and improve overall form performance](https://supportcenter.devexpress.com/ticket/details/s171794/conditionalappearance-how-to-avoid-excessive-appearance-and-immediatepostdata-rule).
