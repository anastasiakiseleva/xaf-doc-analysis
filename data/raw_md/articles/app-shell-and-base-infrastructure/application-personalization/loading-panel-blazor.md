---
uid: "404738"
title: Loading Panels / Splash Forms (ASP.NET Core Blazor)
owner: Irina Nikolaeva
seealso:
  - linkId: '112680'
---
# Loading Panels / Splash Forms (ASP.NET Core Blazor)

This topic describes how to show a loading panel/indicator in an XAF Blazor application.

![DevExpress XAF - Loading Panel](~/images/loading-panel.png)

## Related API Members

### Server-Side API

* `ILoadingIndicatorProvider.Hold(string reason)` -- Prevents a loading panel from being hidden. You can use this method in asynchronous `SimpleAction.Execute` event handlers. 
* `ILoadingIndicatorProvider.Release(string reason)` -- Hides a loading panel when there is no reason to hold it. As a parameter, this method expects the same string identifier (`reason`) that was passed to the `Hold` method. If the `Hold` method hasn't been called yet, you can pass any `reason` to hide the loading panel.

### Client-Side API
* `xaf.loadingIndicator.show()` -- Displays a loading panel.
* `xaf.loadingIndicator.hide()` --  Hides a loading panel.

## Examples


### JavaScript-Based Approach with Server-Side API

#### Use a Predefined XAF CSS Class

XAF has built-in code that shows a loading indicator after a user clicks a UI element marked with the `xaf-action` CSS class. If you want to show a loading indicator after a user clicks an element, add this CSS class to the markup.

The code below adds a **Run** button to the login page of your application. When the user clicks this button, the application displays the loading panel. After 2 seconds, the `Release` method hides the panel.

**File**:  _YourSolutionName/App.razor_

```Razor{1-2,15-22}
@using DevExpress.ExpressApp.Blazor.Services;
@inject ILoadingIndicatorProvider LoadingIndicatorProvider

<Router AppAssembly="@typeof(Program).Assembly" AdditionalAssemblies="new[] { typeof(DevExpress.ExpressApp.Blazor.BlazorApplication).Assembly }">
    <Found Context="routeData">
        <RouteView RouteData="@routeData" />
    </Found>
    <NotFound>
        <LayoutView>
            <p>Sorry, there's nothing at this address.</p>
        </LayoutView>
    </NotFound>
</Router>

<DxButton Click=OnClick class="xaf-action" Text="Run" />

@code {
    public async Task OnClick() {
        await Task.Delay(2000);
        LoadingIndicatorProvider.Release(string.Empty);
    }
}
```

#### Use a Custom CSS Class

The following example shows how to handle a double-click on an HTML button with a specific class name and display the loading panel. The client-side event handler is used to display the panel as soon as the event is triggered. If you use a server-side handler, there may be a delay in client-server interactions, so a user may click the element several times before the panel appears.

To use this approach, add the following JavaScript code to a page (for example, __YourSolutionName/App.razor_).

```JS
<script type="text/javascript">
    document.body.addEventListener('dblclick', (e) => {
        if (e.target instanceof HTMLElement) {
            const myButton = e.target.closest(".my-button");
            if (myButton) {
                xaf.loadingIndicator.show();
            }
        }
    });
</script>
```

Next, apply a matching CSS class to the required element. For example, you can add the following code to your Blazor project's __YourSolutionName/App.razor_ file.

```Razor{1-2,26-33}
@using DevExpress.ExpressApp.Blazor.Services;
@inject ILoadingIndicatorProvider LoadingIndicatorProvider

<script type="text/javascript">
    document.body.addEventListener('dblclick', (e) => {
        if (e.target instanceof HTMLElement) {
            const myButton = e.target.closest(".my-button");
            if (myButton) {
                xaf.loadingIndicator.show();
            }
        }
    });
</script>

<Router AppAssembly="@typeof(Program).Assembly" AdditionalAssemblies="new[] { typeof(DevExpress.ExpressApp.Blazor.BlazorApplication).Assembly }">
    <Found Context="routeData">
        <RouteView RouteData="@routeData" />
    </Found>
    <NotFound>
        <LayoutView>
            <p>Sorry, there's nothing at this address.</p>
        </LayoutView>
    </NotFound>
</Router>

<button @ondblclick=OnClick class="my-button">Run</button>

@code {
    public async Task OnClick() {
        await Task.Delay(2000);
        LoadingIndicatorProvider.Release(string.Empty);
    }
}
```

#### Use the Hold Method Within the Controller

Add the following controller (the _TestController.cs_ file) to your Blazor project.

```csharp{20}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Blazor.Services;
using DevExpress.Persistent.Base;

namespace TestApplication.Blazor.Server.Controllers;

public class TestController : ViewController {

    private readonly IServiceProvider serviceProvider;

    [ActivatorUtilitiesConstructor]
    public TestController(IServiceProvider serviceProvider) : this() {
        this.serviceProvider = serviceProvider;
    }

    public TestController() {
        SimpleAction myAction = new(this, "MyAction", PredefinedCategory.Edit);
        myAction.Execute += async (s, e) => {
            serviceProvider.GetService<ILoadingIndicatorProvider>().Hold("WaitMyAction");
            await Task.Delay(5000);
            serviceProvider.GetService<ILoadingIndicatorProvider>().Release("WaitMyAction");
        };
    }
}
```

Note that the `Hold` method above prevents the loading panel from being hidden until the `Release` method is called with a matching `reason` value. This forces the `Execute` event to wait for 5 seconds and only then hide the panel. 

The asynchronous `Execute` event handler with a [void return type](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/async-return-types#void-return-type) cannot be waited on. Without the `Hold` method call, the event caller would continue execution and hide the loading panel before the 5-second delay has elapsed.

### JSRuntime-Based Approach with Client-Side API

> [!Note]
> This section illustrates a technique that calls JavaScript code from a server-side event handler. You can use this solution in certain scenarios. However, we recommend that you use client-side events to display indicator panels instead of server-side Blazor events. If you use a server-side handler, there may be a delay in client-server interactions. A user may click on the element several times before the panel appears.

To use this approach, add the following code to your Blazor project's __YourSolutionName/App.razor_ file. This snippet adds a **Run** button to your application's login page. When a user clicks **Run**, the application displays the loading panel and automatically hides it after 2 seconds.

**File**:  __YourSolutionName/App.razor_

```Razor{1,14-22}
@inject IJSRuntime JSRuntime

<Router AppAssembly="@typeof(Program).Assembly" AdditionalAssemblies="new[] { typeof(DevExpress.ExpressApp.Blazor.BlazorApplication).Assembly }">
    <Found Context="routeData">
        <RouteView RouteData="@routeData" />
    </Found>
    <NotFound>
        <LayoutView>
            <p>Sorry, there's nothing at this address.</p>
        </LayoutView>
    </NotFound>
</Router>

<DxButton Click=OnClick Text="Run" />

@code {
    public async Task OnClick() {
        await JSRuntime.InvokeVoidAsync("xaf.loadingIndicator.show");
        await Task.Delay(2000);
        await JSRuntime.InvokeVoidAsync("xaf.loadingIndicator.hide");
    }
}
```
