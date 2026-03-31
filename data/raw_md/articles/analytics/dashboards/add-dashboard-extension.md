---
uid: "404496"
title: "How to: Add a Dashboard Extension to an XAF ASP.NET Core Blazor Application"
---
# How to: Add a Dashboard Extension to an XAF ASP.NET Core Blazor Application

You can use [extensions](xref:117543) to customize the dashboard control used by the [Dashboards Module](xref:117449). This topic integrates a simple [example extension](https://github.com/DevExpress-Examples/dashboard-blazor-server-js-customization) into your XAF ASP.NET Core Blazor application.

## Step-by-Step Instructions

1. Copy the following dashboard extension files to the _YourApplicationName.Blazor.Server\\wwwroot_ folder:

    * [BlazorDashboardApp\\wwwroot\\parameter-item.js](https://github.com/DevExpress-Examples/dashboard-blazor-server-js-customization/blob/24.2.2%2B/CS/BlazorDashboardApp/wwwroot/parameter-item.js). This file contains the definition of the `ParameterCustomItem` extension. You will create a Controller that loads this script in the last step.

        ```JS
        window.ParameterCustomItem = /*...*/;
        ```

    * [BlazorDashboardApp\\wwwroot\\dashboard-events-scripts.js](https://github.com/DevExpress-Examples/dashboard-blazor-server-js-customization/blob/24.2.2%2B/CS/BlazorDashboardApp/wwwroot/dashboard-events-scripts.js). This file contains the code that registers the extension in the dashboard control and adds custom toolbar buttons to Grid item captions:

        ```JS
        window.dashboardEvents = {
            onBeforeRender: (args) => {
                // Registers the Parameter item and the Dashboard Panel.
                var dashboardControl = args.component;
                dashboardControl.registerExtension(new ParameterCustomItem(dashboardControl));
                // ...
            },
            // Adds a new custom toolbar item to the dashboard item caption.
            extensions: {
                viewerApi: {
                    onItemCaptionToolbarUpdated: function (e) {
                        // ...
                    }
                }
            }    
        }
        ```

2. Create a new JavaScript file in the _YourApplicationName.Blazor.Server\\wwwroot_ folder and name it _xaf-dashboard-user-script.js_. Copy the following code snippet to the file:

    ```JS
    const xafDashboardUserScript = {
        onBeforeRender: function (dashboardControl) {
            window.dashboardEvents.onBeforeRender({ component: dashboardControl });
            const viewerApi = dashboardControl.findExtension("viewerApi");
            viewerApi.on("itemCaptionToolbarUpdated",
                window.dashboardEvents.extensions.viewerApi.onItemCaptionToolbarUpdated);
        }
    };

    window.xafBlazorDashboardUserScripts = [xafDashboardUserScript];
    ```
    
    `xafDashboardUserScript` is a plain JavaScript object that contains a single `onBeforeRender` method. XAF calls this method before it renders a dashboard, because `xafDashboardUserScript` is included in the `xafBlazorDashboardUserScripts` array. The `onBeforeRender` method does the following:

    * Calls the `window.dashboardEvents.onBeforeRender` method (defined in the _dashboard-events-scripts.js_ file) that registers a custom toolbar item.
    * Ensures that the `onItemCaptionToolbarUpdated` method is called. XAF does not support `extensions: { viewerApi: { ... } }` syntax, therefore you must subscribe to the `ViewerApiExtension`'s [itemCaptionToolbarUpdated](xref:js-DevExpress.Dashboard.ViewerApiExtensionEvents) event explicitly.

3. To add custom scripts and the extension's icons to the application, navigate to the _YourApplicationName.Blazor.Server\\Pages\\\_Host.cshtml_ file and add the following links to it: _dashboard-events-scripts.js_ and _xaf-dashboard-user-script.js_.

    ```HTML{3-4}
    <link href="_content/DevExpress.ExpressApp.Blazor/styles.css" asp-append-version="true" rel="stylesheet" />
    <link href="css/site.css" rel="stylesheet" />
    <script src="dashboard-events-scripts.js"></script>
    <script src="xaf-dashboard-user-script.js"></script>
    ```

4. Navigate to _YourApplicationName.Blazor.Server\\App.razor_ and add the following line at the top of the file:

    ```Razor
    @DxResourceManager.RegisterScripts((config) => config.Register(new DxResource("/parameter-item.js", 900)))
    ```

    This ensures that the _parameter-item.js_ script is loaded in the correct order (after all other required scripts have been loaded).

The Parameter custom item is now available in the Dashboard Designer, and you can see a custom toolbar item in the first Grid dashboard item.

![|XAF ASP.NET Core Blazor Dashboard With Custom Extension, DevExpress|](~/images/add-dashboard-extension_result.png)