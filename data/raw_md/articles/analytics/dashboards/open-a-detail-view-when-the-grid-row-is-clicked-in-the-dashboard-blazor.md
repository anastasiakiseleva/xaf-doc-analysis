---
uid: "403531"
title: Open a Detail View When the Grid Row is Clicked in the Dashboard (Blazor)
owner: Yekaterina Kiseleva
seealso:
  - linkId: '118348'
---
# Open a Detail View When the Grid Row is Clicked in the Dashboard (Blazor)

This topic describes how to invoke a Detail View when a user clicks a row in [](xref:DevExpress.DashboardCommon.GridDashboardItem). In the invoked Detail View, a user can view or edit a [business object](xref:113664) corresponding to the clicked row.

This example consists of the following parts: 

* [Dashboard Hidden Measure](#add-a-dashboard-hidden-measure)  
  Allows you to get an identifier of an object displayed in a clicked row.
* [Client-Side Script](#create-a-client-side-script)  
  Handles row clicks and delegates Detail View invocation to the server side.
* [Server-Side Controller](#create-a-server-side-controller)  
  Registers a reference to itself on the client side and opens the Detail View.

[!example[Open a Detail View When the Grid Row is Clicked in the Dashboard (Blazor)](https://github.com/DevExpress-Examples/xaf-blazor-open-detail-view-when-grid-row-is-clicked-in-the-dashboard)]

## Add a Dashboard Hidden Measure 

Add a key property to the Dashboard [hidden measures](xref:15706) and set the summary type to Min or Max. The key property in this example is `Oid`. Since `Oid` values are unique in the underlying dataset, the Min or Max function generates a list of identifiers that are unique within the aggregated data. This associates each row with `Oid` of the underlying object.

![DashboardDesigner_OidMeasure_Web](~/images/dashboarddesigner_oidmeasure_web129866.png)

## Create a Client-Side Script

In your Blazor application project (_MySolution.Blazor.Server_), add a new JavaScript file to the _wwwroot/js_ folder. In this file, declare an object (`customScript`) and implement the following methods in it:

registerController 
:   Stores a reference to the server-side Controller that calls this method. 
processItemClick
:   A callback that retrieves the ID of the object clicked in the Dashboard grid item and passes this ID to the server-side Controller's `ShowDetailView` method. 
onBeforeRender
:   Registers `processItemClick` as a callback that the [Dashboard control](xref:js-DevExpress.Dashboard.DashboardControl) invokes when a user clicks a grid row.

# [MySolution.Blazor.Server\wwwroot\js\customScript.js](#tab/tabid-js)
```JS
"use strict";

globalThis.customScript = {
    showDetailViewControllers: {},
    onBeforeRender: function (dashboardControl) {
        const viewerApi = dashboardControl.findExtension("viewerApi");
        viewerApi.on("itemClick", globalThis.customScript.processItemClick.bind(dashboardControl));
    },
    registerController: function (key, controller) {
        globalThis.customScript.showDetailViewControllers[key] = controller;
    },
    unregisterController: function (key) {
        delete globalThis.customScript.showDetailViewControllers[key];
    },
    processItemClick: function (args) {
        const itemData = args.getData(),
            dataSlice = itemData.getSlice(args.getAxisPoint()),
            oidMeasure = dataSlice.getMeasures().find((measure) => measure.dataMember === 'ID').id,
            measureValue = dataSlice.getMeasureValue(oidMeasure),
            objectId = measureValue.getValue(),
            controllerId = this.element().dataset["showdetailid"];
        globalThis.customScript.showDetailViewControllers[controllerId].invokeMethodAsync("ShowDetailView", objectId);
    }
}
```
***

In the same file, create the `globalThis.xafBlazorDashboardUserScripts` array if it does not exist and add the `customScript` object to it. This ensures that the object's `onBeforeRender` method is called before the Dashboard control is rendered.

# [MySolution.Blazor.Server\wwwroot\js\customScript.js](#tab/tabid-js)
```JS
// ...
if (!globalThis.xafBlazorDashboardUserScripts) {
    globalThis.xafBlazorDashboardUserScripts = [];
}
globalThis.xafBlazorDashboardUserScripts.push(globalThis.customScript);
```
***


Reference this script in the _\_Host.cshtml_ file in a `<script>` tag:

# [MySolution.Blazor.Server\Pages\\_Host.cshtml](#tab/tabid-html)
```CSHTML{7}
<!-- ... -->
<html lang="en">
<!-- ... -->
<body>
    <!-- ... -->
    <script src="_framework/blazor.server.js"></script>
    <script src="js/customScript.js"></script>
</body>
</html>
```
***

## Create a Server-Side Controller

Declare a `BlazorShowDetailViewFromDashboardController` [](xref:DevExpress.ExpressApp.ObjectViewController`2) with the [](xref:DevExpress.ExpressApp.DetailView) and [](xref:DevExpress.Persistent.Base.IDashboardData) generic parameters in the ASP.NET Core Blazor [application project](xref:118045) (_MySolution.Blazor.Server_). Customize the Controller as outlined below:
* Create a [DotNetObjectReference](xref:Microsoft.JSInterop.DotNetObjectReference`1) that stores the reference to this Controller.
* In the overridden `OnActivated` method, use the [IJSRuntime](xref:Microsoft.JSInterop.IJSRuntime) service to register a reference to this Controller on the client side. To do this, call the `customScript.registerController` method with this reference.
* Declare the `ShowDetailView` method and decorate it with the [JSInvokable](xref:Microsoft.JSInterop.JSInvokableAttribute) attribute. This method is called from the client side and opens the Detail View for the clicked object.

# [MySolution.Blazor.Server\Controllers\BlazorShowDetailViewFromDashboardController.cs](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Dashboards.Blazor.Components;
using DevExpress.Persistent.Base;
using OpenViewFromDashboardEF.Module.BusinessObjects;
using Microsoft.JSInterop;

namespace OpenViewFromDashboard.Blazor.Server.Controllers;
public class BlazorShowDetailViewFromDashboardController : ObjectViewController<DetailView, IDashboardData> {
    private string clientId = Guid.NewGuid().ToString();
    private DotNetObjectReference<BlazorShowDetailViewFromDashboardController> controllerReference;
    public BlazorShowDetailViewFromDashboardController() {
        controllerReference = DotNetObjectReference.Create(this);
    }
    protected override void OnActivated() {
        base.OnActivated();
        Application.ServiceProvider.GetRequiredService<IJSRuntime>().InvokeVoidAsync("customScript.registerController", clientId, controllerReference).Preserve();
        View.CustomizeViewItemControl<BlazorDashboardViewerViewItem>(this, CustomizeDashboardViewerViewItem);
    }
    private void CustomizeDashboardViewerViewItem(BlazorDashboardViewerViewItem dashboardViewerViewItem) {
        dashboardViewerViewItem.ComponentModel.SetAttribute("data-showdetailid", clientId);
    }
    protected override void OnDeactivated() {
        Application.ServiceProvider.GetRequiredService<IJSRuntime>().InvokeVoidAsync("customScript.unregisterController", clientId).Preserve();
        base.OnDeactivated();
    }
    protected override void Dispose(bool disposing) {
        base.Dispose(disposing);
        controllerReference.Dispose();
    }
    [JSInvokable]
    public void ShowDetailView(string oidString) {
        if(!Guid.TryParse(oidString, out var id)) {
            return;
        }
        var objectSpace = Application.CreateObjectSpace(typeof(Contact));
        var item = objectSpace.FirstOrDefault<Contact>(c => c.ID == id);
        if(item is not null) {
            var detailView = Application.CreateDetailView(objectSpace, item, true);
            Application.ShowViewStrategy.ShowViewFromCommonView(detailView);
        } else {
            objectSpace.Dispose();
        }
    }
}
```
***

[`ObjectViewController`]: xref:DevExpress.ExpressApp.ObjectViewController`2
[`IJSRuntime`]: xref:Microsoft.JSInterop.IJSRuntime
[`DotNetObjectReference`]: xref:Microsoft.JSInterop.DotNetObjectReference`1
[`Create`]: xref:Microsoft.JSInterop.DotNetObjectReference.Create*
[`BlazorApplication`]: xref:DevExpress.ExpressApp.Blazor.BlazorApplication
[`Application`]: xref:DevExpress.ExpressApp.Controller.Application
[`GetRequiredService`]: xref:Microsoft.Extensions.DependencyInjection.ServiceProviderServiceExtensions.GetRequiredService*
[`InvokeVoidAsync`]: xref:Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync*
[`JSInvokable`]: xref:Microsoft.JSInterop.JSInvokableAttribute
[`TryParse`]: xref:System.Guid.TryParse*
[`CreateObjectSpace`]: xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type)
[`FirstOrDefault`]: xref:DevExpress.ExpressApp.IObjectSpace.FirstOrDefault``1(System.Linq.Expressions.Expression{System.Func{``0,System.Boolean}})
[`CreateDetailView`]: xref:DevExpress.ExpressApp.XafApplication.CreateDetailView(DevExpress.ExpressApp.IObjectSpace,System.Object)
[`SetView`]: xref:DevExpress.ExpressApp.Frame.SetView(DevExpress.ExpressApp.View)
