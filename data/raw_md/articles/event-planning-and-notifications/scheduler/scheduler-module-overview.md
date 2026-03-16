---
uid: "112812"
seealso:
- linkId: "112571"
- linkId: "404214"
title: Scheduler Module Overview
owner: Ekaterina Kiseleva
---
# Scheduler Module Overview

The Scheduler module allows you to use event/appointment management UI in a [List View](xref:112611). You can switch between different calendar views - from a single day to multiple weeks, display side-by-side calendars, enable synchronized date navigator control, and use many other capabilities available in DevExpress Scheduler controls for WinForms, ASP.NET and Blazor.

## Scheduler Module Components

### Modules

| Platform | Module |
| -------- | ------ |
| Platform-agnostic | [](xref:DevExpress.ExpressApp.Scheduler) |
| ASP.NET Core Blazor | `DevExpress.ExpressApp.Scheduler.Blazor.SchedulerBlazorModule` |
| Windows Forms | [](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerWindowsFormsModule) |

### Integrated DevExpress Controls

| Platform | Editor | Control | Demo / Overview |
| -------- | ------ | ------ | ----- |
| ASP.NET Core Blazor | `DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor` | [Blazor.DxScheduler](xref:DevExpress.Blazor.DxScheduler) | [DxScheduler Demo](https://demos.devexpress.com/blazor/Scheduler) |
| Windows Forms | [Win.SchedulerListEditor](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor) | [XtraScheduler.SchedulerControl](xref:DevExpress.XtraScheduler.SchedulerControl) | [Scheduler Overview](xref:1971) |

> [!TIP]
> You can change the Scheduler List Editor type to a regular List Editor. For more information, refer to the following topic: [](xref:404726).

## Scheduler Data Types

### Events

A Scheduler [List Editor](xref:113189) can visualize a list of `DevExpress.Persistent.Base.General.IEvent` objects. XAF declares this interface in its [Business Class Library](xref:112571). Note that the Scheduler module implements special [Property Editors](xref:112612) for `IEvent` properties. 

You can implement event/appointment objects from scratch or use pre-defined `DevExpress.Persistent.BaseImpl.EF.Event` (Entity Framework Core) or `DevExpress.Persistent.BaseImpl.Event` (XPO) classes from the [Business Class Library](xref:112571). Inherit from these classes to add specific members to your objects.

To see how these classes are implemented, refer to the following resources:
* _[!include[PathToPersistentBaseImplSource](~/templates/path-to-persistent-baseimpl-sources.md)]EFCore_
* _[!include[PathToPersistentBaseImplSource](~/templates/path-to-persistent-baseimpl-sources.md)]Xpo_

For more information on how to implement a custom event class, refer to the following example: [XAF - Create Custom Event and Resource Classes for XAF Scheduler](https://github.com/DevExpress-Examples/xaf-how-to-create-custom-event-and-resource-classes-for-scheduler).

> [!NOTE]
> If you use a custom `IEvent` implementations, set the List View's @DevExpress.ExpressApp.Model.IModelView.AllowEdit property to `True` to allow event/appointment drag and drop.

To use the `Event` class as is, add it to the application module. For more information, refer to the following topic: [](xref:404214).

#### Relationship Between Events and Appointments

Appointments are abstractions of the underlying Business Object Event class instances (`DevExpress.Persistent.BaseImpl.EF.Event` and `DevExpress.Persistent.BaseImpl.Event`) that are actually stored in the database.

The Scheduler module uses the following appointment classes:
* `DevExpress.Blazor.DxSchedulerAppointmentItem` (ASP.NET Core Blazor)
* `DevExpress.XtraScheduler.Appointment` (Windows Forms)

XAF maps appointments to events. If you use standard Event classes or [implement the IEvent interface in your custom class](https://github.com/DevExpress-Examples/xaf-how-to-create-custom-event-and-resource-classes-for-scheduler), you do not have to change the mapping configuration. You can still use the `AppointmentsMappings` property to re-map the appointments to other properties, if needed:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Scheduler.Blazor.Editors;

namespace YourApplicationName.Module.Controllers {
    public class SchedulerController : ObjectViewController<ListView, CustomEvent> {
        protected override void OnViewControlsCreated() {
            base.OnViewControlsCreated();
            ((SchedulerListEditor)View.Editor).AppointmentsMappings.Start = "CustomStart";
        }
    }
}
```

Generally, you would not need to customize appointment classes. In some cases, you may need to obtain an appointment class (for example, in a Scheduler event handler). To access the underlying Event class, use the `SourceObjectHelper` property of the `SchedulerListEditorBase` class:

```csharp
using DevExpress.Blazor;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Scheduler.Blazor.Editors;
using DevExpress.Persistent.BaseImpl;
using Microsoft.AspNetCore.Components;

namespace YourApplicationName.Module.Controllers {
    public class SchedulerController : ObjectViewController<ListView, Event> {
        protected override void OnViewControlsCreated() {
            base.OnViewControlsCreated();
            var schedulerListEditor = (SchedulerListEditor)View.Editor;
            schedulerListEditor.SchedulerModel.AppointmentUpdated = 
            EventCallback.Factory.Create<DxSchedulerAppointmentItem>(this, appointment => {
                    var sourceEvent = schedulerListEditor.SourceObjectHelper.GetSourceObject(appointment);
                    SendEmail($"Event {sourceEvent.Subject} is updated.");
            });
        }
    }
} 
```

### Properties and Corresponding Property Editors

The `IEvent` interface has the following properties: `Subject`, `Description`, `StartOn`, `EndOn`, `AllDay`, `Location`, `Label`, `Status`, `Type` (set by the Scheduler Control), and `ResourceId` (see [Resources in a Schedule](xref:112813)).
The `Label` and `Status` properties define event colors in the Scheduler List Editor. The following property editors allow users to set these colors in a Detail View:

ASP.NET Core Blazor
:   `SchedulerLabelPropertyEditor`

    `SchedulerStatusPropertyEditor`

Windows Forms
:   `SchedulerLabelPropertyEditor`

    `SchedulerStatusPropertyEditor`

They display the `IEvent.Label` and `IEvent.Status` properties in a Detail View, respectively. A value that you select for these properties is bound to a specific color. This color represents the property value in the Event List View. For more information about the corresponding property types, refer to the following topic [](xref:113576).

For information on how to customize these properties, refer to the following topic: [](xref:404714).

ASP.NET Core Blazor
:   ![Scheduler Module Detail View ASP.NET Core Blazor, DevExpress](~/images/scheduler-module-detail-view-blazor.png)

    ![|Scheduler Module List View ASP.NET Core Blazor, DevExpress|](~/images/scheduler-module-list-view-blazor.png)

Windows Forms
:   ![Scheduler Module Detail View Windows Forms, DevExpress](~/images/schedulermodule_detailview115590.png)
    
    ![Scheduler Module List View Windows Forms, DevExpress](~/images/schedulermodule_listview115591.png)

### Switch between Calendar Types (Day, Week, Month, and others)

The Event List View has several view types (the Day View is displayed in the image above). An Event object's properties are displayed in different ways in each view. To set the required view, use the `SchedulerViewType` property of the Application Model's [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node.

### Resources (Side-by-Side Calendar Display)

You can link events to resources. For instance, in a car rental application, an event is a time interval when a car is booked, and the car is a resource. You can schedule the time when a particular resource (car) is busy. Scheduler controls can display calendars for multiple resources side-by-side. For more information about resources, refer to the following topic: [Resources in a Schedule](xref:112813).

### Cross-Platform Compatibility

To make your custom `Event` classes compatible with the Scheduler module in ASP.NET Core Blazor applications, add the `RecurrenceInfoXmlBlazor` property. You can see the implementation in the _Event.cs_ file at the following location:
* Entity Framework Core: _[!include[PathToPersistentBaseImplSource](~/templates/path-to-persistent-baseimpl-sources.md)]EFCore_
* XPO: _[!include[PathToPersistentBaseImplSource](~/templates/path-to-persistent-baseimpl-sources.md)]Xpo_

In the file, look for the `#region Blazor compatibility` tag.

## Add the Scheduler Module to Your Application

### Template Kit

You can add the Scheduler module to your application when you use the [Template Kit](xref:405447) to create a new XAF solution. Select the module in the **Additional Modules** section.

### Existing Application

For step-by-step instructions of how to add the Scheduler module to your application, refer to the following topic: [](xref:404214).
