---
uid: DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor
name: SchedulerListEditor
type: Class
summary: Implements the Scheduling [List Editor](xref:113189) used in the XAF Windows Forms applications.
syntax:
  content: 'public class SchedulerListEditor : SchedulerListEditorBase, IExportable, ISupportBorderStyle'
seealso:
- linkId: DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor._members
  altText: SchedulerListEditor Members
- linkId: "112811"
- linkId: "113189"
---
List Views use List Editors to display object collections in a UI. `SchedulerListEditor` ships with the [Scheduler module](xref:112811). It displays and manages scheduling information:

![SchedulerListEditor_Win](~/images/schedulerlisteditor_win116344.png)

To display object collections, `XafSchedulerControl` is used as the underlying control. `XafSchedulerControl` is a descendant of the [](xref:DevExpress.XtraScheduler.SchedulerControl) class.

`SchedulerListEditor` supports a range of features out of the box:

* This List Editor has a Date Navigator which provides a quick and easy way to change the dates in the scheduling area:
    
    ![SchedulerListEditor_Win_DateNavigator](~/images/schedulerlisteditor_win_datenavigator116352.png)
    
    The Date Navigator can be accessed using the [SchedulerListEditor.DateNavigator](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor.DateNavigator) property.
* Implements the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface - can be exported with the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) and printed using the [](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController):
    
    ![Export_SchedulerListEditor](~/images/export_schedulerlisteditor116968.png)
    
    ![SchedulerListEditor_Printing](~/images/schedulerlisteditor_printing116346.png)
* As a descendant of the [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase), `SchedulerListEditor` implements the `IControlOrderProvider` interface and supports the  [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController)'s **PreviousObject** and **NextObject** [Actions](xref:112622):
    
    ![RecordsNavigationController_Actions_Win](~/images/recordsnavigationcontroller_actions_win115934.png)
* Supports [Resources](xref:112813) and [Recurring Events](xref:113128).

XAF uses `SchedulerListEditor` for objects that implement the `IEvent` interface from the [Business Class Library](xref:112571).

For a thorough explanation of `SchedulerListEditor`, refer to the following topic: [Scheduler Module](xref:112811).

> [!NOTE]
> `SchedulerListEditor` does not support [Server, ServerView, InstantFeedback, and InstantFeedbackView](xref:118450) mode ([CollectionSourceBase.DataAccessMode](xref:DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode)).

> [!TIP]
> XAF Core does not let you create objects directly from a nested List View for many-to-many related objects. This restriction affects the Scheduler. When you try to edit an occurrence in a series using the Scheduler Control of a Resource, you cannot create the object if the Resource Detail View opens through an Event Detail View and you have not edited the occurrence before.
>
> The system stores information about an exception from a recurring event in a separate `IEvent` object. When you click "Edit this occurrence" for the first time, the system creates a new object.
>
> The internal code in `SchedulerListEditor` calls [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction) to create the object. This action does not appear in the UI in the case described in this note.