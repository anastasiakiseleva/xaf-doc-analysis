---
uid: "113183"
seealso:
- linkId: "112610"
- linkId: DevExpress.ExpressApp.Actions.ParametrizedAction
- linkId: DevExpress.XtraBars.BarEditItem
- linkId: DevExpress.XtraEditors.Repository.RepositoryItemDateEdit
- linkId: DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-win-custom-action-with-custom-action-control
  altText: 'GitHub example: Xaf WinForms - Create a custom action type and associated custom control'
title: 'How to: Customize Action Controls'
owner: Ekaterina Kiseleva
---
# How to: Customize Action Controls

This example demonstrates how to customize the control that visualizes an [Action](xref:112622) in a UI. A custom Action will be created, allowing users to enter a date and filter the List View accordingly. The implemented Action will accept keyboard input, as well as provide a drop-down calendar. The control representing the Action will be customized to accept keyboard input using a custom mask. The image below shows the resulting Action in a UI.

![AccessActionControl](~/images/accessactioncontrol116324.png)

> [!NOTE]
> You can see a demonstration of the `CustomizeParametrizedActionController` for WinForms in the **Actions** section of the **Feature Center** application that is shipped with XAF. [!include[FeatureCenterLocationNote](~/templates/featurecenterlocationnote111102.md)]

First, define the sample `MyDomainObject` business class. The class contains two properties. The first is the `CreatedOn` property of the `DateTime` type, and the second is the `Title` property of the `string` type.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
// ...
[DefaultClassOptions]
public class MyDomainObject : BaseObject {
    public virtual DateTime CreatedOn { get; set; }
    public virtual string Title { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
// ...
[DefaultClassOptions]
public class MyDomainObject : BaseObject {
    public MyDomainObject(Session session) : base(session) { }

    public DateTime CreatedOn {
        get { return GetPropertyValue<DateTime>(nameof(CreatedOn)); }
        set { SetPropertyValue(nameof(CreatedOn), value); }
    }

    public string Title {
        get { return GetPropertyValue<string>(nameof(Title)); }
        set { SetPropertyValue(nameof(Title), value); }
    }
}
```
***

Next, create a new [View Controller](xref:112621) and define a [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction). Configure the Controller and Action so that they activate for the `MyDomainObject` class only. Set the Action's [ParametrizedAction.ValueType](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.ValueType) to `DateTime`. In the Action's [ParametrizedAction.Execute](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.Execute) event handler, check whether a date was entered. If a date was entered, filter the `MyDomainObject` List View to contain only the objects whose "CreatedOn" property's value equals the entered date. If a user has executed the Action with an empty edit field, remove the applied filter, so that the List View displays all the objects, without regard to their creation date.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
//...
public class MyFilterController : ViewController {
    public ParametrizedAction dateFilterAction;
    public MyFilterController() {
        TargetViewType = ViewType.ListView;
        TargetObjectType = typeof(MyDomainObject);
        dateFilterAction = new ParametrizedAction(this, "MyDateFilter", PredefinedCategory.Search, typeof(DateTime));
        dateFilterAction.NullValuePrompt = "Enter date";
        dateFilterAction.Execute += dateFilterAction_Execute;
    }
    private void dateFilterAction_Execute(object sender, ParametrizedActionExecuteEventArgs e) {
        CriteriaOperator criterion = null;
        if(e.ParameterCurrentValue != null && e.ParameterCurrentValue.ToString() != string.Empty) {
            criterion = new BinaryOperator("CreatedOn", Convert.ToDateTime(e.ParameterCurrentValue));
        }
        ((ListView)View).CollectionSource.Criteria[dateFilterAction.Id] = criterion;
    }
}
```
***

To set up a custom edit mask, subscribe to the [ActionBase.CustomizeControl](xref:DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl) event. This event allows you to customize the created items control, and provides access to the corresponding Action Control.

## WinForms
    
# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.XtraBars;
using DevExpress.XtraEditors.Repository;
//...
public class CustomizeActionControlControllerWin : Controller {
    protected override void OnActivated() {
        base.OnActivated();
        Frame.GetController<MyFilterController>().dateFilterAction.CustomizeControl += CustomizeActionControlControllerWin_CustomizeControl;
    }
    private void CustomizeActionControlControllerWin_CustomizeControl(object sender, 
CustomizeControlEventArgs e) {
        BarEditItem barItem = e.Control as BarEditItem;
        if (barItem != null) {
            RepositoryItemDateEdit repositoryItem = (RepositoryItemDateEdit)barItem.Edit;
            repositoryItem.Mask.UseMaskAsDisplayFormat = true;
            repositoryItem.Mask.EditMask = "yyyy-MMM-dd";
            barItem.Width = 270;
        }
    }
    protected override void OnDeactivated() {
        Frame.GetController<MyFilterController>().dateFilterAction.CustomizeControl -= 
CustomizeActionControlControllerWin_CustomizeControl;
        base.OnDeactivated();
    }
}
```
***

## ASP.NET Core Blazor


Add the following Controller to the ASP.NET Core Blazor [application project](xref:118045) (_MySolution.Blazor.Server_).

# [C#](#tab/tabid-csharp-1)
 
```csharp
using MySolution.Module.Controllers;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Templates.Toolbar.ActionControls;
// ...

public class CustomizeActionControlControllerBlazor : Controller {
    private MyFilterController myFilterController;
    protected override void OnActivated() {
        base.OnActivated();
        myFilterController = Frame.GetController<MyFilterController>();
        if(myFilterController != null) {
            myFilterController.dateFilterAction.CustomizeControl += 
                CustomizeActionControlController_CustomizeControl;
        }
    }
    private void CustomizeActionControlController_CustomizeControl(object sender, 
        CustomizeControlEventArgs e) {
        if(e.Control is DxToolbarItemParametrizedActionControl actionControl && 
            actionControl.EditModel is DxDateEditModel dateEditModel) {
            dateEditModel.Format = "yyyy-MMM-dd";
        }
    }
    protected override void OnDeactivated() {
        if(myFilterController != null) {
            myFilterController.dateFilterAction.CustomizeControl -= 
            CustomizeActionControlController_CustomizeControl;
            myFilterController = null;
        }
        base.OnDeactivated();
    }
}
```
 
***

![|xaf ASP.NET Core Blazor access action control|](~/images/access-action-control-blazor.png)

> [!TIP]
> You can also customize an inline Action control. For more information, refer to the following topic: [Customize Inline Action Control (ASP.NET Core Blazor)](xref:404559#customize-inline-action-control).