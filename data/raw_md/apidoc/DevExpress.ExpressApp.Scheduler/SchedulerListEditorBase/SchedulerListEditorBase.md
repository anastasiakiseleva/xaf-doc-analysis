---
uid: DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase
name: SchedulerListEditorBase
type: Class
summary: An abstract class that serves as the base class for the Scheduling [List Editors](xref:113189) from the [Scheduler module](xref:112811).
syntax:
  content: 'public abstract class SchedulerListEditorBase : ListEditor, IControlOrderProvider, IOrderProvider, IComplexListEditor, ISupportUpdate'
seealso:
- linkId: DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase._members
  altText: SchedulerListEditorBase Members
- linkId: "112811"
---
List Views use List Editors to display object collections in a UI. Scheduling List Editors are the best way to present and manage schedule information. These List Editors are targeted for objects that implement the `IEvent` interface from the [Business Class Library](xref:112571). The `SchedulerListEditorBase` class declares members common to all the built-in Scheduling List Editors.

`SchedulerListEditorBase` is an abstract class and cannot be instantiated. However, it exposes the following public events that are not defined in the base [](xref:DevExpress.ExpressApp.Editors.ListEditor) class.

| Name | Type | Description |
|---|---|---|
| [SchedulerListEditorBase.ExceptionEventCreated](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ExceptionEventCreated) | Event | Occurs when an exceptional Event occurrence is created. |
| [SchedulerListEditorBase.ResourceDataSourceCreating](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreating) | Event | Occurs before the resources data source has been instantiated. |
| [SchedulerListEditorBase.ResourceDataSourceCreated](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreated) | Event | Occurs after the resources data source has been instantiated. |

The `SchedulerListEditorBase` is the base class from which all the built-in Scheduler List Editors are inherited. The following table lists XAF's built-in Scheduler List Editors.

| Platform | List Editor |
|---|---|
| ASP.NET Core Blazor | `DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor` |
| Windows Forms | [](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor) |

For additional information on the Scheduling List Editors, refer to the [Scheduler Module](xref:112811) topic.
