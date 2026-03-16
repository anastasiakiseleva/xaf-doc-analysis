---
uid: "113178"
seealso:
- linkId: "112812"
- linkId: "113128"
- linkId: "404214"
title: "How to: Perform Custom Actions When an Exception is Added to a Recurring Event"
owner: Anastasiya Kisialeva
---
# How to: Perform Custom Actions When an Exception is Added to a Recurring Event

XAF ships with the [Scheduler Module](xref:112812) designed to manage scheduling information. This module uses [integrated DevExpress controls](xref:112812#integrated-devexpress-controls) to display a List View of `IEvent` objects. Each object is an event that can occur once or follow a recurrence pattern.

If you use a custom class that implements the `IEvent` and `ISupportReccurrence` interfaces, any custom properties that are not defined in the `IEvent` interface lose their values when you create an exception for a [recurring event](xref:113128).

This topic explains the reason behind this behavior and demonstrates how to preserve the values of such properties.

## Step-by-Step Instructions

1. In the _YourSolutionName.Module\BusinessObjects_ folder, create a new class and call it `ExtendedEvent`. Inherit the class from `DevExpress.Persistent.BaseImpl.EF.Event` (for EF Core) or `DevExpress.Persistent.BaseImpl.Event` (for XPO) to implement the `IEvent` and `ISupportRecurrence` interfaces and add a public property not defined in the `IEvent` interface.

    # [C# (EF Core)](#tab/tabid-csharp-ef)

    ```csharp
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;

    //...
    [DefaultClassOptions]
    public class ExtendedEvent : Event {
        public virtual string Notes { get; set; }
    }

    // Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
    ```

    # [C# (XPO)](#tab/tabid-csharp-xpo)

    ```csharp
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl;

    namespace YourSolutionName.Module.BusinessObjects {
        [DefaultClassOptions]
        public class ExtendedEvent : Event {
            public ExtendedEvent(Session session) : base(session) { }
            private string notes;
            public string Notes {
                get { return notes; }
                set { SetPropertyValue<string>(nameof(Notes), ref notes, value); }
            }
        }
    }
    ```
    ***

2. Run the application. Create a weekly meeting that starts at 9:00 AM and set its `Notes` property to "regular meetings" (note the recurring event icon in the lower-right corner of this event):

    ![|XAF ASP.NET Core Blazor Scheduler Recurring Event, DevExpress|](~/images/schedulercustomevent1116275.png)

    ![|XAF ASP.NET Core Blazor Scheduler Recurring Event's Properties, DevExpress|](~/images/schedulercustomevent2116276.png)

3. Set the start time for a single event from the series to 8:00 AM. Note that the recurring event icon is crossed out, which means that this event no longer matches the recurrence pattern.

    ![|XAF ASP.NET Core Blazor Edited Recurring Event Logo|](~/images/schedulercustomevent3116277.png)

4. Open the edited event and check the `Notes` property value. As you can see, it is empty.

    ![|XAF ASP.NET Core Blazor Scheduler Edited Event Empty Property, DevExpress|](~/images/schedulercustomevent4116278.png)

    When you edit a single event in the recurring series, the Scheduler only duplicates properties defined in the `IEvent` interface. To include custom properties, you need to handle the [SchedulerListEditorBase.ExceptionEventCreated](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ExceptionEventCreated) event. This event occurs when you create an exception. The event handler's argument has two properties.

    * [ExceptionEventCreatedEventArgs.PatternEvent](xref:DevExpress.ExpressApp.Scheduler.ExceptionEventCreatedEventArgs.PatternEvent) - the original event occurrence that you changed.
    * [ExceptionEventCreatedEventArgs.ExceptionEvent](xref:DevExpress.ExpressApp.Scheduler.ExceptionEventCreatedEventArgs.ExceptionEvent) - the modified event you created (the exception).

5. In the _YourSolutionName.Module\Controllers_ folder, create a new [View Controller](xref:112621) and handle the @DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ExceptionEventCreated event as displayed in the following code snippet:

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Scheduler;
    using DevExpress.Persistent.Validation;
    using MySolution.Module.BusinessObjects;

    namespace MySolution.Module.Controllers {
        public class CustomEventController : ViewController<ListView> {
            private SchedulerListEditorBase schedulerEditor;
            protected override void OnActivated() {
                base.OnActivated();
                schedulerEditor = View.Editor as SchedulerListEditorBase;
                if (schedulerEditor != null) {
                    schedulerEditor.ExceptionEventCreated += schedulerEditor_ExceptionEventCreated;
                }
            }
            protected override void OnDeactivated() {
                base.OnDeactivated();
                if (schedulerEditor != null) {
                    schedulerEditor.ExceptionEventCreated -= schedulerEditor_ExceptionEventCreated;
                }
            }
            void schedulerEditor_ExceptionEventCreated(object sender, ExceptionEventCreatedEventArgs e) {
                if (e.PatternEvent is ExtendedEvent patternEvent && e.ExceptionEvent is ExtendedEvent exceptionEvent) {
                    exceptionEvent.Notes = patternEvent.Notes;
                }
            }
        }
    }
    ```
    ***

    The Controller checks whether the current List View's [List Editor](xref:113189) derives from the [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase). If it does, the Controller subscribes to the @DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ExceptionEventCreated event. In the event handler, the Controller checks whether the Scheduler is activated for the `ExtendedEvent` class. If so, the Controller copies the `Notes` property value from the object returned by the `PatternEvent` property to the object returned by the `ExceptionEvent` property. Upon deactivation, it unsubscribes from the `ExceptionEventCreated` event.

6. Run the application and set the start time for a single event from the series to 8:00 AM again. Open the edited event and check the `Notes` property value. It should be preserved.

    ![|XAF ASP.NET Core Blazor Scheduler Edited Event's Notes Property, DevExpress|](~/images/schedulercustomevent5116279.png)

## Validate Custom Properties in Recurrence Exceptions

When you apply [validation rules](xref:113684) to custom properties processed by the @DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ExceptionEventCreated event, you cannot use the standard `Save` validation context. XAF checks this context when it raises the [IObjectSpace.Committing](xref:DevExpress.ExpressApp.IObjectSpace.Committing) event. However, it copies custom property values to an exception event later, when it raises the [IObjectSpace.ObjectSaving](xref:DevExpress.ExpressApp.IObjectSpace.ObjectSaving) event.

To implement validation rules for custom properties, define a custom validation context in the `ExtendedEvent` class, as shown in the following code snippet:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp{11-12}
//...
using DevExpress.Persistent.Validation;
using Microsoft.Extensions.DependencyInjection;

namespace YourSolutionName.Module.BusinessObjects {
    [DefaultClassOptions]
    public class ExtendedEvent : Event {
        // ...
        public override void OnSaving() {
            base.OnSaving();
            var validator = ObjectSpace.ServiceProvider.GetRequiredService<IValidator>();
            validator.RuleSet.Validate(ObjectSpace, this, "SchedulerValidation");
        }
    }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp{11-12}
// ...
using DevExpress.ExpressApp.Validation;
using DevExpress.ExpressApp.Xpo;

namespace YourSolutionName.Module.BusinessObjects {
    [DefaultClassOptions]
    public class ExtendedEvent : Event {
        // ...
        protected override void OnSaving() {
            base.OnSaving();
            var validator = Session.ServiceProvider.GetRequiredService<IValidator>();
            validator.RuleSet.Validate(ObjectSpace, this, "SchedulerValidation");
        }
    }
}

```

***

You can also trigger validation when you specify a custom property value. In the `CustomEventController` class, modify the handler of the @DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ExceptionEventCreated event as displayed in the code snippet below:

```csharp{11-12}
// ...
using DevExpress.Persistent.Validation;
using Microsoft.Extensions.DependencyInjection;

namespace MySolution.Module.Controllers {
    public class CustomEventController : ViewController<ListView> {
        // ...
        void schedulerEditor_ExceptionEventCreated(object sender, ExceptionEventCreatedEventArgs e) {
            if (e.PatternEvent is ExtendedEvent patternEvent && e.ExceptionEvent is ExtendedEvent exceptionEvent) {
                exceptionEvent.Notes = patternEvent.Notes;
                var validator = Application.ServiceProvider.GetRequiredService<IValidator>();
                validator.RuleSet.Validate(ObjectSpace, this, "SchedulerValidation");
            }
        }
    }
}
```
