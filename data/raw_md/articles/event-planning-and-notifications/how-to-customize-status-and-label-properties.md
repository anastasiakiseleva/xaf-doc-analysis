---
uid: "404714"
title: "How to: Customize Status and Label Properties"
---
# How to: Customize Status and Label Properties

This topic describes how to define custom statuses and labels for your Scheduler events in XAF ASP.NET Core Blazor or Windows Forms applications.

> [!NOTE]
> For this article, you can use the **MainDemo** application installed as part of the XAF package. The default location of the application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\\Components\XAF_.

The instructions below explain how to define the following custom items:

* "Vacation" and "Personal" labels
* "Free" and "Out of Office" statuses

## ASP.NET Core Blazor

XAF stores source data for labels and status items in a @DevExpress.Blazor.DxSchedulerDataStorage object. Use the @DevExpress.ExpressApp.Scheduler.Blazor.SchedulerEvents.OnSchedulerDataStorageCreated event to customize this object's settings. Specified values will be available for `Label` and `Status` properties of the built-in `Event` object (or your custom `IEvent` implementation).

1. In the **Solution Explorer**, navigate to the _MainDemo.Blazor.Server\Startup.cs_ file and make the following changes to the @DevExpress.ExpressApp.Blazor.ApplicationBuilder.SchedulerApplicationBuilderExtensions.AddScheduler(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Scheduler.Blazor.SchedulerOptions}) method:

    [!include[<MainDemo>](~/templates/customize-scheduler-options.md)]

2. Build the project and run the application. The `Event` Detail View displays new labels and status items:

    ![|XAF ASP.NET Core Blazor Custom Status and Label, DevExpress](~/images/xaf-blazor-scheduler-custom-status-and-label-devexpress.png)

## Windows Forms

XAF stores source data for labels and status items in a @DevExpress.XtraScheduler.SchedulerStorage object. Use @DevExpress.XtraScheduler.SchedulerStorage.Appointments property to access @DevExpress.XtraScheduler.AppointmentStorage.Labels and @DevExpress.XtraScheduler.AppointmentStorage.Statuses collections.

1. In the _MainDemo.Win.Controllers_ folder, create a _WinSchedulerController_ class. Replace the generated class declaration with the code sample below:

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Scheduler.Win;
    using DevExpress.XtraScheduler;
    using DevExpress.XtraScheduler.UI;
    
    namespace MainDemo.Win.Controllers;
    
    public class WinSchedulerController : ViewController {
        protected override void OnActivated() {
            base.OnActivated();
            if(View is DetailView detailView) {
                detailView.CustomizeViewItemControl<SchedulerLabelPropertyEditor>(this, labelPropertyEditor => {
                    var labelEdit = (AppointmentLabelEdit)labelPropertyEditor.Control;
                    SetupLabels(labelEdit.Storage);
                    labelEdit.RefreshData();
                });
                detailView.CustomizeViewItemControl<SchedulerStatusPropertyEditor>(this, statusPropertyEditor => {
                    var statusEdit = (AppointmentStatusEdit)statusPropertyEditor.Control;
                    SetupStatuses(statusEdit.Storage);
                    statusEdit.RefreshData();
                });
            }
        }
        protected override void OnViewControlsCreated() {
            base.OnViewControlsCreated();
            if(View is DevExpress.ExpressApp.ListView listView && listView.Editor is SchedulerListEditor schedulerListEditor) {
                SetupLabels(schedulerListEditor.SchedulerControl.Storage);
                SetupStatuses(schedulerListEditor.SchedulerControl.Storage);
            }
        }
        private static void SetupLabels(ISchedulerStorageBase storage) {
            storage.Appointments.Labels.Clear();
            AddLabel(storage, Color.DeepPink, "Vacation");
            AddLabel(storage, Color.LightSeaGreen, "Personal");
        }
        private static void AddLabel(ISchedulerStorageBase storage, Color color, string caption) {
            var item = storage.Appointments.Labels.CreateNewLabel(caption);
            item.NamedColorValue = color.Name;
            storage.Appointments.Labels.Add(item);
        }
        private static void SetupStatuses(ISchedulerStorageBase storage) {
            storage.Appointments.Statuses.Clear();
            AddStatus(storage, Color.Yellow, "Free");
            AddStatus(storage, Color.MediumTurquoise, "Out of Office");
        }
        private static void AddStatus(ISchedulerStorageBase storage, Color color, string caption) {
            var item = storage.Appointments.Statuses.CreateNewStatus(caption);
            item.SetBrush(new SolidBrush(color));
            storage.Appointments.Statuses.Add(item);
        }
    }
    ```

2. Build the project and run the application. The `Event` Detail View displays new labels and status items:

    ![|XAF Windows Forms Custom Status and Label, DevExpress](~/images/xaf-winforms-scheduler-custom-status-and-label-devexpress.png)
