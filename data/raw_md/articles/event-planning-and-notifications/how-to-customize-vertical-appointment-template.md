---
uid: "404733"
title: 'How to: Customize Vertical Appointment Template (ASP.NET Core Blazor)'
owner: Anastasiya Kisialeva
---
# How to: Customize Vertical Appointment Template (ASP.NET Core Blazor)

This article explains how to implement a custom @DevExpress.Blazor.Base.DxSchedulerDayViewBase.VerticalAppointmentTemplate in your ASP.NET Core Blazor application.

> [!NOTE]
> For the purposes of this article, you can use the **MainDemo** application installed as a part of the XAF package. The default location of the application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\\Components\XAF_.

The default @DevExpress.Blazor.Base.DxSchedulerDayViewBase.VerticalAppointmentTemplate has the following look:

![|XAF ASP.NET Core Blazor Default Vertical Appointment Template, DevExpress](~/images/xaf-maindemo-defaultverticalappointmenttemplate-devexpress.png)

1. In the **Solution Explorer**, navigate to the `MainDemo.Blazor.Server` project, create a new folder, and name it _MyComponents_.
2. In the _MyComponents_ folder, create a new [Razor component](https://learn.microsoft.com/en-us/aspnet/core/blazor/components) and name it _DayViewTemplate.razor_. Replace the auto-generated content with the following code:

    ```Razor
    @using DevExpress.Blazor
    @namespace MyComponents
    <div class="card shadow-sm bg-white p-2" style="overflow: hidden; height: 100%;box-shadow: .125rem .25rem rgba(34,34,34,0.15)">
        <span class="text-dark ps-0 mb-1" style="font-weight:600; font-size: .925em;">@Context.Appointment.Subject</span>
    </div>

    @code {
        [Parameter]
        public DxSchedulerAppointmentView Context { get; set; } = default!;
        public static RenderFragment Create(DxSchedulerAppointmentView appointmentView) =>
            @<DayViewTemplate Context=@appointmentView />;
    }
    ```

3. Navigate to the properties of the _DayViewTemplate.razor_ file and set the **Build Action** property to `Content`.

    ![|XAF ASP.NET Core Blazor Razor Component Properties, DevExpress|](~/images/xaf-blazor-razorcomponentproperties-devexpress.png)

4. In the _MainDemo.Blazor.Server\Controllers_ folder, create a [View Controller](xref:112621) and name it _SchedulerTemplateCustomizationController.cs_. Replace the auto-generated content with the following code:

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Scheduler.Blazor.Controllers;
    using DevExpress.ExpressApp.Scheduler.Blazor.Editors;
    using DevExpress.Persistent.Base.General;
    using Microsoft.AspNetCore.Components;
    using MyComponents;

    namespace MainDemo.Blazor.Server.Controllers {
        public class SchedulerTemplateCustomizationController : ObjectViewController<ListView, IEvent> {
            protected override void OnActivated() {
                base.OnActivated();
                //  Deactivate SchedulerAppointmentTemplatesController because it assigns the VerticalAppointmentTemplate property and can override your customization.
                Frame.GetController<SchedulerAppointmentTemplatesController>().Active["ByDesign"] = false;
            }
            protected override void OnViewControlsCreated() {
                base.OnViewControlsCreated();
                if(View.Editor is SchedulerListEditor schedulerListEditor) {
                    schedulerListEditor.DayViewModel.VerticalAppointmentTemplate = appointmentView => DayViewTemplate.Create(appointmentView);
                }
            }
            protected override void OnDeactivated() {
                Frame.GetController<SchedulerAppointmentTemplatesController>().Active.RemoveItem("ByDesign");
                base.OnDeactivated();
            }
        }
    }
    ```

5. Build the project and run the application. Navigate to the **Calendar** List View. The customized @DevExpress.Blazor.Base.DxSchedulerDayViewBase.VerticalAppointmentTemplate should look like this:

    ![|XAF ASP.NET Core Blazor Customized Vertical Appointment Template, DevExpress](~/images/xaf-maindemo-customizedverticalappointmenttemplate-devexpress.png)

> [!TIP]
> * This example demonstrates the customized [Day View](https://demos.devexpress.com/blazor/Scheduler/ViewTypes/DayView), but the same technique is applicable to other View types as well. 
> * You can use this technique to customize @DevExpress.Blazor.Base.DxSchedulerDayViewBase.HorizontalAppointmentTemplate.
