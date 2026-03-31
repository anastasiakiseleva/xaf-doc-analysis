---
uid: "404428"
title: Access Form Layout Control in XAF DetailView and DashboardView
seealso:
- linkId: "402154"
- linkId: "402153"
---
# Access Form Layout Control in XAF DetailView and DashboardView

To display View Items according to layout settings defined in a DetailView or DashboardView node of the Application Model, XAF applications use platform-specific Layout Managers. Each Layout Manager uses its own component to show controls in a [Composite View](xref:DevExpress.ExpressApp.CompositeView):

ASP.NET Core Blazor
:   `BlazorLayoutManager`: @DevExpress.Blazor.DxFormLayout
Windows Forms
:   `WinLayoutManager`: @DevExpress.XtraLayout.LayoutControl

You can use either of the following techniques to access these components and their items, and to define settings that are not exposed in the [Application Model](xref:112579):

* For an application-wide impact, override the `CreateLayoutManagerCore` virtual method of the [](xref:DevExpress.ExpressApp.XafApplication) class in the platform-specific _Application.cs_ file.
* If you want to limit the impact to a specific View, use a [View Controller](xref:112621).

See the sections below for platform-specific implementations of these techniques.

## ASP.NET Core Blazor

Handle the `BlazorLayoutManager.ItemCreated` event to access the properties of the following components:

* @DevExpress.Blazor.DxFormLayout
* @DevExpress.Blazor.DxFormLayoutTabPages
* @DevExpress.Blazor.DxFormLayoutTabPage
* @DevExpress.Blazor.DxFormLayoutGroup
* @DevExpress.Blazor.DxFormLayoutItem

For example, you can use the following code sample to set the second tab to active when a user opens a Detail View.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Layout;
using YourApplicationName.Module.BusinessObjects;  

namespace YourApplicationName.Blazor.Server.Controllers {
    public class AccessLayoutManagerController : ObjectViewController<DetailView, Employee> {
        protected override void OnActivated() {
            base.OnActivated();
            ((BlazorLayoutManager)View.LayoutManager).ItemCreated += 
            AccessLayoutManagerController_ItemCreated;
        } 

        protected override void OnDeactivated() {
            ((BlazorLayoutManager)View.LayoutManager).ItemCreated -=
            AccessLayoutManagerController_ItemCreated;

            base.OnDeactivated(); 

        } 

        private void AccessLayoutManagerController_ItemCreated(object sender, BlazorLayoutManager.ItemCreatedEventArgs e) { 
            if(e.ModelLayoutElement.Id == "Tabs" && e.LayoutControlItem is DxFormLayoutTabPagesModel tabbedGroup) { 
                tabbedGroup.ActiveTabIndex = 1; 
            } 
        } 
    } 
} 
```

XAF ASP.NET Core Blazor applications store the active tab index in the Application Model. Use the [IModelTabbedGroupBlazor.ActiveTabIndex](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelTabbedGroupBlazor.ActiveTabIndex) property of the corresponding Detail View to specify this index in the [](xref:112830).

For additional information on how to customize the Detail View's layout in code, refer to the following example: [How to Show the Number of Nested List View Items In Tab Captions](https://github.com/DevExpress-Examples/XAF-How-to-show-the-number-of-nested-list-views-items-in-tab-captions).

## Windows Forms

>[!NOTE]
> The Windows Forms module of your application should have a reference to the _DevExpress.XtraLayout.v<:xx.x:>_ assembly.

To customize the Layout control for all Views, override the `CreateLayoutManagerCore` virtual method of the [](xref:DevExpress.ExpressApp.XafApplication) class in the _YourApplicationName.Win\YourApplicationNameWinApplication.cs_ file. For example, you can use the following code to enable the [OptionsFocus.EnableAutoTabOrder](xref:DevExpress.XtraLayout.OptionsFocus.EnableAutoTabOrder) option: 
	
```csharp
using DevExpress.ExpressApp.Layout; 
using DevExpress.ExpressApp.Win; 
using DevExpress.XtraLayout; 

namespace YourApplicationName.Win; 

public class YourApplicationNameWinApplication : WinApplication { 
    // 
    protected override LayoutManager CreateLayoutManagerCore(bool simple) { 
        LayoutManager layoutManager = base.CreateLayoutManagerCore(simple); 
        if(layoutManager.Container is LayoutControl layoutControl) { 
            layoutControl.OptionsFocus.EnableAutoTabOrder = false; 
        } 
        return layoutManager; 
    } 
} 
```

To customize the Layout control for a specific View, create a new [View Controller](xref:112621) in your Windows Forms module. To access `LayoutControl`, override the `OnViewControlsCreated` method or subscribe to the `LayoutManager.LayoutCreated` event.

```csharp
using DevExpress.ExpressApp; 
using DevExpress.XtraLayout; 

namespace YourApplicationName.Win.Controllers;
public class LayoutControlViewController : ViewController<DetailView> { 
    protected override void OnViewControlsCreated() { 
        base.OnViewControlsCreated(); 
        if(View.LayoutManager.Container is LayoutControl layoutControl) { 
            layoutControl.OptionsFocus.EnableAutoTabOrder = false; 
        } 
    } 
} 
```

Subscribe to the `WinLayoutManager.ItemCreated` event to access the following Layout control items:
* @DevExpress.XtraLayout.LayoutControlItem
* @DevExpress.XtraLayout.LayoutControlGroup
* @DevExpress.XtraLayout.TabbedControlGroup.

For example, you can use the following code sample to set the second tab as active when a user opens a Detail View: 

 
```csharp
using System; 
using DevExpress.ExpressApp; 
using DevExpress.XtraLayout; 
using DevExpress.ExpressApp.Win.Layout; 

namespace YourApplicationName.Win { 

    public class WinCustomizeTabControlViewController : ViewController<DetailView> { 

        TabbedControlGroup tabbedGroup; 
        WinLayoutManager layoutManager; 

        protected override void OnActivated() { 
            base.OnActivated(); 
            layoutManager = (WinLayoutManager)View.LayoutManager; 
            layoutManager.ItemCreated += OnItemCreated; 
            layoutManager.LayoutCreated += OnLayoutCreated; 
        } 

        void OnItemCreated(object sender, ItemCreatedEventArgs e) { 
            // Check the Id in the YourApplicationName.Module\Model.DesignedDiffs.xafml file 
            if (e.ModelLayoutElement.Id == "MyTabbedGroup") { 
                tabbedGroup = (TabbedControlGroup)e.Item; 
            } 
        } 

        private void OnLayoutCreated(object sender, EventArgs e) { 
            if (tabbedGroup != null) { 
               tabbedGroup.SelectedTabPageIndex = 1; 
            } 
        } 

        protected override void OnDeactivated() { 
            if (layoutManager != null) { 
                layoutManager.ItemCreated -= OnItemCreated; 
                layoutManager.LayoutCreated -= OnLayoutCreated; 
                layoutManager = null; 
            } 

            tabbedGroup = null; 

            base.OnDeactivated(); 
        } 
    } 
} 
```

For details of this implementation, see the following example: [How to access a tab control in a Detail View layout](https://github.com/DevExpress-Examples/xaf-how-to-access-a-tab-control-in-a-detail-view-layout). 

For additional information on how to customize the Detail View layout in code, refer to the following topics and examples:

- [](xref:2327)
- [How to Show the Number of Nested List View Items In Tab Captions](https://github.com/DevExpress-Examples/XAF-How-to-show-the-number-of-nested-list-views-items-in-tab-captions)
