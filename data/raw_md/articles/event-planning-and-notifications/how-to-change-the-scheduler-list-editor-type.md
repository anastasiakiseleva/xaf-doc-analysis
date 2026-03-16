---
uid: "404726"
title: "How to: Display Appointments in a Data Table (Grid List Editor)"
owner: Anastasiya Kisialeva
---
# How to: Display Appointments in a Data Table (Grid List Editor)

This article explains how display events in a regular List View grid in XAF ASP.NET Core Blazor and Windows Forms applications.

> [!NOTE]
> For the purposes of this article, you can use the **MainDemo** application installed as a part of the XAF package. The default location of the application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\\Components\XAF_.

The **MainDemo** application uses [DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor](xref:DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor) and [DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor) to display Scheduler in UI. The image below shows the current Scheduler List Editor:

ASP.NET Core Blazor

:   ![|ASP.NET Core Blazor Scheduler as SchedulerListEditor, DevExpress](~/images/xaf-blazor-scheduler-schedulerlisteditor-devexpress.png)

Windows Forms

:   ![Windows Forms Scheduler as SchedulerListEditor, DevExpress](~/images/xaf-winforms-scheduler-schedulerlisteditor-devexpress.png)

The instructions below explain how to change the List Editor type.

1. In the **Solution Explorer**, expand the `MainDemo.Blazor.Server` or `MainDemo.Win` project and double-click the _Model.xafml_ file to open it in the [Model Editor](xref:112582).
2. Depending on the ORM tool used in your application, navigate to one of the following nodes:
    * **Views** | **DevExpress.Persistent.BaseImpl.EF | Event | Event_ListView** for [Entity Framework Core](xref:401886).
    * **Views** | **DevExpress.Persistent.BaseImpl | Event | Event_ListView** for [XPO](xref:112600).
3. Set the [IModelListView.EditorType](xref:DevExpress.ExpressApp.Model.IModelListView.EditorType) property to a regular List Editor value:
    * [DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor](xref:DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor) for ASP.NET Core Blazor.
    * [DevExpress.ExpressApp.Win.Editors.GridListEditor](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) for Windows Forms.
4. Save the changes and run the application. When you invoke the **Calendar** List View, it should look like this:

   ASP.NET Core Blazor

   :   ![|ASP.NET Core Blazor Scheduler as DxGridListEditor, DevExpress](~/images/xaf-blazor-scheduler-dxgridlisteditor-devexpress.png)

   Windows Forms

   :   ![Windows Forms Scheduler as GridListEditor, DevExpress](~/images/xaf-winforms-scheduler-gridlisteditor-devexpress.png)

> [!TIP]
> You can add an Action that allows users to switch between different List Editors. For more information, refer to the following topic: [View Variants Module](xref:113011).