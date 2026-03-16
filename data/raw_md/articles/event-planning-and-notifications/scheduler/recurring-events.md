---
uid: "113128"
seealso:
- linkId: "113178"
title: Recurring Events
owner: Ekaterina Kiseleva
---
# Recurring Events

This topic introduces the concept of the [Recurring Events](xref:1753) feature supported by the [Scheduler Module](xref:112812), describes how to create and use recurring events in your schedule, and details how recurrence settings can be edited.

## Non-Recurring and Recurring Events

The Scheduler module supports the following event types:

Simple
:   Occur only once in the specified time interval.
Recurring
:   Occur many times with the same time interval.

The Scheduler module works with business classes that implement the `DevExpress.Persistent.Base.General.IEvent` interface. To support recurring events, these classes must implement an additional `IRecurrentEvent` interface. If you already have a custom class that implements the `IEvent` interface, you can implement the `IRecurrentEvent` interface yourself. Alternatively, you can use the `DevExpress.Persistent.BaseImpl.EF.Event` (Entity Framework Core) or `DevExpress.Persistent.BaseImpl.Event` (XPO) class from the [Business Class Library](xref:112571) that implements the `IEvent` and `IRecurrentEvent` interfaces. 

To see how these classes are implemented, refer to the following resources:
* _[!include[PathToPersistentBaseImplSource](~/templates/path-to-persistent-baseimpl-sources.md)]Xpo_
* _[!include[PathToPersistentBaseImplSource](~/templates/path-to-persistent-baseimpl-sources.md)]EFCore_) 

To extend the class with custom properties, inherit from it.

## Creating a Recurring Event

To create a recurring event, create an Event and specify its recurrence via the `Recurrence` property. XAF uses `SchedulerRecurrenceInfoPropertyEditor` to display this property in the Event Detail View.

ASP.NET Core Blazor
:   ![|Scheduler Event Recurrence in ASP.NET Core Blazor, DevExpress|](~/images/xaf-blazor-scheduler-event-recurrence-devexpress.png)

Windows Forms
:   ![Scheduler Event Recurrence in Windows Forms, DevExpress](~/images/schedulereventrecurrence2116143.png)

Click the Recurrence editor's ellipsis button (Windows Forms) or select a combo box value (ASP.NET Core Blazor) to invoke the **Recurrence** dialog and specify the required settings.

ASP.NET Core Blazor
:   ![|Recurrence Dialog in ASP.NET Core Blazor, DevExpress|](~/images/scheduler-recurrence-menu-blazor.png)

Windows Forms
:   ![Recurrence Dialog in Windows Forms, DevExpress](~/images/schedulereventrecurrence116142.png)

The recurrence settings specified in this dialog comprise the Recurrence Pattern.

## Recurrence Pattern

A recurring event's recurrence settings are stored in the Recurrence Pattern. When the Scheduler module needs to visualize the recurring event's occurrences on a time line, it reads the recurrence settings from the Recurrence Pattern. However, a recurring event is not really useful in real-life applications if you cannot customize its individual occurrences. For instance, if you have a recurring event that represents a weekly meeting, you may want to specify that the next week's meeting starts an hour later than usual. You cannot do this in the event's **Recurrence** dialog. Instead, you can edit the required occurrence on the Scheduler's time line. The Scheduler module handles such customizations automatically with the help of a special collection associated with the event. This collection stores all the occurrences of the event that were changed or deleted. So, a recurring event is defined by its Recurrence Pattern and the collection of changes.

### ASP.NET Core Blazor

To edit a single occurrence of a recurring event, double-click the event or click the event and click **Edit** in the tooltip. In the displayed dialog select **Edit appointment**.

To edit the series, click the event and click **Edit** in the tooltip. In the displayed dialog select either **Edit series** or **Edit appointment**.

![Scheduler Edit Series Tooltip in ASP.NET Core Blazor, DevExpress](~/images/scheduler-edit-tooltip-blazor-devexpress.png)

![Scheduler Edit Series Tooltip in ASP.NET Core Blazor, DevExpress](~/images/scheduler-edit-popup-blazor-devexpress.png)

