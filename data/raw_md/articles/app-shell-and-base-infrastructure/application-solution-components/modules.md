---
uid: "118046"
title: Modules
seealso:
  - linkType: HRef
    linkId: https://community.devexpress.com/blogs/xaf/archive/2011/07/04/best-practices-of-creating-reusable-xaf-modules-by-example-of-a-view-variants-module-extension.aspx
    altText: 'Best practices of creating reusable XAF modules by example of a View Variants module extension'
---
# Modules

An XAF module is a ready-to-use package for a feature. A module introduces additional [Controllers](xref:112621), [Actions](xref:112622), [List Editors](xref:113189), [View Items](xref:112612), [Application Model](xref:112580) nodes, and properties. 

An XAF module is a class library that contains a class derived from @DevExpress.ExpressApp.ModuleBase. This class allows XAF to recognize a library as a module. XAF-specific classes in a module are automatically collected by [reflection](https://learn.microsoft.com/en-us/dotnet/framework/reflection-and-codedom/reflection) and used for UI generation. [Controllers](xref:112621) declared in a module are created in every [Frame](xref:112608) of an XAF application. They allow you to implement custom code that runs when the Controller is activated.

XAF supports the following module types:

System Modules
:   XAF applications include system modules. These modules supply basic application functionality, such as a [Navigation System](xref:113198), [Printing](xref:113012), and [Export](xref:113362), and cannot be disabled.
Built-in XAF Modules (listed below)
:   XAF includes a number of ready-to-use modules that are listed and described below. For information about how to register a built-in module in your application, refer to the following help topic: <xref:118047>.
Custom XAF Modules
:   You can implement a custom module for your solution. Such a module can be reused in other XAF applications. For more information, refer to the following topic: <xref:405523>.
Third-Party XAF Modules
:   XAF supports work with third-party modules, such as [Llamachant Framework Modules](https://www.llamachant.com/docs/Modules), [Reactive.XAF Modules](https://github.com/eXpandFramework/Reactive.XAF), and other [XAF Community Extensions](https://www.devexpress.com/products/net/application_framework/#extensions). They are usually registered similar to custom XAF modules (<xref:405523>). Refer to the module vendor documentation for more details.

{| class = "dx-feature-list-table"
|-
| colspan="2" | ## Audit Trail Module
|-
| ![|EM_Audit](~/images/em_audit120041.png)
| The Audit Trail module tracks changes to application data. It shows the object and the changes applied to that object by the user, and records old and new property values. The module logs each change when the system saves the object.

**Additional information:** <xref:112782>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## Chart Module
|-
| ![|EM_Chart](~/images/em_chart120046.png)
| This module adds [List Editors](xref:113189) to visualize data with various 2D and 3D chart controls. The module integrates the [Chart Designer](xref:114070) into the [Model Editor](xref:112582) in WinForms projects.

**Additional information:** <xref:113302>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## Clone Object Module

|-
| ![|EM_Clone](~/images/em_clone120049.png)
| Allows end users to quickly create similar business objects by copying an existing object and changing property values.

**Additional information:** <xref:112835>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.


|-
| colspan="2" | ## ConditionalAppearance

|-
| ![|EM_ConditionalAppearance](~/images/em_conditionalappearance120050.png)
| This module allows you to change the user interface based on business rules. You can highlight editors, change their availability or visibility, and update font styles. You can also define or edit these rules at runtime without recompiling the application.

**Additional information:** <xref:113286>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## Dashboards Module

|-
| ![|EM_Dashboards](~/images/em_dashboards125591.png)
| The Dashboards module integrates [DevExpress Dashboard](xref:12049) controls into XAF applications. Users can create dashboards at runtime and save them in the application database.

**Additional information:** <xref:117449>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## File Attachments Module

|-
| ![|EM_FileAttachment](~/images/em_fileattachment120052.png)
| This module displays properties of the [file data](xref:113548) type in the FileDataPropertyEditor and allows users to perform file management operations (upload, download, open, and save files).

**Additional information:** <xref:112781>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## Maps Module

|-
| ![|EM_Maps](~/images/em_maps120056.png)
| This module adds List and Property Editors that display business objects on a map.

**Additional information:** -

**Supported platforms:** [ASP.NET Core Blazor](https://supportcenter.devexpress.com/ticket/details/t995233/blazor-how-to-support-the-xaf-maps-module-scenarios-display-vector-and-raster-maps)[^1], [Windows Forms](https://supportcenter.devexpress.com/ticket/details/t287322/winforms-how-to-display-geospatial-information-in-xaf-views-using-google-bing-or)[^1].

|-
| colspan="2" | ## Multi-Tenancy (Data per Tenant)

|-
| ![|Multi-Tenancy](~/images/multitenancy-module.png)
| This module helps you build multi-tenant or SaaS-ready applications for CRUD use cases.

**Additional information:** <xref:404436>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## Notifications Module

|-
| ![|EM_Notifications](~/images/em_notifications120068.png)
| The Notifications module displays reminders for [scheduler](xref:112811) appointments or custom business objects. The application shows a pop-up alert at the scheduled time. Users can view, cancel, or delay these notifications.

**Additional information:** <xref:113688>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## Office Module

|-
| ![|EM_Office](~/images/em_office.png)
| The Office module integrates the following DevExpress controls:
* Rich Text Editor
* Spreadsheet Editor
* PDF Viewer

**Additional information:** <xref:400003>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## Pivot Grid Module

|-
| ![|EM_Pivot](~/images/em_pivot120074.png)
| This module adds [List Editors](xref:113189) for data analysis with pivot grid controls and integrates the [PivotGrid Designer](xref:1825) into the [Model Editor](xref:112582).

**Additional information:** <xref:113303>

**Supported platforms:** [ASP.NET Core Blazor](https://supportcenter.devexpress.com/ticket/details/t994515/blazor-how-to-integrate-the-pivot-grid-into-an-xaf-app)[^1], Windows Forms.

|-
| colspan="2" | ## Reports V2 Module

|-
| ![|EM_Reports](~/images/em_reports120073.png)
| This module integrates [DevExpress Reporting](xref:2162) into an XAF application. It provides a UI for designing, viewing, and printing reports. The app stores reports as business objects in the database.

**Additional information:** <xref:113591>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## Scheduler Module
|-
| ![|EM_Scheduler](~/images/em_scheduler120078.png)
| This module adds [List Editors](xref:113189) that integrate scheduler controls in an XAF application. Schedulers implement various date-time views, multiple resources display, date navigator, and other features.

**Additional information:** <xref:112811>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## State Machine Module

|-
| ![|EM_StateMachine](~/images/em_statemachine120082.png)
| This module provides a UI to manage state transitions for business objects with different states. You can create states, define valid transitions, and link them to a business class. You can also set [Conditional Appearance](xref:113286) rules for each state.

**Additional information:** <xref:113336>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## TreeList Editors Module

|-
| ![|EM_TreeList](~/images/em_treelist120202.png)
| This module adds [List Editors](xref:113189) that integrate TreeList controls and allows you to display data as a tree, a grid, or both.

**Additional information:** <xref:112841>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## Validation Module

|-
| ![|EM_Validation](~/images/em_validation120207.png)
| This module lets you validate user input against business rules set in code at design time or at runtime.

**Additional information:** <xref:113684>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.

|-
| colspan="2" | ## View Variants Module

|-
| ![|EM_ViewVariants](~/images/em_viewvariants120206.png)
| This module lets you store multiple [View](xref:112611) layout variants in the Application Model. Users can switch between layouts at runtime.

**Additional information:** <xref:113011>

**Supported platforms:** ASP.NET Core Blazor, Windows Forms.
|}

[^1]: This feature requires a custom solution with DevExpress UI components. You can find examples in our [Outlook Inspired Demo](xref:113577#net-winforms--blazor-outlook-inspired-demo-multi-tenancysaas-readyxref404669). For more information, see [Integrate Custom UI Components](xref:403277#integrate-custom-ui-components).

      To get more ready-to-use modules, visit [XAF Community Extensions](https://www.devexpress.com/products/net/application_framework/#extensions).

