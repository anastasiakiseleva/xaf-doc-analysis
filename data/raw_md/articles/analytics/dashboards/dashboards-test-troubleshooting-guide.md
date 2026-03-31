---
uid: "404346"
title: Dashboards Module Troubleshooting Guide
---
# Dashboards Module Troubleshooting Guide

This topic describes common issues that you may encounter when using the [](xref:117449), and steps you can follow to diagnose and resolve these issues.

***

## The "The DevExtreme library is included before the Knockout library. Check the order in which the scripts appear on the page" error message in v24.2+

**Problem Description:**

This error may appear if you previously integrated a DevExtreme widget into your XAF Blazor application with the **Dashboards Module** using the solution described [below](#the-your-xaf-application-contains-the-dashboards-module-and-devextreme-widget-error-message-in-v241-and-earlier). 

In v24.2, two breaking changes were introduced that negated the previous workaround:

- [The mechanism of adding DevExtreme into Blazor applications has changed](https://supportcenter.devexpress.com/ticket/details/t1262237/the-mechanism-of-adding-devextreme-into-blazor-applications-has-changed)
- [Dashboard for Blazor - The OnScriptsLoading event became obsolete](https://supportcenter.devexpress.com/ticket/details/t1262320/dashboard-for-blazor-the-onscriptsloading-event-became-obsolete)

**Solution:**

1. Remove `<script>` elements that explicitly load DevExtreme and its libraries:

    **File:** _MySolution.Blazor.Server\\Pages\\\_Host.cshtml_

    ```HTML
    <!-- <script type="text/javascript" src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-3.6.2.min.js"></script> -->
    <!-- <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/knockout/3.5.0/knockout-min.js"></script> -->
    <!-- <script type="text/javascript" src="https://cdn3.devexpress.com/jslib/<:xx.x.x:>/js/dx.all.js"></script> -->
    ```
1. Remove the controller (`MyController`) subscribed to the `dashboardViewItem.JSCustomizationModel.OnScriptsLoading` event from the **MySolution.Blazor.Server** project.

1. Add the following line at the top of the _MySolution.Blazor.Server\\App.razor_ file:

    **File:** _MySolution.Blazor.Server\\App.razor_

    ```Razor
    @DxResourceManager.RegisterScripts(config => config.Register(CommonResources.DevExtremeJS))
    ```


## The "Your XAF application contains the Dashboards Module and DevExtreme widget" error message in v24.1 and earlier

**Problem Description:**

An ASP.NET Core Blazor-based XAF application displays the following error message if you add both the **Dashboards Module** and [DevExtreme widget](xref:403578) to it:

_Your XAF application contains the Dashboards Module and DevExtreme widget. This scenario requires additional setup as described in the following topic: \<link\>._

**Solution:**

Follow the steps below to configure such applications:

1. Add the following code that implements a custom controller to the **MySolution.Blazor.Server** project.

    ```csharp
    using DevExpress.DashboardBlazor;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Dashboards.Blazor.Components;
    using Microsoft.AspNetCore.Components;
    
    public class MyController : ViewController<DetailView> {
        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl<BlazorDashboardViewerViewItem>(this, CustomizeDashboardViewerViewItem);
        }
        void CustomizeDashboardViewerViewItem(BlazorDashboardViewerViewItem dashboardViewItem) {
            dashboardViewItem.JSCustomizationModel.OnScriptsLoading =
                EventCallback.Factory.Create<ScriptsLoadingEventArgs>(this, OnScriptsLoading);
        }
        private void OnScriptsLoading(ScriptsLoadingEventArgs args) {
            args.Scripts.Remove(ScriptIdentifiers.JQuery);
            args.Scripts.Remove(ScriptIdentifiers.Knockout);
            args.Scripts.Remove(ScriptIdentifiers.DevExtreme);
        }
    }
    ```

2. Import the JQuery and Knockout libraries into the _MySolution.Blazor.Server\\Pages\\\_Host.cshtml_ file before the DevExtreme library.

    ```HTML{1,2}
    <script type="text/javascript" src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-3.6.2.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/knockout/3.5.0/knockout-min.js"></script>
    <script type="text/javascript" src="https://cdn3.devexpress.com/jslib/<:xx.x.x:>/js/dx.all.js"></script>
    ```

3. Rebuild and run the application. 


***

If this document does not contain sufficient information on how to resolve your issue, feel free to contact Developer Express support engineers at the [Support Center](https://supportcenter.devexpress.com).