If an occurrence has been modified, you can restore its settings to the ones used in the series it belongs to. To do this, use the **Restore Occurrence** command.

![|Scheduler Restore Occurrence in ASP.NET Core Blazor, DevExpress|](~/images/scheduler-blazor-restore-occurrence-devexpress.png)

### Windows Forms
To edit a single occurrence of a recurring event, invoke the context menu and click **Open**. To change the settings of all the occurrences, except those that have been changed or deleted, click **Edit Series**:

![|Scheduler Edit Series Context Menu in Windows Forms, DevExpress|](~/images/schedulereditserieswin1116194.png)

If an occurrence has been modified, you can restore its settings to the ones used in the series it belongs to. To do this, use the **Restore Default State** command.

![Scheduler Restore Default State in Windows Forms, DevExpress](~/images/schedulereditserieswin2116312.png)

## Create and Edit Recurrent Events in Code

The code sample below shows how to create recurrent events programmatically. You can reuse this code in the `Updater` class of your XAF application to populate your database with data.

1. Add the **DevExpress.Scheduler.Core** NuGet package to the project and rebuild the solution.
2. Create a new class and replace the auto-generated code with the following code:

    # [EF Core](#tab/tabid-efcore)

    ```csharp{16-20}
    using DevExpress.ExpressApp.Actions;
    using DevExpress.ExpressApp;
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;
    using DevExpress.XtraScheduler;
    using DevExpress.XtraScheduler.Xml;
    namespace YourApplicationName.Module.Controllers {
        public class RecurrenceController : ObjectViewController<ListView, Event> {
            public RecurrenceController() {
                var makeRecurrentEventAction = new SimpleAction(this, "MakeRecurrent", PredefinedCategory.ObjectsCreation);
                makeRecurrentEventAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
                makeRecurrentEventAction.Execute += (s, e) => {
                    Event schedulerEvent = (Event)View.CurrentObject;
                    if (schedulerEvent.Type == (int)AppointmentType.Normal) {
                        schedulerEvent.Type = (int)AppointmentType.Pattern;
                        RecurrenceInfo recurrenceInfo = new RecurrenceInfo(schedulerEvent.StartOn.Value);
                        // You can specify other options of the RecurrenceInfo class here.
                        RecurrenceInfoXmlPersistenceHelper helper = new RecurrenceInfoXmlPersistenceHelper(recurrenceInfo);
                        schedulerEvent.RecurrenceInfoXml = helper.ToXml();
                        ObjectSpace.CommitChanges();
                        View.Refresh();
                    }
                };
            }
        }
    }
    ```

    # [XPO](#tab/tabid-xpo)

    ```csharp{16-20}
    using DevExpress.ExpressApp.Actions;
    using DevExpress.ExpressApp;
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl;
    using DevExpress.XtraScheduler;
    using DevExpress.XtraScheduler.Xml;
    namespace YourApplicationName.Blazor.Server.Controllers {
        public class RecurrenceController : ObjectViewController<ListView, Event> {
            public RecurrenceController() {
                var makeRecurrentEventAction = new SimpleAction(this, "MakeRecurrent", PredefinedCategory.ObjectsCreation);
                makeRecurrentEventAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
                makeRecurrentEventAction.Execute += (s, e) => {
                    Event schedulerEvent = (Event)View.CurrentObject;
                    if (schedulerEvent.Type == (int)AppointmentType.Normal) {
                        schedulerEvent.Type = (int)AppointmentType.Pattern;
                        RecurrenceInfo recurrenceInfo = new RecurrenceInfo(schedulerEvent.StartOn);
                        // You can specify other options of the RecurrenceInfo class here.
                        RecurrenceInfoXmlPersistenceHelper helper = new RecurrenceInfoXmlPersistenceHelper(recurrenceInfo);
                        schedulerEvent.RecurrenceInfoXml = helper.ToXml();
                        ObjectSpace.CommitChanges();
                        View.Refresh();
                    }
                };
            }
        }
    }
    ```

    ***
